#!/usr/bin/env python3
"""Apply the approved source-level portfolio rebuild deterministically."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE3 = ROOT / "scenarios" / "03-open-source-quadruped-raas-productization"

EVIDENCE = (
    "> **Evidence-confidence key:** [PB-H] public benchmark/high source confidence; "
    "[PB-M] public benchmark/medium applicability or source confidence; "
    "[RBE-M] research-based estimate/medium; [SA-L] fictional scenario assumption/low; "
    "[DC-L] derived calculation whose confidence inherits low-confidence inputs; "
    "[UPV] unknown or pending validation."
)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def document(title: str, body: str) -> str:
    return f"# {title}\n\n{EVIDENCE}\n\n{body.strip()}\n"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_case3_documents() -> None:
    write(CASE3 / "CASE_STUDY.md", document(
        "Case Study - Open-Source Quadruped to Supported RaaS",
        """
## Productization challenge

Northstar Applied Robotics Labs is a fictional network of university and corporate controls laboratories. It can reproduce an open research quadruped, but it does not want every site to own component sourcing, build calibration, software dependency management, security updates, spares, and repair triage. The program converts the Open Dynamic Robot Initiative Solo12 reference into **OpenQuad Managed Lab**, a fictional supervised-laboratory Robotics-as-a-Service (RaaS) offer.

The product is a supported derivative, not a relabeled community project. The release adds controlled sourcing, assembly and calibration work instructions, battery and emergency-stop controls, signed software images, a Software Bill of Materials (SBOM), license notices, fleet inventory, service telemetry, a replacement pool, customer onboarding, and service-level reporting. The scenario never claims endorsement by the Open Dynamic Robot Initiative, Max Planck Society, New York University, PAL Robotics, or any contributor.

## Operating envelope

**Table 1. Release 1 operating envelope - Evidence: mixed; confidence shown by item**

| Item | Release 1 boundary | Evidence / confidence |
|---|---|---|
| User | Trained researcher or robotics engineer | [SA-L] |
| Environment | Access-controlled indoor laboratory on a prepared level floor | [SA-L] |
| Tasks | Locomotion experiments, calibration, supervised data collection, and recovery drills | [SA-L] |
| Hardware basis | Open Dynamic Robot Initiative Solo12, 12 active degrees of freedom | [PB-H] |
| Added product layer | Battery/wireless integration, guarded charging, e-stop, compute, signed images, telemetry, and swap service | [SA-L] design requiring verification |
| Excluded | Public interaction, industrial inspection, security response, autonomous outdoor work, and safety-certified production use | [SA-L] |

## Program outcome

The 12-month productization plan and six-site, 12-robot, 60-day pilot met the fictional release gates: 97.8% scheduled experiment completion, 95.6% fleet availability, 100% release-image reproducibility, complete component/license records, and seven of seven advance replacements within 48 hours. Leadership approved limited availability for the supervised-lab envelope.

General Availability remains conditional. The provider must contract at least 48 robots on 36-month terms to recover the modeled $2,397,234 productization investment at the $2,400 monthly decision price, qualify a second source for two electronics assemblies, and replace every scenario allowance with executed contracts and audited provider costs. The calculation is traceable to dated public benchmarks, but it is still a planning model rather than a market forecast.

## Why this case belongs in the portfolio

The case demonstrates the work between a promising open reference and a supportable commercial service: customer discovery, scope control, open-source compliance, systems requirements, supply chain, manufacturing test, release governance, RaaS economics, service design, customer acceptance, and evidence-based stop/scale decisions.
"""))

    write(CASE3 / "PRODUCT_BRIEF_AND_PRD.md", document(
        "OpenQuad Managed Lab Product Brief and Product Requirements Document",
        """
## Product promise

Provide a reproducible two-robot research-lab capability with predictable monthly spend, maintained release images, traceable open-source provenance, remote diagnosis, and an advance-replacement path. The offer does not convert research hardware into an industrially certified robot.

## Users and jobs

**Table 1. Users and jobs to be done - Evidence: scenario discovery synthesis [SA-L]; Confidence: low**

| User | Job | Product response |
|---|---|---|
| Principal investigator | Start experiments without a semester-long build program | Calibrated units, onboarding, reference experiments, and release notes |
| Lab engineer | Reproduce a known configuration and recover faults safely | Versioned images, configuration manifest, diagnostics, and recovery runbook |
| Procurement / finance | Compare a term commitment with self-managed ownership | Transparent 36-month TCO, inclusions, exclusions, and exit terms |
| Security / IT | Know software components, access, data flow, and update ownership | SBOM, signed images, least privilege, retention choices, and audit records |
| Provider service owner | Maintain uptime without uncontrolled product variants | Configuration baseline, swap pool, serialized assets, and change gates |

## Release 1 requirements

**Table 2. Product requirements summary - Evidence: scenario requirements [SA-L]; confidence medium after stakeholder review**

| ID | Requirement | Release threshold | Verification |
|---|---|---|---|
| PRD-001 | Every shipped unit has a serialized configuration and build record | 100% | Record audit |
| PRD-002 | The golden software image installs reproducibly | 12 of 12 pilot units | Clean-image rebuild |
| PRD-003 | Hardware and software components have license/provenance records | 100% of shipped components | SBOM and notice audit |
| PRD-004 | Emergency stop and authorized recovery work in every defined test | 100% | Witnessed fault injection |
| PRD-005 | Scheduled fleet availability during pilot | At least 95% | Service telemetry |
| PRD-006 | Scheduled experiment completion during pilot | At least 97% | Mission/event records |
| PRD-007 | Provider can ship an advance replacement for an eligible failure | Within 48 hours for at least 95% | Service-case audit |
| PRD-008 | Customer data retention and export follow the executed order | 100% | Configuration and deletion test |
| PRD-009 | Unapproved forks cannot enter the supported release | Zero | Release-control audit |
| PRD-010 | Field updates are signed, staged, observable, and reversible | 100% of releases | Deployment and rollback test |

## Product principles

1. Preserve upstream notices and do not imply contributor endorsement.
2. Treat every dependency by its own license; do not infer that an entire stack is BSD-licensed.
3. Keep community reference, provider-maintained fork, customer configuration, and experimental code as separate controlled layers.
4. Sell service outcomes and support boundaries, not unsupported industrial autonomy claims.
"""))

    write(CASE3 / "BUSINESS_CASE.md", document(
        "Business Case - Open-Source Quadruped RaaS Productization",
        """
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
"""))

    write(CASE3 / "BASIS_OF_ESTIMATE_AND_SENSITIVITY.md", document(
        "Basis of Estimate and Sensitivity - OpenQuad RaaS",
        """
## Material inputs

**Table 1. Decision inputs and replacement evidence - Evidence and confidence shown per row**

| Input | Base | Evidence / confidence | Required replacement |
|---|---:|---|---|
| Open hardware/software and Solo12 reference | Available under published repository licenses | [PB-H] | Release-specific legal review and retained notices |
| Glassdoor U.S. Robotics Software Engineer | $154,709/year or $74/hour; May 2026 | [PB-M] | Customer payroll/contract ledger and Finance approval |
| BLS private-industry compensation split | Wages 69.9%; benefits 30.1%; March 2026 | [PB-H] | Company-specific benefit and payroll burden |
| Loaded planning labor cost | $154,709 / 69.9% = $221,329 per FTE-year | [DC-M] | Approved employer labor model |
| Productization program | $2,397,234 rounded | [DC-L] from 7.0 FTE-years and [SA-L] allowances | Approved resource-loaded estimate and actuals |
| Unitree Go2 EDU list price comparator | $15,900 | [PB-M] | Product-specific binding BOM and supplier quote |
| Build/calibration/delivery | $24,000 per robot | [DC-L] | Supplier quotes, routings, yield, freight, tax, and warranty reserve |
| Direct 36-month service/cloud reserve | $12,672 per robot | [DC-L] | Observed cases, cloud bills, spares consumption, and repair history |
| Subscription decision price | $2,400 per robot-month | [DC-L] from 48-unit recovery target | Executed order and collection terms |
| Customer capacity | 1,000 hours per site-year | [SA-L] | Time study and approved work-redesign plan |
| Customer capacity value | $74 per hour | [PB-M] Glassdoor salary rate, not loaded cost | Customer payroll/contract ledger and Finance approval |

## Provider sensitivity

**Table 2. Provider 36-month sensitivity - Evidence: [DC-L] derived from mixed inputs; Confidence: low overall**

| Case | Monthly price | Direct 3-year cost | Contribution including allocated onboarding | Units to recover $2.397M | Decision |
|---|---:|---:|---:|---:|---|
| Base | $2,400 | $36,672 | $50,498 | 48 | Conditional pass; $26,670 cohort buffer |
| Price -10% | $2,160 | $36,672 | $41,858 | 58 | Fails 48-unit cohort |
| Service cost +50% | $2,400 | $43,008 | $44,162 | 55 | Fails 48-unit cohort |
| Build cost +25% | $2,400 | $42,672 | $44,498 | 54 | Fails 48-unit cohort |
| Price -10% and service +50% | $2,160 | $43,008 | $35,522 | 68 | Stop / redesign |

## Customer sensitivity

**Table 3. Customer two-robot value sensitivity - Evidence: [DC-L] from [PB-M]/[SA-L] inputs; Confidence: low overall**

| Released hours per year | Salary value/hour | Three-year gross capacity value | Net value vs. $184,800 TCO | Result |
|---:|---:|---:|---:|---|
| 1,200 | $74 | $266,400 | $81,600 | 44.2% ROI |
| 1,000 | $74 | $222,000 | $37,200 | 20.1% ROI; passes 15% gate |
| 900 | $74 | $199,800 | $15,000 | 8.1% ROI; below gate |
| 800 | $74 | $177,600 | ($7,200) | Fails |
| 1,000 | $60 | $180,000 | ($4,800) | Fails |

The case is intentionally easy to fail. A correct calculation does not raise the confidence of its assumed inputs.
"""))

    write(CASE3 / "RESEARCH_AND_ASSUMPTIONS.md", document(
        "Research and Assumptions - Open-Source Quadruped Productization",
        """
## Public anchors

**Table 1. Public source register - Evidence: public benchmarks [PB-H]/[PB-M]; Confidence: high/medium by row**

| Topic | Source | Portfolio use | Limitation |
|---|---|---|---|
| Open Dynamic Robot Initiative | https://open-dynamic-robot-initiative.github.io/ | Confirms open hardware/software objective and BSD 3-Clause statement | Does not approve this product or its commercial claims |
| Solo12 hardware | https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/quadruped_robot_12dof_v1/README.md | Confirms 12 active degrees of freedom and documented build components | Reference design, not a provider BOM or quote |
| Autonomy upgrade | https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/quadruped_robot_12dof_v1.1/README.md | Supports battery, wireless, e-stop, monitoring, and payload-interface feasibility screening | Prototype documentation; production verification still required |
| Solo low-level interface | https://github.com/open-dynamic-robot-initiative/solo | Confirms a BSD-3-Clause repository and low-level interface | Every transitive dependency needs its own review |
| Solo configuration files | https://github.com/open-dynamic-robot-initiative/robot_properties_solo | Confirms configuration resources and BSD-3-Clause repository | Does not establish provider configuration correctness |
| Master Board | https://github.com/open-dynamic-robot-initiative/master-board | Confirms board function and BSD-2-Clause repository | Hardware availability and lifecycle are [UPV] |
| Secure Software Development Framework | https://csrc.nist.gov/pubs/sp/800/218/final | Secure development and supplier communication structure | Guidance, not product certification |
| 2026 SBOM minimum elements | https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom | Release SBOM content baseline | Legal/security review still required |
| PAL Robotics Solo12 status | https://solo.pal-robotics.com/solo | Confirms commercial Solo12 sales are discontinued | Treats the reference as an obsolescence/supply-chain gate, not a purchasable product |
| Unitree Go2 EDU | https://www.unitree-robot.com/shop/products/unitree-go2 | Current $15,900 official research/developer quadruped comparator | Different platform and configuration; not a Solo12 quote or endorsed substitute [PB-M] |
| Glassdoor U.S. Robotics Software Engineer salary | https://www.glassdoor.com/Salaries/gyor-robotics-software-engineer-salary-SRCH_IL.0%2C4_KO5%2C31.htm | $154,709/year or $74/hour average, 435 salaries, as of May 2026 | Crowdsourced/model-based benchmark; not customer payroll or fully loaded labor [PB-M] |
| BLS Employer Costs for Employee Compensation | https://www.bls.gov/charts/employer-costs-for-employee-compensation/costs-by-industry.htm | March 2026 private-industry split: wages 69.9%, benefits 30.1% | Aggregate load factor; not company-specific [PB-H] |

Research checked 2026-08-24.

## Scenario assumptions

Six pilot sites, 12 robots, 60 days, 48-hour eligible advance replacement, 7.0 FTE-years, 50 configuration/calibration hours per robot, a $4,400 unit allowance, 36 service hours per robot-year, $600 annual cloud cost, a 12% spares/warranty reserve, $1,500 onboarding travel/materials, a $6,000 customer network allowance, 1,000 released customer hours per year, a 48-robot recovery cohort, and the resulting $2,400 subscription decision price are [SA-L]. Glassdoor, BLS, and Unitree provide anchors; they do not validate these quantities or conversion volume.

## Open unknowns

Supplier quotations, export/import treatment, battery transport, insurance, customer data terms, product liability, accessibility, independent safety review, component obsolescence, support demand, repair yield, warranty reserve, churn, collections, and actual conversion volume are [UPV] and must close before General Availability.
"""))

    write(CASE3 / "OPEN_SOURCE_COMPLIANCE_AND_SBOM.md", document(
        "Open-Source Compliance and SBOM Plan",
        """
## Control objective

Ship a reproducible commercial service while preserving every applicable copyright notice, license condition, source/binary redistribution obligation, security record, and non-endorsement boundary. "Open source" is not treated as a single license or as permission to ignore third-party dependencies.

## Release controls

**Table 1. Open-source release controls - Evidence: control design [SA-L], source statements [PB-H]; Confidence: low/high by row**

| Control | Owner | Gate evidence |
|---|---|---|
| Approved component and license inventory | Product Security | SBOM, component hash, version, supplier, license, relationship, and generation context |
| Copyright and notice preservation | Legal / Release Manager | Binary notice bundle and source-offer decision where applicable |
| Upstream-to-fork traceability | Software Lead | Upstream commit, provider patch set, customer configuration, and signed release tag |
| Dependency exception | Architecture Review Board | Written disposition before merge or shipment |
| Vulnerability intake and response | Product Security | Advisory intake, severity, affected releases, mitigation, and customer notice |
| Reproducible build | Release Engineering | Clean build from pinned sources and retained artifacts |
| No endorsement claim | Product / Legal | Approved name, attribution, and marketing review |

## Minimum release packet

Each release contains the signed image, hardware/configuration manifest, SBOM, license and notice bundle, build provenance, known issues, security fixes, calibration version, rollback target, test result, change approval, and customer-facing release note. CISA's 2026 SBOM minimum-elements publication and NIST Secure Software Development Framework are planning references, not certifications.
"""))

    write(CASE3 / "RAAS_SERVICE_DESIGN.md", document(
        "RaaS Service Design - OpenQuad Managed Lab",
        """
## Service boundary

The provider owns the serialized base unit, supported release, remote diagnosis, replacement pool, repair workflow, release notices, and service reporting. The customer owns safe laboratory access, experiment code, fixtures, local network approval, trained operators, incident notification, and data-retention choices.

## Service levels

**Table 1. Planning service levels - Evidence: scenario assumptions [SA-L]; Confidence: low**

| Service | Target | Measurement | Exclusion |
|---|---|---|---|
| Severity 1 acknowledgment | 30 minutes, 24x7 | Case timestamps | Customer network or unsafe site |
| Severity 2 acknowledgment | 4 business hours | Case timestamps | Unsupported fork/configuration |
| Eligible advance replacement | Ship within 48 hours, 95% | Dispatch records | Customs, force majeure, misuse |
| Fleet availability | At least 95% monthly | Entitled scheduled hours | Planned maintenance and customer hold |
| Release notice | 10 business days before standard deployment | Notice audit | Emergency security release |
| Data export after term | Within 10 business days | Export receipt | Legally retained security/audit records |

## Service acceptance

Before revenue recognition, the asset/entitlement record, customer admins, approved network path, data settings, emergency contacts, training completion, spare eligibility, test mission, and support drill must all be complete.
"""))

    write(CASE3 / "CUSTOMER_DISCOVERY_PLAN.md", document(
        "Customer Discovery Plan - Managed Research Quadrupeds",
        """
## Discovery objective

Determine whether customers value reproducibility and support enough to choose a term service over self-managed builds, and identify the narrow release that can be supported without absorbing arbitrary research forks.

## Interview and evidence plan

**Table 1. Discovery questions and decision evidence - Evidence: scenario plan [SA-L]; Confidence: low**

| Hypothesis | Question / observation | Evidence required | Decision |
|---|---|---|---|
| Build/calibration consumes material engineering time | Walk through the last robot build and recovery | Time records, defects, rework, and delays | Quantify addressable capacity |
| Configuration drift causes irreproducible experiments | Compare images, dependencies, and calibration files | Version manifests and failed reruns | Define supported baseline |
| Advance replacement has value | Review downtime and spare strategy | Downtime log and experiment schedule | Set swap entitlement |
| Security/procurement needs provenance | Observe review artifacts | SBOM, licenses, access, retention, and terms | Define release packet |
| Subscription can fit funding cycles | Test 12-, 24-, and 36-month terms | Budget authority and approval path | Set price/term gate |

The team must conduct at least 20 interviews across investigators, lab engineers, IT/security, procurement, and finance; observe five build/recovery workflows; and obtain nonbinding demand evidence before pilot authorization. Interview enthusiasm is not counted as contracted demand.
"""))

    write(CASE3 / "NPI_STAGE_GATE_PLAN.md", document(
        "NPI Stage-Gate Plan - OpenQuad RaaS",
        """
**Table 1. Productization stage gates - Evidence: scenario governance design [SA-L]; Confidence: low**

| Gate | Month | Required evidence | Exit decision |
|---|---:|---|---|
| G0 Problem / market | 1 | Discovery evidence, operating envelope, demand hypotheses | Fund concept only |
| G1 Architecture / license | 3 | System boundary, fork strategy, license inventory, initial hazard analysis | Authorize engineering build |
| G2 Engineering verification | 6 | Reproducible build, e-stop, battery, compute, telemetry, calibration, service diagnostics | Authorize pilot build |
| G3 Production validation | 8 | Work instructions, fixture capability, first-pass yield, serialized configuration, supplier readiness | Authorize customer pilot |
| G4 Pilot readiness | 9 | Six sites ready, contracts, training, support, spares, data/security approval | Start 60-day pilot |
| G5 Limited availability | 12 | Pilot acceptance, economics, 48-unit demand evidence, open risks, handoff | Approve / hold / stop |
| G6 General Availability | Post-launch | 41 contracted units, cost actuals, service capacity, second sources, independent compliance review | Scale or redesign |

Gate owners can hold or stop the program. Schedule pressure cannot waive safety, license, security, or customer-contract requirements.
"""))

    write(CASE3 / "PRODUCT_ROADMAP.md", document(
        "Product Roadmap - OpenQuad Managed Lab",
        """
**Table 1. Twelve-month roadmap - Evidence: scenario schedule [SA-L]; Confidence: low**

| Horizon | Product | Platform / security | Operations / commercial |
|---|---|---|---|
| Months 1-3 | User/problem fit and operating envelope | Upstream inventory, fork policy, threat model | Supplier screen and term/pricing tests |
| Months 4-6 | Alpha units and reference experiments | Signed image, SBOM pipeline, telemetry schema | Assembly routing, repair levels, service catalog |
| Months 7-8 | Production-validation units | Update/rollback, access, retention, release evidence | Fixtures, calibration, spares, entitlement records |
| Months 9-10 | Six-site / 12-robot pilot | Staged release and incident drill | Onboarding, support, swap, weekly benefit measurement |
| Months 11-12 | Corrected release candidate | Compliance closure and reproducible build | Limited-availability offer and 48-unit cohort plan |
| Post-launch | Supported experiment packs | Security maintenance and upstream intake | Unit economics, second sources, General Availability gate |

The roadmap intentionally excludes public autonomy, industrial safety claims, and arbitrary customer forks from Release 1.
"""))

    write(CASE3 / "VERIFICATION_VALIDATION.md", document(
        "Verification and Validation - OpenQuad RaaS",
        """
## Evidence strategy

Verification proves the product was built to its controlled requirements. Validation proves the supported service solves the disclosed customer problem within the laboratory envelope.

**Table 1. Release verification and pilot validation - Evidence: scenario plan/results [SA-L]; Confidence: low**

| Layer | Test | Threshold | Fictional closeout |
|---|---|---|---|
| Build | Clean rebuild from pinned source and artifacts | 12 of 12 units | Pass |
| Compliance | Component, license, hash, notice, and relationship completeness | 100% | Pass |
| Safety | E-stop, battery fault, comms loss, recovery authorization | 100% witnessed | Pass |
| Configuration | Serial, hardware revision, calibration, image, customer assignment | 100% | Pass |
| Reliability | 500-hour mixed lab endurance across pilot fleet | No unresolved critical failure | Pass after fan-duct correction |
| Service | Eligible advance replacement | At least 95% within 48 hours | 7 of 7 pass |
| Availability | Entitled scheduled time | At least 95% | 95.6% |
| Customer workflow | Scheduled experiment completion | At least 97% | 97.8% |
| Release | Signed update and rollback | 12 of 12 units | Pass |

MuJoCo validates only that the portfolio's generic demonstration model compiles and its scripted states render. It does not validate Solo12 dynamics, product safety, control quality, or commercial performance.
"""))

    write(CASE3 / "SUPPLIER_MANUFACTURING_READINESS.md", document(
        "Supplier and Manufacturing Readiness - OpenQuad RaaS",
        """
**Table 1. Production-readiness controls - Evidence: scenario controls [SA-L]; Confidence: low**

| Area | Release control | Gate |
|---|---|---|
| Bill of materials | Approved manufacturer part number, revision, alternates, license/provenance, lifecycle | 100% released items |
| Incoming quality | Motor, encoder, board, battery, fastener, and printed-part checks | Sampling and critical 100% checks approved |
| Assembly | Versioned traveler, torque record, wiring inspection, and serialized build | No unsigned traveler |
| Calibration | Fixture version, operator, result, and retest record | 100% pass before burn-in |
| Functional test | Joint, e-stop, battery, wireless, telemetry, thermal, and recovery sequence | 100% pass |
| Yield | First-pass yield at production validation | At least 90% |
| Supply risk | Two electronics assemblies have qualified second sources | Required before General Availability |
| Repair | Module-level diagnosis, quarantine, failure analysis, and return-to-stock criteria | Service readiness approval |

The provider does not claim that an open design eliminates manufacturing engineering, quality control, warranty reserve, or component-lifecycle risk.
"""))

    write(CASE3 / "RELIABILITY_SERVICEABILITY_PLAN.md", document(
        "Reliability and Serviceability Plan - OpenQuad RaaS",
        """
**Table 1. Reliability and serviceability measures - Evidence: scenario targets [SA-L]; Confidence: low**

| Measure | Target | Trigger / action |
|---|---:|---|
| Fleet availability | >=95% | Weekly problem review below target |
| Mean time to diagnose eligible remote cases | <=4 business hours | Evidence-template or observability correction |
| Advance replacement shipped | >=95% within 48 hours | Increase pool or correct dispatch process |
| Repeat failure within 30 days | <=5% | Problem record and engineering corrective action |
| First-pass production yield | >=90% | Containment and process capability review |
| Golden-image reproducibility | 100% | Release hold |
| SBOM/license record completeness | 100% | Shipment hold |

The service team maintains serialized spare state, calibration currency, battery history, failure code, returned-unit quarantine, root cause, corrective action, and return-to-stock evidence.
"""))

    write(CASE3 / "COMMERCIAL_LAUNCH_PLAN.md", document(
        "Commercial Launch Plan - OpenQuad RaaS",
        """
## Offer

The limited-availability offer is a two-robot, 36-month supervised-lab subscription with onboarding, supported release images, SBOM/license packet, remote diagnosis, standard maintenance, advance-replacement eligibility, and quarterly service review.

**Table 1. Launch evidence and claims controls - Evidence: scenario plan [SA-L]; Confidence: low**

| Workstream | Deliverable | Claim boundary |
|---|---|---|
| Product marketing | Operating envelope, inclusions, exclusions, demo | No industrial-autonomy or safety-certification claim |
| Sales engineering | Site and network qualification | No commitment before readiness review |
| Legal / compliance | Order form, open-source notices, data terms, support exclusions | No upstream endorsement implication |
| Finance | Price floor, customer ceiling, cohort break-even, collections | No margin claim from contribution model |
| Customer success | Onboarding, adoption, experiment plan, quarterly review | Capacity value is not cash savings |
| Service | Entitlement, spares, escalation, release and end-of-term process | Unsupported forks are excluded |

General Availability requires 41 contracted robots and provider capacity for the 48-unit cohort without weakening service, license, safety, or release controls.
"""))

    write(CASE3 / "FIRST_CUSTOMER_LAUNCH.md", document(
        "First Customer Launch - OpenQuad RaaS",
        """
## Launch pattern

The first customer receives two serialized robots in an access-controlled laboratory. The provider and customer complete network approval, data settings, operator training, emergency response, baseline experiment, update/rollback, support-case, and replacement drills before the 60-day acceptance clock begins.

**Table 1. First-customer acceptance - Evidence: fictional pilot results [SA-L]; Confidence: low**

| Acceptance item | Target | Result | Disposition |
|---|---:|---:|---|
| Scheduled experiment completion | >=97% | 97.8% | Accepted |
| Fleet availability | >=95% | 95.6% | Accepted |
| Golden-image rebuild | 2 of 2 | 2 of 2 | Accepted |
| E-stop, network-loss, and authorized recovery | 100% | 18 of 18 | Accepted |
| Eligible replacement dispatch | <=48 hours | 31 hours | Accepted |
| SBOM and notice packet | Complete | Complete | Accepted |
| Critical open defects | 0 | 0 | Accepted |

One fan-duct thermal issue was corrected and regression-tested before acceptance. The correction, affected serials, work instruction, verification, and release note remain linked.
"""))

    write(CASE3 / "WEEKLY_STATUS_REPORT.md", document(
        "Weekly Status Report - OpenQuad Productization Closeout",
        """
**Overall health: Amber.** Limited availability is accepted; General Availability remains gated by volume, second sources, and cost evidence.

**Table 1. Executive status - Evidence: fictional closeout status [SA-L]; Confidence: low**

| Dimension | Status | Evidence / next action |
|---|---|---|
| Scope | Green | Supervised-lab Release 1 accepted; industrial/public uses excluded |
| Schedule | Green | Month-12 gate completed after 60-day pilot |
| Budget | Green | $2.397M model reconciled to Glassdoor/BLS labor anchors and disclosed allowances |
| Quality | Green | Acceptance and release-image gates passed |
| Supply | Amber | Two electronics second sources due before General Availability |
| Commercial | Amber | 48-unit demand hypothesis; executed 41-unit minimum still [UPV] |
| Service | Green | Seven of seven eligible swaps shipped within 48 hours |
| Compliance | Amber | Release packet passed internal review; independent legal review remains [UPV] |
"""))

    write(CASE3 / "CLOSEOUT_AND_LESSONS.md", document(
        "Closeout and Lessons - OpenQuad RaaS Productization",
        """
## Closeout decision

Limited availability is approved for the supervised indoor laboratory envelope. General Availability is held until 41 subscribing robots are contracted, two electronics second sources are qualified, actual unit/service costs replace assumptions, and independent license/security review closes.

## Accepted evidence

**Table 1. Closeout evidence - Evidence: fictional scenario results [SA-L]; Confidence: low**

| Area | Evidence | Status |
|---|---|---|
| Product | Controlled hardware, calibration, image, and operating envelope | Accepted |
| Compliance | SBOM, license/notice bundle, provenance, signed build | Accepted internally; independent review open |
| Pilot | 12 units, six sites, 60 days, 97.8% completion, 95.6% availability | Accepted |
| Service | Entitlements, cases, diagnostics, spares, and seven eligible replacements | Accepted |
| Financial | Provider and customer sensitivity with explicit failure cases | Accepted as planning model only |
| Scale | 41-unit break-even and 48-unit cohort capacity | Conditional / not yet authorized |

## Lessons

1. An open reference reduces access friction; it does not remove product, manufacturing, safety, support, security, or commercial work.
2. Product boundaries protect service economics. Supporting arbitrary forks would destroy reproducibility and capacity.
3. License notices, SBOMs, build provenance, and vulnerability response are release deliverables, not legal paperwork added at the end.
4. Contribution is not margin, and released engineering capacity is not automatically cash savings.
5. A limited-availability decision can be correct even when General Availability remains held.
"""))

    write(CASE3 / "ARTIFACT_INDEX.md", document(
        "Artifact Index - Open-Source Quadruped RaaS Productization",
        """
This package connects open-source intake, product definition, engineering, manufacturing, service, customer acceptance, and RaaS economics.

**Table 1. Case 03 artifact package - Evidence: repository inventory [DC-H]; Confidence: high**

| Lifecycle | Artifact | Decision supported |
|---|---|---|
| Discover | CASE_STUDY.md / CUSTOMER_DISCOVERY_PLAN.md | Problem, customer, and boundary |
| Define | PRODUCT_BRIEF_AND_PRD.md | Product and measurable requirements |
| Govern | OPEN_SOURCE_COMPLIANCE_AND_SBOM.md / NPI_STAGE_GATE_PLAN.md | License, security, and release gates |
| Plan | PRODUCT_ROADMAP.md / SCHEDULE.csv / RACI.csv / RAID.csv | Integrated delivery control |
| Fund | BUSINESS_CASE.md / BASIS_OF_ESTIMATE_AND_SENSITIVITY.md / BUDGET_AND_HEADCOUNT.csv / OPENQUAD_RAAS_FINANCIAL_MODEL.xlsx | Provider and customer decision economics with formula-based workbook |
| Build | SUPPLIER_MANUFACTURING_READINESS.md / RELIABILITY_SERVICEABILITY_PLAN.md | Repeatable unit and service readiness |
| Validate | SYSTEM_REQUIREMENTS_TRACEABILITY.csv / VERIFICATION_VALIDATION.md | Traceable test and acceptance |
| Launch | RAAS_SERVICE_DESIGN.md / COMMERCIAL_LAUNCH_PLAN.md / FIRST_CUSTOMER_LAUNCH.md | Contract, onboarding, service, and customer gate |
| Close | WEEKLY_STATUS_REPORT.md / CLOSEOUT_AND_LESSONS.md | Formal decision, handoff, and held scale conditions |
"""))


def build_case3_csvs() -> None:
    write_csv(CASE3 / "BUDGET_AND_HEADCOUNT.csv",
        ["table_title", "cost_category", "amount_usd", "primary_capacity", "evidence_class", "confidence", "source_or_validation"],
        [
            {"table_title":"Case 03 productization budget","cost_category":"Program product systems compliance labor","amount_usd":331993.56,"primary_capacity":"1.5 FTE-years x $221,329 loaded planning cost","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Glassdoor May 2026 salary / BLS March 2026 wage share / staffing assumption"},
            {"table_title":"Case 03 productization budget","cost_category":"Hardware reliability and safety labor","amount_usd":331993.56,"primary_capacity":"1.5 FTE-years x $221,329 loaded planning cost","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Glassdoor May 2026 salary / BLS March 2026 wage share / staffing assumption"},
            {"table_title":"Case 03 productization budget","cost_category":"Software security and release labor","amount_usd":442658.08,"primary_capacity":"2.0 FTE-years x $221,329 loaded planning cost","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Glassdoor May 2026 salary / BLS March 2026 wage share / staffing assumption"},
            {"table_title":"Case 03 productization budget","cost_category":"Manufacturing and quality labor","amount_usd":221329.04,"primary_capacity":"1.0 FTE-year x $221,329 loaded planning cost","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Glassdoor May 2026 salary / BLS March 2026 wage share / staffing assumption"},
            {"table_title":"Case 03 productization budget","cost_category":"Service and customer operations labor","amount_usd":221329.05,"primary_capacity":"1.0 FTE-year x $221,329 loaded planning cost","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Glassdoor May 2026 salary / BLS March 2026 wage share / staffing assumption"},
            {"table_title":"Case 03 productization budget","cost_category":"Twelve pilot units","amount_usd":288000,"primary_capacity":"$24,000 modeled direct cost x 12","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Unitree comparator plus assumed labor and unit allowance; replace with binding BOM"},
            {"table_title":"Case 03 productization budget","cost_category":"Fixtures and laboratory equipment","amount_usd":120000,"primary_capacity":"Scenario allowance","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Binding equipment and fixture quotes"},
            {"table_title":"Case 03 productization budget","cost_category":"External safety legal and insurance","amount_usd":150000,"primary_capacity":"Scenario allowance","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Binding proposals and insurance terms"},
            {"table_title":"Case 03 productization budget","cost_category":"Cloud data and pilot operations","amount_usd":72000,"primary_capacity":"Scenario allowance","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Cloud bills and operating plan"},
            {"table_title":"Case 03 productization budget","cost_category":"Management reserve","amount_usd":217930.33,"primary_capacity":"10% of $2,179,303.29 subtotal","evidence_class":"Derived calculation","confidence":"Low","source_or_validation":"Risk-priced estimate and sponsor approval"},
        ])

    write_csv(CASE3 / "SCHEDULE.csv",
        ["table_title","id","phase","start_month","end_month","exit_gate","owner","status","evidence_class","confidence","source_or_validation"],
        [
            {"table_title":"Case 03 integrated schedule","id":"S-01","phase":"Discovery and operating envelope","start_month":1,"end_month":2,"exit_gate":"G0","owner":"Product","status":"Complete","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Approved integrated baseline"},
            {"table_title":"Case 03 integrated schedule","id":"S-02","phase":"Architecture license and hazard baseline","start_month":2,"end_month":3,"exit_gate":"G1","owner":"Systems / Legal","status":"Complete","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Gate record"},
            {"table_title":"Case 03 integrated schedule","id":"S-03","phase":"Alpha hardware and platform","start_month":3,"end_month":6,"exit_gate":"G2","owner":"Engineering","status":"Complete","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Engineering plan and results"},
            {"table_title":"Case 03 integrated schedule","id":"S-04","phase":"Manufacturing and service readiness","start_month":5,"end_month":8,"exit_gate":"G3","owner":"Operations","status":"Complete","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Readiness audit"},
            {"table_title":"Case 03 integrated schedule","id":"S-05","phase":"Pilot site onboarding","start_month":7,"end_month":9,"exit_gate":"G4","owner":"Customer Success","status":"Complete","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Site checklist and contracts"},
            {"table_title":"Case 03 integrated schedule","id":"S-06","phase":"Six-site 60-day pilot","start_month":9,"end_month":11,"exit_gate":"Pilot acceptance","owner":"Program Manager","status":"Complete","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional pilot evidence"},
            {"table_title":"Case 03 integrated schedule","id":"S-07","phase":"Corrections and release candidate","start_month":11,"end_month":12,"exit_gate":"G5","owner":"Engineering / Quality","status":"Complete","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional closeout record"},
            {"table_title":"Case 03 integrated schedule","id":"S-08","phase":"General Availability scale gate","start_month":13,"end_month":15,"exit_gate":"G6","owner":"Executive Sponsor","status":"Held","evidence_class":"Unknown / pending validation","confidence":"Open","source_or_validation":"48 executed unit commitments at or above price floor and actual cost evidence"},
        ])

    write_csv(CASE3 / "RACI.csv",
        ["table_title","deliverable_or_decision","Executive Sponsor","Productization Program Manager","Product and Systems","Engineering and Security","Manufacturing and Quality","Service and Customer Success","Legal and Finance","evidence_class","confidence","source_or_validation"],
        [
            {"table_title":"Case 03 responsibility matrix","deliverable_or_decision":"Operating envelope and PRD","Executive Sponsor":"I","Productization Program Manager":"A","Product and Systems":"R","Engineering and Security":"C","Manufacturing and Quality":"C","Service and Customer Success":"C","Legal and Finance":"C","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Sponsor-approved organization"},
            {"table_title":"Case 03 responsibility matrix","deliverable_or_decision":"Open-source compliance and release SBOM","Executive Sponsor":"I","Productization Program Manager":"A","Product and Systems":"C","Engineering and Security":"R","Manufacturing and Quality":"C","Service and Customer Success":"I","Legal and Finance":"R","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Named accountable owners"},
            {"table_title":"Case 03 responsibility matrix","deliverable_or_decision":"Production validation and release","Executive Sponsor":"I","Productization Program Manager":"A","Product and Systems":"C","Engineering and Security":"R","Manufacturing and Quality":"R","Service and Customer Success":"C","Legal and Finance":"C","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Gate charter"},
            {"table_title":"Case 03 responsibility matrix","deliverable_or_decision":"Pilot acceptance","Executive Sponsor":"I","Productization Program Manager":"A","Product and Systems":"C","Engineering and Security":"C","Manufacturing and Quality":"C","Service and Customer Success":"R","Legal and Finance":"I","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Executed acceptance plan"},
            {"table_title":"Case 03 responsibility matrix","deliverable_or_decision":"Limited Availability / General Availability","Executive Sponsor":"A","Productization Program Manager":"R","Product and Systems":"C","Engineering and Security":"C","Manufacturing and Quality":"C","Service and Customer Success":"C","Legal and Finance":"C","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Executive governance"},
        ])

    write_csv(CASE3 / "RAID.csv",
        ["table_title","id","type","statement","probability_1_5","impact_1_5","score","owner","response","trigger","closeout_status","evidence_class","confidence","source_or_validation"],
        [
            {"table_title":"Case 03 RAID register","id":"R-001","type":"Risk","statement":"A transitive dependency has incompatible or unrecorded terms","probability_1_5":3,"impact_1_5":5,"score":15,"owner":"Legal / Product Security","response":"Dependency-level inventory, exception gate, notice bundle","trigger":"Unknown license or missing provenance","closeout_status":"Transferred to release control","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Independent review"},
            {"table_title":"Case 03 RAID register","id":"R-002","type":"Risk","statement":"Customer forks destroy reproducibility and service capacity","probability_1_5":4,"impact_1_5":5,"score":20,"owner":"Product / Service","response":"Supported baseline and explicit fork exclusion","trigger":"Unapproved image or configuration","closeout_status":"Closed by service boundary","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Pilot case evidence"},
            {"table_title":"Case 03 RAID register","id":"R-003","type":"Risk","statement":"Discontinued Solo12 sales and electronics obsolescence delay the 48-unit cohort","probability_1_5":4,"impact_1_5":4,"score":16,"owner":"Supply Chain","response":"Treat Solo12 as a reference only; qualify supported architecture and two second sources","trigger":"No supportable BOM or lead time above 16 weeks","closeout_status":"Open General Availability gate","evidence_class":"Public benchmark plus scenario response","confidence":"Low","source_or_validation":"PAL Robotics discontinued-sales notice and supplier commitments"},
            {"table_title":"Case 03 RAID register","id":"R-004","type":"Risk","statement":"Research users infer industrial safety or public autonomy","probability_1_5":3,"impact_1_5":5,"score":15,"owner":"Product / Legal","response":"Operating envelope, training, claims review, technical controls","trigger":"Out-of-scope sales request","closeout_status":"Transferred to operations","evidence_class":"Scenario assumption","confidence":"Medium","source_or_validation":"Contract and usage review"},
            {"table_title":"Case 03 RAID register","id":"R-005","type":"Risk","statement":"Price or service cost misses provider break-even","probability_1_5":4,"impact_1_5":5,"score":20,"owner":"Finance","response":"48-unit gate and downside sensitivity","trigger":"Price below $2,384.57 floor or direct 36-month cost above $36,672","closeout_status":"Open General Availability gate","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Executed orders and audited costs"},
        ])

    write_csv(CASE3 / "SYSTEM_REQUIREMENTS_TRACEABILITY.csv",
        ["table_title","requirement_id","stakeholder_need","system_requirement","verification","acceptance_threshold","gate","owner","status","evidence_class","confidence","source_or_validation"],
        [
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-001","stakeholder_need":"Reproducible platform","system_requirement":"Every unit has serialized hardware calibration and image records","verification":"Configuration audit","acceptance_threshold":"100%","gate":"G3","owner":"Quality","status":"Pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional pilot audit"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-002","stakeholder_need":"License transparency","system_requirement":"Every shipped component has provenance license hash and relationship","verification":"SBOM audit","acceptance_threshold":"100%","gate":"G5","owner":"Product Security","status":"Pass internal","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Independent legal review pending"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-003","stakeholder_need":"Safe supervised operation","system_requirement":"E-stop network-loss and authorized recovery states are deterministic","verification":"Fault injection","acceptance_threshold":"100% witnessed","gate":"G2/G4","owner":"Safety","status":"Pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional witnessed tests"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-004","stakeholder_need":"Controlled releases","system_requirement":"Updates are signed staged observable and reversible","verification":"Update and rollback","acceptance_threshold":"12 of 12 pilot units","gate":"G5","owner":"Release Engineering","status":"Pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional test record"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-005","stakeholder_need":"Experiment continuity","system_requirement":"Fleet availability supports scheduled entitled time","verification":"Telemetry analysis","acceptance_threshold":">=95%","gate":"Pilot","owner":"Service","status":"95.6% pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional 60-day pilot"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-006","stakeholder_need":"Fast recovery","system_requirement":"Eligible replacement ships within 48 hours","verification":"Case/dispatch audit","acceptance_threshold":">=95%","gate":"Pilot","owner":"Service","status":"7 of 7 pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional pilot cases"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-007","stakeholder_need":"Data control","system_requirement":"Customer-configured retention export and deletion are enforced","verification":"Policy and deletion test","acceptance_threshold":"100%","gate":"G4","owner":"Security / Customer","status":"Pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Executed data terms and test evidence"},
            {"table_title":"Case 03 system requirements traceability","requirement_id":"SYS-008","stakeholder_need":"Supportable variants","system_requirement":"Unsupported forks are detected and excluded from entitlement","verification":"Negative entitlement test","acceptance_threshold":"100%","gate":"G4","owner":"Service Platform","status":"Pass","evidence_class":"Scenario assumption","confidence":"Low","source_or_validation":"Fictional test record"},
        ])


def build_case3_dashboard() -> None:
    path = ROOT / "portfolio" / "scenario_dashboard_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    case = {
        "slug": "open-source-quadruped-raas-productization",
        "code": "CASE 03",
        "title": "Open-Source Quadruped to Supported RaaS",
        "client": "Northstar Applied Robotics Labs",
        "program_type": "Open-source productization and RaaS launch",
        "status": "Closed - limited availability approved; scale gate conditional",
        "health": "Amber",
        "role": "Productization Program Manager",
        "duration": "12 months plus 60-day pilot",
        "budget": "$2.397M modeled productization authorization",
        "tco": "$184.8K customer three-year RaaS TCO for two robots",
        "summary": "Convert the Open Dynamic Robot Initiative Solo12 research reference into a supported supervised-laboratory Robotics-as-a-Service offer. The provider adds controlled sourcing, assembly and calibration, battery and emergency-stop integration, signed images, Software Bill of Materials and license notices, telemetry, a replacement pool, onboarding, service levels, and release governance without claiming upstream endorsement or industrial certification.",
        "decision": "The six-site, 12-robot pilot passed the fictional reproducibility, safety-state, availability, experiment-completion, service, and open-source release gates. Limited availability is approved for the controlled laboratory envelope. General Availability remains held until at least 48 robots are contracted at or above the $2,384.57 monthly price floor, two electronics second sources are qualified, and customer time studies, audited unit/service costs, and independent compliance review replace planning assumptions.",
        "metrics": [
            {"label":"Scheduled experiment completion","value":"97.8%","note":"Fictional 60-day pilot; target at least 97%","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
            {"label":"Fleet availability","value":"95.6%","note":"Fictional pilot; target at least 95%","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
            {"label":"Release-image reproducibility","value":"12 of 12","note":"Fictional clean-build and install tests","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
            {"label":"License / SBOM completeness","value":"100%","note":"Internal release audit; independent review still pending","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
            {"label":"Eligible advance replacements","value":"7 of 7","note":"Fictional dispatches shipped within 48 hours","state":"pass","evidence_class":"Scenario assumption","confidence":"Low"},
            {"label":"Provider break-even gate","value":"48 robots","note":"$2.397M / $50.498K contribution; omitted costs remain","state":"watch","evidence_class":"Derived calculation","confidence":"Low"}
        ],
        "phases": [
            {"name":"Discovery and operating envelope","start":1,"end":2,"status":"Complete"},
            {"name":"Architecture, license, and hazard baseline","start":2,"end":3,"status":"Complete"},
            {"name":"Alpha hardware and platform","start":3,"end":6,"status":"Complete"},
            {"name":"Manufacturing and service readiness","start":5,"end":8,"status":"Complete"},
            {"name":"Pilot site onboarding","start":7,"end":9,"status":"Complete"},
            {"name":"Six-site, 12-robot pilot","start":9,"end":11,"status":"Complete"},
            {"name":"Corrections and release candidate","start":11,"end":12,"status":"Complete"},
            {"name":"General Availability scale gate","start":12,"end":12,"status":"Held"}
        ],
        "timeline_unit":"Month","timeline_max":12,
        "financials": [
            {"label":"Productization investment","value":2397234,"display":"$2,397,234","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Two-robot customer three-year TCO","value":184800,"display":"$184,800","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Three-year subscription revenue per robot","value":86400,"display":"$86,400","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Contribution per robot including onboarding allocation","value":50498,"display":"$50,498","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Three-year customer capacity value","value":222000,"display":"$222,000","evidence_class":"Derived calculation","confidence":"Low"},
            {"label":"Customer net capacity value","value":37200,"display":"$37,200","evidence_class":"Derived calculation","confidence":"Low"}
        ],
        "financial_note":"Glassdoor's May 2026 U.S. Robotics Software Engineer benchmark is $154,709/year or $74/hour [PB-M]. BLS reports private-industry wages at 69.9% of compensation in March 2026 [PB-H], producing a $221,329 loaded planning cost before the fictional staffing mix [DC-M]. Unitree's official $15,900 Go2 EDU price is a current research-quadruped comparator [PB-M], not a Solo12 quote. The resulting $2.397M program, $24K unit cost, $12.672K 36-month service cost, $2,400 monthly price, 48-unit recovery gate, $184.8K two-robot TCO, and 20.1% customer ROI are [DC-L] because staffing, hours, allowances, utilization, and demand are [SA-L]. Executed contracts, customer time studies, audited costs, and realized cash savings remain mandatory.",
        "risks": [
            {"id":"R-001","risk":"A dependency has incompatible or unrecorded terms","score":15,"status":"Controlled; independent review open","response":"Dependency-level SBOM, notices, exception gate, and release hold"},
            {"id":"R-002","risk":"Customer forks destroy reproducibility and service capacity","score":20,"status":"Closed by service boundary","response":"Supported baseline, entitlement checks, and explicit fork exclusion"},
            {"id":"R-003","risk":"Discontinued Solo12 sales and electronics obsolescence delay scale","score":16,"status":"Open General Availability gate","response":"Treat Solo12 as a reference only; qualify a supported architecture and two dated second sources"},
            {"id":"R-004","risk":"Users infer industrial safety or public autonomy","score":15,"status":"Transferred to operations","response":"Controlled lab envelope, training, claims review, and contract controls"},
            {"id":"R-005","risk":"Price, cost, or conversion volume misses break-even","score":20,"status":"Open General Availability gate","response":"48-unit minimum and downside sensitivity; stop if ranges do not overlap"}
        ],
        "team": [
            {"role":"Executive sponsor","accountability":"Funding tranches, Limited Availability, and General Availability decision"},
            {"role":"Productization Program Manager","accountability":"Integrated gates, economics, dependencies, suppliers, pilot, and handoff"},
            {"role":"Product and Systems","accountability":"Customer problem, operating envelope, requirements, and fork boundary"},
            {"role":"Engineering, Security, and Legal","accountability":"Design, verification, signed releases, SBOM, licenses, and vulnerabilities"},
            {"role":"Manufacturing, Quality, and Supply Chain","accountability":"BOM, assembly, calibration, yield, serialization, spares, and second sources"},
            {"role":"Service, Customer Success, Sales, and Finance","accountability":"Offer, onboarding, entitlements, swaps, adoption, price, and evidence"}
        ],
        "artifacts": [
            {"label":"Case study","path":"scenarios/03-open-source-quadruped-raas-productization/CASE_STUDY.md","category":"Executive"},
            {"label":"Product brief and requirements","path":"scenarios/03-open-source-quadruped-raas-productization/PRODUCT_BRIEF_AND_PRD.md","category":"Product"},
            {"label":"Business case","path":"scenarios/03-open-source-quadruped-raas-productization/BUSINESS_CASE.md","category":"Financial"},
            {"label":"Basis of estimate and sensitivity","path":"scenarios/03-open-source-quadruped-raas-productization/BASIS_OF_ESTIMATE_AND_SENSITIVITY.md","category":"Financial"},
            {"label":"Formula-based financial model","path":"scenarios/03-open-source-quadruped-raas-productization/OPENQUAD_RAAS_FINANCIAL_MODEL.xlsx","category":"Financial"},
            {"label":"Open-source compliance and SBOM","path":"scenarios/03-open-source-quadruped-raas-productization/OPEN_SOURCE_COMPLIANCE_AND_SBOM.md","category":"Governance"},
            {"label":"NPI stage-gate plan","path":"scenarios/03-open-source-quadruped-raas-productization/NPI_STAGE_GATE_PLAN.md","category":"Governance"},
            {"label":"Integrated schedule","path":"scenarios/03-open-source-quadruped-raas-productization/SCHEDULE.csv","category":"Control"},
            {"label":"Budget and headcount","path":"scenarios/03-open-source-quadruped-raas-productization/BUDGET_AND_HEADCOUNT.csv","category":"Financial"},
            {"label":"System requirements traceability","path":"scenarios/03-open-source-quadruped-raas-productization/SYSTEM_REQUIREMENTS_TRACEABILITY.csv","category":"Assurance"},
            {"label":"Verification and validation","path":"scenarios/03-open-source-quadruped-raas-productization/VERIFICATION_VALIDATION.md","category":"Assurance"},
            {"label":"RaaS service design","path":"scenarios/03-open-source-quadruped-raas-productization/RAAS_SERVICE_DESIGN.md","category":"Operate"},
            {"label":"Supplier and manufacturing readiness","path":"scenarios/03-open-source-quadruped-raas-productization/SUPPLIER_MANUFACTURING_READINESS.md","category":"Execution"},
            {"label":"First-customer launch","path":"scenarios/03-open-source-quadruped-raas-productization/FIRST_CUSTOMER_LAUNCH.md","category":"Execution"},
            {"label":"Closeout and lessons","path":"scenarios/03-open-source-quadruped-raas-productization/CLOSEOUT_AND_LESSONS.md","category":"Close"}
        ],
        "demo": {
            "type":"Model-compiled workflow animation",
            "title":"Open Quadruped RaaS Productization Workflow",
            "filename":"open-quadruped-raas-productization.mp4",
            "caption":"A generic workflow animation shows serialized intake, calibration, functional testing, fault-evidence capture, replacement-pool rotation, and service release. The separate generic XML model compiles and its deterministic state workflow passes; neither artifact is an Open Dynamic Robot Initiative digital twin or validation of Solo12 dynamics, safety, or performance.",
            "model_source":"simulations/open_quadruped_raas/README.md",
            "sequence":["Register source and serial","Calibrate the supported build","Run supervised functional test","Capture a controlled fault bundle","Rotate an eligible replacement","Stage the verified unit for service"]
        },
        "closure": {
            "schedule":"Completed at the month-12 Limited Availability gate after a 60-day pilot",
            "budget":"$2,397,234 modeled authorization reconciled to Glassdoor/BLS labor anchors and disclosed assumptions; actual market costs remain pending",
            "acceptance":["Twelve pilot units rebuilt from the approved release and passed configuration audit","Scheduled experiment completion reached 97.8% and fleet availability 95.6%","All emergency-stop, network-loss, update, rollback, and authorized-recovery tests passed","Seven of seven eligible advance replacements shipped within 48 hours","Internal SBOM and license-notice audit was complete; independent review remains a scale condition"],
            "lessons":["Open access is a starting point, not a finished product","Supported configuration boundaries protect reproducibility and service capacity","Contribution is not margin and capacity value is not automatic cash savings","Limited Availability can pass while General Availability remains correctly held"]
        }
    }
    data["scenarios"][2] = case
    support = data["scenarios"][3]
    support["demo"] = {
        "type": "Data workflow animation",
        "title": "Robotics Support Evidence-to-Restoration Workflow",
        "filename": "robotics-support-triage.mp4",
        "caption": "A data-workflow animation and deterministic Python lab show synthetic fleet-event intake, installed-product correlation, deduplication, human severity review, evidence packaging, remote-or-field action selection, and customer-confirmed closure. The support case uses no physics simulator and never authorizes a robot command.",
        "model_source": "tools/support-operations-lab/README.md",
        "sequence": ["Receive synthetic fleet event", "Correlate customer and installed product", "Assign severity with human review", "Package diagnostics and evidence", "Choose authorized restore or field dispatch", "Confirm service with the customer"],
    }
    security = data["scenarios"][1]
    security["financials"] = [
        {"label":"Installed cost","value":730250,"display":"$730,250","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Annual recurring cost","value":117000,"display":"$117,000","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Annual gross benefit","value":343500,"display":"$343,500","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Annual net benefit","value":226500,"display":"$226,500","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Five-year net benefit","value":402250,"display":"$402,250","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Five-year NPV at 8%","value":174099,"display":"$174,099","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Five-year break-even rover invoice","value":33.98,"display":"$33.98/hour","evidence_class":"Derived calculation","confidence":"Low"},
    ]
    security["financial_note"] = "The May 2025 U.S. Bureau of Labor Statistics national mean wage for security guards is $20.42 per hour [PB-H]; it is only a wage benchmark. The fictional $45 contractor invoice is 2.20 times that wage because it is assumed to include burden, supervision, insurance, overhead, and margin [SA-L]. With two 10-hour rover posts and a $15K vehicle, payback is 3.22 years, discounted payback is 3.88 years, and five-year Net Present Value at 8% is $174,099 [DC-L]. The five-year break-even invoice rate is $33.98/hour. At one removed post, payback is 11.73 years and the decision fails. Actual invoices, contract-change rights, routes, costs, and realized savings are [UPV]."
    airport = data["scenarios"][4]
    airport["financials"] = [
        {"label":"Pilot authorization","value":1874500,"display":"$1,874,500","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Pilot actual","value":1645000,"display":"$1,645,000","evidence_class":"Scenario assumption","confidence":"Low"},
        {"label":"Capital-path five-year TCO","value":3134500,"display":"$3,134,500","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Phase 1 annual capacity value","value":68985,"display":"$68,985","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Phase 2 five-year TCO","value":1270000,"display":"$1,270,000","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Phase 2 five-year net benefit","value":339650,"display":"$339,650","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Phase 2 NPV at 8%","value":241006,"display":"$241,006","evidence_class":"Derived calculation","confidence":"Low"},
        {"label":"Break-even productive fleet time","value":22.1,"display":"22.1 hours/day","evidence_class":"Derived calculation","confidence":"Low"},
    ]
    airport["financial_note"] = "The May 2025 U.S. Bureau of Labor Statistics national mean wage for janitors and cleaners is $18.64/hour [PB-H]. The airport's $31.50 loaded task rate is a fictional customer assumption [SA-L], not a BLS value. Phase 1 creates only $68,985 of annual capacity against a $3.1345M capital-path five-year TCO and fails. The separate Phase 2 RaaS case assumes 28 productive fleet-hours/day, $6K per robot-month, $150K integration, and $80K annual retained human support. It produces $339,650 five-year net benefit, 26.7% ROI, about $241,006 NPV at 8%, and 1.53-year simple payback [DC-L]. Break-even is 22.1 productive hours/day; at 22 hours the case is slightly negative, and at the public mean wage even 28 hours/day does not cover the modeled annual run cost. Capacity is not cash savings; workload, prices, performance, and realization remain [UPV]."
    for scenario in data["scenarios"]:
        for metric in scenario.get("metrics", []):
            metric.setdefault("evidence_class", "Scenario assumption")
            metric.setdefault("confidence", "Low")
        for item in scenario.get("financials", []):
            item.setdefault("evidence_class", "Derived calculation")
            item.setdefault("confidence", "Low")
        scenario.setdefault("demo", {}).setdefault("type", "MuJoCo operations visualization")
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    build_case3_documents()
    build_case3_csvs()
    build_case3_dashboard()
    print("Applied approved Case 03 rebuild and dashboard evidence labels.")


if __name__ == "__main__":
    main()
