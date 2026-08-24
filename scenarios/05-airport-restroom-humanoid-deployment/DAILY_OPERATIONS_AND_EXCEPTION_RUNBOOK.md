# Daily Operations and Exception Runbook

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Start-of-shift release

1. Airport custodian checks room assignment, public-service window, warning signs, barrier, occupancy status, and manual fallback.
2. Operator verifies robot serial, approved configuration, battery, tool, chemical identity, supply levels, telemetry, charger, and support contact.
3. Custodian inspects for sharps, visible blood, vomit, unknown chemical, standing water, smoke, obstruction, damage, or occupied stall. Any prohibited condition blocks dispatch.
4. Airport Duty Manager authorizes the service window; the room is closed and verified empty.
5. Operator dispatches one room mission. Parallel operation requires separate closure and supervision capacity.

## Routine mission

- Establish the top overview and verify the mapped room.
- Service toilet 1, toilet 2, and urinal with the approved tool sequence.
- Clean the open floor using the approved path.
- Wipe sinks and mirrors with the approved surface process.
- Service the entry route, supplies, and waste within the approved scope.
- Return to charge and create a mission record.
- Custodian performs the twelve-point inspection and either reopens or assigns corrective work.

## Stop conditions

**Table 1. Stop conditions — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Condition | Robot action | Human action | Reopen authority |
|---|---|---|---|
| Person enters or occupancy uncertain | Protective stop | Clear room and investigate entry control | Airport Duty Manager |
| Sharps, blood, vomit, or prohibited contamination | Stop without contact and flag location | Trained specialist follows airport exposure-control procedure | Custodial Supervisor |
| Chemical mismatch or leak | Stop, isolate dispenser, retain record | Follow Safety Data Sheet and airport spill procedure | Airport Safety |
| Standing water or plumbing fault | Stop outside affected zone | Isolate fixture and dispatch Facilities | Facilities Supervisor |
| Network loss | Local safe state | Restore network or manually recover | Seller Support plus Airport Cybersecurity |
| Collision/contact or damaged fixture | Emergency stop | Protect area, inspect person/robot/fixture, open incident | Airport Safety |
| Low energy or thermal limit | Return to dock or safe stop | Inspect telemetry and recover per manufacturer procedure | Robot Operator |
| Inspection failure | Remain closed | Corrective human cleaning and defect classification | Custodian |

## Severity and communication

- Severity 1: injury, uncontrolled entry, chemical release, collision, privacy event, or both robots unavailable. Notify Airport Duty Manager and Safety immediately; seller acknowledgement target 15 minutes.
- Severity 2: one robot unavailable, repeated quality failure, charger failure, or room blocked. Notify custodial supervisor and seller; acknowledgement target 30 minutes.
- Severity 3: non-blocking defect or documentation issue. Record before shift end; review in daily triage.

## End-of-shift

Reconcile scheduled versus completed missions, inspections, exceptions, supplies, chemical use, battery, faults, interventions, public complaints, support cases, and room downtime. The Airport Project Manager reviews daily during commissioning and weekly during steady pilot operation.
