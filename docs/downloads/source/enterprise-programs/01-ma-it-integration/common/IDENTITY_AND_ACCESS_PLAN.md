# M&A Identity and Access Integration Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Establish a controlled identity bridge, converge accounts and entitlements, and remove temporary access after acceptance.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Identity source | Company ABC HR/IAM becomes authoritative after approved roster cut | HR + IAM | Joiner/mover/leaver reconciliation |
| Coexistence | Cross-tenant or federation bridge limited to approved groups for 90 days | IAM Architect | Access package + expiry |
| Authentication | MFA and device-compliance controls; break-glass accounts excluded and monitored | Security | Policy test and logs |
| Privileges | Named admin accounts, just-in-time elevation, no shared credentials | Security + system owner | Privileged access review |
| Deprovisioning | Source access removed only after destination validation and legal approval | IAM Operations | Disablement evidence |

## Execution sequence

1. Inventory directories, domains, identity providers, account types, groups, roles, service principals, keys, and emergency accounts.
2. Normalize unique identity keys; resolve duplicate email addresses and contractor ownership before migration.
3. Map personas to least-privilege role bundles and separate birthright, requestable, privileged, and service access.
4. Pilot with 25 non-privileged and five privileged personas; review logs, token lifetime, conditional access, and recovery.
5. Stage identities before application/data cutovers; reconcile entitlements after each wave.
6. Disable the bridge and orphaned accounts only after business owner, IAM, and Security acceptance.

## Acceptance evidence

- [ ] 680 roster records reconcile to a unique destination identity or an approved exception.
- [ ] 100% of privileged roles have named owners, approval, MFA, logging, and expiry where applicable.
- [ ] No orphaned service principal, unmanaged shared account, or unresolved duplicate identity remains at closure.
- [ ] Access-review evidence shows source, destination, exception, and approver for each critical entitlement.

## Exception, rollback, and escalation

If authentication failure exceeds 2% in a wave, privileged-role mapping differs from approval, or logging is incomplete, stop the wave. Re-enable the approved source route for that cohort, preserve logs, and correct mapping before retry. Security incidents use the enterprise incident process, not the project issue log alone.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `authoritative sources`
- `unique identity key`
- `domain strategy`
- `persona bundles`
- `MFA / conditional access`
- `privileged access`
- `service identities`
- `coexistence expiry`
- `reconciliation queries`
- `decommission approval`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
