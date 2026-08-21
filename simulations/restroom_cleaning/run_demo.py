#!/usr/bin/env python3
"""Open and run the two-loop public-restroom cleaning audit in MuJoCo."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import mujoco
from mujoco import viewer as mujoco_viewer

from restroom_sequence import SEQUENCE_END_SECONDS, update


def camera_id(model: mujoco.MjModel, name: str) -> int:
    result = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, name)
    if result < 0:
        raise ValueError(f"Missing fixed camera: {name}")
    return int(result)


def run(duration: float) -> None:
    xml_path = Path(__file__).with_name("restroom.xml")
    model = mujoco.MjModel.from_xml_path(str(xml_path))
    data = mujoco.MjData(model)
    started = time.monotonic()
    current_camera = ""
    current_state = ""

    with mujoco_viewer.launch_passive(model, data) as viewer:
        viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED

        while viewer.is_running():
            elapsed = time.monotonic() - started
            camera, state, loop_number = update(model, data, elapsed)

            if camera != current_camera:
                viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
                viewer.cam.fixedcamid = camera_id(model, camera)
                current_camera = camera

            if state != current_state:
                shown_time = min(elapsed, SEQUENCE_END_SECONDS)
                print(f"[{shown_time:6.1f}s] loop {loop_number}: {state}")
                current_state = state

            mujoco.mj_forward(model, data)
            viewer.sync()

            if duration > 0.0 and elapsed >= duration:
                break
            time.sleep(0.02)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--duration",
        type=float,
        default=0.0,
        help=(
            "Seconds before the window closes. The default 0 keeps the stopped "
            "final scene open after the 146-second two-loop audit."
        ),
    )
    parser.add_argument(
        "--viewer",
        action="store_true",
        help="Accepted for compatibility; this command always opens the viewer.",
    )
    args = parser.parse_args()
    run(args.duration)


if __name__ == "__main__":
    main()
