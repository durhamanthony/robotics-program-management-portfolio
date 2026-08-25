# Case Study 1 — Retail Backroom Humanoid Fulfillment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Scenario

Fictional Meridian Store 214 has a backroom designed for people: a truck-receiving door, 0.9–1.2 meter aisles, standard doors, a short split-level route, mixed shelf heights, garment rails, stock carts, and a courtesy drop-off table. Sales associates leave customers to locate shoe sizes and garments. The store will not rebuild the backroom for dedicated wheeled-robot lanes or fixed automation during this pilot. [SA-L]

Two humanoid robots are deployed for employee-only receiving, stocking, retrieval, return put-away, and cycle counts. During inbound receiving, a robot-operated forklift visibly carries a full pallet from the truck, places it in the center receiving zone, and returns into the truck before humanoid missions are released. One humanoid stores cartons on ground-level racks; the other uses the visible stair route for raised storage. During fulfillment, a tablet request includes Stock-Keeping Unit (SKU), size, color, priority, and drop-off point. A robot confirms the location, pulls an approved shoe box or already-hung garment, scans it, places it on the courtesy drop-off table, and turns toward the shelves. A human sales associate bends both arms to collect the packages through the staffed service window, turns around, and walks away; package removal closes the custody event. Tangled hangers, torn packaging, loose garments, heavy items, ladders, and customer-floor work route to people. [SA-L]

## Program-manager decisions

1. Kept the first release narrow enough to test: full-pallet inbound receipt, two item classes, one store, employee-only courtesy drop-off, and staffed service-window collection.
2. Required Factory Acceptance Test (FAT), Site Acceptance Test (SAT), and User Acceptance Testing (UAT) evidence before the 30-day pilot.
3. Separated operational acceptance from financial scale approval.
4. Required every cost to be labeled as a public benchmark, fictional result, planning allowance, calculated value, or binding quote required.

## Pilot results

**Table 1. Pilot results — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Measure | Gate | Fictional 30-day result | Outcome |
|---|---:|---:|---|
| Retrieval mission success | at least 97% | 98.1% | pass |
| Median request-to-drop-off | no more than 4.0 minutes | 3.4 minutes | pass |
| Inventory location accuracy | at least 98% | 98.7% | pass |
| Interventions | no more than 3/100 | 2.2/100 | pass |
| Damage or wrong item | no more than 0.5% | 0.2% | pass |
| Recordable safety events | zero | zero | pass |
| Annual gross value | at least $346,000 for five-year payback | $148,258 | fail |

## Outcome

Store operations accepted the workflow, controls, training, support model, and residual-risk owners. Finance held chain rollout because annual gross value was below recurring cost and $197,742 below the five-year scale threshold. The result is intentionally credible: the pilot proved that the process could work, but not that it should yet scale.

## Why the scenario is useful

It demonstrates the work between a promising robot capability and an operating decision: workflow observation, scope control, safety, privacy, integration, employee adoption, acceptance evidence, support readiness, Total Cost of Ownership (TCO), sensitivity, and a documented no-go/conditional scale decision.
