# MuJoCo Operations Demonstrations

These small, explainable simulations support project/program discussions by exposing operating states, faults, telemetry, acceptance evidence, and service handoffs. They are not production controllers, certified safety systems, learned locomotion policies, or vendor-accurate digital twins.

## Demonstrations

- `retail_humanoids` — two humanoid visual agents follow tablet-driven retail backroom retrieval routes through existing human-scale aisles, a door, and a short split-level area.
- `quadruped_security` — three quadruped visual agents patrol a campus route while network, sensor, battery, and human-supervision events are exercised.
- `new_robot_npi` — an actuated mobile-manipulator concept runs a repeatable two-station verification sequence and injected controlled stop.
- `support_lab` — converts robot fault telemetry into deduplicated service cases and a support scorecard.

The retail and security models use MuJoCo mocap bodies for operations visualization. The new-product model uses physical joints and position actuators. Browser videos are operational animations built for recruiters; they are not labeled as MuJoCo renders.

## Run locally

```bash
pip install -r simulations/requirements.txt
python simulations/retail_humanoids/run_demo.py --viewer --duration 36
python simulations/quadruped_security/run_demo.py --viewer --duration 45
python simulations/new_robot_npi/run_demo.py --viewer
python simulations/support_lab/triage.py
python simulations/test_models.py
```

Use `--viewer` only on a graphical desktop. Website visitors need no terminal, Python, or MuJoCo.
