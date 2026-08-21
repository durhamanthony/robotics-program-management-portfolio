# Research and Assumptions — Airport Restroom Humanoid Pilot

## Evidence hierarchy

Public sources define safety and cleaning constraints. All airport names, volumes, costs, results, and benefit inputs below are fictional scenario data unless explicitly identified as a public benchmark. Robot procurement amounts are planning allowances, not vendor quotations.

## Public sources used

| Source | What it supports | Portfolio use |
|---|---|---|
| Centers for Disease Control and Prevention, *When and How to Clean and Disinfect a Facility*, April 16, 2024, https://www.cdc.gov/hygiene/about/when-and-how-to-clean-and-disinfect-a-facility.html | Clean high-touch surfaces regularly; clean before disinfecting; follow product directions; train and protect workers | Cleaning sequence, training, quality inspection, chemical controls |
| Centers for Disease Control and Prevention, *How to Prevent Norovirus*, January 13, 2025, https://www.cdc.gov/norovirus/prevention/index.html | Body-fluid events require immediate controlled cleanup; gloves and pathogen-appropriate disinfection | Human specialist exception path; robot does not autonomously remediate a body-fluid event |
| United States Environmental Protection Agency, *Registered Antimicrobial Products Effective Against Norovirus — List G*, current page reviewed August 2026, https://www.epa.gov/pesticide-registration/epas-registered-antimicrobial-products-effective-against-norovirus-feline | Product registration and wet contact time must match the label | Approved-chemical list, dwell-time requirement, material-compatibility test |
| Occupational Safety and Health Administration, *Hazard Communication*, 29 Code of Federal Regulations 1910.1200, https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1200 | Labels, Safety Data Sheets, chemical information, and training | Chemical custody, storage, robot refill procedure, responder training |
| Occupational Safety and Health Administration, *Bloodborne Pathogens — Overview*, https://www.osha.gov/bloodborne-pathogens/ | Employers determine exposure and use an exposure-control plan where occupational exposure exists | Sharps and visible-blood safe stop, site exposure determination, trained human response |
| United States Bureau of Labor Statistics, *Janitors and Building Cleaners*, May 2024 wage data, https://www.bls.gov/ooh/building-and-grounds-cleaning/janitors-and-building-cleaners.htm | National median wage was $17.27 per hour; work commonly includes variable shifts | External reasonableness check only; not used as a local airport quotation |

## Fictional airport baseline

| Input | Value | Evidence class | Owner / validation |
|---|---:|---|---|
| Pilot terminal | Terminal 4 | Scenario fact | Airport sponsor |
| Pilot restrooms | 4 | Scenario fact | Airport Facilities |
| Routine missions | 3 per restroom per day | Scenario planning input | Custodial time study |
| Pilot duration | 90 days | Approved plan | Steering committee |
| Scheduled missions | 4 × 3 × 90 = 1,080 | Derived | Project controls |
| Observed routine labor per mission | 0.50 labor-hour | Fictional pre-pilot time study | Airport Facilities; repeat before scale |
| Airport loaded labor rate | $31.50 per hour | Fictional customer input | Finance and Procurement |
| Annualized routine capacity | 4 × 3 × 365 × 0.50 = 2,190 hours | Derived | Benefits owner |
| Annualized capacity value | 2,190 × $31.50 = $68,985 | Derived, not cash savings | Finance |

The Bureau of Labor Statistics wage is a national wage benchmark, not a loaded airport cost. The scenario's $31.50 rate includes fictional benefits, shift premiums, and contractor overhead and must be replaced with the airport's actual payroll or contract data.

## Cost assumptions requiring quotation

| Cost input | Base | Low | High | Status |
|---|---:|---:|---:|---|
| Two humanoid robots and chargers | $500,000 | $300,000 | $700,000 | Request for Quotation required |
| Manufacturer application engineering | $220,000 | $150,000 | $320,000 | Statement of Work required |
| Integrator configuration and commissioning | $310,000 | $220,000 | $450,000 | Statement of Work required |
| Airport site, network, cybersecurity, and entry controls | $145,000 | $100,000 | $230,000 | Site design required |
| Independent safety and acceptance | $120,000 | $80,000 | $180,000 | Test proposal required |
| Training and operational change | $70,000 | $45,000 | $110,000 | Training plan required |
| Pilot support, spares, and consumables | $110,000 | $75,000 | $180,000 | Support quote required |
| Integrated program management | $155,000 | $120,000 | $230,000 | Resource plan required |

The direct-cost base is $1,630,000. A fifteen-percent uncertainty allowance of $244,500 creates a $1,874,500 pilot authorization. This is a planning envelope, not a market-price claim.

## Claim rules

- “Mission success” means the scripted routine scope completed and a telemetry record closed; it does not prove autonomous cleaning efficacy.
- “First-pass inspection” means an authorized custodian passed all twelve checklist points at first inspection.
- “Capacity released” is time available for other assigned work. It is not headcount reduction or cash savings.
- A passed pilot is not a scale approval, product certification, infection-control guarantee, or safety certification.
- Expansion requires actual quotations, site measurements, employee consultation, airport authority approval, and an updated hazard analysis.

