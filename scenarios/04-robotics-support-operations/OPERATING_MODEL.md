# Robotics Support Operating Model

## Organization

| Function | Mission | Example roles |
|---|---|---|
| Level 1 (L1) customer support | Intake, entitlement, safe initial response, communication, evidence | Support agents/leads |
| Level 2 (L2) robotics support / remote operations | Logs, replay, configuration, calibration guidance, controlled intervention | Robotics support engineers |
| Field service | Onsite inspection, FRU replacement, calibration, validation | Field technicians/engineers, dispatch |
| Level 3 (L3) engineering | Product root cause and fix | Hardware, firmware, software, Artificial Intelligence/perception, systems |
| Service program/product operations | Process, tools, readiness, Key Performance Indicators (KPIs), customer governance | Service operations manager, program manager, analyst |
| Reliability/problem | Trends, Root Cause Analysis (RCA), corrective/preventive action | Reliability/problem engineers |
| Parts/Return Material Authorization (RMA)/depot | Availability, logistics, repair, disposition | Supply/service logistics |

## System-of-record rules

- Salesforce owns customer/account/site, installed product, contract, and entitlement.
- ServiceNow Customer Service Management/Field Service Management (CSM/FSM) or Zendesk owns customer case and communication. ServiceNow FSM or the selected field module owns work orders/dispatch/parts activity.
- Jira owns engineering defect/change/release work, not the customer conversation.
- The robot platform, Foxglove, and MCAP robotics log format own high-fidelity diagnostic evidence.
- Grafana owns service/infrastructure visualization and alert views; it does not replace case history.
- Every linked object carries the same correlation identifier and robot serial.

## Handoff contract

### Level 1 to Level 2 requires

Robot/site/version, safety state, impact/severity, timestamps/time zone, mission, fault code, recent change, reproduction, logs/MCAP window, photos/video only if safe/approved, steps already tried, customer contact, and correlation ID.

### Level 2 to field requires

Remote diagnosis, suspected Field-Replaceable Unit (FRU), required skill/tool/part, access/site safety instructions, customer window, return-to-service test, and escalation contact.

### Level 2/field to Level 3 requires

Minimal reproduction, affected versions/configurations, expected versus actual, evidence, frequency, impact, workaround, suspected subsystem, hardware-return availability, and linked case/work order/Return Material Authorization.

## Governance

Daily severity/launch review; weekly KPI and aging review; weekly case-defect-release review; monthly reliability/problem council; monthly workforce/parts forecast; customer Quarterly Business Review (QBR); release and deployment support-readiness gate.
