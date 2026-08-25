# Hardware Refresh Security, Compliance, and Sanitization Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Protect access and data on new and returned devices and maintain auditable custody through reuse or disposal.

## New-device controls

| Control | Release requirement | Evidence |
| --- | --- | --- |
| Identity/management | Approved join/enrollment; unique device and user assignment | Entra/Intune/SCCM/MDM record |
| Protection | Encryption, supported OS/update, EDR, firewall, screen lock, standard user | Compliance and security report |
| Access | Conditional access validated in report-only/pilot before enforcement as applicable | Policy result and exception |
| Data | Approved backup/sync complete; protected locations known | Migration checklist and user validation |
| Evidence | Asset, build, policy, owner, site, warranty, support identifiers reconciled | CMDB/inventory acceptance |

## Returned-device controls

NIST SP 800-88 Rev. 2 is used as program-level guidance: classify media/data, select an organization-approved sanitization method/standard, authorize tools/vendors, preserve custody, validate effectiveness, retain evidence, and manage reuse/disposal. The project does not prescribe a destructive technique without the organization’s security and records requirements.

## Chain of custody

Scan at user handoff, site secure storage, transport pickup, processing receipt, sanitization start/finish, validation, and final reuse/recycle/destruction. Record serial/asset/media identifiers, people/organizations, date/time/location, seal/container, method/tool/version, result, validation, exception, and certificate/reference.

## Stop conditions

Unknown identity/serial, missing legal-hold release, encryption/EDR/compliance failure, suspected loss/tamper, unsuccessful sanitization validation, or vendor evidence gap. Quarantine the asset and invoke Security/Records/Asset Management; never mark complete from a vendor invoice alone.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `new-device controls`
- `compliance policy and exceptions`
- `data classification/hold`
- `sanitization program authority`
- `approved methods/standards/vendors`
- `custody events`
- `validation`
- `certificate/evidence retention`
- `failed media`
- `final disposition`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
