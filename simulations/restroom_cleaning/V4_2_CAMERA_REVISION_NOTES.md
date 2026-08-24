# Restroom MuJoCo v4.2 — Camera Revision

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


This revision responds to the v10, v11, and v12 visual audit screenshots.

1. The sink/mirror camera was moved from the fixture side to a centered position directly behind and above the robot.
2. The sink view now looks over the robot toward both sinks and mirrors, keeping the robot body and both animated arms visible.
3. The opening, toilet-cleaning, and floor-cleaning cameras were pulled farther back.
4. Their fields of view were widened to keep the complete restroom, all toilet/urinal bays, and room boundaries visible in MuJoCo's narrow center viewport.
5. The model title now reads `public_restroom_humanoid_cleaning_v4_2`, making the updated file easy to verify.

No room geometry, cleaning choreography, timing, or collision logic changed in this camera-only revision.
