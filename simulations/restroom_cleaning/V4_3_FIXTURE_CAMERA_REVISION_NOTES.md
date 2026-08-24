# Restroom MuJoCo v4.3 — Fixture Camera Revision

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This camera-only refinement follows the review of the v4.2 sequence.

1. Toilet 1, toilet 2, and urinal cleaning now use the approved v3 elevated diagonal audit angle.
2. That angle shows the robot, fixture bays, and more of the restroom at the same time.
3. The v4.2 floor-cleaning camera remains unchanged.
4. The approved v4.2 behind-the-robot sink/mirror camera remains unchanged.
5. The model title now reads `public_restroom_humanoid_cleaning_v4_3`.

No room geometry, robot path, cleaning motion, timing, or two-loop logic changed.
