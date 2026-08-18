# Deployment and Cutover Runbook

## Site readiness gate

- Approved layout, controlled zone, pedestrian/forklift separation, egress, signage, lighting, floor condition, dock/trailer assumptions, and recovery access.
- Power/charging, network coverage/segmentation, identity/certificates, time synchronization, telemetry destination, data retention, and remote-access approval.
- Conveyor/WMS test endpoint and fallback workflow.
- Safe staging/storage for robots, tools, batteries/charging equipment, and spares.
- Customer safety, operations, IT, security, facilities, and labor representatives approve readiness.

## Installation sequence

1. Confirm shipment, serials, damage inspection, and configuration baseline.
2. Establish controlled work area and daily safety briefing.
3. Position chargers and infrastructure; validate utilities and network.
4. Power on one robot; verify firmware, identity, certificates, calibration, and E-stop/protective-stop paths with qualified personnel.
5. Validate telemetry, logs, alerts, support case creation, and evidence correlation.
6. Run dry missions without cartons, then representative cartons, exceptions, and recovery.
7. Repeat standardized commissioning for robots 2–5.
8. Run fleet concurrency, conveyor/WMS loss, network loss, low-battery, sensor fault, safe recovery, and shift-handoff scenarios.
9. Complete SAT, safety validation, operator/support assessment, soak, and customer acceptance.

## Production cutover

| Sequence | Action | Owner | Validation | Rollback/stop trigger |
|---:|---|---|---|---|
| 1 | Freeze approved configuration | Release lead | Hash/version register | Unapproved variance |
| 2 | Confirm staffing, contacts, spares, bridge | Program manager | Readiness roll call | Missing critical role |
| 3 | Start one lane/one robot | Customer ops | 30-minute stable run | Safety event or acceptance breach |
| 4 | Add robots sequentially | Fleet lead | KPI check after each | Repeated intervention or congestion |
| 5 | Begin production observation | Joint team | Dashboard and manual tally agree | Telemetry gap or unknown failure |
| 6 | Approve shift expansion | Go/no-go board | Defined soak targets met | Open severity 1/2 issue |

## Hypercare

Two weeks; onsite day-shift lead plus 24/7 remote severity-1 coverage. Daily review of availability, mission success, interventions, carton exceptions, safety observations, incidents, parts, software changes, and customer feedback. Exit requires five consecutive days above thresholds, no open severity-1 issue, stable support routing, trained ownership, and accepted known-error/workaround list.

