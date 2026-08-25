# Statement of Work — Retail Backroom Humanoid Pilot

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Purpose

Configure and deploy two vendor-supplied humanoid robots plus a robot-operated forklift interface at fictional Meridian Store 214 for an employee-only backroom workflow. At inbound receipt, the forklift visibly carries a full pallet from the truck, places it in the center receiving zone, and returns into the truck before humanoid missions begin; humanoids then transfer approved cartons to lower and raised storage racks. For fulfillment, a sales associate submits an item request from a tablet; the robot verifies the request, walks an approved route, retrieves a shoe box or already-hung garment, places it on the courtesy drop-off table, and turns toward the shelves. A human associate bends both arms to collect the merchandise through the staffed service window, turns around, walks away, package removal is confirmed, and the transaction closes. Between requests, robots perform approved return put-away and cycle-count missions. [SA-L]

## Deliverables and acceptance evidence

**Table 1. Deliverables and acceptance evidence — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Deliverable | Vendor/Program team | Meridian | Acceptance evidence |
|---|---|---|---|
| Validated workflow | observe, document, bound use cases | provide staff, volume, item classes | signed task/envelope map |
| Inbound receiving cell | configure loaded truck-to-center forklift path, pallet state, return-into-truck route, work-zone interlock, and carton-release logic | provide dock window, traffic rules, pallet standard, and witnesses | 20 witnessed unload/return/clear/release cycles without overlap |
| Route and safety design | map aisles, doors, stair, stops, faults | approve access and emergency rules | hazard log and design review |
| Tablet/inventory integration | configure identity, request, scan, event, retry | provide test tenant and data | 20 normal/fault interface tests pass |
| Courtesy handoff cell | configure table placement, robot turn-away, human service window, articulated pickup, human walk-away, pickup confirmation, and custody close | provide staffed service window and witnesses | 20 witnessed drop/turn/collect/depart cycles complete with both packages removed |
| Configured fleet | robot, charger, end effector, telemetry | provide power, network, staging | Factory Acceptance Test (FAT) report |
| Commissioned store | install, map, calibrate, test safe states | provide access and trained witnesses | Site Acceptance Test (SAT) report |
| Controlled pilot | hypercare, daily review, defects, reports | operate, log exceptions, measure benefits | 30-day User Acceptance Testing (UAT) report |
| Handoff/closeout | runbooks, spares, training, final report | accept owners and residual risks | signed operational acceptance and financial decision |

## Boundaries

Only standard, stable full pallets at the approved truck interface; approved shoe boxes from 0.3 to 8 kilograms; and already-hung garments within the validated reach envelope are handled. Mixed forklift/humanoid traffic, unstable pallets, damaged cartons, tangled hangers, loose clothing, heavy or hazardous items, customer-floor work, ladders, and electrical work route to a human exception queue.

## Commercial assumptions

The $640,000 pilot budget and $218,000 annual recurring cost are fictional planning allowances, not market quotes. The customer must obtain binding robot, integration, software, support, insurance, freight, and tax quotations before procurement or rollout.

## Completion

The Statement of Work is complete when FAT, SAT, UAT, safety, training, support, and 30-day pilot evidence is accepted; assets and residual risks have named owners; and Finance records a separate rollout decision. Operational acceptance does not imply financial approval.
