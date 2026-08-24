# Deployment Runbook — Retail Backroom Humanoid Pilot

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Preconditions

Approved configuration and route; signed readiness checklist; change freeze; trained onsite authority; rollback owner; inventory test tenant; segmented network; chargers; emergency equipment; representative item/exception set; Factory Acceptance Test (FAT) exit; defect list with no open critical item.

## Installation and commissioning

1. Confirm serial numbers, software, checksums, certificates, warranties, spares, and shipping condition.
2. Verify truck position, ramp/threshold, pallet staging, forklift park, zone interlock, route, four-step stair, doors, fire egress, courtesy drop-off table, charger, exception zone, and stock-cart parking against the signed drawing.
3. Connect each robot with least-privilege identity; validate access logging and revocation.
4. Load the approved map, speed, stop, item, reach, charging, retention, and safe-state configuration.
5. Test receiving schedule, pallet identification, forklift mission, pallet-stable state, parked/zone-clear signal, stocking scan, tablet, inventory lookup, pick, courtesy drop-off, event, and case correlation.
6. Run full-pallet unload and clear-zone cycles, lower/raised stocking, empty routes, approved items, human/cart intrusions, blocked route, wrong location, network loss, low battery, sensor fault, and emergency stop.
7. Execute Site Acceptance Test (SAT); record witness, configuration, timestamp, result, and defect for each case.
8. Complete 100-request User Acceptance Testing (UAT) in shadow mode before pilot authorization.

## Cutover checklist

- Store Sponsor and Safety Lead sign go/no-go.
- Human fallback is staffed and tablet can route requests to people.
- All shifts know pause, emergency stop, exception, and escalation procedures.
- Monitoring, service desk, Level 2 (L2), field on-call, and spare kits are live.
- Baseline queries and daily KPI report are frozen and versioned.

## Stop and rollback triggers

Any contact/injury; forklift/humanoid overlap; unstable pallet; safety-control bypass; robot outside route; fire-egress interference; repeated uncontrolled drop; security compromise; wrong-item rate above 0.5%; mission success below 97% for two days; or unavailable human fallback. Stop missions, establish safe state, notify authority, preserve evidence, reconcile transactions, and route receiving/picking to the human fallback. Restore only after root-cause, approved change, regression test, and signed restart.

## Hypercare

Thirty days: onsite opening/closing owner, daily issue/KPI huddle, weekly sponsor/Finance review, and 24/7 Severity-1 remote coverage. Exit requires five consecutive days above operational thresholds, trained ownership, tested support, accepted known errors, reconciled benefit data, and recorded financial decision.
