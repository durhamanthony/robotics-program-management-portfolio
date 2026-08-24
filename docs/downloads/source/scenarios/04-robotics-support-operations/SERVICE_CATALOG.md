# Robotics Service Catalog

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Customer-facing services

**Table 1. Customer-facing services — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Service | Scope | Request path | Target/entitlement |
|---|---|---|---|
| Safety/critical incident intake | 24×7 receipt, incident command, technical/customer coordination | Emergency support channel | Contract and `SEVERITY_SLA.md` |
| Technical support | Workflow, configuration, connectivity, robot faults, evidence-led diagnosis | Portal/Application Programming Interface/phone by entitlement | Coverage tier |
| Remote diagnostics | Approved MCAP robotics-log replay and controlled diagnostic session | Linked support case | Authorization and audit required |
| Field service | Onsite inspection, Field-Replaceable Unit replacement, calibration, return-to-service | Work order from case | Geography/parts/skill dependent |
| Parts and Return Material Authorization | Spare shipment, failed-part return, depot repair/disposition | Linked case/work order/Return Material Authorization | Warranty/contract |
| Software/update support | Release notice, staged deployment, rollback and defect linkage | Change/release process | Approved maintenance window |
| Training/knowledge | Role onboarding, recertification, job aids, advisories | Learning/knowledge portal | Product/contract |
| Service review | Key Performance Indicators, incidents, risks, reliability, actions, roadmap | Monthly/Quarterly Business Review | Named customer governance |

## Internal enabling services

Fleet health monitoring; alert engineering; installed-base/configuration management; problem/known-error management; product-release readiness; field capacity/parts planning; reliability feedback; incident exercises; tooling/data governance.

Each catalog item needs owner, hours, eligibility, intake, exclusions, inputs, fulfillment flow, target, dependencies, escalation, measurement, and cost-to-serve. Safety controls and emergency services remain independent of commercial support availability.
