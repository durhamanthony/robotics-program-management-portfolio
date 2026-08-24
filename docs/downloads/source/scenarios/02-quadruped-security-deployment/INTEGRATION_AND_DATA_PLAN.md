# Integration and Data Plan — Night Security

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Workflow

Schedule/dispatcher → fleet mission → quadruped route → observation/health event → human operator verification → security case/dispatch if warranted → retained evidence and audit.

## Interface controls

**Table 1. Interface controls — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Interface | Required data | Failure response |
|---|---|---|
| Mission/fleet | Robot, route, geofence version, schedule, battery, mission state | Do not start or execute approved safe-return/hold behavior |
| SOC/alert | Alert type, confidence/context, robot/location, time, media reference | Retry/alternate channel; create visible delivery failure |
| Evidence system | Case/correlation ID, immutable timestamp, approved media/log excerpt, access audit | Preserve local buffer; prohibit untracked copies |
| Identity/remote access | Named user/device, least privilege, MFA, approval, session log | Deny by default and escalate |
| Service tooling | Serial/version/health, fault, mission and MCAP/log window | Create linked case; redact according to policy |

## Data rules

Document collection purpose, cameras/sensors, location fields, retention, access groups, evidence holds, subject requests, redaction, cross-border/cloud location, deletion, and breach response. Disable collection outside approved zones where technically feasible. No facial recognition or secondary AI training is assumed.

## Testing

Test delayed/duplicate/missing alerts, time synchronization, coverage loss, exhausted storage, dock offline, geofence version mismatch, credential expiry, manual takeover authorization, evidence export, deletion, and full audit reconstruction.
