# Business Case and TCO (Total Cost of Ownership) — Quadruped Night Security

## Decision

Deploy the three purchased quadrupeds through a 30-night controlled pilot. Approve the three-robot operating plan only if the customer can remove **two contracted walking-rover posts per night while retaining an on-site human responder**, and if the patrol, alert, privacy, safety, and support tests pass.

The base case pays back in 3.22 years. If operations can remove only one rover post, payback increases to 11.7 years. That conservative result does not justify expansion.

## Evidence status

Published mobility specifications and the $100,000 base-unit reference are **public benchmarks**. Route suitability is a **research-based estimate**. Payload, integration, support, labor-post, vehicle, and operating-cost inputs are **scenario assumptions**. Total Cost of Ownership, payback, and sensitivity results are **derived calculations**. Configured system price, actual route performance, staffing changes, insurance, service terms, and realized savings are **unknown / pending validation**.

## Why a legged platform can reduce site alteration

The campus route includes code-compliant stairs, curbs, gravel, and uneven outdoor sections. Current manufacturer specifications provide useful feasibility anchors:

- Boston Dynamics lists Spot at a 30-degree maximum slope, 300 millimeter maximum step, IP54 ingress protection, and 90-minute average runtime.
- Unitree describes the industrial B2 as capable of sustained stair climbing, uneven/slippery terrain, 40-centimeter obstacles, and more than five hours of unloaded walking.
- Agility states that human-form robots are intended to work in existing human infrastructure without the costly retrofits often required by single-purpose automation.

These statements support route screening, not final acceptance. Legged mobility can reduce continuous-path reconstruction compared with a wheeled robot and can avoid a fixed arm's engineered work cell, but the project still requires docks, power, wireless coverage, lighting review, signs, geofences, route repair, and a retrieval method.

## Cost model

The public Unitree B2-W listing of $100,000 is used only as a current industrial-quadruped price reference. It is not a vendor selection or a claim that the listed configuration is suitable for security. Sensor payloads, docks, software, integration, support, insurance, taxes, and compliance remain quote-required.

| Cost | Calculation | Amount |
|---|---:|---:|
| Base one-time items | Robots, payloads, docks, integration, site, controls, training, logistics | $635,000 |
| Contingency and management reserve | Item contingency plus sponsor reserve | $95,250 |
| Installed one-time cost | $635,000 + $95,250 | **$730,250** |
| Annual recurring cost | Fleet software/support $75,000 + maintenance/spares $30,000 + evidence storage $12,000 | **$117,000** |
| Five-year TCO (Total Cost of Ownership) | $730,250 + 5 × $117,000 | **$1,315,250** |

Line-item sources and replacement evidence are in [BUDGET.csv](BUDGET.csv).

## Benefit model

The customer scenario input is a $45/hour contracted rover invoice rate. It includes vendor wages, benefits, management, insurance, and margin; it is not represented as a BLS wage. The customer must replace it with actual invoices.

| Benefit | Calculation | Annual value |
|---|---:|---:|
| Two walking-rover posts avoided | 2 rovers × 10 hours × 365 nights × $45/hour | $328,500 |
| One patrol vehicle avoided | Customer fleet input | $15,000 |
| Gross annual benefit | $328,500 + $15,000 | **$343,500** |
| Less recurring robot cost |  | ($117,000) |
| Net annual benefit |  | **$226,500** |

The existing fixed-post human responder remains. Robot alerts are verified by that authorized human; the model does not remove human incident authority. No theft prevention, liability avoidance, or incident avoidance is monetized.

## Base and conservative results

| Result | Base: two rover posts removed | Conservative: one rover post removed |
|---|---:|---:|
| Annual gross benefit | $343,500 | $179,250 |
| Annual net benefit after recurring cost | $226,500 | $62,250 |
| Simple payback | 3.22 years | 11.73 years |
| Five-year net benefit | $402,250 | ($419,000) |
| Five-year ROI (Return on Investment) | 30.6% | Negative |
| Five-year NPV (Net Present Value) at 8% | $174,099 | Negative |

The minimum gross annual benefit for five-year simple payback is $263,050: $730,250 ÷ 5 + $117,000.

## Thirty-night acceptance tied to the scenario

1. Robots A and B complete eight combined scheduled patrol circuits per night; Robot C provides charging rotation and reserve coverage.
2. At least 98% of scheduled patrol circuits complete over 30 nights.
3. All 50 witnessed critical-alert tests reach the SOC (Security Operations Center) within 15 seconds and are linked to the correct robot, time, route, and evidence.
4. After tuning, false alerts requiring operator review do not exceed six per 10-hour night.
5. There are zero geofence violations and zero uncommanded entries into exclusion zones.
6. Mandatory stair, curb, rough-terrain, low-light, network-loss, low-battery, docking, sensor-degradation, and retrieval tests pass.
7. Privacy masks, authorized access, retention, deletion, and audit tests pass before unattended patrol.
8. A human verifies every critical alert and owns dispatch, notification, and escalation decisions.

## Research anchors

- [Unitree B2-W product page and public price reference](https://shop.unitree.com/products/unitree-b2-w)
- [Boston Dynamics Spot specifications](https://bostondynamics.com/products/spot/)
- [Agility human-environment deployment rationale](https://www.agilityrobotics.com/content/agility-robotics-launches-next-generation-of-digit-worlds-first-human-centric-multi-purpose-robot-made-for-logistics-work)
- [BLS Security Guards, May 2023](https://www.bls.gov/oes/2023/may/oes339032.htm), used only to test the reasonableness of a customer contract rate
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20)

Research checked August 16, 2026. See [Research and Assumptions](RESEARCH_AND_ASSUMPTIONS.md) for limits and replacement rules.
