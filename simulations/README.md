# MuJoCo Operations Demonstrations

These demos are intentionally small and explainable. They support program-management and service-operations conversations by creating robot state, faults, telemetry, acceptance evidence, and incident workflows.

They are **not** production controllers, safety systems, learned locomotion policies, or vendor-accurate digital twins.

## Demos

- `warehouse_humanoids` — five articulated humanoid visual agents work in separate conveyor-fed lanes, carry cartons to floor pallets, and stop when the center stack reaches seven. A robot-operated forklift transfers the loaded pallet into an open-back green truck and returns empty before a worker installs a replacement pallet. See the [warehouse demo guide](warehouse_humanoids/README.md).
- `quadruped_security` — three simplified quadruped visual agents patrol a campus route; network, sensor, and battery events test human-supervised escalation.
- `new_robot_npi` — an actuated mobile-manipulator concept executes a repeatable validation sequence and an injected controlled stop.
- `support_lab` — converts fault telemetry into a deduplicated service-ticket register and scorecard.

The warehouse and security models use MuJoCo mocap bodies as an operations visualization. The new-robot model uses physical joints and position actuators. This distinction is documented so viewers do not mistake motion scripting for advanced control engineering.

## Outputs

Each demo produces CSV, JSONL, MCAP, and JSON summary files in `outputs/`. Open the MCAP files with Foxglove; use CSV/JSONL in analytics or the support lab.

## Run

```bash
pip install -r simulations/requirements.txt
python simulations/warehouse_humanoids/run_demo.py --duration 72
python simulations/quadruped_security/run_demo.py --duration 45
python simulations/new_robot_npi/run_demo.py
python simulations/support_lab/triage.py
python simulations/test_models.py
```

Use `--viewer` only on a machine with a graphical desktop.
