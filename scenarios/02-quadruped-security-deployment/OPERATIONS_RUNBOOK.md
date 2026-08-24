# Security Robotics Operations Runbook

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Start of patrol

Review weather/site restrictions; confirm operator coverage; inspect robots/docks; check battery, localization, sensors, version, alerts, time sync, and network; review open incidents/route changes; authorize missions.

## Alert handling

1. Confirm robot health, location, time, confidence, and observation context.
2. Do not command closer approach when doing so exceeds the approved route or risk rule.
3. Human operator classifies observation: benign, needs review, security incident, safety hazard, or robot fault.
4. Create the corresponding security incident or robotics support case with correlation ID.
5. Preserve approved evidence and communications; follow privacy/chain-of-custody policy.
6. Dispatch human security or field support according to authority and severity.

## Degraded modes

- Network loss: execute the approved safe-state or return behavior; local safety remains active.
- Sensor degradation: flag reduced capability and suspend missions that depend on the sensor.
- Low battery/dock unavailable: end route and move to approved safe location; activate coverage plan.
- Localization uncertainty: stop within safe boundary; remote recovery only under approved conditions.
- Weather outside operating envelope: do not launch or recall the robot.

## Shift handoff

Fleet state, locations, batteries, routes completed/missed, alerts, active security incidents, robot support cases, known degraded capabilities, field dispatches, changes, and next shift constraints.
