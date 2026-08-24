# Public Restroom Humanoid Cleaning — MuJoCo Capability Demo v4.4

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This fictional generic demonstration supports Case 05, the Pacific Gateway International Airport controlled restroom-cleaning pilot. It shows a human-scale robot cleaning an existing public restroom without retooling the room for a wheeled platform. It is a visualization of a planned operating sequence, not a certified cleaning process or a claim of autonomous production performance.

The corresponding program dashboard separates three accountable viewpoints: seller/integrator Project Manager, humanoid manufacturer Project Manager, and airport owner/operator Project Manager. The completed case artifacts are in `scenarios/05-airport-restroom-humanoid-deployment/`.

## Audit-approved room layout

- Two toilets and one wall-mounted urinal are grouped along the back of the room.
- The marked privacy wall was moved to the outer side of toilet 1; the other stall walls remain.
- Both toilet doors were removed, leaving open-front cleaning bays.
- The supply cabinet and charging station sit against the right building wall.
- The two sinks, faucets, mirrors, mirror backing wall, garbage bin, and paper-towel dispenser remain visible.
- The entry walls stay low so the full room can be seen during the audit.
- The nonreflective checkerboard material covers the full floor; reduced lighting prevents a washed-out white center.
- The opening, toilet, and floor cameras are pulled farther back and widened so the complete restroom footprint, every toilet bay, and the urinal remain visible even when both MuJoCo control panels are open.
- Toilet and urinal cleaning use a higher, farther elevated diagonal audit angle, keeping the robot, both toilet bays, the urinal, and more of the restroom visible together.
- The sink/mirror camera is centered directly behind and above the robot, keeping its body, both animated arms, both sinks, and both mirrors visible during wiping.

## Complete 146-second sequence

**Table 1. Complete 146-second sequence — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Time | Camera | Demonstrated action |
|---:|---|---|
| 0–3 seconds | Top overview | Start from the elevated top angle and establish the room. |
| 3–12 seconds | Elevated diagonal fixture angle | Enter toilet 1; Swiffer the left side, right side, and middle; exit. |
| 12–21 seconds | Elevated diagonal fixture angle | Repeat the three-pass process for toilet 2. |
| 21–30 seconds | Elevated diagonal fixture angle | Repeat the three-pass process at the urinal. |
| 30–38 seconds | Floor angle | Swiffer a visible zig-zag route across the open middle floor. |
| 38–48 seconds | Sink angle | Reach with both arms to wipe sinks and mirrors, then Swiffer the sink-area floor. |
| 48–58 seconds | Toilet angle | Return to the doorway and Swiffer from the door to the charging station. |
| 58–88 seconds | Toilet angle | Wait at the charging station for 30 seconds. |
| 88–146 seconds | Same staged angles | Repeat the complete cleaning loop once more. |
| After 146 seconds | Top overview | Stop at the charging station and keep the final audit scene open. |

The Swiffer is a visible tool body that travels with the robot. The two arm bodies are independently animated during sink and mirror wiping. The choreography uses clear approach paths and open stall fronts so the robot does not pass through retained walls or fixtures.

## Run on Windows

From the repository root, double-click `RUN_RESTROOM_DEMO_WINDOWS.bat`.

Alternatively, run:

```text
.venv\Scripts\python.exe simulations\restroom_cleaning\run_demo.py --viewer
```

The live audit completes its second loop at 146 seconds and then remains stopped at the charger until you close the window. To close automatically at 150 seconds, add `--duration 150`.

## Source of truth

- `restroom.xml` — v4 room, fixtures, labeled equipment, collision geometry, and four fixed cameras.
- `restroom_sequence.py` — shared timed choreography used by the live viewer and video renderer.
- `run_demo.py` — Windows-friendly live-view entry point.
- `../../scripts/render_mujoco_videos.py` — generates the matching browser-playable portfolio video.
