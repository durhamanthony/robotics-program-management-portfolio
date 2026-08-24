# MuJoCo Operations Demonstrations

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


These small, explainable simulations support project/program discussions by exposing operating states, faults, telemetry, acceptance evidence, and service handoffs. They are not production controllers, certified safety systems, learned locomotion policies, or vendor-accurate digital twins.

## Demonstrations

- `retail_inbound` + `retail_humanoids` — one retail story begins with a robot-operated forklift unloading a full pallet from a truck. After the forklift clears receiving, humanoids stock lower and raised racks, visibly using four physical stair treads where required. The video then cuts to tablet-driven retrieval and delivery to a courtesy drop-off table.
- `quadruped_security` — three quadruped visual agents move through a fenced industrial site with pavement, rough ground, steps, a loading platform, a vehicle gate, and charging docks. Abstract colored route lines are intentionally excluded.
- `open_quadruped_raas` — a generic open-source-derived quadruped fleet moves through source intake, calibration, functional test, fault capture, replacement rotation, and service-release states. It is not a digital twin of a named platform.
- `restroom_cleaning` — a humanoid visual agent follows a restroom servicing route across toilets, sinks, mirrors, floors, paper supplies, and trash. Electrical work and light-bulb replacement are excluded.

Retail, security, and restroom browser videos are rendered from the MuJoCo XML models in this repository. Productization uses a workflow animation plus a separately compiled generic model and deterministic state check. The support case uses a synthetic event-to-case data workflow in `tools/support-operations-lab`. These artifacts do not establish learned locomotion, grasp reliability, collision-safe autonomy, certified controls, robot-operated forklift safety, or vendor-equivalent performance.

## Run locally

```bash
pip install -r simulations/requirements.txt
python simulations/retail_humanoids/run_demo.py --viewer --duration 36
python simulations/quadruped_security/run_demo.py --viewer --duration 45
python simulations/open_quadruped_raas/run_demo.py --viewer --duration 36
python tools/support-operations-lab/build_cases.py
python simulations/test_models.py
```

To regenerate the case-study videos on Windows, double-click `RENDER_ALL_MUJOCO_VIDEOS_WINDOWS.bat`. The retail renderer composes the inbound and order-fulfillment models into one 40-second clip. The support animation is rebuilt from its synthetic data workflow by the same script. Use interactive viewers only on a graphical desktop. Website visitors need no terminal, Python, or simulator installation.
