#!/usr/bin/env python3
"""Timed choreography for the public-restroom MuJoCo capability demo."""

from __future__ import annotations

import math

import mujoco


CLEANING_LOOP_SECONDS = 58.0
CHARGING_WAIT_SECONDS = 30.0
SECOND_LOOP_START_SECONDS = CLEANING_LOOP_SECONDS + CHARGING_WAIT_SECONDS
SEQUENCE_END_SECONDS = SECOND_LOOP_START_SECONDS + CLEANING_LOOP_SECONDS

DOOR_POSE = (-6.00, -1.35, 0.0, 0.0)
DOCK_POSE = (5.45, -0.70, 0.0, 0.0)
TOILET_1_X = -5.35
TOILET_2_X = -2.65
URINAL_X = 0.00


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def smooth(value: float) -> float:
    value = clamp(value)
    return value * value * (3.0 - 2.0 * value)


def blend(a: tuple[float, ...], b: tuple[float, ...], amount: float) -> tuple[float, ...]:
    amount = smooth(amount)
    return tuple(start + (end - start) * amount for start, end in zip(a, b))


def path_pose(progress: float, points: list[tuple[float, float, float]]) -> tuple[float, float, float, float]:
    progress = clamp(progress)
    scaled = progress * (len(points) - 1)
    index = min(int(scaled), len(points) - 2)
    local = scaled - index
    start, end = points[index], points[index + 1]
    x_pos, y_pos, z_pos = blend(start, end, local)
    yaw = math.atan2(end[1] - start[1], end[0] - start[0])
    return x_pos, y_pos, z_pos, yaw


def mocap_id(model: mujoco.MjModel, name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)
    if body_id < 0 or model.body_mocapid[body_id] < 0:
        raise ValueError(f"Missing MuJoCo mocap body: {name}")
    return int(model.body_mocapid[body_id])


def set_mocap(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    name: str,
    pose: tuple[float, float, float, float],
) -> None:
    x_pos, y_pos, z_pos, yaw = pose
    index = mocap_id(model, name)
    data.mocap_pos[index] = (x_pos, y_pos, z_pos)
    data.mocap_quat[index] = (math.cos(yaw / 2.0), 0.0, 0.0, math.sin(yaw / 2.0))


def relative_xy(pose: tuple[float, float, float, float], forward: float, lateral: float) -> tuple[float, float]:
    x_pos, y_pos, _, yaw = pose
    return (
        x_pos + forward * math.cos(yaw) - lateral * math.sin(yaw),
        y_pos + forward * math.sin(yaw) + lateral * math.cos(yaw),
    )


def place_robot_and_arms(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    pose: tuple[float, float, float, float],
    arm_mode: str = "swiffer",
    motion: float = 0.0,
) -> None:
    set_mocap(model, data, "cleaning_humanoid", pose)
    _, _, _, yaw = pose

    if arm_mode == "sink":
        arm_height = 1.30
        forward = 0.24
        swing = 0.16 * math.sin(motion * 2.0 * math.pi)
    elif arm_mode == "mirror":
        arm_height = 1.88
        forward = 0.34
        swing = 0.22 * math.sin(motion * 4.0 * math.pi)
    else:
        arm_height = 1.48
        forward = 0.05
        swing = 0.05 * math.sin(motion * 2.0 * math.pi)

    left_x, left_y = relative_xy(pose, forward, 0.25 + swing)
    right_x, right_y = relative_xy(pose, forward, -0.25 - swing)
    set_mocap(model, data, "left_arm", (left_x, left_y, arm_height, yaw + swing))
    set_mocap(model, data, "right_arm", (right_x, right_y, arm_height, yaw - swing))


def place_swiffer(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    robot_pose: tuple[float, float, float, float],
    lateral: float = 0.0,
    forward: float = 0.72,
) -> None:
    tool_x, tool_y = relative_xy(robot_pose, forward, lateral)
    set_mocap(model, data, "cleaning_tool", (tool_x, tool_y, 0.72, robot_pose[3]))


def three_pass_lateral(cleaning_seconds: float) -> tuple[float, str]:
    """Return left, right, then center Swiffer motion for a 5.5-second pass."""
    if cleaning_seconds < 1.8:
        return -0.38 + 0.08 * math.sin(cleaning_seconds * math.pi * 2.0), "left side"
    if cleaning_seconds < 3.6:
        local = cleaning_seconds - 1.8
        return 0.38 + 0.08 * math.sin(local * math.pi * 2.0), "right side"
    local = cleaning_seconds - 3.6
    return 0.18 * math.sin(local * math.pi * 2.6), "middle"


def fixture_task(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    local_seconds: float,
    start: tuple[float, float, float],
    fixture_x: float,
    label: str,
    work_y: float = 2.55,
) -> str:
    approach = (fixture_x, 1.05, 0.0)
    work = (fixture_x, work_y, 0.0)
    if local_seconds < 2.0:
        pose = path_pose(local_seconds / 2.0, [start, approach, work])
        place_robot_and_arms(model, data, pose, motion=local_seconds / 2.0)
        place_swiffer(model, data, pose)
        return f"enter {label} bay"
    if local_seconds < 7.5:
        pose = (fixture_x, work_y, 0.0, math.pi / 2.0)
        lateral, pass_name = three_pass_lateral(local_seconds - 2.0)
        place_robot_and_arms(model, data, pose, motion=(local_seconds - 2.0) / 5.5)
        place_swiffer(model, data, pose, lateral=lateral, forward=0.78)
        return f"Swiffer {label}: {pass_name}"
    pose = path_pose((local_seconds - 7.5) / 1.5, [work, approach])
    place_robot_and_arms(model, data, pose, motion=(local_seconds - 7.5) / 1.5)
    place_swiffer(model, data, pose)
    return f"exit {label} bay"


def floor_task(model: mujoco.MjModel, data: mujoco.MjData, local_seconds: float) -> str:
    points = [
        (URINAL_X, 1.05, 0.0),
        (-3.2, 0.55, 0.0),
        (3.4, 0.55, 0.0),
        (-3.2, -0.65, 0.0),
        (3.4, -0.65, 0.0),
        (0.0, -1.55, 0.0),
    ]
    pose = path_pose(local_seconds / 8.0, points)
    place_robot_and_arms(model, data, pose, motion=local_seconds / 8.0)
    place_swiffer(model, data, pose, lateral=0.44 * math.sin(local_seconds * math.pi * 1.8))
    return "Swiffer open floor"


def sink_task(model: mujoco.MjModel, data: mujoco.MjData, local_seconds: float) -> str:
    floor_end = (0.0, -1.55, 0.0)
    sink_pose = (1.20, -2.75, 0.0, -math.pi / 2.0)
    if local_seconds < 2.0:
        pose = path_pose(local_seconds / 2.0, [floor_end, (1.20, -2.20, 0.0), (1.20, -2.75, 0.0)])
        place_robot_and_arms(model, data, pose, motion=local_seconds / 2.0)
        place_swiffer(model, data, pose)
        return "approach sinks"
    if local_seconds < 4.5:
        motion = (local_seconds - 2.0) / 2.5
        place_robot_and_arms(model, data, sink_pose, arm_mode="sink", motion=motion)
        set_mocap(model, data, "cleaning_tool", (1.90, -2.45, 0.72, 0.0))
        return "wipe sinks with both arms"
    if local_seconds < 8.0:
        motion = (local_seconds - 4.5) / 3.5
        place_robot_and_arms(model, data, sink_pose, arm_mode="mirror", motion=motion)
        set_mocap(model, data, "cleaning_tool", (1.90, -2.45, 0.72, 0.0))
        return "wipe mirrors with both arms"
    motion = (local_seconds - 8.0) / 2.0
    place_robot_and_arms(model, data, sink_pose, motion=motion)
    place_swiffer(model, data, sink_pose, lateral=0.42 * math.sin(motion * math.pi * 4.0), forward=0.40)
    return "Swiffer sink-area floor"


def door_to_dock_task(model: mujoco.MjModel, data: mujoco.MjData, local_seconds: float) -> str:
    sink_pose = (1.20, -2.75, 0.0)
    if local_seconds < 2.5:
        pose = path_pose(local_seconds / 2.5, [sink_pose, (0.0, -1.6, 0.0), DOOR_POSE[:3]])
        label = "return to doorway"
    else:
        pose = path_pose((local_seconds - 2.5) / 7.5, [DOOR_POSE[:3], (-2.0, -1.0, 0.0), (2.2, -0.8, 0.0), DOCK_POSE[:3]])
        label = "Swiffer doorway-to-charging route"
    place_robot_and_arms(model, data, pose, motion=local_seconds / 10.0)
    place_swiffer(model, data, pose, lateral=0.40 * math.sin(local_seconds * math.pi * 1.6))
    return label


def cleaning_loop(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    seconds: float,
    loop_number: int,
) -> tuple[str, str]:
    if seconds < 3.0:
        if loop_number == 1:
            pose = DOOR_POSE
            state = "opening overhead audit view"
        else:
            pose = path_pose(seconds / 3.0, [DOCK_POSE[:3], (1.5, -0.8, 0.0), DOOR_POSE[:3]])
            state = "begin second cleaning loop"
        place_robot_and_arms(model, data, pose, motion=seconds / 3.0)
        place_swiffer(model, data, pose)
        return "top_overview", state
    if seconds < 12.0:
        state = fixture_task(model, data, seconds - 3.0, DOOR_POSE[:3], TOILET_1_X, "toilet 1")
        return "fixture_cleaning", state
    if seconds < 21.0:
        state = fixture_task(model, data, seconds - 12.0, (TOILET_1_X, 1.05, 0.0), TOILET_2_X, "toilet 2")
        return "fixture_cleaning", state
    if seconds < 30.0:
        state = fixture_task(
            model,
            data,
            seconds - 21.0,
            (TOILET_2_X, 1.05, 0.0),
            URINAL_X,
            "urinal",
            work_y=3.15,
        )
        return "fixture_cleaning", state
    if seconds < 38.0:
        return "floor_cleaning", floor_task(model, data, seconds - 30.0)
    if seconds < 48.0:
        return "sink_cleaning", sink_task(model, data, seconds - 38.0)
    return "toilet_cleaning", door_to_dock_task(model, data, seconds - 48.0)


def hold_at_charger(model: mujoco.MjModel, data: mujoco.MjData) -> None:
    place_robot_and_arms(model, data, DOCK_POSE, arm_mode="swiffer")
    set_mocap(model, data, "cleaning_tool", (5.15, -1.48, 0.72, 0.0))


def update(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    elapsed_seconds: float,
) -> tuple[str, str, int]:
    """Update the complete two-loop sequence and return camera, state, and loop."""
    elapsed_seconds = max(0.0, elapsed_seconds)
    set_mocap(model, data, "paper_refill", (5.75, 1.05, 0.75, 0.0))
    set_mocap(model, data, "trash_bag", (-2.50, -3.65, 0.95, 0.0))

    if elapsed_seconds < CLEANING_LOOP_SECONDS:
        camera, state = cleaning_loop(model, data, elapsed_seconds, 1)
        return camera, state, 1
    if elapsed_seconds < SECOND_LOOP_START_SECONDS:
        hold_at_charger(model, data)
        remaining = math.ceil(SECOND_LOOP_START_SECONDS - elapsed_seconds)
        return "toilet_cleaning", f"charging wait: {remaining} seconds remaining", 1
    if elapsed_seconds < SEQUENCE_END_SECONDS:
        camera, state = cleaning_loop(model, data, elapsed_seconds - SECOND_LOOP_START_SECONDS, 2)
        return camera, state, 2

    hold_at_charger(model, data)
    return "top_overview", "two cleaning loops complete; stopped at charging station", 2
