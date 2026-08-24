# Robotics Program Management Plan

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Purpose

Provide one operating framework for moving a robotics initiative from approved need through safe, supportable operations. The plan applies to customer deployments, product/NPI programs, and service-operations implementations.

## Lifecycle and required gates

**Table 1. Lifecycle and required gates — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Phase | Required decision | Minimum evidence |
|---|---|---|
| Discover | Is the problem and operating context understood? | Use case, users, current-state data, constraints, initial risks |
| Commit | Should funding and capacity be authorized? | Business case, charter, SOW, success measures, sponsor approval |
| Design | Is the solution and operating model viable? | Requirements baseline, architecture, site design, hazard analysis, support concept |
| Build/configure | Is the product/configuration ready to test? | Integrated plan, configuration baseline, supplier readiness, test procedures |
| Verify | Does it meet specifications? | FAT/EVT/DVT evidence, defect disposition, traceability |
| Validate | Does it work safely in the customer workflow? | SAT/UAT, safety validation, training results, operational acceptance |
| Launch | Is controlled production authorized? | Cutover plan, rollback, on-call, spares, communications, signed go/no-go |
| Stabilize | Is performance stable enough to hand over? | Hypercare trends, incident review, SLA/KPI evidence, open-risk acceptance |
| Close/scale | Were outcomes achieved and is expansion justified? | Handoff, closeout, benefits review, lessons, roadmap decision |

## Integrated workstreams

1. Program governance and customer/stakeholder management.
2. Product, hardware, software, firmware, autonomy, and configuration.
3. Site, facilities, power, charging, network, and material flow.
4. Safety, human factors, regulatory, privacy, and cybersecurity.
5. Integration, data, telemetry, observability, and systems of record.
6. Supply chain, logistics, installation, spares, warranty, and RMA.
7. Test, quality, commissioning, acceptance, and configuration control.
8. Training, organizational change, support readiness, and handoff.
9. Financial management, vendors, contracts, and benefits realization.

## Governance bodies

- **Executive steering committee:** monthly and at major gates; owns funding, scope boundary, critical risk acceptance, and expansion decisions.
- **Program leadership team:** weekly; resolves cross-workstream dependencies and approves changes within delegated tolerances.
- **Technical/safety review:** weekly during design and test; owns evidence quality, defect disposition, and safety blockers.
- **Site readiness review:** weekly beginning eight weeks before delivery; owns facilities, access, training, and local operations readiness.
- **Daily launch stand-up:** during installation, cutover, and hypercare; owns safety, incidents, blockers, and the next 24-hour plan.

## Baselines and tolerances

- Scope, acceptance criteria, safety controls, contract deliverables, production configuration, and cutover dates are controlled baselines.
- Workstream leads may manage tasks within approved scope and budget.
- Any change affecting a safety control, customer acceptance, committed milestone, warranty, data handling, or more than 5% of approved contingency requires formal review.
- Red status, safety events, Sev-1 incidents, and forecast breaches beyond tolerance are escalated immediately rather than waiting for the next meeting.

## Systems of record

- Jira: delivery backlog, engineering work, defects, and dependencies.
- ServiceNow or Zendesk: incidents, problems, requests, changes, and knowledge.
- Salesforce: customer, contract, entitlement, installed-base, and commercial status.
- GitHub: versioned portfolio code, simulation, and sanitized public documentation.
- Approved document repository: signed contracts, safety evidence, acceptance records, and restricted customer data.

## PM operating rhythm

The program manager maintains the integrated milestone plan, RAID, actions, decisions, changes, financial forecast, resource outlook, and acceptance evidence index. Weekly status must explain what changed, what decision is needed, who owns the next action, and how the forecast compares with the approved baseline.
