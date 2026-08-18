# Warehouse Palletizing and Truck-Loading Demo — Version 4

## What you should see

The MuJoCo window title must say `warehouse_palletizing_forklift_v4`. The scene contains five separate blue worker lanes, five long black conveyor belts, five floor pallet stations, a yellow robot-operated forklift, and an open-back green truck with a differentiated cab, windows, wheels, lights, cargo interior, and loading ramp.

The complete visual sequence runs for 72 seconds:

1. A carton advances along each worker's conveyor.
2. Each robot walks only in its assigned lane and stops before the conveyor frame.
3. The robot lifts the carton, turns without passing it through its body, and visibly carries it to the floor pallet.
4. The robot places the carton on its pallet and returns for the next carton.
5. The center pallet builds one carton at a time until the stack is seven cartons high.
6. At seven cartons, all five workers stop under a global transfer-zone interlock.
7. A robot-driven forklift enters the center aisle, raises its fork carriage with the entire pallet and seven-carton stack, turns toward the truck, climbs the ramp, and drives through the open rear.
8. The loaded forklift disappears inside the truck while depositing the load, then emerges with empty forks and clears the aisle.
9. Worker 05 retrieves a stored empty pallet, carries it through the protected cross aisle, and installs it at the empty center station.

The lane status lights are green during palletizing, amber during the full-pallet interlock, and cyan while Worker 05 replenishes the pallet.

## Run on Windows

From Command Prompt in the repository root:

```text
.venv\Scripts\python.exe simulations\warehouse_humanoids\run_demo.py --viewer --duration 72
```

The side panels are hidden when the viewer opens. The default portfolio camera changes at the worker interlock, truck-loading phase, and pallet-replenishment phase so each handoff can be seen clearly. Press `Tab` or `Shift+Tab` to reveal the panels.

For one user-controlled camera with no automatic camera changes, add `--manual-camera`. Then use left-drag to orbit, right-drag to pan, and the mouse wheel to zoom.

If the window title does not say `warehouse_palletizing_forklift_v4`, Windows is still running an older copy of the files.

## Generated evidence

The run writes CSV, JSONL, MCAP, and an acceptance-summary JSON file to `outputs/`. The summary checks the conveyor motion, stop clearance, visible carrying, seven-carton stack, global interlock, forklift load, truck entry, empty return, and replacement-pallet installation.

## Portfolio boundary

These simulations are fictitious generic scenarios for demonstration purposes only.
