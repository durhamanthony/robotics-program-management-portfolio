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
from quadruped_security.security_sequence import frame_at, route_clearance_report  # noqa: E402


def _smooth(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


def _yaw_quat(yaw: float) -> list[float]:
    return [math.cos(yaw / 2.0), 0.0, 0.0, math.sin(yaw / 2.0)]


def _timeline_pose(
    sim_time: float,
    keyframes: list[tuple[float, float, float, float]],
) -> tuple[float, float, float, float]:
    if sim_time <= keyframes[0][0]:
        _, x_pos, y_pos, z_pos = keyframes[0]
        return x_pos, y_pos, z_pos, 0.0
    for start, end in zip(keyframes, keyframes[1:]):
        if sim_time <= end[0]:
            duration = max(0.001, end[0] - start[0])
            blend = _smooth((sim_time - start[0]) / duration)
            x_pos = start[1] + (end[1] - start[1]) * blend
            y_pos = start[2] + (end[2] - start[2]) * blend
            z_pos = start[3] + (end[3] - start[3]) * blend
            yaw = math.atan2(end[2] - start[2], end[1] - start[1])
            return x_pos, y_pos, z_pos, yaw
    _, x_pos, y_pos, z_pos = keyframes[-1]
    return x_pos, y_pos, z_pos, 0.0


ROBOT_A_ROUTE = [
    (0.0, -6.7, -5.1, 0.0),
    (9.0, 5.7, -5.1, 0.0),
    (15.0, 6.6, -1.4, 0.0),
    (25.0, 6.6, -1.4, 0.0),
    (28.0, 6.6, 1.0, 0.0),
    (32.0, 6.6, 1.0, 0.0),
    (40.0, 6.6, 5.1, 0.0),
    (50.0, -6.6, 5.1, 0.0),
    (60.0, -6.6, -4.5, 0.0),
]

ROBOT_B_ROUTE = [
    (0.0, -5.35, -5.1, 0.0),
    (7.0, -5.0, 2.8, 0.0),
    (12.0, -3.9, 3.85, 0.12),
    (17.0, 2.2, 3.75, 0.0),
    (23.0, 4.15, 3.75, 1.24),
    (27.0, 4.7, 3.75, 1.24),
    (31.0, 2.2, 3.75, 0.0),
    (39.0, -4.2, 1.0, 0.0),
    (48.0, -4.8, -3.8, 0.0),
    (60.0, -5.35, -5.1, 0.0),
]

ROBOT_C_ROUTE = [
    (0.0, -4.0, -5.1, 0.0),
    (10.0, -4.0, -5.1, 0.0),
    (17.0, 0.0, -4.3, 0.0),
    (25.0, 4.1, -3.1, 0.0),
    (34.0, 2.8, 1.8, 0.0),
    (40.0, 0.0, 2.8, 0.0),
    (50.0, -4.0, -5.1, 0.0),
    (60.0, -4.0, -5.1, 0.0),
]


def _body_mocap_id(model: mujoco.MjModel, name: str) -> int:
    body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)
    if body_id < 0:
        raise ValueError(f"Missing MuJoCo body: {name}")
    return int(model.body_mocapid[body_id])


def _geom_id(model: mujoco.MjModel, name: str) -> int:
    geom_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, name)
    if geom_id < 0:
        raise ValueError(f"Missing MuJoCo geom: {name}")
    return int(geom_id)


def run(
    duration: float,
    viewer_enabled: bool,
    output_dir: Path,
    cinematic_camera: bool = True,
) -> dict:
    model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("security.xml")))
    data = mujoco.MjData(model)
    robots = ["quadruped_01", "quadruped_02", "quadruped_03"]
    mocap_ids = [_body_mocap_id(model, robot) for robot in robots]
    sensor_ids = [_geom_id(model, f"sensor_{index:02d}") for index in range(1, 4)]
    event_beacon_id = _geom_id(model, "event_beacon")
    soc_indicator_id = _geom_id(model, "soc_indicator")
    dock_light_id = _geom_id(model, "dock_c_light")

    records: list[dict] = []
    next_sample = 0.0
    sample_period = 0.5
    flags = {
        "route_traversal": False,
        "stair_and_terrain_traversal": False,
        "anomaly_detected": False,
        "human_verified": False,
        "network_safe_stop": False,
        "sensor_degraded": False,
        "low_battery_docked": False,
    }

    def one_step() -> None:
        nonlocal next_sample
        sim_time = float(data.time)

        flags["route_traversal"] = flags["route_traversal"] or sim_time >= 10.0
        flags["stair_and_terrain_traversal"] = flags["stair_and_terrain_traversal"] or sim_time >= 34.0
        flags["anomaly_detected"] = flags["anomaly_detected"] or sim_time >= 18.0
        flags["human_verified"] = flags["human_verified"] or sim_time >= 22.0
        flags["network_safe_stop"] = flags["network_safe_stop"] or sim_time >= 28.0
        flags["sensor_degraded"] = flags["sensor_degraded"] or sim_time >= 33.0
        flags["low_battery_docked"] = flags["low_battery_docked"] or sim_time >= 50.0

        model.geom_rgba[event_beacon_id] = [1.0, 0.12, 0.05, 1.0] if 18.0 <= sim_time < 25.0 else [1.0, 0.58, 0.05, 1.0]
        model.geom_rgba[soc_indicator_id] = [0.05, 0.82, 0.95, 1.0] if sim_time >= 22.0 else [0.08, 0.85, 0.30, 1.0]
        model.geom_rgba[sensor_ids[0]] = [1.0, 0.18, 0.05, 1.0] if 28.0 <= sim_time < 32.0 else [0.05, 0.75, 0.95, 1.0]
        model.geom_rgba[sensor_ids[1]] = [1.0, 0.62, 0.02, 1.0] if 33.0 <= sim_time < 39.0 else [0.05, 0.75, 0.95, 1.0]
        model.geom_rgba[sensor_ids[2]] = [0.08, 0.85, 0.30, 1.0] if sim_time >= 50.0 else [0.05, 0.75, 0.95, 1.0]
        model.geom_rgba[dock_light_id] = [0.08, 0.85, 0.30, 1.0] if sim_time >= 50.0 else [0.08, 0.35, 0.18, 1.0]

        frame = frame_at(sim_time / 60.0)
        visual_states = [
            (frame.perimeter_pose, frame.perimeter_state),
            (frame.stair_pose, frame.stair_state),
            (frame.reserve_pose, frame.reserve_state),
        ]
        for index, (robot, mocap_id, visual) in enumerate(zip(robots, mocap_ids, visual_states)):
            (x_pos, y_pos, z_pos, yaw), state = visual
            safety = "normal"
            fault = ""
            severity = ""
            component = "fleet"
            message = "Human-supervised scheduled patrol"
            battery = 94.0 - sim_time * (0.50 + index * 0.03)
            rssi = -56 - index * 3

            if index == 0 and 18.0 <= sim_time < 25.0:
                state = "observation_hold"
                component = "security_observation"
                fault = "GATE_ANOMALY_OBSERVED"
                severity = "S2"
                message = "Gate anomaly sent to human responder"
                if sim_time >= 22.0:
                    message = "Human responder verified and dispositioned gate anomaly"
            if index == 0 and 28.0 <= sim_time < 32.0:
                state = "communications_safe_stop"
                safety = "safe_stop"
                component = "network"
                fault = "NETWORK_LOSS"
                severity = "S2"
                message = "Network lost; robot holds inside approved geofence"
                rssi = -100
            if index == 1 and 33.0 <= sim_time < 39.0:
                state = "degraded_patrol"
                component = "thermal_camera"
                fault = "THERMAL_CAMERA_DEGRADED"
                severity = "S3"
                message = "Thermal capability degraded; operator receives health alert"
            if index == 2 and sim_time < 10.0:
                state = "charging_reserve"
                message = "Reserve robot available at assigned dock"
                battery = 98.0
            if index == 2 and 40.0 <= sim_time < 50.0:
                state = "low_battery_return"
                component = "battery"
                fault = "LOW_BATTERY_RETURN"
                severity = "S3"
                message = "Coverage rotation active; robot returns to assigned dock"
                battery = max(18.0, 32.0 - (sim_time - 40.0) * 1.4)
            if index == 2 and sim_time >= 50.0:
                state = "docked_charging"
                component = "battery"
                message = "Low-battery return completed; charging confirmed"
                battery = min(28.0, 18.0 + (sim_time - 50.0))

            data.mocap_pos[mocap_id] = [x_pos, y_pos, z_pos]
            data.mocap_quat[mocap_id] = _yaw_quat(yaw)

            if sim_time + 1e-9 >= next_sample:
                records.append(
                    {
                        "table_title": "Table 1. Quadruped security scripted telemetry",
                        "timestamp_ns": 1_800_100_000_000_000_000 + int(sim_time * 1e9),
                        "sim_time_s": round(sim_time, 3),
                        "scenario": "three_quadruped_night_security",
                        "site_id": "SEC-DEMO-01",
                        "robot_id": robot.upper(),
                        "robot_model": "PORTFOLIO-Q1",
                        "software_version": "demo-2.0.0",
                        "mission_id": f"PATROL-{index + 1:02d}",
                        "operational_state": state,
                        "safety_state": safety,
                        "battery_pct": round(max(0.0, battery), 1),
                        "network_rssi_dbm": rssi,
                        "x_m": round(x_pos, 3),
                        "y_m": round(y_pos, 3),
                        "z_m": round(z_pos, 3),
                        "component": component,
                        "fault_code": fault,
                        "severity": severity,
                        "correlation_id": f"SEC-{robot[-2:]}-{int(sim_time):04d}" if fault else "",
                        "human_verification": "verified" if index == 0 and 22.0 <= sim_time < 25.0 else "",
                        "message": message,
                        "evidence_class": "Derived calculation",
                        "confidence": "Low",
                        "source_or_validation": "Deterministic scripted MuJoCo workflow; not production autonomy evidence",
                    }
                )
        if sim_time + 1e-9 >= next_sample:
            next_sample += sample_period
        mujoco.mj_step(model, data)

    if viewer_enabled:
        from mujoco import viewer

        with viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False) as active_viewer:
            active_camera_name = frame_at(0.0).camera
            if cinematic_camera:
                active_viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
                active_viewer.cam.fixedcamid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, active_camera_name)
            active_viewer.sync()
            while data.time < duration and active_viewer.is_running():
                started = time.time()
                one_step()
                next_camera_name = frame_at(float(data.time) / 60.0).camera
                if cinematic_camera and next_camera_name != active_camera_name:
                    active_camera_name = next_camera_name
                    active_viewer.cam.fixedcamid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_CAMERA, active_camera_name)
                active_viewer.sync()
                remaining = model.opt.timestep - (time.time() - started)
                if remaining > 0:
                    time.sleep(remaining)
    else:
        while data.time < duration:
            one_step()

    paths = write_records(records, output_dir, "quadruped_security")
    summary = {
        "scenario": "Three-quadruped human-supervised night-security operations demo",
        "robots": len(robots),
        "simulated_duration_s": round(float(data.time), 2),
        "telemetry_records": len(records),
        "acceptance_checks": {"model_loaded": True, **flags, **route_clearance_report()},
        "outputs": paths,
    }
    summary["passed"] = all(
        value for key, value in summary["acceptance_checks"].items()
        if key != "minimum_active_robot_center_separation_m"
    )
    summary["summary_path"] = write_summary(summary, output_dir, "quadruped_security")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument("--manual-camera", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    args = parser.parse_args()
    print(run(args.duration, args.viewer, args.output_dir, cinematic_camera=not args.manual_camera))


if __name__ == "__main__":
    main()
