# Hardware Refresh Procurement, Staging, and Logistics Plan

> **Portfolio case study — Filled example + reusable template.** Company ABC and Company XYZ are fictional. Dates, headcounts, costs, performance, and decisions are scenario assumptions unless explicitly identified as verified experience or a public source. As of 2026-08-25.

## Purpose

Control forecasts, purchase orders, receipts, serialized custody, capacity, site kits, shipping, and spares.

## Filled example

| Work package | Scenario baseline | Accountable owner | Evidence / gate |
| --- | --- | --- | --- |
| Procurement | 360 devices plus 5% temporary spares where approved; model/accessory standards | Procurement | PO, price, lead time, warranty, terms |
| Receipt | Serialized scan against PO/ASN; damage and shortage exceptions | Asset Management | Receipt reconciliation |
| Staging | Capacity 40 devices/day; network/power/benches/secure storage | Endpoint Lead | Daily input/output/defect counts |
| Distribution | Site kits and remote courier with appointment/user mapping | Logistics Lead | Custody scan and delivery confirmation |
| Returns | Old device collected, quarantine and asset record updated | Asset Management | Return aging and chain of custody |

## Execution sequence

1. Forecast by model/persona/site/wave plus spares; validate budget, contract, tax, delivery, warranty, and return terms.
2. Place and track purchase orders; reconcile order acknowledgment, advanced shipping notice, receipt, invoice, and asset records.
3. Securely stage, tag, enroll, configure, test, pack, and scan devices against the wave roster.
4. Pre-position site kits only in approved secure storage; keep user/device/accessory mapping intact.
5. Record handoff signatures and immediately triage no-show, damage, loss, or wrong-device exceptions.
6. Reconcile new issue and old return daily; investigate any serial without one authoritative state.

## Acceptance evidence

- [ ] PO, receipt, invoice, and asset serial quantities reconcile or have approved exceptions.
- [ ] No device leaves controlled custody without asset tag, assignee/site/wave, build status, and scan.
- [ ] Staging capacity and defect/rework do not exceed the next wave demand and WIP limit.
- [ ] Remote delivery and return have tracking, identity verification, and exception escalation.

## Exception, rollback, and escalation

Hold shipment or site release for serial mismatch, lost custody, damaged/tampered package, failed build/security, or user mismatch. Quarantine and investigate. Use controlled spare inventory; never substitute an untracked device.

## Reporting

Report total scope, completed, passed, failed, deferred with approved reason, and unknown. Percentages always show the numerator and denominator. Owners update the control source before the dashboard is refreshed.

## Reusable template fields

Copy this artifact and replace the scenario values with approved project evidence:

- `demand/model forecast`
- `PO/vendor/price/lead time`
- `receipt/ASN/invoice`
- `staging capacity and WIP`
- `secure storage`
- `asset scan`
- `site/remote distribution`
- `spares`
- `returns`
- `exceptions`

## Control note

The project manager owns document currency and traceability, not every technical decision. Accountable technical, security, privacy, legal, finance, procurement, HR, and business owners approve decisions in their domains. A blank approval, untested rollback, or unverified user/device count remains open; it is never converted into a green status by narrative.
