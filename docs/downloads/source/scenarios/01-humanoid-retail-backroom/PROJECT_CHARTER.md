# Project Charter — Two Humanoids for Retail Backroom Fulfillment

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Authorization

Meridian Department Store authorizes a 20-week, $640,000 controlled pilot at fictional Store 214. The Deployment Program Manager may coordinate the vendor, store, safety, information-security, inventory, and field-service work inside this charter. Any customer-floor operation, ladder work, electrical repair, new merchandise class, additional store, or budget increase requires sponsor-approved change control.

## Business problem and human-form-factor rationale

Sales associates leave customers to search a legacy backroom with a truck-receiving interface, narrow human aisles, standard doors, a short stair route, mixed shelves, garment racks, and no dedicated autonomous-mobile-robot lanes. Rebuilding the store for fixed automation or a wheeled fleet would disrupt operations and still leave receiving, stairs, doors, shelves, garment rails, and courtesy drop-off points. A humanoid pilot tests whether one system can use those existing human interfaces after a robot-operated forklift safely stages inbound pallets. [SA-L]

Sanctuary AI publicly reported a one-week Mark's retail-store pilot in which a general-purpose robot completed 110 retail-related tasks, including picking, packing, cleaning, tagging, labeling, and folding. Agility Robotics describes its humanoid form factor as intended for spaces and infrastructure designed for people. These vendor statements support category relevance; they do not validate Meridian's cost, autonomy, safety, or return.

## Objective and measurable outcomes

During a 30-day employee-only pilot:

- complete at least 97% of approved retrieval missions without manual recovery;
- keep median associate request-to-courtesy-drop-off time at or below 4.0 minutes;
- complete 20 of 20 witnessed forklift unload, park, zone-clear, and humanoid-release cycles without task overlap;
- reach at least 98% inventory-location accuracy;
- require no more than 3 interventions per 100 missions;
- keep damage or wrong-item events at or below 0.5%; and
- record zero safety-control bypasses or recordable injuries.

## In scope

Full-pallet truck unloading by a robot-operated forklift; stable-pallet verification; forklift-to-humanoid zone release; carton stocking at lower and raised racks; tablet request; Stock-Keeping Unit (SKU), size, and color validation; shoe-box and already-hung-garment retrieval; existing aisle, door, and short-stair navigation; courtesy drop-off table; return put-away; cycle counts; charging; identity and inventory integration; telemetry; training; Factory Acceptance Test (FAT); Site Acceptance Test (SAT); User Acceptance Testing (UAT); support drill; 30-day pilot; closeout.

## Out of scope

Customer-floor operation; customer interaction; trailer entry by humanoids; mixed forklift/humanoid traffic; unstable, over-height, or damaged pallets; tangled-hanger separation; loose-garment folding; ladders; light-bulb or electrical work; spills or restroom cleaning; hazardous goods; construction; unsupervised safety decisions; facial recognition; chain rollout.

## Governance and gates

**Table 1. Governance and gates — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Gate | Chair | Required evidence | Decision |
|---|---|---|---|
| G1 workflow baseline | Store sponsor | observed task map, baseline sample, scope | approve design |
| G2 design/safety | Safety lead | hazard log, route, interfaces, privacy limits | authorize FAT |
| G3 FAT | Engineering lead | witnessed normal/fault tests | ship/configure onsite |
| G4 SAT/UAT | Store sponsor | site tests, trained users, rollback | start 30-day pilot |
| G5 operational acceptance | Store sponsor | KPI results and handoff | accept operating procedure |
| G6 financial scale | Finance | binding quotes and measured value | rollout, rework, or hold |

## Approved baseline

Schedule: 20 weeks. Pilot authorization: $640,000. Five-year planning Total Cost of Ownership (TCO): $1,730,000. Operational closeout and chain-rollout approval are separate decisions.
