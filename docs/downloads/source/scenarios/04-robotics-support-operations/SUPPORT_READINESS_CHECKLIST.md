# Support Readiness Gate

## Product and evidence

- [ ] Serial/configuration/version/installed-base data model defined.
- [ ] Fault taxonomy, severity mapping, event dictionary, and owner documented.
- [ ] Required telemetry/logs/MCAP window and time synchronization validated.
- [ ] Remote diagnostics, authorization, audit, and break-glass process tested.
- [ ] Known limitations, safe states, recovery, maintenance, and LOTO procedures approved.

## People and process

- [ ] L1/L2/field/L3 RACI and contact tree tested.
- [ ] Coverage, on-call, territories, dispatch, and language/time-zone plan staffed.
- [ ] Role training and competency assessment complete.
- [ ] Customer communication, incident command, and safety/security escalation drilled.
- [ ] Knowledge author/reviewer/expiry ownership assigned.

## Systems

- [ ] CRM installed product/entitlement links to case and work order.
- [ ] Case creates/links Jira defect with correlation ID.
- [ ] Fleet/Foxglove/Grafana dashboards and alerts are accessible to the right roles.
- [ ] OTA release ring, rollback, change, and maintenance window tested.
- [ ] Reporting captures SLA, availability, mission success, intervention, first-time fix, recurrence, parts, and cost.

## Field/parts/RMA

- [ ] FRU list, skill/tool matrix, maintenance intervals, and service time objectives defined.
- [ ] Site/depot spares, min/max, replenishment, serialized inventory, and hazardous shipping requirements ready.
- [ ] RMA authorization, packaging, chain of custody, depot diagnosis, warranty disposition, and failure analysis tested.
- [ ] Return-to-service acceptance checklist approved.

## Gate rule

No release/deployment when a credible safety escalation has no staffed path, a core fault cannot produce evidence, a critical FRU has no recovery plan, or support cannot identify the customer/robot/configuration/entitlement.

