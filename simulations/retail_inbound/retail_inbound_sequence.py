"""Deterministic inbound-receiving sequence for the retail backroom story.

The full pallet starts inside the truck. A robot-operated forklift backs down
the ramp and places the pallet in the receiving zone. Two humanoid visual
agents then move cartons to ground and raised storage racks. Motion is a
scripted operations illustration, not a locomotion or manipulation controller.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


Pose = tuple[float, float, float, float]


@dataclass(frozen=True)
class InboundFrame:
    forklift_pose: Pose
    pallet_pose: Pose
    low_worker_pose: Pose
    low_carton_pose: Pose
    low_state: str
    high_worker_pose: Pose
    high_carton_pose: Pose
    high_state: str
    camera: str


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


FORKLIFT_UNLOAD_ROUTE = [
    (7.60, 0.0, 0.42),
    (6.30, 0.0, 0.42),
    (5.15, 0.0, 0.20),
    (3.40, 0.0, 0.0),
    (0.60, 0.0, 0.0),
]
FORKLIFT_CLEAR_ROUTE = [
    (0.60, 0.0, 0.0),
    (-0.20, 0.0, 0.0),
    (-0.20, -1.20, 0.0),
    (0.60, -4.80, 0.0),
]
LOW_APPROACH_ROUTE = [
    (-0.40, 3.70, 0.0),
    (0.10, 2.60, 0.0),
    (0.35, 1.40, 0.0),
    (0.72, 0.68, 0.0),
]
LOW_STOCK_ROUTE = [
    (0.72, 0.68, 0.0),
    (-0.20, 1.35, 0.0),
    (-1.80, 2.20, 0.0),
    (-3.10, 2.50, 0.0),
    (-3.52, 2.72, 0.0),
]
HIGH_APPROACH_ROUTE = [
    (-0.40, -3.70, 0.0),
    (0.10, -2.60, 0.0),
    (0.35, -1.40, 0.0),
    (0.72, -0.68, 0.0),
]
HIGH_STAIR_ROUTE = [
    (0.72, -0.68, 0.0),
    (-0.10, -1.65, 0.0),
    (-0.90, -2.75, 0.0),
    (-1.55, -2.75, 0.20),
    (-2.20, -2.75, 0.40),
    (-2.78, -2.75, 0.60),
    (-3.58, -2.75, 1.00),
    (-4.35, -2.75, 1.00),
]

PALLET_TRUCK: Pose = (8.55, 0.0, 0.42, 0.0)
PALLET_STAGE: Pose = (1.55, 0.0, 0.0, 0.0)
LOW_CARTON_PALLET: Pose = (1.55, 0.45, 1.10, 0.0)
HIGH_CARTON_PALLET: Pose = (1.55, -0.45, 1.10, 0.0)
LOW_CARTON_RACK: Pose = (-4.42, 2.72, 1.52, 0.0)
HIGH_CARTON_RACK: Pose = (-5.45, -2.75, 2.00, 0.0)


def forklift_sequence(progress: float) -> tuple[Pose, Pose]:
    if progress < 0.30:
        fork = path_pose(progress / 0.30, FORKLIFT_UNLOAD_ROUTE)
        pallet = (fork[0] + 0.95, fork[1], fork[2], fork[3])
        return fork, pallet
    if progress < 0.37:
        fork = path_pose((progress - 0.30) / 0.07, FORKLIFT_CLEAR_ROUTE)
        return fork, PALLET_STAGE
    return (0.60, -4.80, 0.0, math.pi / 2), PALLET_STAGE


def low_sequence(progress: float) -> tuple[Pose, Pose, str]:
    if progress < 0.36:
        return LOW_APPROACH_ROUTE[0] + (0.0,), LOW_CARTON_PALLET, "wait_for_pallet"
    if progress < 0.51:
        pose = path_pose((progress - 0.36) / 0.15, LOW_APPROACH_ROUTE)
        return pose, LOW_CARTON_PALLET, "approach_full_pallet"
    if progress < 0.57:
        pose = LOW_APPROACH_ROUTE[-1] + (math.pi / 2,)
        item = blend(LOW_CARTON_PALLET, held_item(pose), (progress - 0.51) / 0.06)
        return pose, item, "pick_carton"
    if progress < 0.80:
        pose = path_pose((progress - 0.57) / 0.23, LOW_STOCK_ROUTE)
        return pose, held_item(pose), "carry_to_lower_rack"
    if progress < 0.87:
        pose = LOW_STOCK_ROUTE[-1] + (math.pi,)
        item = blend(held_item(pose), LOW_CARTON_RACK, (progress - 0.80) / 0.07)
        return pose, item, "place_on_lower_rack"
    return LOW_STOCK_ROUTE[-1] + (math.pi,), LOW_CARTON_RACK, "lower_stock_complete"


def high_sequence(progress: float) -> tuple[Pose, Pose, str]:
    if progress < 0.39:
        return HIGH_APPROACH_ROUTE[0] + (0.0,), HIGH_CARTON_PALLET, "wait_for_pallet"
    if progress < 0.54:
        pose = path_pose((progress - 0.39) / 0.15, HIGH_APPROACH_ROUTE)
        return pose, HIGH_CARTON_PALLET, "approach_full_pallet"
    if progress < 0.60:
        pose = HIGH_APPROACH_ROUTE[-1] + (-math.pi / 2,)
        item = blend(HIGH_CARTON_PALLET, held_item(pose), (progress - 0.54) / 0.06)
        return pose, item, "pick_carton"
    if progress < 0.92:
        pose = path_pose((progress - 0.60) / 0.32, HIGH_STAIR_ROUTE)
        return pose, held_item(pose), "carry_up_visible_stairs"
    if progress < 0.98:
        pose = HIGH_STAIR_ROUTE[-1] + (math.pi,)
        item = blend(held_item(pose), HIGH_CARTON_RACK, (progress - 0.92) / 0.06)
        return pose, item, "place_on_upper_rack"
    return HIGH_STAIR_ROUTE[-1] + (math.pi,), HIGH_CARTON_RACK, "upper_stock_complete"


def frame_at(progress: float) -> InboundFrame:
    progress = clamp(progress)
    fork, pallet = forklift_sequence(progress)
    low_pose, low_item, low_state = low_sequence(progress)
    high_pose, high_item, high_state = high_sequence(progress)
    if progress < 0.31:
        camera = "unload"
    elif progress < 0.58:
        camera = "receiving"
    elif progress < 0.70:
        camera = "stocking"
    else:
        camera = "stairs"
    return InboundFrame(fork, pallet, low_pose, low_item, low_state, high_pose, high_item, high_state, camera)


def route_validation_report(samples: int = 501) -> dict[str, float | bool]:
    """Validate the intended direction, final destinations, and stair heights."""
    first = frame_at(0.0)
    last = frame_at(1.0)
    stair_expected = [0.20, 0.40, 0.60, 1.00]
    stair_actual = [point[2] for point in HIGH_STAIR_ROUTE[3:7]]
    min_worker_separation = float("inf")
    for index in range(samples):
        frame = frame_at(index / (samples - 1))
        min_worker_separation = min(min_worker_separation, math.dist(frame.low_worker_pose[:2], frame.high_worker_pose[:2]))
    return {
        "pallet_starts_inside_truck": first.pallet_pose[0] >= 8.0,
        "pallet_ends_in_receiving_zone": last.pallet_pose[0] <= 2.0,
        "forklift_moves_out_of_truck": last.forklift_pose[0] < first.forklift_pose[0],
        "lower_carton_ends_on_rack": math.dist(last.low_carton_pose[:3], LOW_CARTON_RACK[:3]) < 0.01,
        "upper_carton_ends_on_rack": math.dist(last.high_carton_pose[:3], HIGH_CARTON_RACK[:3]) < 0.01,
        "stair_heights_match_treads": stair_actual == stair_expected,
        "minimum_worker_center_separation_m": round(min_worker_separation, 3),
        "worker_separation_passed": min_worker_separation >= 0.70,
    }
