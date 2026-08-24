#!/usr/bin/env python3
"""Simplified MuJoCo operations visualization for retail backroom fulfillment."""

from __future__ import annotations

import argparse
import csv
import json
import math
import time
from pathlib import Path

import mujoco


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def lerp(a: float, b: float, amount: float) -> float:
    return a + (b - a) * clamp(amount)


def stair_height(x: float) -> float:
    """Match the four-step platform geometry used by retail.xml."""
    profile = [
        (-0.75, 0.0),
        (-0.40, 0.20),
        (0.25, 0.40),
        (0.82, 0.60),
        (1.34, 0.80),
        (1.59, 1.00),
    ]
    if x <= profile[0][0]:
        return 0.0
    if x >= profile[-1][0]:
        return 1.0
    for (x0, z0), (x1, z1) in zip(profile, profile[1:]):
        if x <= x1:
            return lerp(z0, z1, (x - x0) / (x1 - x0))
    return 1.0


def mocap_id(model: mujoco.MjModel, body_name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, body_name)
    return int(model.body_mocapid[body_id])


def set_pose(data: mujoco.MjData, index: int, x: float, y: float, z: float, yaw: float = 0.0) -> None:
    data.mocap_pos[index] = (x, y, z)
    data.mocap_quat[index] = (math.cos(yaw / 2), 0.0, 0.0, math.sin(yaw / 2))


def mission_pose(local_time: float, lane_y: float) -> tuple[float, float, float, float, str, bool]:
    """Return robot pose and whether the item is being carried for one 18-second mission."""
    t = local_time % 18.0
    if t < 2:
        return -3.6, lane_y, 0.0, 0.0, "tablet_request", False
    if t < 6:
        p = (t - 2) / 4
        x = lerp(-3.6, 3.0, p)
        z = stair_height(x) if lane_y < 0 else 0.0
        return x, lane_y, z, 0.0, "walk_existing_route", False
    if t < 8:
        return 3.0, lane_y, 1.0 if lane_y < 0 else 0.0, 0.0, "verify_and_pick", False
    if t < 12:
        p = (t - 8) / 4
        x = lerp(3.0, -3.7, p)
        z = stair_height(x) if lane_y < 0 else 0.0
        return x, lane_y, z, math.pi, "carry_to_employee", True
    if t < 14:
        return -3.7, lane_y, 0.0, math.pi, "employee_handoff", True
    if t < 17:
        p = (t - 14) / 3
        return lerp(-3.7, -3.2, p), lane_y, 0.0, 0.0, "inventory_confirmed", False
    return -3.2, lane_y, 0.0, 0.0, "ready_for_next_request", False


def run(duration: float, viewer_enabled: bool, output_dir: Path) -> None:
    model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("retail.xml")))
    data = mujoco.MjData(model)
    robot_ids = [mocap_id(model, "robot_1"), mocap_id(model, "robot_2")]
    item_ids = [mocap_id(model, "shoe_box_1"), mocap_id(model, "shoe_box_2")]
    lanes = [-1.55, 2.15]
    rows: list[dict[str, object]] = []
    start = time.monotonic()
    elapsed = 0.0
    last_sample = -1

    viewer = None
    if viewer_enabled:
        from mujoco import viewer as mujoco_viewer
        viewer = mujoco_viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False)
        camera_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, "overview")
        if camera_id < 0:
            raise RuntimeError("retail.xml is missing the required 'overview' camera")
        viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
        viewer.cam.fixedcamid = camera_id

    try:
        while elapsed < duration:
            for index, lane in enumerate(lanes):
                local = elapsed + index * 4.5
                x, y, z, yaw, state, carrying = mission_pose(local, lane)
                set_pose(data, robot_ids[index], x, y, z, yaw)
                if carrying:
                    item_x = x + 0.42 * math.cos(yaw)
                    item_y = y + 0.42 * math.sin(yaw)
                    set_pose(data, item_ids[index], item_x, item_y, z + 1.0, yaw)
                else:
                    item_home_y = -1.55 if index == 0 else 2.70
                    item_home_z = 1.32 if index == 0 else 1.04
                    item_home_x = 3.65 if index == 0 else 1.80
                    set_pose(data, item_ids[index], item_home_x, item_home_y, item_home_z)
                sample = int(elapsed)
                if sample != last_sample:
                    rows.append({"second": sample, "robot": index + 1, "state": state, "x_m": round(x, 2), "y_m": y, "carrying": carrying})
            last_sample = int(elapsed)
            mujoco.mj_forward(model, data)
            if viewer:
                if not viewer.is_running():
                    break
                viewer.sync()
            if viewer:
                time.sleep(0.02)
                elapsed = time.monotonic() - start
            else:
                elapsed += 0.02
    finally:
        if viewer:
            viewer.close()

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "retail_humanoid_telemetry.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["second", "robot", "state", "x_m", "y_m", "carrying"])
        writer.writeheader()
        writer.writerows(rows)
    states = sorted({str(row["state"]) for row in rows})
    required_states = {
        "tablet_request", "walk_existing_route", "verify_and_pick", "carry_to_employee",
        "employee_handoff", "inventory_confirmed", "ready_for_next_request",
    }
    summary = {
        "scenario": "Retail backroom humanoid fulfillment",
        "model": "retail_backroom_humanoid_fulfillment",
        "duration_seconds": duration,
        "robots": 2,
        "scope": "workflow visualization only",
        "states_demonstrated": states,
        "validation": {
            "required_states_present": required_states.issubset(states),
            "both_robots_sampled": {int(row["robot"]) for row in rows} == {1, 2},
            "camera_name": "overview",
            "stair_platform_height_m": 1.0,
        },
    }
    summary["passed"] = all(value for key, value in summary["validation"].items() if key not in {"camera_name", "stair_platform_height_m"})
    (output_dir / "retail_humanoid_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if not summary["passed"]:
        raise SystemExit("Retail workflow validation failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument("--duration", type=float, default=36.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    run(args.duration, args.viewer, args.output_dir)
