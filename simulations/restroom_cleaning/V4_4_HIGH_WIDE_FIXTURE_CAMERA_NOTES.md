# Restroom MuJoCo v4.4 — Higher, Wider Fixture Camera

## Correction made

The toilet-and-urinal camera is now higher and farther from the room than the v4.3 camera. It uses the same high, wide framing as the opening overview so the cleaning robot, both toilet bays, the urinal bay, and the complete restroom footprint remain visible when MuJoCo's two control panels are open.

## Preserved behavior

- The room layout and cleaning choreography are unchanged.
- The floor-cleaning camera remains the approved wide diagonal view.
- The sink-and-mirror camera remains the approved behind-and-above-the-robot view.
- The complete two-loop sequence still lasts 146 seconds, including the 30-second charging wait.

## Verification

The MuJoCo window title must read `public_restroom_humanoid_cleaning_v4_4`.
