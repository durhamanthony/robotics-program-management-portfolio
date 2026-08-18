# Quadruped Night-Security Operations Demo

## What the viewer shows

The scene is a fenced industrial campus with a warehouse, guard station, vehicle gate, pavement, stairs, raised loading platform, rough-terrain section, three charging docks, perimeter lighting, and a human Security Operations Center responder. Earlier colored map-like route lines were removed because they were visually ambiguous; the physical pavement, terrain, robot positions, gate beacon, and docks now communicate the patrol sequence.

The 60-second sequence demonstrates:

1. Robot A patrols the outer perimeter while Robot B covers the building and terrain route; Robot C begins as the charging reserve.
2. Robot B traverses the rough-ground section and the stepped loading-platform route.
3. Robot A detects a staged gate anomaly. The event beacon changes from amber to red and the human responder records verification; the robot does not decide or execute a security response.
4. Robot A enters a communications safe stop during an injected network loss and resumes only after recovery.
5. Robot B reports a degraded thermal sensor; its status lamp turns amber and the evidence records the reduced capability.
6. Robot C rotates into coverage, reaches the low-battery threshold, returns to its assigned dock, and turns its dock/status indicators green.

## Run on Windows

From Command Prompt in the repository root:

```text
.venv\Scripts\python.exe simulations\quadruped_security\run_demo.py --viewer --duration 60
```

The viewer opens without side panels. Add `--manual-camera` to disable the two automatic overview changes. Use left-drag to orbit, right-drag to pan, and the mouse wheel to zoom.

## Evidence

The run writes CSV, JSONL, MCAP, and JSON summary files into `outputs/`. The summary checks route traversal, stair/terrain traversal, anomaly detection, human verification, communications safe stop, sensor-degradation alert, and low-battery dock return.

The operational thresholds for the 30-night pilot remain in the [Case 2 requirements matrix](../../scenarios/02-quadruped-security-deployment/REQUIREMENTS_TRACEABILITY.csv); one accelerated animation is not a substitute for that acceptance window.
