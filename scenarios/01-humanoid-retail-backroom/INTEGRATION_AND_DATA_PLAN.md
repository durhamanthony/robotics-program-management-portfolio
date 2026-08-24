# Integration and Data Plan — Retail Backroom Pilot

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Transaction flow

Inbound: receiving schedule → truck/pallet identifier → forklift mission → pallet-stable confirmation → forklift parked/zone-clear signal → humanoid stocking missions → rack-location scans → inventory/event update.

Fulfillment: associate tablet → identity service → request service → inventory-location lookup → mission orchestrator → robot/fleet service → pick scan → courtesy drop-off scan → inventory/event update → telemetry and support case when required.

## Interface controls

**Table 1. Interface controls — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Interface | Request/response | Timeout/retry | Failure behavior | Evidence |
|---|---|---|---|---|
| Dock/pallet receipt | truck, dock, pallet, arrival, stability | one active unload mission; no silent retry | hold forklift and humanoids; notify dock lead | 20 normal/fault unload cases |
| Zone interlock | forklift parked and receiving zone clear → release stocking | positive confirmation required | keep humanoid missions inhibited | 20 witnessed clear/release cycles |
| Tablet/identity | user, store, role, item, drop-off point | 5 seconds; one retry | no anonymous mission; show explicit error | authentication and revocation tests |
| Inventory service | SKU, size, color → bin/rail location | 3 seconds; two retries | no movement without valid location; human search queue | 20 normal/error cases |
| Mission service | validated request → route/item mission | idempotency key; no duplicate mission | safe hold and operator alert | duplicate/replay test |
| Stock/pick/drop-off scan | pallet, item, rack, pick, and courtesy-table confirmation | scan at each custody change | reject mismatch; return to exception point | transaction reconciliation |
| Telemetry/support | robot, mission, event, fault, configuration | buffer during outage; ordered resend | local safe state; correlated case | network-loss and case drill |

## Data ownership and retention

Meridian owns requests, inventory, employee identity, and business measures. The vendor owns robot diagnostic data subject to contract. Video is limited to navigation/manipulation evidence in employee-only zones; no facial recognition. Operational clips retain 7 days unless attached to an incident; incident evidence retains 90 days or the legal schedule. Access is role-based, logged, reviewed monthly, and revoked at role termination.

## Data-quality rules

- Truck, pallet, carton, rack, SKU, size, color, request, mission, and courtesy-drop-off identifiers must reconcile one-to-one.
- Times use synchronized Universal Time Coordinated (UTC) plus displayed local time.
- Missing or low-confidence location data blocks autonomous retrieval.
- Dashboard measures are produced from versioned queries; the animation never supplies KPI data.
- Pilot raw data, calculation workbook, and approved result snapshot are retained with closeout evidence.

## Cutover and rollback

Run interfaces in shadow mode for 100 requests. If wrong-item rate exceeds 0.5%, duplicate missions occur, security logs fail, or safe-state evidence is missing, disable robot mission creation, retain the tablet as a human pick queue, reconcile open transactions, and restore only after change approval and regression testing.
