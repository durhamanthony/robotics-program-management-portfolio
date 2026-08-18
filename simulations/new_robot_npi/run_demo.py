from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

import mujoco
import numpy as np

SIM_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SIM_ROOT.parent
sys.path.insert(0, str(SIM_ROOT))

from common.telemetry import write_records, write_summary  # noqa: E402


TARGETS = [
    ("initialize", np.array([0.0, 0.0, 0.0, 0.0, -20.0, 0.0])),
    ("approach_source", np.array([-0.7, 0.45, 25.0, 35.0, -70.0, 10.0])),
    ("tote_transfer_pose", np.array([0.0, 0.35, 0.0, 45.0, -85.0, 15.0])),
    ("approach_destination", np.array([0.7, 0.45, -25.0, 30.0, -65.0, -10.0])),
    ("home", np.array([0.0, 0.0, 0.0, 0.0, -20.0, 0.0])),
]


def run(viewer_enabled: bool, output_dir: Path, phase_seconds: float = 2.5) -> dict:
    model = mujoco.MjModel.from_xml_path(str(Path(__file__).with_name("ad01.xml")))
    data = mujoco.MjData(model)
    records: list[dict] = []
    next_sample = 0.0
    sample_period = 0.1
    controlled_stop_seen = False
    joint_limit_ok = True
    phase_index = 0
    phase_start = 0.0

    def control_target(target: np.ndarray) -> np.ndarray:
        converted = target.copy()
        converted[2:] = np.deg2rad(converted[2:])
        return converted

    targets = [(name, control_target(values)) for name, values in TARGETS]

    def one_step() -> None:
        nonlocal next_sample, controlled_stop_seen, joint_limit_ok, phase_index, phase_start
        sim_time = float(data.time)
        if phase_index < len(targets) - 1 and sim_time - phase_start >= phase_seconds:
            phase_index += 1
            phase_start = sim_time
        phase_name, desired = targets[phase_index]

        stop_active = 6.0 <= sim_time < 6.8
        if stop_active:
            data.ctrl[:] = data.qpos[:6]
            data.qvel[:] = 0.0
            state = "controlled_stop"
            safety = "stop_test"
            fault = "INJECTED_STOP"
            severity = "S2"
            message = "Injected stop held current configuration; release requires validation"
            controlled_stop_seen = True
        else:
            data.ctrl[:] = desired
            state = phase_name
            safety = "normal"
            fault = ""
            severity = ""
            message = "AD-01 concept verification sequence"

        for joint_index in range(model.njnt):
            if model.jnt_limited[joint_index]:
                q_index = model.jnt_qposadr[joint_index]
                lower, upper = model.jnt_range[joint_index]
                if data.qpos[q_index] < lower - 1e-4 or data.qpos[q_index] > upper + 1e-4:
                    joint_limit_ok = False

        if sim_time + 1e-9 >= next_sample:
            error = np.abs(data.qpos[:6] - desired)
            records.append(
                {
                    "timestamp_ns": 1_800_200_000_000_000_000 + int(sim_time * 1e9),
                    "sim_time_s": round(sim_time, 3),
                    "scenario": "ad01_new_robot_npi",
                    "site_id": "LAB-DEMO-01",
                    "robot_id": "AD01-EVT-001",
                    "robot_model": "AD-01-CONCEPT",
                    "software_version": "evt-sim-0.1.0",
                    "mission_id": "VVT-SEQUENCE-001",
                    "operational_state": state,
                    "safety_state": safety,
                    "battery_pct": round(95.0 - sim_time * 0.25, 1),
                    "network_rssi_dbm": -48,
                    "x_m": round(float(data.qpos[0]), 3),
                    "y_m": round(float(data.qpos[1]), 3),
                    "component": "motion_control",
                    "fault_code": fault,
                    "severity": severity,
                    "correlation_id": "AD01-STOP-0001" if fault else "",
                    "message": f"{message}; max tracking error={float(error.max()):.4f}",
                }
            )
            next_sample += sample_period
        mujoco.mj_step(model, data)

    duration = phase_seconds * len(targets) + 1.5
    if viewer_enabled:
        from mujoco import viewer

        with viewer.launch_passive(model, data) as active_viewer:
            while data.time < duration and active_viewer.is_running():
                started = time.time()
                one_step()
                active_viewer.sync()
                remaining = model.opt.timestep - (time.time() - started)
                if remaining > 0:
                    time.sleep(remaining)
    else:
        while data.time < duration:
            one_step()

    final_target = targets[-1][1]
    final_error = np.abs(data.qpos[:6] - final_target)
    paths = write_records(records, output_dir, "new_robot_npi")
    checks = {
        "model_loaded": model.nq >= 6 and model.nu == 6,
        "controlled_stop_recorded": controlled_stop_seen,
        "joint_limits_respected": joint_limit_ok,
        "returned_near_home": bool(float(final_error.max()) < math.radians(6.0)),
        "telemetry_created": len(records) > 20,
    }
    summary = {
        "scenario": "AD-01 new robot NPI verification demo",
        "scenario_notice": "These simulations are fictitious generic scenarios for demonstration purposes only.",
        "simulated_duration_s": round(float(data.time), 2),
        "max_final_error": round(float(final_error.max()), 6),
        "acceptance_checks": checks,
        "outputs": paths,
        "passed": all(checks.values()),
    }
    summary["summary_path"] = write_summary(summary, output_dir, "new_robot_npi")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--viewer", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    parser.add_argument("--phase-seconds", type=float, default=2.5)
    args = parser.parse_args()
    print(run(args.viewer, args.output_dir, args.phase_seconds))


if __name__ == "__main__":
    main()
