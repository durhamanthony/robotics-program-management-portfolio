# Business Continuity — Robotics Support

## Critical service dependencies

Customer intake, identity/access, case/work order, robot/fleet telemetry, communications, engineering escalation, on-call paging, parts logistics, field dispatch, cloud/network, knowledge and customer/site contacts.

## Continuity playbooks

| Disruption | Minimum service mode |
|---|---|
| Case platform outage | Controlled offline intake/timeline; emergency contacts; later reconciliation |
| Fleet/telemetry outage | Treat unknown state conservatively; customer/local verification; no unsupported remote action |
| Remote-access outage | Local safe operations and field dispatch according to severity/entitlement |
| Cloud/network regional event | Failover if designed; controlled site behavior; customer cadence |
| Supplier/part shortage | Allocate by safety/impact/contract; approved alternatives; repair/loaner plan |
| Workforce/site disruption | Cross-region on-call, partner coverage, skills matrix, welfare limits |
| Cyber incident | Security incident plan, isolate/revoke, preserve evidence, approved recovery |

## Program controls

Define RTO/RPO by service and evidence type; backup/restore and contact trees; alternative communications; critical spares; vendor SLAs; manual procedures; quarterly tabletop and periodic technical restore/dispatch tests. Record gaps as owned corrective actions and retest.
