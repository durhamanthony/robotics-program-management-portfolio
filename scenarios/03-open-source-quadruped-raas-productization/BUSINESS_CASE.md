# Business Case - Open-Source Quadruped RaaS Productization

> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; [PB-M] public benchmark/medium applicability or source confidence; [RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; [DC-L] derived calculation whose confidence inherits low-confidence inputs; [UPV] unknown or pending validation.

## Decision

Authorize limited availability for a 48-robot launch cohort only if signed 36-month subscriptions support the $2,400 per robot-month decision price and each customer accepts the supervised-laboratory scope. At the disclosed inputs, 48 robots recover the modeled $2,397,234 productization investment. The model is a planning screen, not a quotation or demand forecast.

## Evidence status

Open-source availability, the Solo12 architecture, PAL Robotics' discontinued-sales notice, and published license statements are [PB-H]. Glassdoor's May 2026 U.S. Robotics Software Engineer benchmark and the official Unitree Go2 EDU list price are [PB-M]. The March 2026 Bureau of Labor Statistics (BLS) private-industry compensation split is [PB-H]. Staffing mix, labor hours, allowances, service demand, subscription price, customer capacity, cohort size, and fictional pilot performance are [SA-L]. All totals, recovery screens, and Return on Investment (ROI) values inherit low confidence as [DC-L]. Executed orders, audited costs, realized cash savings, and warranty history remain [UPV].

## Provider unit economics

**Table 1. Provider economics per robot over a 36-month term - Evidence: [PB-M], [SA-L], and [DC-L]; Confidence: low overall**

| Item | Calculation | Amount |
|---|---:|---:|
| Subscription revenue [SA-L] | $2,400 x 36 months | $86,400 |
| Build, calibration, and delivery [DC-L] | $15,900 Go2 EDU comparator [PB-M] + 50 hours x $74 [SA-L/PB-M] + $4,400 allowance [SA-L] | ($24,000) |
| Direct service, cloud, and reserve [DC-L] | 36 hours/year x $74 x 3 + $600/year cloud x 3 + 12% of build cost | ($12,672) |
| Contribution before onboarding [DC-L] | $86,400 - $36,672 | **$49,728** |
| Onboarding contribution per robot [DC-L] | ($6,000 price - (40 hours x $74 + $1,500)) / 2 robots | **$770** |
| Total contribution per robot [DC-L] | $49,728 + $770 | **$50,498** |

The unrounded price floor is **$2,384.57 per robot-month**: (($2,397,233.62 / 48) + $24,000 + $12,672 - $770) / 36. The decision price rounds up to $2,400. Development recovery = $2,397,233.62 / $50,498 = 47.47, rounded up to **48 subscribing robots**. A 48-robot cohort produces $2,423,904 of modeled contribution, only $26,670 above the rounded authorization, before sales expense, corporate overhead, financing, taxes, bad debt, or profit. Those omissions prevent this figure from being called net margin.

## Customer screen for a two-robot lab

**Table 2. Customer 36-month value screen - Evidence: [PB-M], [SA-L], and [DC-L]; Confidence: low overall**

| Item | Calculation | Amount |
|---|---:|---:|
| Onboarding [SA-L] | One site | $6,000 |
| Subscription [DC-L] | 2 robots x $2,400 x 36 months | $172,800 |
| Subscription plus onboarding subtotal [DC-L] | $6,000 + $172,800 | **$178,800** |
| Three-year RaaS TCO [DC-L] | $178,800 + $6,000 lab-network allowance [SA-L] | **$184,800** |
| Engineering/support capacity value [DC-L] | 1,000 hours/year [SA-L] x $74 Glassdoor rate [PB-M] x 3 years | **$222,000** |
| Net capacity value [DC-L] | $222,000 - $184,800 | **$37,200** |
| Three-year ROI [DC-L] | $37,200 / $184,800 | **20.1%** |

The separate $6,000 lab-network allowance is an explicit customer scenario input, not a hidden arithmetic plug. The $74 hourly value is the Glassdoor U.S. average salary rate for a Robotics Software Engineer as of May 2026; it is not a customer payroll actual or a fully loaded employer cost. Released engineering time is capacity, not booked cash savings unless an invoice, overtime payment, contractor expense, or funded position is actually avoided.

## Price and utilization gates

At 1,000 released hours per year and $74 per hour, the maximum subscription price that preserves a 15% three-year customer ROI is **$2,514 per robot-month**, rounded down from $2,514.49. The base $2,400 offer has a 20.1% modeled ROI. At 900 hours, ROI falls to 8.1% and misses the 15% gate; at 800 hours, net value is negative. The break-even utilization is 833 released hours per year after rounding up from 832.43. Limited availability therefore requires a customer-specific time study and a price at or below the approved ceiling.

## Decision outcome

Limited availability is conditionally approved for the disclosed lab envelope. General Availability is not approved until 48 units are contracted at or above the price floor, salary and capacity inputs are replaced with customer evidence, supplier and service allowances are replaced with audited costs, the 48-unit service load is capacity-tested, and an independent license/security review closes all [UPV] items.
