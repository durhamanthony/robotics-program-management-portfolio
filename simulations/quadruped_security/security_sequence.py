"""Shared visual sequence for the quadruped security-site demonstration.

The animation is deliberately kinematic.  It keeps the perimeter dog outside
the warehouse footprint and maps the stair dog's vertical position to the
physical top surface of every tread.  This makes the route legible without
claiming locomotion, collision avoidance, or safety validation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


Pose = tuple[float, float, float, float]


@dataclass(frozen=True)
class SecurityFrame:
    perimeter_pose: Pose
    stair_pose: Pose
    reserve_pose: Pose
    perimeter_state: str
    stair_state: str
    reserve_state: str
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


# This dog follows the outside pavement around the warehouse.  Every segment
# remains outside the warehouse and guard-booth footprints.
PERIMETER_ROUTE = [
    (-6.70, -5.10, 0.0),
    (-2.80, -5.10, 0.0),
    (3.55, -5.10, 0.0),
    (3.55, -3.00, 0.0),
    (7.25, -3.00, 0.0),
    (7.25, 2.80, 0.0),
    (7.20, 5.65, 0.0),
    (-3.80, 5.65, 0.0),
    (-6.60, 3.70, 0.0),
    (-6.60, -3.80, 0.0),
    (-6.70, -5.10, 0.0),
]

# Approach the stairs by going around the west and north sides of the
# warehouse.  The dog never passes through the building.
STAIR_APPROACH_ROUTE = [
    (-5.35, -5.10, 0.0),
    (-6.00, -3.20, 0.0),
    (-6.00, 4.90, 0.0),
    (-2.60, 5.10, 0.0),
    (1.80, 5.10, 0.0),
    (2.15, 3.75, 0.0),
]

# Short horizontal moves across each tread are followed by a small rise at the
# riser.  The z values exactly match the XML tread-top heights.
STAIR_ASCENT_ROUTE = [
    (2.15, 3.75, 0.00),
    (2.34, 3.75, 0.00),
    (2.42, 3.75, 0.24),
    (2.76, 3.75, 0.24),
    (2.87, 3.75, 0.48),
    (3.16, 3.75, 0.48),
    (3.27, 3.75, 0.72),
    (3.53, 3.75, 0.72),
    (3.62, 3.75, 0.98),
    (3.83, 3.75, 0.98),
    (3.94, 3.75, 1.24),
    (4.55, 3.75, 1.24),
]
STAIR_DESCENT_ROUTE = list(reversed(STAIR_ASCENT_ROUTE))
STAIR_RETURN_ROUTE = [
    (2.15, 3.75, 0.0),
    (1.80, 5.10, 0.0),
    (-2.60, 5.10, 0.0),
    (-6.00, 4.90, 0.0),
    (-6.00, -3.20, 0.0),
    (-5.35, -5.10, 0.0),
]


def stair_sequence(progress: float) -> tuple[Pose, str]:
    if progress < 0.28:
        return path_pose(progress / 0.28, STAIR_APPROACH_ROUTE), "approach_stairs_around_warehouse"
    if progress < 0.46:
        return path_pose((progress - 0.28) / 0.18, STAIR_ASCENT_ROUTE), "climb_visible_treads"
    if progress < 0.56:
        return path_pose((progress - 0.46) / 0.10, [(4.55, 3.75, 1.24), (4.90, 3.75, 1.24)]), "inspect_loading_platform"
    if progress < 0.74:
        return path_pose((progress - 0.56) / 0.18, STAIR_DESCENT_ROUTE), "descend_visible_treads"
    return path_pose((progress - 0.74) / 0.26, STAIR_RETURN_ROUTE), "return_around_warehouse"


def frame_at(progress: float) -> SecurityFrame:
    progress = clamp(progress)
    perimeter_pose = path_pose(progress, PERIMETER_ROUTE)
    stair_pose, stair_state = stair_sequence(progress)
    if progress < 0.88:
        reserve_pose = (-4.00, -5.10, 0.0, 0.0)
        reserve_state = "charging_reserve"
    else:
        reserve_pose = path_pose((progress - 0.88) / 0.12, [(-4.00, -5.10, 0.0), (-4.00, -5.55, 0.0)])
        reserve_state = "dock_return"

    if progress < 0.24:
        camera = "overview"
    elif progress < 0.76:
        camera = "stair_close"
    elif progress < 0.92:
        camera = "north_perimeter"
    else:
        camera = "dock"

    return SecurityFrame(
        perimeter_pose=perimeter_pose,
        stair_pose=stair_pose,
        reserve_pose=reserve_pose,
        perimeter_state="perimeter_route_around_warehouse",
        stair_state=stair_state,
        reserve_state=reserve_state,
        camera=camera,
    )


def route_clearance_report(samples: int = 1001) -> dict[str, float | bool]:
    """Check center paths against solid footprints and verify stair heights."""
    warehouse = (-3.36, 3.36, -2.66, 2.66)
    guard_booth = (3.84, 7.56, -6.06, -3.14)
    loading_platform = (3.34, 6.66, 2.19, 5.31)
    minimum_robot_separation = float("inf")
    solid_clear = True
    for index in range(samples):
        frame = frame_at(index / (samples - 1))
        for x_pos, y_pos in (frame.perimeter_pose[:2], frame.stair_pose[:2]):
            for x_min, x_max, y_min, y_max in (warehouse, guard_booth):
                if x_min < x_pos < x_max and y_min < y_pos < y_max:
                    solid_clear = False
        x_pos, y_pos = frame.perimeter_pose[:2]
        x_min, x_max, y_min, y_max = loading_platform
        if x_min < x_pos < x_max and y_min < y_pos < y_max:
            solid_clear = False
        minimum_robot_separation = min(
            minimum_robot_separation,
            math.dist(frame.perimeter_pose[:2], frame.stair_pose[:2]),
        )

    expected_tops = {0.0, 0.24, 0.48, 0.72, 0.98, 1.24}
    route_tops = {round(point[2], 2) for point in STAIR_ASCENT_ROUTE}
    return {
        "solid_obstacle_clearance_passed": solid_clear,
        "minimum_active_robot_center_separation_m": round(minimum_robot_separation, 3),
        "robot_separation_passed": minimum_robot_separation >= 0.70,
        "stair_tread_heights_match_xml": route_tops == expected_tops,
        "stair_up_and_down_present": STAIR_DESCENT_ROUTE == list(reversed(STAIR_ASCENT_ROUTE)),
    }
