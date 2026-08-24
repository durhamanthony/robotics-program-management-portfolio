# Business Case and Total Cost of Ownership — Retail Backroom Humanoids

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Decision

Fund one controlled store pilot to test operational feasibility in an unchanged human workspace. Do not approve chain rollout until binding vendor quotations replace planning allowances and measured annual gross value reaches at least $346,000.

## Evidence status

The Glassdoor labor salary is a **research-based estimate** because it is crowd-sourced rather than Meridian payroll. The workflow relevance is also a **research-based estimate**. Robot, integration, license, support, workload, and margin-recovery inputs are **scenario assumptions**. Totals, gaps, and thresholds are **derived calculations**. Actual store workload, benefits, vendor pricing, gross-margin recovery, service levels, and realized savings are **unknown / pending validation**.

## Why a humanoid is being tested

The fictional store has a truck-receiving interface, standard doors, narrow aisles, mixed shelf heights, garment rails, a short stair route, hand-carried merchandise, and a courtesy drop-off table. These are human interfaces. Sanctuary AI reported a retail pilot covering front- and back-of-store activities; Agility Robotics states that its humanoid is designed for spaces and infrastructure built for people. That is evidence that the category is relevant, not evidence that this scenario's robot will meet its targets.

## Five-year planning model

**Table 1. Five-year planning model — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Item | Formula | Five-year value | Evidence class |
|---|---|---:|---|
| Installed pilot | two robot allowances + integration + site/safety + training + reserve | $640,000 | quote required |
| Recurring operation | $218,000 × 5 years | $1,090,000 | quote required |
| Total Cost of Ownership (TCO) | $640,000 + $1,090,000 | **$1,730,000** | calculated |
| Labor-capacity value | 4,965 hours × ($40,242 ÷ 2,080 hours) × 5 | $480,292 | Glassdoor salary benchmark + fictional measured hours |
| Gross-margin recovery | $52,200 × 5 | $261,000 | fictional pilot measurement |
| Total five-year value | $480,292 + $261,000 | **$741,292** | calculated |
| Five-year value gap | $1,730,000 − $741,292 | **$988,708 shortfall** | calculated |

Glassdoor reported a June 2026 U.S. Retail Sales Associate average salary of $40,242 per year, based on 94,388 anonymously submitted salaries. Dividing by 2,080 paid hours gives a $19.35/hour planning equivalent. This crowd-sourced salary benchmark is [RBE-M]; it excludes Meridian benefits, payroll burden, location, overtime, scheduling, and realizable cash savings.

## Scale threshold

To recover installation within five years while covering recurring cost:

`$640,000 ÷ 5 + $218,000 = $346,000 required annual gross value`

The fictional pilot produced $148,258 annualized gross value:

`4,965 hours × ($40,242 ÷ 2,080) = $96,058 labor-capacity value`  
`$96,058 + $52,200 margin recovery = $148,258`

The annual gap to the five-year threshold is $197,742. Because gross value is $69,742 below recurring cost, there is no positive simple payback at current inputs.

## Sensitivity

**Table 2. Sensitivity — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Case | Installed | Recurring/year | Gross value/year | Five-year net | Decision |
|---|---:|---:|---:|---:|---|
| Pilot result | $640,000 | $218,000 | $148,258 | -$988,708 | hold rollout |
| Cost-down | $480,000 | $140,000 | $148,258 | -$438,708 | still hold |
| Value-up | $640,000 | $218,000 | $346,000 | $0 | minimum five-year gate |
| Cost-down + value-up | $480,000 | $140,000 | $346,000 | $550,000 | candidate; revalidate risk/capacity |

## Benefit guardrails

Time returned to associates counts only when schedules, overtime, vacancy coverage, or documented customer-facing capacity changes. It is not automatically booked as cash savings. Margin recovery requires a transaction-level control group and Finance approval. Robot animation timing is never used as a productivity claim.

## Sources

- [Glassdoor — U.S. Retail Sales Associate salary, June 2026](https://www.glassdoor.com/Salaries/retail-sales-associate-salary-SRCH_IN1_KO0%2C22.htm)
- [Sanctuary AI — Mark's retail-store deployment](https://sanctuary.ai/news/sanctuary-ai-deploys-first-humanoid-general-purpose-robot-commercially/)
- [Agility Robotics — human-centric robot for existing/as-built spaces](https://www.agilityrobotics.com/content/agility-robotics-launches-next-generation-of-digit-worlds-first-human-centric-multi-purpose-robot-made-for-logistics-work)
