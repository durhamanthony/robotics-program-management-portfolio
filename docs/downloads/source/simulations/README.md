# MuJoCo Operations and Capability Demonstrations

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


These small, explainable simulations support project/program discussions by exposing operating states, faults, telemetry, acceptance evidence, and service handoffs. They are not production controllers, certified safety systems, learned locomotion policies, or vendor-accurate digital twins.

## Demonstrations

- `retail_humanoids` — two humanoid visual agents follow tablet-driven retail backroom retrieval routes through existing human-scale aisles, a receiving zone, garment rack, four-step stock platform, shoe shelves, and employee handoff.
- `quadruped_security` — three quadruped visual agents move through a fenced industrial site with pavement, rough ground, steps, a loading platform, a vehicle gate, and charging docks. Abstract colored route lines are intentionally excluded.
- `open_quadruped_raas` — a generic open-source-derived quadruped fleet moves through source intake, calibration, functional test, fault capture, replacement rotation, and service-release states. It is not a digital twin of a named platform.
- `restroom_cleaning` — a humanoid visual agent follows a restroom servicing route across toilets, sinks, mirrors, floors, paper supplies, and trash. Electrical work and light-bulb replacement are excluded.
- `warehouse_capability` — two humanoid visual agents move cartons from conveyors to a seven-carton pallet load before a robot-operated forklift transfers the load into a truck and an empty pallet is staged.

Retail, security, restroom, and warehouse browser videos are rendered from the MuJoCo XML models in this repository. Productization uses a workflow animation plus a separately compiled generic model and deterministic state check. The support case uses a synthetic event-to-case data workflow in `tools/support-operations-lab`. These artifacts do not establish learned locomotion, grasp reliability, collision-safe autonomy, certified controls, or vendor-equivalent performance.

## Run locally

```bash
pip install -r simulations/requirements.txt
python simulations/retail_humanoids/run_demo.py --viewer --duration 36
python simulations/quadruped_security/run_demo.py --viewer --duration 45
python simulations/open_quadruped_raas/run_demo.py --viewer --duration 36
python tools/support-operations-lab/build_cases.py
python simulations/test_models.py
```

To regenerate the five simulator videos on Windows, double-click `RENDER_ALL_MUJOCO_VIDEOS_WINDOWS.bat`. The support animation is rebuilt from its synthetic data workflow by the same script. Use interactive viewers only on a graphical desktop. Website visitors need no terminal, Python, or simulator installation.
