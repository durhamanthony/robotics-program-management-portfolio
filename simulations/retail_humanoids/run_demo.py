#!/usr/bin/env python3
"""Validate the composed retail inbound-to-fulfillment operations story."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from pathlib import Path

import mujoco

from retail_sequence import frame_at, route_clearance_report

INBOUND_DIR = Path(__file__).resolve().parents[1] / "retail_inbound"
sys.path.insert(0, str(INBOUND_DIR))
from retail_inbound_sequence import route_validation_report as inbound_validation_report


def mocap_id(model: mujoco.MjModel, body_name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, body_name)
    return int(model.body_mocapid[body_id])


def geom_id(model: mujoco.MjModel, geom_name: str) -> int:
    result = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, geom_name)
    if result < 0:
        raise RuntimeError(f"retail.xml is missing required geometry {geom_name!r}")
    return int(result)


def set_pose(data: mujoco.MjData, index: int, *pose: float) -> None:
    data.mocap_pos[index] = pose[:3]
    if len(pose) == 4:
        yaw = pose[3]
        data.mocap_quat[index] = (math.cos(yaw / 2), 0.0, 0.0, math.sin(yaw / 2))
    elif len(pose) == 7:
        data.mocap_quat[index] = pose[3:]
    else:
        raise ValueError(f"Unsupported mocap pose with {len(pose)} values")


def run(duration: float, viewer_enabled: bool, output_dir: Path) -> None:
    model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("retail.xml")))
    data = mujoco.MjData(model)
    robot_ids = [mocap_id(model, "robot_1"), mocap_id(model, "robot_2")]
    item_ids = [mocap_id(model, "shoe_box_1"), mocap_id(model, "shoe_box_2")]
    human_ids = [
        mocap_id(model, "sales_associate"),
        mocap_id(model, "sales_associate_left_upper_arm"),
        mocap_id(model, "sales_associate_left_forearm"),
        mocap_id(model, "sales_associate_right_upper_arm"),
        mocap_id(model, "sales_associate_right_forearm"),
    ]
    item_geom_ids = [geom_id(model, "shoe_box_1_geom"), geom_id(model, "shoe_box_2_geom")]
    human_geom_ids = [
        index
        for index in range(model.ngeom)
        if (mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, index) or "").startswith("human_")
    ]
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
            frame = frame_at((elapsed % 18.0) / 18.0)
            robot_frames = [
                (frame.blue_pose, frame.blue_item_pose, frame.blue_state, frame.blue_carrying),
                (frame.green_pose, frame.green_item_pose, frame.green_state, frame.green_carrying),
            ]
            for index, (pose, item_pose, state, carrying) in enumerate(robot_frames):
                x, y, z, yaw = pose
                set_pose(data, robot_ids[index], x, y, z, yaw)
                set_pose(data, item_ids[index], *item_pose)
                sample = int(elapsed)
                if sample != last_sample:
                    rows.append({
                        "table_title": "Table 1. Retail humanoid scripted telemetry",
                        "second": sample,
                        "robot": index + 1,
                        "state": state,
                        "x_m": round(x, 2),
                        "y_m": round(y, 2),
                        "z_m": round(z, 2),
                        "carrying": carrying,
                        "evidence_class": "Derived calculation",
                        "confidence": "Low",
                        "source_or_validation": "Deterministic scripted MuJoCo workflow; not production autonomy evidence",
                    })
            for human_id, pose in zip(human_ids, (
                frame.human_pose,
                frame.human_left_upper_arm_pose,
                frame.human_left_forearm_pose,
                frame.human_right_upper_arm_pose,
                frame.human_right_forearm_pose,
            )):
                set_pose(data, human_id, *pose)
            for human_geom_id in human_geom_ids:
                model.geom_rgba[human_geom_id][3] = 1.0 if frame.human_visible else 0.0
            model.geom_rgba[item_geom_ids[0]][3] = 1.0 if frame.blue_item_visible else 0.0
            model.geom_rgba[item_geom_ids[1]][3] = 1.0 if frame.green_item_visible else 0.0
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
        writer = csv.DictWriter(handle, fieldnames=[
            "table_title", "second", "robot", "state", "x_m", "y_m", "z_m", "carrying",
            "evidence_class", "confidence", "source_or_validation",
        ])
        writer.writeheader()
        writer.writerows(rows)
    states = sorted({str(row["state"]) for row in rows})
    required_states = {
        "blue_walk_stair_route", "blue_verify_and_pick", "blue_carry_to_courtesy_table",
        "blue_courtesy_dropoff", "blue_turn_toward_shelves", "blue_wait_for_human_pickup",
        "green_receive_pick_request", "green_walk_to_ground_stock",
        "green_pick_requested_carton", "green_carry_to_courtesy_table",
        "green_courtesy_dropoff", "green_turn_toward_shelves", "green_wait_for_human_pickup",
    }
    clearance = route_clearance_report()
    inbound = inbound_validation_report()
    final_frame = frame_at(1.0)
    summary = {
        "scenario": "Retail backroom inbound receiving and fulfillment",
        "models": ["retail_backroom_inbound_receiving_v2", "retail_backroom_humanoid_fulfillment_v6"],
        "duration_seconds": duration,
        "robots": 2,
        "scope": "workflow visualization only",
        "states_demonstrated": states,
        "validation": {
            "required_states_present": required_states.issubset(states),
            "both_robots_sampled": {int(row["robot"]) for row in rows} == {1, 2},
            "blue_item_carry_observed": any(row["robot"] == 1 and row["carrying"] for row in rows),
            "green_item_carry_observed": any(row["robot"] == 2 and row["carrying"] for row in rows),
            "human_service_window_pickup_complete": final_frame.human_state == "human_departed",
            "human_turn_walk_and_exit_complete": final_frame.human_state == "human_departed" and not final_frame.human_visible,
            "packages_removed_after_pickup": not final_frame.blue_item_visible and not final_frame.green_item_visible,
            "inbound_story_checks_passed": all(value for value in inbound.values() if isinstance(value, bool)),
            "inbound_story": inbound,
            **clearance,
            "camera_sequence": ["overview", "stairs", "shelves", "courtesy"],
            "stair_platform_height_m": 1.0,
        },
    }
    summary["passed"] = all(
        value for key, value in summary["validation"].items()
        if key not in {"camera_sequence", "stair_platform_height_m", "minimum_robot_center_separation_m", "inbound_story"}
    )
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
