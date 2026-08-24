"""Order-picking half of the retail backroom MuJoCo visualization.

Both humanoids retrieve requested merchandise from different stock levels and
place it on the courtesy drop-off table. The sequence keeps robot centers
outside furniture footprints. It is an operations illustration, not a
collision-avoidance or grasping controller.
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
    (-4.45, -0.85, 0.0),
]
GREEN_GROUND_PICK_ROUTE = [
    (-4.30, 2.15, 0.0),
    (-2.50, 1.35, 0.0),
    (0.00, 1.35, 0.0),
    (1.80, 1.75, 0.0),
    (3.15, 2.05, 0.0),
]
GREEN_DROPOFF_ROUTE = [
    (3.15, 2.05, 0.0),
    (1.50, 1.55, 0.0),
    (0.00, 1.35, 0.0),
    (-2.50, 1.35, 0.0),
    (-4.45, 0.85, 0.0),
]
GREEN_RETURN_ROUTE = [
    (-4.45, 0.85, 0.0),
    (-2.50, 1.35, 0.0),
    (-4.30, 2.15, 0.0),
]

BLUE_ITEM_HOME: Pose = (3.20, -1.55, 1.32, 0.0)
BLUE_ITEM_DROPOFF: Pose = (-5.55, -0.85, 1.19, 0.0)
GREEN_ITEM_HOME: Pose = (3.15, 2.92, 1.52, 0.0)
GREEN_ITEM_DROPOFF: Pose = (-5.55, 0.85, 1.19, 0.0)


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
        return pose, held_item(pose), "blue_carry_to_courtesy_table", True
    if progress < 0.88:
        pose = (-4.45, -0.85, 0.0, math.pi)
        item = blend(held_item(pose), BLUE_ITEM_DROPOFF, (progress - 0.80) / 0.08)
        return pose, item, "blue_courtesy_dropoff", progress < 0.86
    pose = path_pose((progress - 0.88) / 0.12, [(-4.45, -0.85, 0.0), (-4.20, -0.85, 0.0)])
    return pose, BLUE_ITEM_DROPOFF, "blue_inventory_confirmed", False


def green_sequence(progress: float) -> tuple[Pose, Pose, str, bool]:
    if progress < 0.08:
        return (-4.30, 2.15, 0.0, 0.0), GREEN_ITEM_HOME, "green_receive_pick_request", False
    if progress < 0.32:
        pose = path_pose((progress - 0.08) / 0.24, GREEN_GROUND_PICK_ROUTE)
        return pose, GREEN_ITEM_HOME, "green_walk_to_ground_stock", False
    if progress < 0.40:
        pose = GREEN_GROUND_PICK_ROUTE[-1] + (math.pi / 2,)
        item = blend(GREEN_ITEM_HOME, held_item(pose), (progress - 0.32) / 0.08)
        return pose, item, "green_pick_requested_carton", progress >= 0.37
    if progress < 0.78:
        pose = path_pose((progress - 0.40) / 0.38, GREEN_DROPOFF_ROUTE)
        return pose, held_item(pose), "green_carry_to_courtesy_table", True
    if progress < 0.86:
        pose = (-4.45, 0.85, 0.0, math.pi)
        item = blend(held_item(pose), GREEN_ITEM_DROPOFF, (progress - 0.78) / 0.08)
        return pose, item, "green_courtesy_dropoff", progress < 0.84
    pose = path_pose((progress - 0.86) / 0.14, GREEN_RETURN_ROUTE)
    return pose, GREEN_ITEM_DROPOFF, "green_inventory_confirmed", False


def frame_at(progress: float) -> RetailFrame:
    progress = clamp(progress)
    blue_pose, blue_item, blue_state, blue_carrying = blue_sequence(progress)
    green_pose, green_item, green_state, green_carrying = green_sequence(progress)
    camera = "overview"
    if 0.20 <= progress < 0.58:
        camera = "stairs"
    elif 0.58 <= progress < 0.76:
        camera = "shelves"
    elif progress >= 0.76:
        camera = "courtesy"
    return RetailFrame(
        blue_pose=blue_pose,
        blue_item_pose=blue_item,
        blue_state=blue_state,
        blue_carrying=blue_carrying,
        green_pose=green_pose,
        green_item_pose=green_item,
        green_state=green_state,
        green_carrying=green_carrying,
        camera=camera,
    )


def route_clearance_report(samples: int = 501) -> dict[str, float | bool]:
    """Check 2-D center clearance against furniture footprints and each robot."""
    # Expanded by the humanoid's 0.23 m body half-width plus a 0.10 m visual margin.
    obstacles = {
        "courtesy_dropoff_table": (-6.63, -4.57, -1.88, 1.88),
        "ground_stock_rack": (2.14, 4.16, 2.17, 4.53),
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
