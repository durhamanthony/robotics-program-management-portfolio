# Safety, Quality, and Acceptance Plan

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Safety operating rule

The robot operates only in a closed, verified-empty restroom. A human controls reopening. The system is not approved to clean around passengers.

## Hazard controls

**Table 1. Hazard controls — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Hazard | Prevention | Detection | Response |
|---|---|---|---|
| Public entry | Barrier, sign, lock/attendant, occupancy check | Door and occupancy state | Immediate stop; human clears room |
| Sharps or body fluid | Pre-scan and prohibited-task rule | Vision cue or human report | Stop without contact; isolate; dispatch trained specialist |
| Cleaning chemical | Approved cartridge, label, Safety Data Sheet, locked recipe | Identity, level, leak, dwell timer | Stop; ventilate or contain per airport procedure; human response |
| Wet floor | Controlled application and drying step | Moisture check and inspection | Keep room closed; place warning; corrective dry |
| Pinch/collision | Speed/force limits, mapped fixtures, guarded tool | Contact/force and route monitor | Protective stop and inspection |
| Loss of network | Local safe behavior | Heartbeat | Stop, retain evidence, manual recovery |
| Battery or thermal limit | Mission-energy check and reserve | Battery/temperature telemetry | Return to dock or safe stop |
| Blocked egress | Marked dock/supply envelope | Daily clearance inspection | Remove obstruction before service |

## Cleaning quality audit

An authorized custodian scores twelve points: toilet/urinal exterior; seat and contact points; sink basin; faucet; counter; mirror; floor visible soil; floor moisture; waste removal; paper/soap supply; odor/visual condition; and evidence record. Any critical contamination, sharps, chemical, slip, or access issue fails the mission regardless of score.

## Test stages

- Engineering verification: manufacturer evidence for pilot configuration.
- Factory Acceptance Test: integrated robot, tool, charger, faults, telemetry, and test-room sequence before shipment.
- Site Acceptance Test: each airport room, entry control, network, route, fixture, chemical, recovery, and support path.
- Shadow mode: robot runs while a custodian controls each step; no autonomous reopening.
- User Acceptance Testing: airport custodians, safety, cybersecurity, and operations witness the defined workflows.
- Pilot acceptance: thresholds in the Requirements Traceability Matrix and signed closeout records.

## Acceptance authority

The airport accepts the pilot. The seller accepts contract completion. The manufacturer accepts or rejects the pilot product release. None can substitute for another party's decision.
