"""Shared scripted sequence for the retail backroom MuJoCo visualization.

The sequence deliberately keeps robot centers outside the visual footprints of
the counter, receiving table, and put-away cart.  It is an operations
illustration, not a collision-avoidance or grasping controller.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


Pose = tuple[float, float, float, float]


@dataclass(frozen=True)
class RetailFrame:
    blue_pose: Pose
    blue_item_pose: Pose
    blue_state: str
    blue_carrying: bool
    green_pose: Pose
    green_item_pose: Pose
    green_state: str
    green_carrying: bool
    camera: str = "overview"


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def smooth(value: float) -> float:
    value = clamp(value)
    return value * value * (3.0 - 2.0 * value)


def blend(a: tuple[float, ...], b: tuple[float, ...], amount: float) -> tuple[float, ...]:
    amount = smooth(amount)
    return tuple(start + (end - start) * amount for start, end in zip(a, b))


def path_pose(progress: float, points: list[tuple[float, float, float]]) -> Pose:
    progress = clamp(progress)
    scaled = progress * (len(points) - 1)
    index = min(int(scaled), len(points) - 2)
    local = scaled - index
    start, end = points[index], points[index + 1]
    x_pos, y_pos, z_pos = blend(start, end, local)
    yaw = math.atan2(end[1] - start[1], end[0] - start[0])
    return x_pos, y_pos, z_pos, yaw


def held_item(pose: Pose, height: float = 1.08) -> Pose:
    x_pos, y_pos, z_pos, yaw = pose
    return (
        x_pos + 0.42 * math.cos(yaw),
        y_pos + 0.42 * math.sin(yaw),
        z_pos + height,
        yaw,
    )


BLUE_STAIR_ROUTE = [
    (-4.20, -0.85, 0.0),
    (-4.20, -1.55, 0.0),
    (-1.00, -1.55, 0.0),
    (-0.40, -1.55, 0.20),
    (0.25, -1.55, 0.40),
    (0.82, -1.55, 0.60),
    (1.55, -1.55, 1.0),
    (2.72, -1.55, 1.0),
]
BLUE_RETURN_ROUTE = [
    *reversed(BLUE_STAIR_ROUTE),
    (-4.20, -0.85, 0.0),
    (-4.65, -0.85, 0.0),
]
GREEN_RECEIVING_ROUTE = [
    (-4.30, 2.15, 0.0),
    (-2.50, 1.35, 0.0),
    (0.00, 1.35, 0.0),
    (1.80, 1.55, 0.0),
]
GREEN_PUTAWAY_ROUTE = [
    (1.80, 1.55, 0.0),
    (0.00, 1.20, 0.0),
    (-2.30, 1.50, 0.0),
    (-3.10, 2.60, 0.0),
    (-3.10, 3.35, 0.0),
]
GREEN_RETURN_ROUTE = [
    (-3.10, 3.35, 0.0),
    (-2.30, 2.20, 0.0),
    (-2.50, 1.35, 0.0),
    (-4.30, 2.15, 0.0),
]

BLUE_ITEM_HOME: Pose = (3.20, -1.55, 1.32, 0.0)
BLUE_ITEM_HANDOFF: Pose = (-5.25, -0.85, 1.24, 0.0)
GREEN_ITEM_HOME: Pose = (2.20, 2.70, 0.85, 0.0)
GREEN_ITEM_PUTAWAY: Pose = (-3.10, 3.88, 1.24, 0.0)


def blue_sequence(progress: float) -> tuple[Pose, Pose, str, bool]:
    if progress < 0.34:
        pose = path_pose(progress / 0.34, BLUE_STAIR_ROUTE)
        return pose, BLUE_ITEM_HOME, "blue_walk_stair_route", False
    if progress < 0.42:
        pose = (2.72, -1.55, 1.0, 0.0)
        item = blend(BLUE_ITEM_HOME, held_item(pose), (progress - 0.34) / 0.08)
        return pose, item, "blue_verify_and_pick", progress >= 0.39
    if progress < 0.80:
        pose = path_pose((progress - 0.42) / 0.38, BLUE_RETURN_ROUTE)
        return pose, held_item(pose), "blue_carry_to_employee", True
    if progress < 0.88:
        pose = (-4.65, -0.85, 0.0, math.pi)
        item = blend(held_item(pose), BLUE_ITEM_HANDOFF, (progress - 0.80) / 0.08)
        return pose, item, "blue_employee_handoff", progress < 0.86
    pose = path_pose((progress - 0.88) / 0.12, [(-4.65, -0.85, 0.0), (-4.20, -0.85, 0.0)])
    return pose, BLUE_ITEM_HANDOFF, "blue_inventory_confirmed", False


def green_sequence(progress: float) -> tuple[Pose, Pose, str, bool]:
    if progress < 0.08:
        return (-4.30, 2.15, 0.0, 0.0), GREEN_ITEM_HOME, "green_receive_putaway_request", False
    if progress < 0.30:
        pose = path_pose((progress - 0.08) / 0.22, GREEN_RECEIVING_ROUTE)
        return pose, GREEN_ITEM_HOME, "green_walk_clear_receiving_aisle", False
    if progress < 0.38:
        pose = (1.80, 1.55, 0.0, math.pi / 2)
        item = blend(GREEN_ITEM_HOME, held_item(pose), (progress - 0.30) / 0.08)
        return pose, item, "green_pick_receiving_carton", progress >= 0.35
    if progress < 0.68:
        pose = path_pose((progress - 0.38) / 0.30, GREEN_PUTAWAY_ROUTE)
        return pose, held_item(pose), "green_carry_carton_to_putaway", True
    if progress < 0.78:
        pose = (-3.10, 3.35, 0.0, math.pi / 2)
        item = blend(held_item(pose), GREEN_ITEM_PUTAWAY, (progress - 0.68) / 0.10)
        return pose, item, "green_place_carton_on_putaway_cart", progress < 0.75
    pose = path_pose((progress - 0.78) / 0.22, GREEN_RETURN_ROUTE)
    return pose, GREEN_ITEM_PUTAWAY, "green_putaway_complete", False


def frame_at(progress: float) -> RetailFrame:
    progress = clamp(progress)
    blue_pose, blue_item, blue_state, blue_carrying = blue_sequence(progress)
    green_pose, green_item, green_state, green_carrying = green_sequence(progress)
    return RetailFrame(
        blue_pose=blue_pose,
        blue_item_pose=blue_item,
        blue_state=blue_state,
        blue_carrying=blue_carrying,
        green_pose=green_pose,
        green_item_pose=green_item,
        green_state=green_state,
        green_carrying=green_carrying,
    )


def route_clearance_report(samples: int = 501) -> dict[str, float | bool]:
    """Check 2-D center clearance against furniture footprints and each robot."""
    # Expanded by the humanoid's 0.23 m body half-width plus a 0.10 m visual margin.
    obstacles = {
        "handoff_counter": (-6.38, -4.82, -1.88, 1.88),
        "receiving_table": (0.22, 3.38, 1.72, 3.68),
        "putaway_cart": (-4.13, -2.07, 3.47, 5.03),
    }
    minimum_robot_separation = float("inf")
    obstacle_clear = True
    for index in range(samples):
        frame = frame_at(index / (samples - 1))
        centers = (frame.blue_pose[:2], frame.green_pose[:2])
        minimum_robot_separation = min(
            minimum_robot_separation,
            math.dist(centers[0], centers[1]),
        )
        for x_pos, y_pos in centers:
            for x_min, x_max, y_min, y_max in obstacles.values():
                if x_min < x_pos < x_max and y_min < y_pos < y_max:
                    obstacle_clear = False
    return {
        "furniture_clearance_passed": obstacle_clear,
        "minimum_robot_center_separation_m": round(minimum_robot_separation, 3),
        "robot_separation_passed": minimum_robot_separation >= 0.70,
    }
