# Hardware Refresh Assumptions, Evidence, and Experience Map

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Separate career evidence, public guidance, scenario inputs, calculations, and discovery unknowns.

## Experience-to-control trace

| Verified experience | Control informed | Scenario boundary |
| --- | --- | --- |
| 37K Macs / 300K Windows modern management | Scale-aware inventory, deployment, policy, telemetry, and support | Only 360 devices are modeled here |
| 98% OS compliance | Compliance definition and post-deployment reporting | The case compliance rate is fictional |
| Intune, SCCM/MECM, Jamf, ServiceNow, Tanium, BeyondTrust | Provisioning, device management, workflow, remote support, telemetry | Tool availability/licensing must be verified at Company ABC |
| Endpoint standards and audit partnership | Device build, encryption, least privilege, evidence, sanitization | No certification or regulatory opinion is claimed |
| Scrum and Kanban leadership | Backlog, ceremonies, flow, WIP, metrics, and continuous improvement | Method outcomes are modeled |

## Scenario baseline

- Four sites; 360 devices: 270 laptops, 60 desktops, 30 phones.
- Company ABC uses Microsoft Intune/Entra for the target Windows/mobile control plane and SCCM/MECM for selected existing-device reimage/co-management paths; a final design must validate actual tenant/licensing and device mix.
- OneDrive Known Folder Move or the approved enterprise backup path protects user data before swap; application data outside approved locations requires explicit handling.
- 344 devices are deployed at the illustrative checkpoint; 16 are controlled exceptions, not silently removed from scope.
- Secure reuse/disposal follows the organization’s sanitization program aligned to NIST SP 800-88 Rev. 2 and approved standards/vendors.

## Unknowns before a real baseline

Actual user/device assignment, hardware age/warranty, remote users, accessibility needs, application/package readiness, local data, network/staging capacity, procurement lead times, licensing, tax/shipping, e-waste requirements, data classification, legal hold, union/work rules, blackout periods, and site operating calendars.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `evidence item`
- `class`
- `source/owner`
- `confidence`
- `validation date`
- `planning impact`
- `replacement evidence`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
