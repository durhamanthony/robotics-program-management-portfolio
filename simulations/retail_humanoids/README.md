# MuJoCo Demo — Retail Backroom Humanoid Fulfillment

This simplified MuJoCo operations visualization mirrors Case 01. Two mocap humanoid figures receive employee tablet requests, move through existing backroom aisles and a short split-level route, retrieve approved shoe boxes, deliver them to an employee handoff counter, and return to staging.

The model demonstrates route ownership, item handoff, exception-safe sequence, and telemetry states. It does not claim a commercial humanoid can autonomously perform the task, and it is not a dynamics, grasp, stair-safety, or certified-control validation.

## Windows run

From the repository folder:

```bat
.venv\Scripts\python.exe simulations\retail_humanoids\run_demo.py --viewer --duration 36
```

The browser-playable portfolio video is a separate operational workflow animation so recruiters do not need Python or MuJoCo.
