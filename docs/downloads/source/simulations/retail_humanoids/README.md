# MuJoCo Demo — Retail Backroom Humanoid Fulfillment

This MuJoCo operations visualization mirrors Case 01. It uses a coherent department-store backroom: a ground-floor receiving table, tablet station, human-scale aisles, garment rack, a guarded four-step stock platform, upper shoe shelving, and an employee handoff point. Two scripted humanoid figures perform retrieval and put-away routes without requiring the store to rebuild the backroom for a wheeled robot.

The model demonstrates route ownership, item handoff, exception-safe sequence, and telemetry states. It does not claim a commercial humanoid can autonomously perform the task, and it is not a dynamics, grasp, stair-safety, or certified-control validation.

## Windows run

From the repository folder:

```bat
.venv\Scripts\python.exe simulations\retail_humanoids\run_demo.py --viewer --duration 36
```

The browser-playable portfolio video is rendered from `retail.xml`. Motion is scripted for program-workflow communication and is not locomotion, grasp, or safety-performance validation.
