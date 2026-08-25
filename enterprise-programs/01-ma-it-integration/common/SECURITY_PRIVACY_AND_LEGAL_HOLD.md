# M&A Security, Privacy, and Legal-Hold Control Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Embed risk governance, evidence, and stop conditions across discovery, coexistence, migration, and decommissioning.

## NIST CSF 2.0 control map

| Function | M&A application | Required evidence |
| --- | --- | --- |
| Govern | Risk appetite, decision rights, due diligence, vendor clauses, privacy/hold authority | Approved risk and control owners |
| Identify | Assets, identities, data, apps, networks, third parties, vulnerabilities, dependencies | Reconciled inventory and classification |
| Protect | MFA, least privilege, compliant devices, segmentation, encryption, backups, change control | Policy/config/test evidence |
| Detect | Cross-tenant authentication, privileged events, data transfer, VPN/firewall, endpoint and SaaS logs | Alert and log ingestion tests |
| Respond | Security bridge, severity, evidence preservation, regulatory/legal decision path | Incident runbook and contacts |
| Recover | Rollback, restore, service priorities, communications, lessons | Tested recovery and restoration evidence |

## Mandatory gates

- No production interconnect before asset/flow inventory, segmentation, logging, vulnerability review, collision remediation, and Security approval.
- No data movement before data classification, legal hold/retention, destination access, encryption, processor/vendor, and validation requirements are approved.
- No privileged migration account without named ownership, least privilege, MFA, logging, key/secret custody, and expiry.
- No source deletion or tenant decommission before business, records/legal, Security, and service-owner acceptance.

## Privacy by design

Use the minimum data required for discovery and testing; mask samples where feasible; record jurisdiction/residency and controller/processor responsibilities; restrict clean-team access; retain migration logs according to approved policy; and delete temporary working copies only through an approved evidence-backed process.

## Risk acceptance

The project manager documents and escalates risk; only the designated business/security authority may accept it. Acceptance includes scope, rationale, compensating controls, owner, expiry, review date, and residual rating.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `security framework/profile`
- `asset and data classifications`
- `control owners`
- `identity/privilege`
- `network segmentation`
- `logging/monitoring`
- `vulnerability and third-party risk`
- `privacy/retention/legal hold`
- `incident and recovery`
- `exceptions and risk acceptance`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
