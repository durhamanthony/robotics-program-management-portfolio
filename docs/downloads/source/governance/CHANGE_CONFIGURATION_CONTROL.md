# Change and Configuration Control

## Controlled items

- Contract scope, SOW deliverables, assumptions, exclusions, and acceptance criteria.
- Integrated schedule, committed launch date, budget, contingency, and resource plan.
- Robot hardware revision, firmware/software release, model/configuration, end effector, and safety settings.
- Site layout, network, charging, zones, integrations, data mappings, and operational procedures.
- Training, support, spares, warranty, remote access, rollback, and escalation design.

## Change workflow

1. Log the request with originator, reason, desired date, and affected baseline.
2. Triage for safety, security, contractual, customer, and schedule urgency.
3. Assess scope, benefit, cost, schedule, quality, resource, risk, test, training, support, and warranty impacts.
4. Identify options, including no change, phased change, or workaround.
5. Obtain decision at the correct authority level.
6. Update baselines, configuration records, requirements, tests, runbooks, training, and communications.
7. Verify implementation and close with evidence.

## Emergency change

Emergency changes are limited to restoring safe service or containing a critical incident. They still require documented authorization, backup/rollback, implementation evidence, customer communication, and retrospective review within one business day.

## Configuration record minimum fields

Configuration ID; robot serial/asset ID; hardware revision; firmware/software versions; safety configuration; maps/models/calibration; network/site configuration; installed options; release date; approver; linked test evidence; rollback version.

## Decision authority

| Impact | Authority |
|---|---|
| Within workstream tolerance; no baseline effect | Workstream lead |
| Cross-workstream or <=5% contingency | Program manager/change board |
| Safety, acceptance, contract, launch date, or >5% contingency | Sponsor/customer steering committee |
