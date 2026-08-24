# Robotics Support Reference Architecture

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Support tiers

**Table 1. Support tiers — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Tier | Owner | Typical scope | Exit condition |
|---|---|---|---|
| L0 | Customer self-service/automation | Status, safe restart criteria, known issues, maintenance reminders | Resolved or case created with evidence |
| L1 | Frontline support | Entitlement, triage, common workflow, evidence collection, communication | Resolved or reproducible escalation package |
| L2 | Robotics support engineer / remote operations | Logs, MCAP replay, configuration, calibration, network, controlled remote intervention | Resolved, field work ordered, or L3 defect |
| Field | Field service technician/engineer | Inspection, replacement, calibration, validation, parts/RMA | Robot passes return-to-service test |
| L3 | Hardware/firmware/software engineering | Reproducible product defect, root cause, code/design fix | Fixed release/ECO and known-error update |

## Case-to-resolution workflow

1. Detect customer report or telemetry alert.
2. Confirm safety state; stop or isolate the robot when required.
3. Validate account, installed asset, entitlement, site, robot ID, and current version.
4. Collect the minimum evidence bundle: timestamps, MCAP/log window, photos/video if safe, fault codes, environment, recent changes, and reproduction steps.
5. Classify severity and route to L1/L2/field/L3.
6. Maintain a customer communication clock independent of engineering activity.
7. Validate recovery against a return-to-service checklist.
8. Link case, work order, RMA, problem, Jira defect, and release through one correlation ID.
9. Publish or update knowledge and review recurring trends.

## Safety boundary

Support tooling is not the safety system. Remote commands must respect manufacturer controls, site safety procedures, authorization, and a positive confirmation that the work area is clear. E-stops, protective stops, energy isolation, and functional-safety controls must remain independent of dashboards and customer-service platforms.
