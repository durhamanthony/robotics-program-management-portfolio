# Restroom MuJoCo v4 — Audit Release Notes

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Changes made from the marked restroom v3 review

1. Moved both toilets and the urinal toward the marked back-room destination.
2. Moved the marked urinal-side partition to the outer side of toilet 1.
3. Moved the cleaning-supply cabinet and charging station to the marked right wall.
4. Removed both marked toilet doors while retaining the other room and privacy walls.
5. Extended the checkerboard floor appearance through the full room and reduced the light/specular washout that created the large white center.
6. Added four fixed audit cameras corresponding to the supplied overview, toilet, open-floor, and sink/mirror references.
7. Added explicit left-side, right-side, and middle Swiffer passes for each toilet and the urinal.
8. Added open-floor Swiffer coverage, two-arm sink and mirror wiping, sink-floor cleaning, and a doorway-to-charger Swiffer route.
9. Added one 30-second charging wait, a complete second cleaning loop, and a final stopped state at the charger.
10. Added a one-click Windows launcher and shared the same choreography with the website-video renderer.

## Timing control

- Cleaning loop 1: 58 seconds
- Charging wait: 30 seconds
- Cleaning loop 2: 58 seconds
- Final stop: 146 seconds elapsed

These simulations are fictitious generic scenarios for demonstration purposes only.
