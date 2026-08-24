#!/usr/bin/env python3
"""Render the browser videos directly from the portfolio's MuJoCo models."""

from __future__ import annotations

import argparse
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import imageio_ffmpeg
import mujoco
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = ROOT / "media" / "videos"
RESTROOM_SIM_DIR = ROOT / "simulations" / "restroom_cleaning"
RETAIL_SIM_DIR = ROOT / "simulations" / "retail_humanoids"
SECURITY_SIM_DIR = ROOT / "simulations" / "quadruped_security"
sys.path.insert(0, str(RESTROOM_SIM_DIR))
sys.path.insert(0, str(RETAIL_SIM_DIR))
sys.path.insert(0, str(SECURITY_SIM_DIR))

from restroom_sequence import SEQUENCE_END_SECONDS, update as restroom_sequence_update
from retail_sequence import frame_at as retail_frame_at
from security_sequence import frame_at as security_frame_at


def smooth(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


def between(value: float, start: float, end: float) -> float:
    return smooth((value - start) / max(1e-6, end - start))


def blend(a: tuple[float, ...], b: tuple[float, ...], amount: float) -> tuple[float, ...]:
    amount = smooth(amount)
    return tuple(x + (y - x) * amount for x, y in zip(a, b))


def path_pose(progress: float, points: list[tuple[float, float, float]]) -> tuple[float, float, float, float]:
    progress = max(0.0, min(1.0, progress))
    scaled = progress * (len(points) - 1)
    index = min(int(scaled), len(points) - 2)
    local = scaled - index
    start, end = points[index], points[index + 1]
    x_pos, y_pos, z_pos = blend(start, end, local)
    yaw = math.atan2(end[1] - start[1], end[0] - start[0])
    return x_pos, y_pos, z_pos, yaw


def body_mocap_id(model: mujoco.MjModel, name: str) -> int:
    body = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)
    if body < 0 or model.body_mocapid[body] < 0:
        raise ValueError(f"Body {name!r} is not a MuJoCo mocap body")
    return int(model.body_mocapid[body])


def geom_id(model: mujoco.MjModel, name: str) -> int:
    result = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, name)
    if result < 0:
        raise ValueError(f"Missing MuJoCo geometry: {name}")
    return int(result)


def set_mocap(model: mujoco.MjModel, data: mujoco.MjData, name: str, pose: tuple[float, float, float, float]) -> None:
    x_pos, y_pos, z_pos, yaw = pose
    index = body_mocap_id(model, name)
    data.mocap_pos[index] = (x_pos, y_pos, z_pos)
    data.mocap_quat[index] = (math.cos(yaw / 2.0), 0.0, 0.0, math.sin(yaw / 2.0))


@dataclass(frozen=True)
class Scene:
    name: str
    xml: Path
    output: str
    duration: float
    update: Callable[[mujoco.MjModel, mujoco.MjData, float], str]


def retail_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    frame = retail_frame_at(t)
    set_mocap(model, data, "robot_1", frame.blue_pose)
    set_mocap(model, data, "shoe_box_1", frame.blue_item_pose)
    set_mocap(model, data, "robot_2", frame.green_pose)
    set_mocap(model, data, "shoe_box_2", frame.green_item_pose)
    return frame.camera


def security_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    frame = security_frame_at(t)
    set_mocap(model, data, "quadruped_01", frame.perimeter_pose)
    set_mocap(model, data, "quadruped_02", frame.stair_pose)
    set_mocap(model, data, "quadruped_03", frame.reserve_pose)
    beacon = geom_id(model, "event_beacon")
    model.geom_rgba[beacon] = (1.0, 0.08, 0.03, 1.0) if 0.34 < t < 0.60 else (1.0, 0.58, 0.05, 1.0)
    return frame.camera


def openquad_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    route = [(-5.2, -2.0, 0.0), (-2.5, -2.0, 0.0), (0.0, 0.0, 0.0), (2.8, 1.8, 0.0), (5.2, 1.8, 0.0)]
    set_mocap(model, data, "test_unit", path_pose(min(t / 0.82, 1.0), route))
    if t < 0.66:
        replacement = (5.2, -2.2, 0.0, math.pi)
    else:
        replacement = path_pose((t - 0.66) / 0.34, [(5.2, -2.2, 0.0), (4.2, -0.5, 0.0), (2.8, 1.8, 0.0)])
    set_mocap(model, data, "swap_unit", replacement)
    beacon = geom_id(model, "fault_beacon")
    model.geom_rgba[beacon] = (0.86, 0.10, 0.08, 1.0) if 0.50 < t < 0.72 else (0.94, 0.57, 0.08, 1.0)
    return "test_lane" if 0.28 < t < 0.78 else "overview"


def restroom_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    camera, _, _ = restroom_sequence_update(model, data, t * SEQUENCE_END_SECONDS)
    return camera


def warehouse_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    worker = path_pose(min(t / 0.45, 1.0), [(-2.2, -1.5, 0.0), (-3.0, -1.5, 0.0), (-2.2, -1.5, 0.0), (0.0, -1.0, 0.0), (2.0, 0.0, 0.0)])
    set_mocap(model, data, "worker_1", worker)
    set_mocap(model, data, "worker_2", path_pose((t * 1.1) % 1.0, [(-2.2, 1.5, 0.0), (-3.0, 1.5, 0.0), (-1.0, 1.2, 0.0), (1.6, 0.5, 0.0), (-2.2, 1.5, 0.0)]))
    if t < 0.16:
        carton = path_pose(t / 0.16, [(-6.0, -1.5, 0.95), (-3.35, -1.5, 0.95)])
    elif t < 0.40:
        x_pos, y_pos, z_pos, yaw = worker
        carton = (x_pos + 0.42, y_pos, z_pos + 1.05, yaw)
    else:
        carton = (2.3, 0, 2.05, 0.0)
    set_mocap(model, data, "active_carton", carton)
    for index in range(1, 8):
        model.geom_rgba[geom_id(model, f"stack_{index}")][3] = 1.0 if t >= 0.12 + index * 0.055 else 0.0
    if t < 0.58:
        fork = (3.8, -3.8, 0.0, 0.0)
        load = (2.3, 0.0, 0.0, 0.0)
    elif t < 0.72:
        fork = path_pose((t - 0.58) / 0.14, [(3.8, -3.8, 0.0), (3.2, -1.5, 0.0), (2.0, 0.0, 0.0)])
        load = (2.3, 0.0, 0.0, 0.0)
    elif t < 0.90:
        fork = path_pose((t - 0.72) / 0.18, [(2.0, 0.0, 0.0), (5.0, 0.0, 0.0), (8.0, 0.0, 0.0)])
        load = (fork[0] + 0.9, fork[1], 0.0, fork[3])
    else:
        fork = path_pose((t - 0.90) / 0.10, [(8.0, 0.0, 0.0), (5.3, 0.0, 0.0), (3.8, -1.5, 0.0)])
        load = (8.7, 0.0, 0.45, 0.0)
    set_mocap(model, data, "forklift", fork)
    set_mocap(model, data, "pallet_load", load)
    replacement = (1.0, 3.6, 0.0, 0.0) if t < 0.92 else path_pose((t - 0.92) / 0.08, [(1.0, 3.6, 0.0), (1.4, 1.8, 0.0), (2.3, 0.0, 0.0)])
    set_mocap(model, data, "replacement_pallet", replacement)
    if t < 0.48:
        return "overview"
    if t < 0.72:
        return "pallet"
    return "truck"


SCENES = {
    scene.name: scene
    for scene in (
        Scene("retail", ROOT / "simulations/retail_humanoids/retail.xml", "retail-humanoid-fulfillment.mp4", 18.0, retail_update),
        Scene("security", ROOT / "simulations/quadruped_security/security.xml", "quadruped-night-security.mp4", 18.0, security_update),
        Scene("openquad", ROOT / "simulations/open_quadruped_raas/open_quadruped.xml", "open-quadruped-raas-productization.mp4", 14.0, openquad_update),
        Scene("restroom", ROOT / "simulations/restroom_cleaning/restroom.xml", "restroom-cleaning-humanoid.mp4", SEQUENCE_END_SECONDS, restroom_update),
        Scene("warehouse", ROOT / "simulations/warehouse_capability/warehouse.xml", "warehouse-palletizing-truck-loading.mp4", 16.0, warehouse_update),
    )
}

# Restroom v4.4 is an explicitly approved 146-second release asset.  Keep it
# available for an intentional `restroom` render, but never replace it during a
# bulk refresh of the other portfolio clips.
DEFAULT_SCENES = [name for name in SCENES if name != "restroom"]


def render(scene: Scene, width: int, height: int, fps: int) -> Path:
    model = mujoco.MjModel.from_xml_path(str(scene.xml))
    data = mujoco.MjData(model)
    renderer = mujoco.Renderer(model, height=height, width=width)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    output = VIDEO_DIR / scene.output
    command = [
        imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{width}x{height}", "-r", str(fps), "-i", "-", "-an",
        "-vcodec", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None
    try:
        frames = max(1, round(scene.duration * fps))
        for frame_index in range(frames):
            progress = frame_index / max(1, frames - 1)
            camera = scene.update(model, data, progress)
            mujoco.mj_forward(model, data)
            renderer.update_scene(data, camera=camera)
            process.stdin.write(np.ascontiguousarray(renderer.render()).tobytes())
    finally:
        process.stdin.close()
        return_code = process.wait()
        renderer.close()
    if return_code:
        raise RuntimeError(f"FFmpeg failed for {scene.name} with exit code {return_code}")
    print(f"Rendered {scene.name}: {output.relative_to(ROOT)}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenes", nargs="*", choices=sorted(SCENES))
    parser.add_argument("--width", type=int, default=960)
    parser.add_argument("--height", type=int, default=540)
    parser.add_argument("--fps", type=int, default=15)
    args = parser.parse_args()
    for name in (args.scenes or DEFAULT_SCENES):
        render(SCENES[name], args.width, args.height, args.fps)


if __name__ == "__main__":
    main()
