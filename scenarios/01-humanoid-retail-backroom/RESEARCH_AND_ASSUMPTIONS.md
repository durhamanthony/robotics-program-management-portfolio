# Research and Assumptions — Retail Backroom Humanoid Pilot

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Public evidence used

**Table 1. Public evidence used — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Source | What it supports | What it does not support |
|---|---|---|
| [Sanctuary AI retail deployment](https://sanctuary.ai/news/sanctuary-ai-deploys-first-humanoid-general-purpose-robot-commercially/) | category relevance: 110 correctly completed retail tasks during a one-week Mark's pilot, including front/back store picking, packing, cleaning, tagging, labeling, and folding | Meridian autonomy, speed, reliability, safety, price, staffing, or payback |
| [Agility Robotics human-centric design](https://www.agilityrobotics.com/content/agility-robotics-launches-next-generation-of-digit-worlds-first-human-centric-multi-purpose-robot-made-for-logistics-work) | rationale for testing a human form factor in existing human spaces and infrastructure | this scenario's dexterity, stair performance, item handling, or cost |
| [Glassdoor U.S. Retail Sales Associate salary, June 2026](https://www.glassdoor.com/Salaries/retail-sales-associate-salary-SRCH_IN1_KO0%2C22.htm) | $40,242/year average, equivalent to $19.35/hour at 2,080 paid hours; 94,388 anonymously submitted salaries [RBE-M] | Meridian payroll, benefits, location, scheduling, vacancy, overtime, or realizable cash savings |

## Fictional scenario inputs

Store layout, route, requests, staffing, baseline wait, inventory accuracy, mission results, damage rate, interventions, margin recovery, schedule, and customer names are invented for a complete program-management exercise. They are deliberately labeled on the dashboard and in calculations.

## Quote-required inputs

Robot purchase/lease; manipulation package; software; remote operations; inventory integration; freight; tax; insurance; cybersecurity review; site work; charging; spare parts; battery replacement; field service; training; support response; and decommissioning.

## Assumption register

**Table 2. Assumption register — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| ID | Assumption | Owner | Validation | If false |
|---|---|---|---|---|
| A-01 | approved shoe boxes weigh 0.3–8 kg | Inventory lead | representative sample and scale log before FAT | reduce item classes/change scope |
| A-02 | short stair and doors meet vendor envelope | Safety lead | measured route and witnessed SAT | use alternate courtesy drop-off/no-go |
| A-06 | existing robot-operated forklift can exchange mission and zone-clear states | Safety lead | interface test and 20 witnessed unload cycles | keep inbound receipt human-operated/no-go |
| A-03 | inventory locations are available by application interface | IT lead | test tenant and 20 interface cases | manual scan workflow/replan |
| A-04 | associates can use returned time for customer service | Store sponsor | staffing and floor-observation study | do not count labor value |
| A-05 | no customer-floor operation is needed | Store sponsor | approved operating procedure | new privacy/safety/change gate |

## Claim discipline

The browser animation demonstrates sequence only. It does not prove robot performance. MuJoCo source demonstrates a simplified state machine and route concept; it is not a safety-certified controller or evidence that a commercial platform can perform the task. Procurement and scale decisions require vendor-specific testing and customer actuals.
