# Safety and Acceptance Plan — Retail Backroom Humanoids

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Operating limits

Employee-only backroom; approved mapped route; low-speed shared-space mode; approved shoe boxes 0.3–8 kilograms and already-hung garments; trained employees present; human emergency-stop and work-stop authority. Customer-floor work, tangled hangers, loose garments, ladders, electrical work, spills, and hazardous goods are prohibited.

## Principal hazards and controls

**Table 1. Principal hazards and controls — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Hazard | Preventive control | Detection/protective control | Recovery |
|---|---|---|---|
| person/cart in aisle | right-of-way, low speed, marked parking | perception, protective stop, emergency stop | supervisor clears/restarts by checklist |
| fall on stair/threshold | mapped route, surface/edge inspection | posture/fault monitor and exclusion distance | isolate area; field retrieval plan |
| dropped/wrong item | approved grasp set; scan before pick | grip/load monitoring; pick/handoff scan | safe stop; human exception |
| blocked fire door/egress | route excludes staging in egress | opening inspection and route-health check | recall robot; use human workflow |
| network/integration loss | local safe behavior; idempotent interface | heartbeat, timeout, transaction reconciliation | pause missions; tablet becomes human queue |
| battery/electrical/thermal | approved charger, inspection, clearances | temperature/fault monitoring | isolate power; emergency response |
| privacy/security misuse | employee-only purpose, least privilege | access logs, masks, retention/deletion checks | revoke access; incident process |

## Mandatory acceptance tests

**Table 2. Mandatory acceptance tests — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Test | Witnessed criterion | Result |
|---|---|---|
| FAT-010 approved-item handling | 100 varied picks with at least 97% success and no uncontrolled drop | pass |
| FAT-020 exception handling | 10/10 tangled/damaged/unsupported cases reject without grasp | pass |
| SAT-010 route/stair/door | 20/20 cycles remain in route and complete safe stops | pass |
| SAT-020 human/cart intrusion | 30/30 approaches stop before protective boundary | pass |
| SAT-030 network/interface loss | 10/10 faults enter defined safe hold; no duplicate transaction | pass |
| SAT-040 emergency stop/restart | each device stops motion; only authorized checklist restart | pass |
| UAT-010 retrieval | at least 97% mission success | 98.1% |
| UAT-020 wait | median no more than 4.0 minutes | 3.4 minutes |
| UAT-030 quality/intervention | wrong/damage at most 0.5%; interventions at most 3/100 | 0.2%; 2.2/100 |

FAT means Factory Acceptance Test, SAT means Site Acceptance Test, and UAT means User Acceptance Testing.

## Authority

Safety Lead approves mandatory safety evidence; Store Sponsor accepts operations; Finance separately decides scale. A failed mandatory safety test is no-go regardless of schedule or financial value.
