# Privacy, Safety, and Acceptance

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Human authority

The robot produces observations and alerts. A trained human verifies alerts and decides whether to dispatch, notify, or escalate. The system must show uncertainty and health status; an unavailable or degraded sensor cannot silently imply “all clear.”

## Data controls

Purpose limitation; approved camera/thermal zones; restricted-area masks; least-privilege access; encryption; audit log; retention and deletion; export/evidence approval; incident hold; third-party/cloud terms; signage and workforce notice; privacy escalation; periodic review.

## Acceptance tests

**Table 1. Acceptance tests — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| ID | Test | Expected result |
|---|---|---|
| Q-SAT-001 | Approved route and geofence | Robot remains within boundary and stops before exclusion zone |
| Q-SAT-010 | Stair/drop-off/obstacle | Detects or safely stops; operator receives usable alert |
| Q-SAT-020 | Low-light/thermal observation | All 20 staged observation tests are detected and presented with robot, time, route segment, confidence, and sensor-health status |
| Q-SAT-030 | Network degradation/loss | Defined degraded mode and safe stop/return; no unsafe remote behavior |
| Q-SAT-040 | Low battery/dock | Safe return and verified charge; alternate coverage starts |
| Q-SAT-050 | Localization uncertainty | Robot stops or executes approved recovery within boundary |
| Q-SAT-060 | Camera/thermal degradation | Health alert identifies reduced capability; mission rule applied |
| Q-SAT-070 | Critical security observation | All 50 witnessed alerts arrive at the Security Operations Center within 15 seconds and a human records verification and disposition |
| Q-SAT-080 | Privacy mask/retention | Restricted area excluded and deletion/audit verified |
| Q-SAT-090 | Remote access | Multi-Factor Authentication (MFA), authorization, audit, and session expiry validated |
| Q-SAT-100 | Field retrieval/return to service | Safe retrieval and post-repair checklist pass |

## Go/no-go blockers

Geofence failure; uncontrolled motion; unresolved critical privacy/security issue; missing human supervision; route completion below 98%; any witnessed critical alert over 15 seconds or lost; more than six operator-reviewed false alerts per night after tuning; missing safe retrieval; or unavailable support/on-call coverage.
