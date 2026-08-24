#!/usr/bin/env python3
"""Run the generic OpenQuad productization and service-state visualization."""

from __future__ import annotations

import argparse
import csv
import json
import math
import time
from pathlib import Path

import mujoco


def smooth(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


def mocap_id(model: mujoco.MjModel, name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)
    if body_id < 0 or model.body_mocapid[body_id] < 0:
        raise ValueError(f"Missing mocap body: {name}")
    return int(model.body_mocapid[body_id])


def set_pose(data: mujoco.MjData, index: int, x: float, y: float, z: float, yaw: float = 0.0) -> None:
    data.mocap_pos[index] = (x, y, z)
    data.mocap_quat[index] = (math.cos(yaw / 2), 0.0, 0.0, math.sin(yaw / 2))


def pose_at(elapsed: float) -> tuple[float, float, float, float, str]:
    cycle = elapsed % 18.0
    stations = [(-5.2, -2.0), (-2.5, -2.0), (0.0, 0.0), (2.8, 1.8), (5.2, 1.8)]
    states = ["source_and_serial", "calibration", "functional_test", "fault_evidence", "replacement_rotation", "ready_for_service"]
    index = min(int(cycle // 3.0), 5)
    if index == 5:
        return 5.2, 1.8, 0.0, 0.0, states[index]
    x0, y0 = stations[min(index, len(stations) - 1)]
    x1, y1 = stations[min(index + 1, len(stations) - 1)]
    local = smooth((cycle % 3.0) / 3.0)
    x = x0 + (x1 - x0) * local
    y = y0 + (y1 - y0) * local
    yaw = math.atan2(y1 - y0, x1 - x0)
    return x, y, 0.0, yaw, states[index]


def run(viewer_enabled: bool, duration: float, output_dir: Path) -> None:
    model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("open_quadruped.xml")))
    data = mujoco.MjData(model)
    test_id = mocap_id(model, "test_unit")
    swap_id = mocap_id(model, "swap_unit")
    start = time.monotonic()
    elapsed = 0.0
    rows: list[dict[str, object]] = []
    last_second = -1
    viewer = None
    if viewer_enabled:
        from mujoco import viewer as mujoco_viewer
        viewer = mujoco_viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False)
        camera = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, "overview")
        if camera < 0:
            raise RuntimeError("open_quadruped.xml is missing the overview camera")
        viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
        viewer.cam.fixedcamid = camera
    try:
        while elapsed < duration:
            x, y, z, yaw, state = pose_at(elapsed)
            set_pose(data, test_id, x, y, z, yaw)
            if state == "replacement_rotation":
                local = smooth((elapsed % 3.0) / 3.0)
                set_pose(data, swap_id, 5.2 - 2.4 * local, -2.2 + 4.0 * local, 0.0, math.pi * 0.75)
            else:
                set_pose(data, swap_id, 5.2, -2.2, 0.0, math.pi)
            mujoco.mj_forward(model, data)
            second = int(elapsed)
            if second != last_second:
                rows.append({"second": second, "unit_id": "OQ-012", "state": state, "x_m": round(x, 2), "y_m": round(y, 2), "supported_release": "1.0.0-rc3"})
                last_second = second
            if viewer:
                if not viewer.is_running():
                    break
                viewer.sync()
                time.sleep(0.02)
                elapsed = time.monotonic() - start
            else:
                elapsed += 0.02
    finally:
        if viewer:
            viewer.close()
    output_dir.mkdir(parents=True, exist_ok=True)
    telemetry = output_dir / "open_quadruped_raas_telemetry.csv"
    with telemetry.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["second", "unit_id", "state", "x_m", "y_m", "supported_release"])
        writer.writeheader()
        writer.writerows(rows)
    demonstrated = sorted({str(row["state"]) for row in rows})
    summary = {
        "scenario": "Open-source quadruped RaaS productization",
        "model": "generic_openquad_validation_cell",
        "scope": "program workflow visualization only; not an upstream digital twin",
        "states_demonstrated": demonstrated,
        "validation_passed": len(demonstrated) == 6,
    }
    (output_dir / "open_quadruped_raas_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument("--duration", type=float, default=36.0)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    run(args.viewer, args.duration, args.output_dir)
