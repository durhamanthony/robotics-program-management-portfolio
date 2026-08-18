# MuJoCo Operations and Capability Demonstrations

These small, explainable simulations support project/program discussions by exposing operating states, faults, telemetry, acceptance evidence, and service handoffs. They are not production controllers, certified safety systems, learned locomotion policies, or vendor-accurate digital twins.

## Demonstrations

- `retail_humanoids` — two humanoid visual agents follow tablet-driven retail backroom retrieval routes through existing human-scale aisles, a receiving zone, garment rack, four-step stock platform, shoe shelves, and employee handoff.
- `quadruped_security` — three quadruped visual agents move through a fenced industrial site with pavement, rough ground, steps, a loading platform, a vehicle gate, and charging docks. Abstract colored route lines are intentionally excluded.
- `new_robot_npi` — the AD-01 Autonomous Tote Transfer Robot, a fictional actuated wheeled mobile manipulator, runs a repeatable transfer between two fixed stations.
- `support_lab` — a physical field-service bay shows fault intake, local diagnosis, a staged replacement module, verification, and return to service. The companion Python lab produces synthetic service-case evidence.
- `restroom_cleaning` — a humanoid visual agent follows a restroom servicing route across toilets, sinks, mirrors, floors, paper supplies, and trash. Electrical work and light-bulb replacement are excluded.
- `warehouse_capability` — two humanoid visual agents move cartons from conveyors to a seven-carton pallet load before a robot-operated forklift transfers the load into a truck and an empty pallet is staged.

All six browser videos are rendered directly from the MuJoCo XML models in this repository. Retail, security, support, restroom, and warehouse use scripted mocap bodies for operations visualization. AD-01 uses physical joints and position actuators. These scenes do not establish learned locomotion, grasp reliability, collision-safe autonomy, certified controls, or vendor-equivalent performance.

## Run locally

```bash
pip install -r simulations/requirements.txt
python simulations/retail_humanoids/run_demo.py --viewer --duration 36
python simulations/quadruped_security/run_demo.py --viewer --duration 45
python simulations/new_robot_npi/run_demo.py --viewer
python simulations/support_lab/triage.py
python simulations/test_models.py
```

To regenerate all six browser videos on Windows, double-click `RENDER_ALL_MUJOCO_VIDEOS_WINDOWS.bat`. Use interactive viewers only on a graphical desktop. Website visitors need no terminal, Python, or MuJoCo.
