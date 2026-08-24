# MuJoCo Demo — Retail Backroom Humanoid Fulfillment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This MuJoCo operations visualization mirrors Case 01. It uses a coherent department-store backroom: a ground-floor receiving table, tablet station, human-scale aisles, garment rack, a guarded four-step stock platform, upper shoe shelving, a put-away cart, and an employee handoff point. The blue humanoid retrieves a shoe carton from the raised shelf and carries it to the employee handoff. The green humanoid picks a carton from receiving, visibly carries it through the open aisle below the table, and places it on the put-away cart.

The model demonstrates route ownership, two distinct item movements, handoff/put-away states, and deterministic route-clearance checks. It does not claim a commercial humanoid can autonomously perform the task, and it is not a dynamics, grasp, collision-avoidance, stair-safety, or certified-control validation.

## Windows run

From the repository folder:

```bat
.venv\Scripts\python.exe simulations\retail_humanoids\run_demo.py --viewer --duration 36
```

The browser-playable portfolio video is rendered from `retail.xml`. Motion is scripted for program-workflow communication and is not locomotion, grasp, or safety-performance validation.
