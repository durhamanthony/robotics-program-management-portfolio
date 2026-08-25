"""Order-picking half of the retail backroom MuJoCo visualization.

Both humanoids retrieve requested merchandise from different stock levels,
place it on the courtesy drop-off table, and turn back toward the shelves. A
human sales associate then reaches through the service window, collects both
packages, and closes the custody cycle. The sequence keeps robot centers
outside furniture footprints. It is an operations illustration, not a
collision-avoidance or grasping controller.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


Pose = tuple[float, float, float, float]
MocapPose = tuple[float, ...]
Point = tuple[float, float, float]

HUMAN_UPPER_ARM_LENGTH = 0.64
HUMAN_FOREARM_LENGTH = 0.86


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
    human_pose: Pose
    human_left_upper_arm_pose: MocapPose
    human_left_forearm_pose: MocapPose
    human_right_upper_arm_pose: MocapPose
    human_right_forearm_pose: MocapPose
    human_state: str
    human_visible: bool
    blue_item_visible: bool
    green_item_visible: bool
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
HUMAN_BACKSTAGE: Pose = (-8.65, 0.0, 0.0, 0.0)
HUMAN_WINDOW: Pose = (-7.15, 0.0, 0.0, 0.0)
HUMAN_TURNED: Pose = (-7.15, 0.0, 0.0, math.pi)
HUMAN_DEPARTED: Pose = (-8.85, 0.0, 0.0, math.pi)

# Hand targets are body-local. Keeping the shoulder and targets on the same
# articulated two-segment chain prevents the arms from floating away from the
# torso while still giving the associate a visible elbow bend.
LEFT_HAND_READY: Point = (0.70, -0.58, 1.18)
RIGHT_HAND_READY: Point = (0.70, 0.58, 1.18)
LEFT_HAND_REACH: Point = (1.33, -0.78, 1.20)
RIGHT_HAND_REACH: Point = (1.33, 0.78, 1.20)
LEFT_HAND_HOLD: Point = (0.48, -0.40, 1.40)
RIGHT_HAND_HOLD: Point = (0.48, 0.40, 1.40)


def turned_toward_shelves(position: tuple[float, float, float], amount: float) -> Pose:
    """Rotate from the table (pi) toward the stock shelves (zero yaw)."""
    return position + (blend((math.pi,), (0.0,), amount)[0],)


def body_point(pose: Pose, local: Point) -> Point:
    """Transform a point from the human body frame into world coordinates."""
    x_pos, y_pos, z_pos, yaw = pose
    x_local, y_local, z_local = local
    cosine = math.cos(yaw)
    sine = math.sin(yaw)
    return (
        x_pos + cosine * x_local - sine * y_local,
        y_pos + sine * x_local + cosine * y_local,
        z_pos + z_local,
    )


def segment_pose(start: Point, end: Point) -> MocapPose:
    """Position a fixed +X capsule between two endpoints using a quaternion."""
    vector = tuple(end[index] - start[index] for index in range(3))
    length = math.sqrt(sum(value * value for value in vector))
    direction = tuple(value / length for value in vector)
    # Quaternion rotating the local +X axis onto the segment direction.
    raw = (1.0 + direction[0], 0.0, -direction[2], direction[1])
    norm = math.sqrt(sum(value * value for value in raw))
    if norm < 1e-8:
        quaternion = (0.0, 0.0, 0.0, 1.0)
    else:
        quaternion = tuple(value / norm for value in raw)
    return start + quaternion


def articulated_arm(pose: Pose, hand_local: Point, side: float) -> tuple[MocapPose, MocapPose, Point]:
    """Solve a stable two-bone arm with an outward and upward elbow bend."""
    shoulder_local = (0.0, 0.34 * side, 1.43)
    shoulder = body_point(pose, shoulder_local)
    hand = body_point(pose, hand_local)
    delta = tuple(hand[index] - shoulder[index] for index in range(3))
    distance = math.sqrt(sum(value * value for value in delta))
    direction = tuple(value / distance for value in delta)
    along = (
        HUMAN_UPPER_ARM_LENGTH ** 2
        - HUMAN_FOREARM_LENGTH ** 2
        + distance ** 2
    ) / (2.0 * distance)
    bend_height = math.sqrt(max(0.0, HUMAN_UPPER_ARM_LENGTH ** 2 - along ** 2))

    # Prefer an elbow above and outside the shoulder, then project that bend
    # direction perpendicular to the shoulder-to-hand line.
    # Reaching elbows stay slightly raised; once the packages are against the
    # chest, the elbows fold naturally down for the turn and walk-away.
    hold_amount = clamp((hand_local[2] - 1.20) / 0.20)
    bend_vertical = 0.35 - hold_amount
    bend_local = (0.0, 0.78 * side, bend_vertical)
    bend_world_tip = body_point((pose[0], pose[1], pose[2], pose[3]), bend_local)
    bend_world = (
        bend_world_tip[0] - pose[0],
        bend_world_tip[1] - pose[1],
        bend_world_tip[2] - pose[2],
    )
    projection = sum(bend_world[index] * direction[index] for index in range(3))
    perpendicular = tuple(
        bend_world[index] - projection * direction[index]
        for index in range(3)
    )
    perpendicular_length = math.sqrt(sum(value * value for value in perpendicular))
    perpendicular = tuple(value / perpendicular_length for value in perpendicular)
    elbow = tuple(
        shoulder[index] + along * direction[index] + bend_height * perpendicular[index]
        for index in range(3)
    )
    return segment_pose(shoulder, elbow), segment_pose(elbow, hand), hand


def blue_sequence(progress: float) -> tuple[Pose, Pose, str, bool]:
    if progress < 0.28:
        pose = path_pose(progress / 0.28, BLUE_STAIR_ROUTE)
        return pose, BLUE_ITEM_HOME, "blue_walk_stair_route", False
    if progress < 0.35:
        pose = (2.72, -1.55, 1.0, 0.0)
        item = blend(BLUE_ITEM_HOME, held_item(pose), (progress - 0.28) / 0.07)
        return pose, item, "blue_verify_and_pick", progress >= 0.32
    if progress < 0.68:
        pose = path_pose((progress - 0.35) / 0.33, BLUE_RETURN_ROUTE)
        return pose, held_item(pose), "blue_carry_to_courtesy_table", True
    if progress < 0.75:
        pose = (-4.45, -0.85, 0.0, math.pi)
        item = blend(held_item(pose), BLUE_ITEM_DROPOFF, (progress - 0.68) / 0.07)
        return pose, item, "blue_courtesy_dropoff", progress < 0.73
    if progress < 0.83:
        pose = turned_toward_shelves((-4.35, -0.85, 0.0), (progress - 0.75) / 0.08)
        return pose, BLUE_ITEM_DROPOFF, "blue_turn_toward_shelves", False
    return (-4.35, -0.85, 0.0, 0.0), BLUE_ITEM_DROPOFF, "blue_wait_for_human_pickup", False


def green_sequence(progress: float) -> tuple[Pose, Pose, str, bool]:
    if progress < 0.06:
        return (-4.30, 2.15, 0.0, 0.0), GREEN_ITEM_HOME, "green_receive_pick_request", False
    if progress < 0.26:
        pose = path_pose((progress - 0.06) / 0.20, GREEN_GROUND_PICK_ROUTE)
        return pose, GREEN_ITEM_HOME, "green_walk_to_ground_stock", False
    if progress < 0.33:
        pose = GREEN_GROUND_PICK_ROUTE[-1] + (math.pi / 2,)
        item = blend(GREEN_ITEM_HOME, held_item(pose), (progress - 0.26) / 0.07)
        return pose, item, "green_pick_requested_carton", progress >= 0.30
    if progress < 0.66:
        pose = path_pose((progress - 0.33) / 0.33, GREEN_DROPOFF_ROUTE)
        return pose, held_item(pose), "green_carry_to_courtesy_table", True
    if progress < 0.73:
        pose = (-4.45, 0.85, 0.0, math.pi)
        item = blend(held_item(pose), GREEN_ITEM_DROPOFF, (progress - 0.66) / 0.07)
        return pose, item, "green_courtesy_dropoff", progress < 0.71
    if progress < 0.81:
        pose = turned_toward_shelves((-4.35, 0.85, 0.0), (progress - 0.73) / 0.08)
        return pose, GREEN_ITEM_DROPOFF, "green_turn_toward_shelves", False
    return (-4.35, 0.85, 0.0, 0.0), GREEN_ITEM_DROPOFF, "green_wait_for_human_pickup", False


def human_sequence(progress: float) -> tuple[Pose, Point, Point, str, bool]:
    if progress < 0.76:
        return HUMAN_BACKSTAGE, LEFT_HAND_HOLD, RIGHT_HAND_HOLD, "human_waiting_beyond_window", False
    if progress < 0.81:
        amount = (progress - 0.76) / 0.05
        return (
            blend(HUMAN_BACKSTAGE, HUMAN_WINDOW, amount),
            LEFT_HAND_READY,
            RIGHT_HAND_READY,
            "human_enters_service_window",
            True,
        )
    if progress < 0.87:
        amount = (progress - 0.81) / 0.06
        return (
            HUMAN_WINDOW,
            blend(LEFT_HAND_READY, LEFT_HAND_REACH, amount),
            blend(RIGHT_HAND_READY, RIGHT_HAND_REACH, amount),
            "human_bends_elbows_and_reaches",
            True,
        )
    if progress < 0.895:
        return HUMAN_WINDOW, LEFT_HAND_REACH, RIGHT_HAND_REACH, "human_grasps_packages", True
    if progress < 0.935:
        amount = (progress - 0.895) / 0.04
        return (
            HUMAN_WINDOW,
            blend(LEFT_HAND_REACH, LEFT_HAND_HOLD, amount),
            blend(RIGHT_HAND_REACH, RIGHT_HAND_HOLD, amount),
            "human_bends_elbows_and_retracts_packages",
            True,
        )
    if progress < 0.965:
        amount = (progress - 0.935) / 0.03
        return (
            blend(HUMAN_WINDOW, HUMAN_TURNED, amount),
            LEFT_HAND_HOLD,
            RIGHT_HAND_HOLD,
            "human_turns_away_with_packages",
            True,
        )
    if progress < 0.995:
        amount = (progress - 0.965) / 0.03
        return (
            blend(HUMAN_TURNED, HUMAN_DEPARTED, amount),
            LEFT_HAND_HOLD,
            RIGHT_HAND_HOLD,
            "human_walks_away_with_packages",
            True,
        )
    return HUMAN_DEPARTED, LEFT_HAND_HOLD, RIGHT_HAND_HOLD, "human_departed", False


def frame_at(progress: float) -> RetailFrame:
    progress = clamp(progress)
    blue_pose, blue_item, blue_state, blue_carrying = blue_sequence(progress)
    green_pose, green_item, green_state, green_carrying = green_sequence(progress)
    human_pose, left_hand_local, right_hand_local, human_state, human_visible = human_sequence(progress)
    left_upper, left_forearm, left_hand = articulated_arm(human_pose, left_hand_local, -1.0)
    right_upper, right_forearm, right_hand = articulated_arm(human_pose, right_hand_local, 1.0)
    if progress >= 0.87:
        left_hand_item = left_hand + (human_pose[3],)
        right_hand_item = right_hand + (human_pose[3],)
        if progress < 0.895:
            blue_item = blend(BLUE_ITEM_DROPOFF, left_hand_item, (progress - 0.87) / 0.025)
            green_item = blend(GREEN_ITEM_DROPOFF, right_hand_item, (progress - 0.87) / 0.025)
        else:
            blue_item = left_hand_item
            green_item = right_hand_item
    items_visible = progress < 0.995
    camera = "overview"
    if 0.18 <= progress < 0.52:
        camera = "stairs"
    elif 0.52 <= progress < 0.66:
        camera = "shelves"
    elif progress >= 0.66:
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
        human_pose=human_pose,
        human_left_upper_arm_pose=left_upper,
        human_left_forearm_pose=left_forearm,
        human_right_upper_arm_pose=right_upper,
        human_right_forearm_pose=right_forearm,
        human_state=human_state,
        human_visible=human_visible,
        blue_item_visible=items_visible,
        green_item_visible=items_visible,
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
    final = frame_at(1.0)
    return {
        "furniture_clearance_passed": obstacle_clear,
        "minimum_robot_center_separation_m": round(minimum_robot_separation, 3),
        "robot_separation_passed": minimum_robot_separation >= 0.70,
        "robots_face_shelves_after_handoff": abs(final.blue_pose[3]) < 0.01 and abs(final.green_pose[3]) < 0.01,
        "human_pickup_complete": final.human_state == "human_departed",
        "human_departed_after_pickup": final.human_state == "human_departed" and not final.human_visible,
        "packages_removed_after_human_pickup": not final.blue_item_visible and not final.green_item_visible,
    }
