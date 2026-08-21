# Cybersecurity, Privacy, and Data Plan

## Purpose limitation

Sensors support navigation, safety, fixture service, exception detection, and evidence inside a closed restroom. The pilot prohibits facial recognition, identity inference, passenger analytics, marketing, law-enforcement use, and operation while the room is occupied.

## Control design

| Control area | Required control | Acceptance evidence |
|---|---|---|
| Identity | Unique robot, service, operator, and support identities; multi-factor authentication for people | Account and authentication test |
| Network | Segmented robot network, only approved destinations and ports | Architecture and rule review |
| Privilege | Operator, support, administrator, auditor, and airport roles separated | Role test and access review |
| Remote support | Airport-approved window, ticket, named person, recorded commands, session timeout | Witnessed support drill |
| Data minimization | Event metadata by default; image capture only for defined fault evidence | Data-flow review |
| Privacy | Closed-room operation, occupancy inhibit, privacy masking, no audio unless separately approved | Eighteen privacy and deletion tests |
| Retention | Routine telemetry 90 days; fault evidence 30 days unless attached to an active investigation; access logs one year | Automated deletion and legal-hold tests |
| Software | Signed release, configuration inventory, rollback, vulnerability intake | Release and rollback drill |
| Incident response | Robot safe state, credential revocation, evidence preservation, airport cyber escalation | Tabletop and technical exercise |

## Data ownership

The airport owns operational and inspection records. Manufacturer access is limited to approved diagnostic data for a ticket or reliability review. The seller cannot reuse airport data to train a model or build a commercial dataset without a separate written agreement.

## Exit

At pilot termination, the seller returns airport data, provides the retained-data inventory, deletes unneeded copies, removes credentials, and certifies remote-access closure. The airport preserves only records required by policy, contract, incident, or legal hold.

