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
sys.path.insert(0, str(RESTROOM_SIM_DIR))

from restroom_sequence import SEQUENCE_END_SECONDS, update as restroom_sequence_update


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
    stairs = [(-4.8, -1.55, 0.0), (-1.0, -1.55, 0.0), (-0.4, -1.55, 0.20), (0.25, -1.55, 0.40), (0.82, -1.55, 0.60), (1.55, -1.55, 1.0), (3.65, -1.55, 1.0)]
    if t < 0.46:
        pose = path_pose(t / 0.46, stairs)
        carried = False
        camera = "overview"
    elif t < 0.56:
        pose = (3.65, -1.55, 1.0, 0.0)
        carried = t >= 0.50
        camera = "overview"
    elif t < 0.90:
        reverse = list(reversed(stairs)) + [(-4.9, -0.6, 0.0)]
        pose = path_pose((t - 0.56) / 0.34, reverse)
        carried = True
        camera = "overview"
    else:
        pose = (-4.9, -0.6, 0.0, math.pi)
        carried = False
        camera = "overview"
    set_mocap(model, data, "robot_1", pose)
    if carried:
        x_pos, y_pos, z_pos, yaw = pose
        set_mocap(model, data, "shoe_box_1", (x_pos + 0.42 * math.cos(yaw), y_pos + 0.42 * math.sin(yaw), z_pos + 1.08, yaw))
    elif t >= 0.90:
        set_mocap(model, data, "shoe_box_1", (-5.25, -0.6, 1.25, 0.0))
    else:
        set_mocap(model, data, "shoe_box_1", (3.65, -1.55, 1.32, 0.0))
    second = path_pose((t * 1.15) % 1.0, [(-4.3, 2.15, 0.0), (1.0, 2.15, 0.0), (3.5, 2.25, 0.0), (1.8, 2.7, 0.0), (-4.3, 2.15, 0.0)])
    set_mocap(model, data, "robot_2", second)
    return camera


def security_update(model: mujoco.MjModel, data: mujoco.MjData, t: float) -> str:
    route_a = [(-6.7, -5.1, 0.0), (5.7, -5.1, 0.0), (6.6, -1.4, 0.0), (6.6, 3.0, 0.0), (2.5, 5.1, 0.0)]
    route_b = [(-5.35, -5.1, 0.0), (-5.2, 2.8, 0.0), (-3.9, 3.85, 0.12), (2.25, 3.75, 0.0), (3.0, 3.75, 0.35), (3.7, 3.75, 0.72), (4.3, 3.75, 1.24)]
    set_mocap(model, data, "quadruped_01", path_pose(min(t / 0.72, 1.0), route_a))
    set_mocap(model, data, "quadruped_02", path_pose(min(t / 0.78, 1.0), route_b))
    reserve = (-4.0, -5.1, 0.0, 0.0) if t < 0.72 else path_pose((t - 0.72) / 0.28, [(-4.0, -5.1, 0.0), (-4.0, -5.55, 0.0)])
    set_mocap(model, data, "quadruped_03", reserve)
    beacon = geom_id(model, "event_beacon")
    model.geom_rgba[beacon] = (1.0, 0.08, 0.03, 1.0) if 0.34 < t < 0.60 else (1.0, 0.58, 0.05, 1.0)
    if t < 0.28:
        return "overview"
    if t < 0.58:
        return "gate"
    if t < 0.82:
        return "terrain"
    return "dock"


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
        Scene("retail", ROOT / "simulations/retail_humanoids/retail.xml", "retail-humanoid-fulfillment.mp4", 14.0, retail_update),
        Scene("security", ROOT / "simulations/quadruped_security/security.xml", "quadruped-night-security.mp4", 14.0, security_update),
        Scene("openquad", ROOT / "simulations/open_quadruped_raas/open_quadruped.xml", "open-quadruped-raas-productization.mp4", 14.0, openquad_update),
        Scene("restroom", ROOT / "simulations/restroom_cleaning/restroom.xml", "restroom-cleaning-humanoid.mp4", SEQUENCE_END_SECONDS, restroom_update),
        Scene("warehouse", ROOT / "simulations/warehouse_capability/warehouse.xml", "warehouse-palletizing-truck-loading.mp4", 16.0, warehouse_update),
    )
}


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
    for name in (args.scenes or list(SCENES)):
        render(SCENES[name], args.width, args.height, args.fps)


if __name__ == "__main__":
    main()
