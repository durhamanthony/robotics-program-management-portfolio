from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

import mujoco

SIM_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SIM_ROOT.parent
sys.path.insert(0, str(SIM_ROOT))

from common.telemetry import write_records, write_summary  # noqa: E402


LANE_Y = [-3.20, -1.60, 0.00, 1.60, 3.20]
CYCLE_SECONDS = [11.0, 10.5, 4.0, 12.0, 9.5]
INTERLOCK_TIME = 28.0
PALLET_X = 2.20
BELT_START_X = -5.90
BELT_PICKUP_X = -3.13
ROBOT_WAIT_X = -2.20
ROBOT_PICKUP_X = -2.55
ROBOT_DROPOFF_X = 1.36
ACTIVE_BOX_Z = 0.91
STACK_BASE_Z = 0.39
STACK_STEP_Z = 0.23
REPLACEMENT_PALLET_OFFSET = 0.90


def _smoothstep(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


def _lerp(start: float, end: float, value: float) -> float:
    return start + (end - start) * _smoothstep(value)


def _yaw_quat(yaw: float) -> list[float]:
    return [math.cos(yaw / 2.0), 0.0, 0.0, math.sin(yaw / 2.0)]


def _body_mocap_id(model: mujoco.MjModel, body_name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, body_name)
    if body_id < 0:
        raise ValueError(f"MuJoCo body not found: {body_name}")
    return int(model.body_mocapid[body_id])


def _geom_id(model: mujoco.MjModel, geom_name: str) -> int:
    geom_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, geom_name)
    if geom_id < 0:
        raise ValueError(f"MuJoCo geom not found: {geom_name}")
    return int(geom_id)


def _joint_qpos_address(model: mujoco.MjModel, joint_name: str) -> int:
    joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, joint_name)
    if joint_id < 0:
        raise ValueError(f"MuJoCo joint not found: {joint_name}")
    return int(model.jnt_qposadr[joint_id])


def _set_pose(
    data: mujoco.MjData,
    mocap_id: int,
    x: float,
    y: float,
    z: float = 0.0,
    yaw: float = 0.0,
) -> None:
    data.mocap_pos[mocap_id] = [x, y, z]
    data.mocap_quat[mocap_id] = _yaw_quat(yaw)


def run(
    duration: float,
    viewer_enabled: bool,
    output_dir: Path,
    cinematic_camera: bool = True,
) -> dict:
    model_path = Path(__file__).with_name("warehouse.xml")
    model = mujoco.MjModel.from_xml_path(str(model_path))
    data = mujoco.MjData(model)

    robots = [f"humanoid_{index:02d}" for index in range(1, 6)]
    cartons = [f"carton_{index:02d}" for index in range(1, 6)]
    pallets = [f"pallet_{index:02d}" for index in range(1, 6)]
    stacks = [f"stack_lane_{index:02d}" for index in range(1, 6)]

    robot_mocap_ids = [_body_mocap_id(model, name) for name in robots]
    carton_mocap_ids = [_body_mocap_id(model, name) for name in cartons]
    pallet_mocap_ids = [_body_mocap_id(model, name) for name in pallets]
    stack_mocap_ids = [_body_mocap_id(model, name) for name in stacks]
    replacement_mocap_id = _body_mocap_id(model, "replacement_pallet")
    forklift_mocap_id = _body_mocap_id(model, "forklift_unit")
    forklift_carriage_mocap_id = _body_mocap_id(model, "forklift_carriage")

    active_geom_ids = [
        (
            _geom_id(model, f"active_box_{index:02d}"),
            _geom_id(model, f"active_label_{index:02d}"),
        )
        for index in range(1, 6)
    ]
    stack_geom_ids = [
        [_geom_id(model, f"stack_{lane:02d}_{level:02d}") for level in range(1, 8)]
        for lane in range(1, 6)
    ]
    status_geom_ids = [_geom_id(model, f"status_{index:02d}") for index in range(1, 6)]
    limb_addresses = [
        {
            "left_shoulder": _joint_qpos_address(model, f"h{index:02d}_l_shoulder"),
            "right_shoulder": _joint_qpos_address(model, f"h{index:02d}_r_shoulder"),
            "left_hip": _joint_qpos_address(model, f"h{index:02d}_l_hip"),
            "right_hip": _joint_qpos_address(model, f"h{index:02d}_r_hip"),
        }
        for index in range(1, 6)
    ]

    records: list[dict] = []
    sample_period = 0.5
    next_sample = 0.0
    dt = float(model.opt.timestep)
    final_stack_counts = [0, 0, 0, 0, 0]

    boxes_move_on_belts = False
    boxes_carried_to_pallets = False
    articulated_gait_seen = False
    center_stack_reaches_seven = False
    all_workers_interlocked = False
    forklift_lifts_loaded_pallet = False
    forklift_enters_truck = False
    forklift_hidden_inside_truck = False
    forklift_returns_empty = False
    fork_carriage_tracks_load = False
    replacement_pallet_installed = False
    worker_lane_ownership_ok = True
    conveyor_clearance_ok = True
    payload_clearance_ok = True

    def set_active_carton_visible(index: int, visible: bool) -> None:
        alpha = 1.0 if visible else 0.0
        for geom_id in active_geom_ids[index]:
            model.geom_rgba[geom_id, 3] = alpha

    def set_stack_count(index: int, count: int) -> None:
        for level, geom_id in enumerate(stack_geom_ids[index], start=1):
            model.geom_rgba[geom_id, 3] = 1.0 if level <= count else 0.0

    def animate_limbs(index: int, moving: bool, carrying: bool, sim_time: float) -> None:
        nonlocal articulated_gait_seen
        gait = 0.0
        if moving:
            gait = 0.42 * math.sin(sim_time * 7.0 + index * 0.85)
            articulated_gait_seen = articulated_gait_seen or abs(gait) > 0.12
        addresses = limb_addresses[index]
        if carrying:
            data.qpos[addresses["left_shoulder"]] = -0.94
            data.qpos[addresses["right_shoulder"]] = -0.94
            data.qpos[addresses["left_hip"]] = gait * 0.55
            data.qpos[addresses["right_hip"]] = -gait * 0.55
        else:
            data.qpos[addresses["left_shoulder"]] = -gait
            data.qpos[addresses["right_shoulder"]] = gait
            data.qpos[addresses["left_hip"]] = gait
            data.qpos[addresses["right_hip"]] = -gait

    def worker_cycle(index: int, sim_time: float) -> dict:
        nonlocal boxes_move_on_belts, boxes_carried_to_pallets
        nonlocal worker_lane_ownership_ok, conveyor_clearance_ok, payload_clearance_ok

        lane_y = LANE_Y[index]
        period = CYCLE_SECONDS[index]
        cycle_number = int(sim_time // period)
        phase = (sim_time % period) / period
        count = min(7, cycle_number + (1 if phase >= 0.82 else 0))
        final_stack_counts[index] = count
        set_stack_count(index, count)

        robot_x = ROBOT_WAIT_X
        robot_y = lane_y
        robot_z = 0.0
        carton_x = BELT_START_X
        carton_y = lane_y
        carton_z = ACTIVE_BOX_Z
        yaw = math.pi
        state = "conveyor_feed"
        message = "Carton advancing on the lane conveyor; robot holding at safe wait point"
        moving = False
        carrying = False
        carton_visible = True

        if phase < 0.18:
            carton_x = _lerp(BELT_START_X, BELT_PICKUP_X, phase / 0.18)
            boxes_move_on_belts = boxes_move_on_belts or carton_x > -4.5
        elif phase < 0.33:
            state = "approach_safe_pickup"
            message = "Robot approaching the marked stop point without entering the conveyor"
            moving = True
            robot_x = _lerp(ROBOT_WAIT_X, ROBOT_PICKUP_X, (phase - 0.18) / 0.15)
            carton_x = BELT_PICKUP_X
        elif phase < 0.42:
            state = "lift_from_conveyor"
            message = "Robot stopped clear of conveyor and lifting carton"
            robot_x = ROBOT_PICKUP_X
            carton_x = BELT_PICKUP_X
            carton_z = _lerp(ACTIVE_BOX_Z, 1.08, (phase - 0.33) / 0.09)
            carrying = True
        elif phase < 0.48:
            state = "turn_with_carton"
            message = "Robot turning in place with carton held outside its body envelope"
            robot_x = ROBOT_PICKUP_X
            turn = (phase - 0.42) / 0.06
            yaw = _lerp(math.pi, 0.0, turn)
            carton_x = robot_x + 0.58 * math.cos(yaw)
            carton_y = lane_y + 0.58 * math.sin(yaw)
            carton_z = 1.08
            carrying = True
        elif phase < 0.70:
            state = "carry_to_pallet"
            message = "Robot carrying carton inside its assigned lane toward the floor pallet"
            moving = True
            carrying = True
            yaw = 0.0
            robot_x = _lerp(ROBOT_PICKUP_X, ROBOT_DROPOFF_X, (phase - 0.48) / 0.22)
            carton_x = robot_x + 0.58
            carton_z = 1.08
        elif phase < 0.82:
            state = "stack_on_pallet"
            message = f"Robot placing carton {min(7, cycle_number + 1)} on the floor pallet"
            carrying = True
            yaw = 0.0
            robot_x = ROBOT_DROPOFF_X
            placement = (phase - 0.70) / 0.12
            carton_x = _lerp(ROBOT_DROPOFF_X + 0.58, PALLET_X, placement)
            carton_z = _lerp(1.08, STACK_BASE_Z + cycle_number * STACK_STEP_Z, placement)
            boxes_carried_to_pallets = boxes_carried_to_pallets or carton_x > 2.05
        else:
            state = "return_to_wait"
            message = f"Carton {count} stacked; robot returning for the next conveyor arrival"
            moving = True
            yaw = math.pi
            robot_x = _lerp(ROBOT_DROPOFF_X, ROBOT_WAIT_X, (phase - 0.82) / 0.18)
            carton_x = PALLET_X
            carton_z = STACK_BASE_Z + max(0, count - 1) * STACK_STEP_Z
            carton_visible = False

        set_active_carton_visible(index, carton_visible)
        _set_pose(data, robot_mocap_ids[index], robot_x, robot_y, robot_z, yaw)
        _set_pose(data, carton_mocap_ids[index], carton_x, carton_y, carton_z)
        animate_limbs(index, moving, carrying, sim_time)

        conveyor_clearance_ok = conveyor_clearance_ok and robot_x - 0.22 >= -2.93
        worker_lane_ownership_ok = worker_lane_ownership_ok and abs(robot_y - lane_y) < 1e-6
        if carrying:
            payload_distance = math.hypot(carton_x - robot_x, carton_y - robot_y)
            payload_clearance_ok = payload_clearance_ok and payload_distance >= 0.55

        return {
            "state": state,
            "message": message,
            "x": robot_x,
            "y": robot_y,
            "moving": moving,
            "carrying": carrying,
            "stack_count": count,
        }

    def hold_worker(index: int, sim_time: float) -> dict:
        set_active_carton_visible(index, True)
        _set_pose(data, carton_mocap_ids[index], BELT_START_X, LANE_Y[index], ACTIVE_BOX_Z)
        _set_pose(data, robot_mocap_ids[index], ROBOT_WAIT_X, LANE_Y[index], 0.0, math.pi)
        animate_limbs(index, False, False, sim_time)
        model.geom_rgba[status_geom_ids[index]] = [1.0, 0.62, 0.02, 1.0]
        return {
            "state": "pallet_full_interlock",
            "message": "All worker motion stopped while forklift owns the transfer zone",
            "x": ROBOT_WAIT_X,
            "y": LANE_Y[index],
            "moving": False,
            "carrying": False,
            "stack_count": final_stack_counts[index],
        }

    def replenish_center_pallet(sim_time: float, state: dict) -> dict:
        """Use worker 05 to install a new pallet after the forklift clears the aisle."""
        nonlocal replacement_pallet_installed, payload_clearance_ok

        index = 4
        moving = False
        carrying = False
        robot_x = ROBOT_WAIT_X
        robot_y = LANE_Y[index]
        robot_z = 0.0
        yaw = 0.19
        pallet_x = 0.82
        pallet_y = 4.35
        pallet_z = 0.0
        phase_state = "approach_replacement_pallet"
        message = "Worker 05 approaching the stored empty pallet after forklift clearance"

        if sim_time < 60.0:
            moving = True
            p = (sim_time - 57.0) / 3.0
            robot_x = _lerp(ROBOT_WAIT_X, 0.82, p)
            robot_y = _lerp(LANE_Y[index], 4.35 - REPLACEMENT_PALLET_OFFSET, p)
        elif sim_time < 61.0:
            phase_state = "lift_empty_pallet"
            message = "Worker 05 lifting the empty replacement pallet"
            carrying = True
            yaw = math.pi / 2.0
            robot_x, robot_y = 0.82, 4.35 - REPLACEMENT_PALLET_OFFSET
            pallet_z = _lerp(0.0, 0.50, sim_time - 60.0)
        elif sim_time < 62.0:
            phase_state = "turn_with_empty_pallet"
            message = "Worker 05 turning the pallet into the protected cross aisle"
            carrying = True
            robot_x, robot_y = 0.82, 4.35 - REPLACEMENT_PALLET_OFFSET
            yaw = _lerp(math.pi / 2.0, -math.pi / 2.0, sim_time - 61.0)
            pallet_x = robot_x + REPLACEMENT_PALLET_OFFSET * math.cos(yaw)
            pallet_y = robot_y + REPLACEMENT_PALLET_OFFSET * math.sin(yaw)
            pallet_z = 0.50
        elif sim_time < 66.0:
            phase_state = "carry_pallet_through_cross_aisle"
            message = "Worker 05 carrying the empty pallet toward the cleared center station"
            moving = True
            carrying = True
            yaw = -math.pi / 2.0
            robot_x = 0.82
            robot_y = _lerp(4.35 - REPLACEMENT_PALLET_OFFSET, REPLACEMENT_PALLET_OFFSET, (sim_time - 62.0) / 4.0)
            pallet_x = robot_x
            pallet_y = robot_y - REPLACEMENT_PALLET_OFFSET
            pallet_z = 0.50
        elif sim_time < 67.0:
            phase_state = "turn_toward_center_station"
            message = "Worker 05 aligning the empty pallet with the center station"
            carrying = True
            robot_x, robot_y = 0.82, REPLACEMENT_PALLET_OFFSET
            yaw = _lerp(-math.pi / 2.0, 0.0, sim_time - 66.0)
            pallet_x = robot_x + REPLACEMENT_PALLET_OFFSET * math.cos(yaw)
            pallet_y = robot_y + REPLACEMENT_PALLET_OFFSET * math.sin(yaw)
            pallet_z = 0.50
        elif sim_time < 69.0:
            phase_state = "carry_pallet_to_center_station"
            message = "Worker 05 moving the empty pallet into the center pallet zone"
            moving = True
            carrying = True
            yaw = 0.0
            robot_x = _lerp(0.82, PALLET_X - REPLACEMENT_PALLET_OFFSET, (sim_time - 67.0) / 2.0)
            robot_y = _lerp(REPLACEMENT_PALLET_OFFSET, 0.00, (sim_time - 67.0) / 2.0)
            pallet_x = robot_x + REPLACEMENT_PALLET_OFFSET
            pallet_y = robot_y
            pallet_z = 0.50
        elif sim_time < 70.0:
            phase_state = "place_new_center_pallet"
            message = "Worker 05 lowering the new empty pallet onto the center station"
            carrying = True
            robot_x, robot_y = PALLET_X - REPLACEMENT_PALLET_OFFSET, 0.00
            pallet_x, pallet_y = PALLET_X, 0.00
            pallet_z = _lerp(0.50, 0.0, sim_time - 69.0)
        else:
            phase_state = "replacement_complete"
            message = "New empty pallet installed; center station ready for work release"
            replacement_pallet_installed = True
            pallet_x, pallet_y, pallet_z = PALLET_X, 0.00, 0.0
            if sim_time < 72.0:
                moving = True
                yaw = math.atan2(
                    LANE_Y[index],
                    ROBOT_WAIT_X - (PALLET_X - REPLACEMENT_PALLET_OFFSET),
                )
                robot_x = _lerp(
                    PALLET_X - REPLACEMENT_PALLET_OFFSET,
                    ROBOT_WAIT_X,
                    (sim_time - 70.0) / 2.0,
                )
                robot_y = _lerp(0.00, LANE_Y[index], (sim_time - 70.0) / 2.0)

        _set_pose(data, robot_mocap_ids[index], robot_x, robot_y, robot_z, yaw)
        _set_pose(data, replacement_mocap_id, pallet_x, pallet_y, pallet_z, yaw if carrying else 0.0)
        animate_limbs(index, moving, carrying, sim_time)
        model.geom_rgba[status_geom_ids[index]] = [0.06, 0.82, 0.95, 1.0]
        if carrying:
            pallet_distance = math.hypot(pallet_x - robot_x, pallet_y - robot_y)
            payload_clearance_ok = payload_clearance_ok and pallet_distance >= 0.86
        state.update(
            {
                "state": phase_state,
                "message": message,
                "x": robot_x,
                "y": robot_y,
                "moving": moving,
                "carrying": carrying,
            }
        )
        return state

    def position_forklift_and_center_load(sim_time: float) -> dict:
        nonlocal forklift_lifts_loaded_pallet, forklift_enters_truck
        nonlocal forklift_hidden_inside_truck, forklift_returns_empty
        nonlocal fork_carriage_tracks_load

        forklift_x, forklift_y, forklift_z, yaw = 4.30, -4.35, 0.0, math.pi / 2.0
        carriage_z = 0.0
        pallet_x, pallet_y, pallet_z, pallet_yaw = PALLET_X, 0.0, 0.0, 0.0
        loaded = False
        hidden = False
        state = "parked"
        message = "Forklift robot parked outside the active lanes"

        if sim_time < 30.0:
            pass
        elif sim_time < 34.0:
            state = "enter_transfer_aisle"
            message = "Forklift entering the transfer aisle after the global interlock"
            forklift_y = _lerp(-4.35, 0.0, (sim_time - 30.0) / 4.0)
        elif sim_time < 36.0:
            state = "approach_full_pallet"
            message = "Forklift aligning forks with the seven-carton center pallet"
            yaw = math.pi
            forklift_x = _lerp(4.30, 3.40, (sim_time - 34.0) / 2.0)
            forklift_y = 0.0
        elif sim_time < 38.0:
            state = "lift_full_pallet"
            message = "Forklift lifting the pallet and all seven cartons as one load"
            loaded = True
            yaw = math.pi
            forklift_x, forklift_y = 3.40, 0.0
            pallet_x, pallet_y = PALLET_X, 0.0
            pallet_z = _lerp(0.0, 0.36, (sim_time - 36.0) / 2.0)
            carriage_z = pallet_z
            pallet_yaw = yaw
            forklift_lifts_loaded_pallet = True
            fork_carriage_tracks_load = fork_carriage_tracks_load or abs(carriage_z - pallet_z) < 1e-6
        elif sim_time < 41.0:
            state = "back_out_with_load"
            message = "Forklift backing the loaded pallet clear of the worker lanes"
            loaded = True
            yaw = math.pi
            forklift_x = _lerp(3.40, 4.20, (sim_time - 38.0) / 3.0)
            forklift_y = 0.0
            pallet_x = forklift_x - 1.20
            pallet_y = 0.0
            pallet_z = 0.36
            carriage_z = 0.36
            pallet_yaw = yaw
        elif sim_time < 43.0:
            state = "turn_toward_truck"
            message = "Forklift turning the seven-carton load toward the open green truck"
            loaded = True
            forklift_x, forklift_y = 4.20, 0.0
            yaw = _lerp(math.pi, 0.0, (sim_time - 41.0) / 2.0)
            pallet_x = forklift_x + 1.20 * math.cos(yaw)
            pallet_y = forklift_y + 1.20 * math.sin(yaw)
            pallet_z = 0.36
            carriage_z = 0.36
            pallet_yaw = yaw
        elif sim_time < 49.0:
            state = "drive_load_into_truck"
            message = "Forklift driving the loaded pallet through the truck's open rear"
            loaded = True
            yaw = 0.0
            forklift_x = _lerp(4.20, 7.30, (sim_time - 43.0) / 6.0)
            forklift_y = 0.0
            ramp_progress = max(0.0, min(1.0, (forklift_x - 4.45) / 1.0))
            forklift_z = _lerp(0.0, 0.46, ramp_progress)
            pallet_x = forklift_x + 1.20
            pallet_y = 0.0
            pallet_z = forklift_z + 0.36
            carriage_z = forklift_z + 0.36
            forklift_enters_truck = forklift_enters_truck or forklift_x > 5.45
        elif sim_time < 52.0:
            state = "inside_truck_delivering_pallet"
            message = "Forklift and driver are inside the truck depositing the loaded pallet"
            hidden = True
            loaded = True
            forklift_x, forklift_y, forklift_z = 8.00, 0.0, -12.0
            carriage_z = -12.0
            pallet_x, pallet_y, pallet_z = 8.80, 0.0, -12.0
            forklift_hidden_inside_truck = True
        elif sim_time < 56.0:
            state = "return_empty_from_truck"
            message = "Forklift robot emerging from the truck with empty forks"
            yaw = math.pi
            forklift_x = _lerp(7.30, 4.30, (sim_time - 52.0) / 4.0)
            forklift_y = 0.0
            ramp_progress = max(0.0, min(1.0, (forklift_x - 4.45) / 1.0))
            forklift_z = _lerp(0.0, 0.46, ramp_progress)
            carriage_z = forklift_z
            pallet_x, pallet_y, pallet_z = 8.80, 0.0, -12.0
            forklift_returns_empty = True
        elif sim_time < 60.0:
            state = "clear_transfer_aisle"
            message = "Empty forklift clearing the center aisle for pallet replenishment"
            yaw = -math.pi / 2.0
            forklift_x = 4.30
            forklift_y = _lerp(0.0, -4.35, (sim_time - 56.0) / 4.0)
            pallet_x, pallet_y, pallet_z = 8.80, 0.0, -12.0
        else:
            state = "parked_empty"
            message = "Forklift parked with empty forks after completing the truck load"
            forklift_x, forklift_y, yaw = 4.30, -4.35, math.pi / 2.0
            pallet_x, pallet_y, pallet_z = 8.80, 0.0, -12.0

        _set_pose(data, forklift_mocap_id, forklift_x, forklift_y, forklift_z, yaw)
        _set_pose(data, forklift_carriage_mocap_id, forklift_x, forklift_y, carriage_z, yaw)
        _set_pose(data, pallet_mocap_ids[2], pallet_x, pallet_y, pallet_z, pallet_yaw)
        _set_pose(data, stack_mocap_ids[2], pallet_x, pallet_y, pallet_z, pallet_yaw)
        return {
            "state": state,
            "message": message,
            "x": forklift_x,
            "y": forklift_y,
            "loaded": loaded,
            "hidden": hidden,
        }

    def one_step() -> None:
        nonlocal next_sample, center_stack_reaches_seven, all_workers_interlocked

        sim_time = float(data.time)

        for index, lane_y in enumerate(LANE_Y):
            _set_pose(data, pallet_mocap_ids[index], PALLET_X, lane_y)
            _set_pose(data, stack_mocap_ids[index], PALLET_X, lane_y)
        _set_pose(data, replacement_mocap_id, 0.82, 4.35)

        worker_states: list[dict] = []
        if sim_time < INTERLOCK_TIME:
            for index in range(5):
                state = worker_cycle(index, sim_time)
                worker_states.append(state)
                model.geom_rgba[status_geom_ids[index]] = [0.08, 0.85, 0.30, 1.0]
            center_stack_reaches_seven = center_stack_reaches_seven or final_stack_counts[2] == 7
        else:
            final_stack_counts[:] = [2, 2, 7, 2, 3]
            for index, count in enumerate(final_stack_counts):
                set_stack_count(index, count)
                worker_states.append(hold_worker(index, sim_time))
            all_workers_interlocked = all_workers_interlocked or all(
                not state["moving"] for state in worker_states
            )

        forklift_state = position_forklift_and_center_load(sim_time)

        if sim_time >= 57.0:
            worker_states[4] = replenish_center_pallet(sim_time, worker_states[4])

        if sim_time + 1e-9 >= next_sample:
            for index, state in enumerate(worker_states):
                records.append(
                    {
                        "timestamp_ns": 1_800_000_000_000_000_000 + int(sim_time * 1e9),
                        "sim_time_s": round(sim_time, 3),
                        "scenario": "five_lane_humanoid_palletizing_and_truck_loading",
                        "site_id": "WH-DEMO-01",
                        "robot_id": robots[index].upper(),
                        "robot_model": "PORTFOLIO-H4",
                        "software_version": "demo-4.0.0",
                        "mission_id": f"PALLETIZE-{index + 1:02d}",
                        "operational_state": state["state"],
                        "safety_state": "controlled_interlock" if sim_time >= INTERLOCK_TIME else "normal",
                        "battery_pct": round(max(20.0, 96.0 - sim_time * (0.12 + index * 0.01)), 1),
                        "network_rssi_dbm": -51 - index,
                        "x_m": round(state["x"], 3),
                        "y_m": round(state["y"], 3),
                        "component": "material_handling",
                        "fault_code": "",
                        "severity": "",
                        "correlation_id": f"WH-PALLET-{int(sim_time):04d}" if sim_time >= INTERLOCK_TIME else "",
                        "message": state["message"],
                    }
                )
            records.append(
                {
                    "timestamp_ns": 1_800_000_000_000_000_000 + int(sim_time * 1e9),
                    "sim_time_s": round(sim_time, 3),
                    "scenario": "five_lane_humanoid_palletizing_and_truck_loading",
                    "site_id": "WH-DEMO-01",
                    "robot_id": "FORKLIFT_ROBOT_01",
                    "robot_model": "PORTFOLIO-FL1",
                    "software_version": "demo-4.0.0",
                    "mission_id": "LOAD-GREEN-TRUCK-01",
                    "operational_state": forklift_state["state"],
                    "safety_state": "exclusive_zone_control" if sim_time >= 30.0 else "normal",
                    "battery_pct": round(max(35.0, 94.0 - sim_time * 0.08), 1),
                    "network_rssi_dbm": -48,
                    "x_m": round(forklift_state["x"], 3),
                    "y_m": round(forklift_state["y"], 3),
                    "component": "forklift_transfer",
                    "fault_code": "",
                    "severity": "",
                    "correlation_id": "WH-LOAD-0001",
                    "message": forklift_state["message"],
                }
            )
            next_sample += sample_period

        data.qvel[:] = 0.0
        mujoco.mj_forward(model, data)
        data.time += dt

    if viewer_enabled:
        from mujoco import viewer

        camera_views = {
            0: ([-1.00, 0.00, 1.00], 12.8, 128.0, -24.0),
            1: ([2.35, 0.00, 1.15], 9.4, 142.0, -23.0),
            2: ([5.55, 0.00, 1.45], 9.6, 172.0, -20.0),
            3: ([1.10, 1.25, 1.00], 9.8, 126.0, -24.0),
        }

        def camera_stage(sim_time: float) -> int:
            if sim_time < INTERLOCK_TIME:
                return 0
            if sim_time < 43.0:
                return 1
            if sim_time < 56.0:
                return 2
            return 3

        def apply_camera(active_camera, stage: int) -> None:
            lookat, distance, azimuth, elevation = camera_views[stage]
            active_camera.lookat[:] = lookat
            active_camera.distance = distance
            active_camera.azimuth = azimuth
            active_camera.elevation = elevation

        with viewer.launch_passive(
            model,
            data,
            show_left_ui=False,
            show_right_ui=False,
        ) as active_viewer:
            active_viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FREE
            active_camera_stage = camera_stage(float(data.time))
            apply_camera(active_viewer.cam, active_camera_stage)
            active_viewer.sync()
            while data.time < duration and active_viewer.is_running():
                started = time.time()
                one_step()
                next_camera_stage = camera_stage(float(data.time))
                if cinematic_camera and next_camera_stage != active_camera_stage:
                    active_camera_stage = next_camera_stage
                    apply_camera(active_viewer.cam, active_camera_stage)
                active_viewer.sync()
                remaining = dt - (time.time() - started)
                if remaining > 0:
                    time.sleep(remaining)
    else:
        while data.time < duration:
            one_step()

    paths = write_records(records, output_dir, "warehouse_humanoids")
    summary = {
        "scenario": "Five-lane humanoid palletizing and robot-forklift truck loading demo",
        "scenario_notice": (
            "These simulations are fictitious generic scenarios for demonstration purposes only."
        ),
        "model_version": "warehouse_palletizing_forklift_v4",
        "worker_robots": len(robots),
        "forklift_robots": 1,
        "final_stack_counts": final_stack_counts,
        "simulated_duration_s": round(float(data.time), 2),
        "telemetry_records": len(records),
        "acceptance_checks": {
            "model_loaded": True,
            "five_separate_worker_lanes_present": len(robots) == len(LANE_Y) == 5,
            "cartons_move_on_conveyors": boxes_move_on_belts,
            "robots_stop_before_conveyor": conveyor_clearance_ok,
            "cartons_are_visibly_carried_to_pallets": boxes_carried_to_pallets,
            "payload_body_clearance_preserved": payload_clearance_ok,
            "worker_lane_ownership_preserved_during_palletizing": worker_lane_ownership_ok,
            "articulated_robot_gait_visible": articulated_gait_seen,
            "center_pallet_reaches_seven_cartons": center_stack_reaches_seven,
            "all_workers_stop_before_forklift_release": all_workers_interlocked,
            "forklift_lifts_seven_carton_pallet": forklift_lifts_loaded_pallet,
            "fork_carriage_rises_with_loaded_pallet": fork_carriage_tracks_load,
            "forklift_drives_load_into_green_truck": forklift_enters_truck,
            "forklift_disappears_inside_truck": forklift_hidden_inside_truck,
            "forklift_returns_with_empty_forks": forklift_returns_empty,
            "worker_installs_empty_replacement_pallet": replacement_pallet_installed,
        },
        "outputs": paths,
    }
    summary["passed"] = all(summary["acceptance_checks"].values())
    summary["summary_path"] = write_summary(summary, output_dir, "warehouse_humanoids")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=72.0)
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument(
        "--manual-camera",
        action="store_true",
        help="Keep one user-controlled camera instead of the four-stage portfolio view",
    )
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    args = parser.parse_args()
    print(
        run(
            args.duration,
            args.viewer,
            args.output_dir,
            cinematic_camera=not args.manual_camera,
        )
    )


if __name__ == "__main__":
    main()
