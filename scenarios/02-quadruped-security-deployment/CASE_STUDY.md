# Case Study 2 — Three Quadrupeds for Night Security

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Scenario

A company has purchased three quadruped robots to patrol a fenced industrial campus at night. The robots perform scheduled routes, collect approved video/thermal observations, detect defined anomalies, and escalate to a human security operator. They do not confront, pursue, detain, or use force.

## Program outcome

Launch a human-supervised, privacy-governed patrol service with defined geofences, safe routes, docking/charging, reliable communications, alert verification, evidence handling, and field/support coverage.

## Operating concept

- Robot A patrols perimeter north/east.
- Robot B patrols perimeter south/west.
- Robot C is reserve/overlap and rotates through charging, exception response, and coverage.
- The security operations center approves missions, watches health, verifies alerts, and dispatches a human responder.
- The robot observes and reports. Human security retains authority for incident decisions.

## Success measures

**Table 1. Success measures — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Measure | Threshold |
|---|---:|
| Scheduled patrol completion | At least 98% over 30 consecutive nights |
| Fleet availability | At least 95% during the 10-hour patrol window |
| Geofence violations | 0 |
| Critical alert delivery | 100% within 15 seconds during 50 witnessed tests |
| False-alert workload | No more than 6 operator-reviewed false alerts per 10-hour night after tuning |
| Safe return/dock on low battery | 100% of tests |
| Privacy/retention compliance | 100% mandatory controls |
| Support drill | End-to-end alert/case/field escalation passes |

## Key risks

Low light/weather; stairs/drop-offs; gates and vehicle traffic; wildlife; uneven/slippery surfaces; loss of localization/network; docking failure; battery depletion; camera/thermal degradation; unauthorized remote control; privacy overcollection; evidence chain-of-custody gaps; human overreliance on an automated alert.

## Phases

1. Security use case, authority, privacy, and policy definition.
2. Route/site survey in daylight and at night.
3. Geofence, mission, network, docking, alert, evidence, and support design.
4. MuJoCo route simulation and FAT (Factory Acceptance Test) of missions, faults, and security-operator workflows.
5. Site commissioning and controlled shadow patrols with human escort.
6. Unattended route segments under human supervision.
7. Full scheduled patrol, hypercare, and handoff.

## Why a legged platform is considered

This campus includes code-compliant stairs, curb transitions, gravel, drainage edges, and narrow human walkways. Public industrial-quadruped specifications show the category can traverse stairs, slopes, and uneven terrain. Compared with a fixed robot arm that normally requires an engineered work cell, or a wheeled robot that needs a continuous wheel-compatible route, a legged robot may reuse more of the existing human path. That can reduce site work, but it does not eliminate it: the plan still funds docks, power, wireless coverage, lighting review, geofences, signage, route repair, and emergency retrieval.

## Financial decision tied to the scenario

The modeled purchase uses the current public $100,000 Unitree B2-W listing only as an industrial-quadruped price reference, with separate quote-required allowances for sensor payloads, docks, integration, training, support, tax, and suitability. The base case requires removing two contracted rover posts while retaining an on-site human responder. If only one rover post can be removed, the simple payback expands from 3.2 years to 11.7 years, so the three-robot operating plan should not expand beyond the pilot. The assumptions and formulas are in [Business Case and Total Cost of Ownership](BUSINESS_CASE_AND_TCO.md).
