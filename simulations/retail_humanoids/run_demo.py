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
        stair = lane_y < 0 and 0.0 < x < 1.2
        z = 0.30 * clamp((x + 0.1) / 1.0) if stair else 0.0
        return x, lane_y, z, 0.0, "walk_existing_route", False
    if t < 8:
        return 3.0, lane_y, 0.30 if lane_y < 0 else 0.0, 0.0, "verify_and_pick", False
    if t < 12:
        p = (t - 8) / 4
        x = lerp(3.0, -3.7, p)
        stair = lane_y < 0 and 0.0 < x < 1.2
        z = 0.30 * clamp((x + 0.1) / 1.0) if stair else 0.0
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
    lanes = [-1.3, 1.3]
    rows: list[dict[str, object]] = []
    start = time.monotonic()
    last_sample = -1

    viewer = None
    if viewer_enabled:
        from mujoco import viewer as mujoco_viewer
        viewer = mujoco_viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False)
        camera_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, "portfolio")
        viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
        viewer.cam.fixedcamid = camera_id

    try:
        while (elapsed := time.monotonic() - start) < duration:
            for index, lane in enumerate(lanes):
                local = elapsed + index * 4.5
                x, y, z, yaw, state, carrying = mission_pose(local, lane)
                set_pose(data, robot_ids[index], x, y, z, yaw)
                if carrying:
                    item_x = x + 0.42 * math.cos(yaw)
                    item_y = y + 0.42 * math.sin(yaw)
                    set_pose(data, item_ids[index], item_x, item_y, z + 1.0, yaw)
                else:
                    item_home_y = -2.3 if index == 0 else 2.3
                    set_pose(data, item_ids[index], 3.2, item_home_y, 0.95)
                sample = int(elapsed)
                if sample != last_sample:
                    rows.append({"second": sample, "robot": index + 1, "state": state, "x_m": round(x, 2), "y_m": y, "carrying": carrying})
            last_sample = int(elapsed)
            mujoco.mj_forward(model, data)
            if viewer:
                if not viewer.is_running():
                    break
                viewer.sync()
            time.sleep(0.02)
    finally:
        if viewer:
            viewer.close()

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "retail_humanoid_telemetry.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["second", "robot", "state", "x_m", "y_m", "carrying"])
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "scenario": "Retail backroom humanoid fulfillment",
        "model": "retail_backroom_humanoid_fulfillment",
        "duration_seconds": duration,
        "robots": 2,
        "scope": "workflow visualization only",
        "states_demonstrated": sorted({str(row["state"]) for row in rows}),
    }
    (output_dir / "retail_humanoid_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument("--duration", type=float, default=36.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    run(args.duration, args.viewer, args.output_dir)
