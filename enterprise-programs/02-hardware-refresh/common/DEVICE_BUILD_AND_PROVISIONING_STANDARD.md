# Hardware Refresh Device Build and Provisioning Standard

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Define a reproducible business-ready configuration and evidence path for laptops, desktops, and phones.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Windows laptops/desktops | OEM image transformed through Windows Autopilot/Intune where feasible; SCCM/MECM task sequence for approved reimage path | Endpoint Engineering | Enrollment, policy, app, update, compliance and user test |
| Mobile phones | Corporate enrollment, required apps, configuration/compliance and number/line validation | Mobility Lead | MDM and call/data test |
| Identity | Microsoft Entra join or approved existing-state transition; standard user by default | IAM + Security | Join, MFA, conditional access test |
| Security | Encryption, supported OS/patch, Defender/EDR, firewall, screen lock, local-admin control | InfoSec | Compliance and risk report |
| Supportability | Asset tag, warranty, owner/site, remote support, monitoring, knowledge and recovery | Service Operations | CMDB/inventory and support acceptance |

## Execution sequence

1. Approve persona and model standards, hardware minimums, accessories, warranty, and exception process.
2. Freeze versioned provisioning profiles, required/available apps, scripts, policies, updates, drivers, and dependencies.
3. Run clean-device, upgrade/reimage, remote, executive, accessibility, and shared-device pilots.
4. Capture automated deployment and compliance reports plus manual business workflow evidence.
5. Release build version only after Endpoint, Security, application owners, Service Desk, and Change approval.
6. Track build drift; change version and retest affected personas before the next wave.

## Acceptance evidence

- [ ] Required apps/configuration install successfully or have approved post-login path and owner.
- [ ] Device reports encryption, supported OS/update, EDR, firewall, and compliance before business release.
- [ ] Standard user, executive/delegate, shared-device, remote/VPN, accessibility, and Tier 1 app personas pass.
- [ ] Asset tag/serial/user/site/warranty/build version and management identifiers reconcile.

## Exception, rollback, and escalation

Quarantine any device with identity mismatch, missing encryption/EDR, failed critical app, unknown custody, or unsupported configuration. Reissue the prior device where safe, use a validated spare, or re-run the approved build. Do not bypass compliance to meet an appointment metric.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `personas/models`
- `OS/build/version`
- `join/enrollment`
- `security policies`
- `apps/scripts`
- `updates/drivers`
- `accessories`
- `test matrix`
- `release approval`
- `exception/quarantine`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
