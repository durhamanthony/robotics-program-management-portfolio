# AD-01 Product Brief and Product Requirements Document

## Product boundary

AD-01 transfers one approved tote family, up to 15 kilograms, between two fixed indoor workstations over an 18-meter marked route. The first release operates on level industrial floors for 16 scheduled hours per day. A trained human owns replenishment, exception recovery, emergency response, and return-to-service approval.

Public access, people transport, stairs, outdoor operation, hazardous material, arbitrary objects, unstructured bin picking, unsupervised site expansion, and operation outside the validated layout are excluded.

## Customer workflow

1. The operator stages an approved tote and requests a mission.
2. AD-01 verifies robot, route, tote, station, battery, and release readiness.
3. The robot travels to the source, stops at the controlled transfer pose, grasps the tote, and confirms lift.
4. The robot carries the tote on the approved route, stops at the destination pose, releases it, and records the outcome.
5. An unsupported condition creates a safe pause and a human-readable exception; the robot never silently substitutes a new route or payload.

## Top-level requirements

Gate abbreviations used below are Design Verification Test (DVT) and Production Validation Test (PVT).

| ID | Requirement | Acceptance target | Verification |
|---|---|---:|---|
| PERF-001 | Supported tote | One baselined geometry, 2–15 kilograms | Geometry inspection and load test |
| PERF-010 | Mission success | At least 98% over 2,000 DVT representative cycles and the 30-day customer mix | Operational test |
| PERF-020 | Sustained rate | At least 40 completed transfers per hour over a 2-hour run | Timed test |
| PERF-030 | Route | Complete the 18-meter source-to-destination route without entering exclusion zones | Route test |
| SAFE-001 | Protective functions | All mandatory hazard-control and stop tests pass | Qualified validation |
| SAFE-010 | Localization or network loss | Enter the approved safe state within 1 second and remain stopped until authorized recovery | Fault injection |
| REL-001 | Scheduled availability | At least 95% during the first-customer 30-day acceptance window | Operations data |
| REL-010 | Human intervention | No more than 3 interventions per 100 missions after tuning | Operations data |
| SERV-001 | Field-Replaceable Unit (FRU) | Replace the battery, compute, or gripper module and pass return-to-service in 60 minutes or less | Service demonstration |
| DATA-001 | Traceable evidence | Every mission record includes robot serial, software version, mission, event time, fault, and correlation identifier | Inspection and test |
| SEC-001 | Device and update security | Unique identity, least privilege, signed update, audit, and rollback tests pass | Security test |
| MFG-001 | Production process | At least 90% first-pass yield and no more than 40 final assembly/test labor hours across the 10-unit PVT build | Production Validation Test |
| COST-001 | Cost of Goods Sold (COGS) | At or below $165,000 at DVT forecast and $150,000 at PVT actual/committed cost | Finance and Bill of Materials review |
| OPS-001 | Training and support | All designated users pass role assessment and the Severity-1 support drill is acknowledged within 5 minutes | Assessment and drill |

## Required exception stories

Payload missing or out of range; blocked path; person enters controlled zone; grasp failure; dropped payload; low battery; charger unavailable; localization/perception uncertainty; network loss; software mismatch; actuator/sensor health alert; emergency stop; manual recovery; failed update; and field intervention.

## Release controls

Targets become controlled product requirements only after product, engineering, safety, operations, manufacturing, service, finance, and the design customer approve the baseline. Changes must update the requirement, hazard analysis, interface, verification, manufacturing test, service material, schedule, cost, and contract impact together.
