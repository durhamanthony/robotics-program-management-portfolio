# Anthony Durham — Technology Program Management Portfolio

This is the public source repository for Anthony Durham's enterprise transformation and robotics program-management portfolio.

Public website: `https://durhamanthony.github.io/robotics-program-management-portfolio/`

## What visitors can review

The GitHub Pages website opens with five complete robotics operating scenarios:

1. Two humanoids piloted for employee-facing retail-backroom fulfillment in an unchanged legacy store.
2. Three quadrupeds deployed for human-supervised night security.
3. An open-source quadruped reference design productized as a supported, supervised Robotics-as-a-Service (RaaS) offer.
4. A robotics support and field-operations model for 250 robots at 60 sites.
5. Two humanoids piloted for controlled routine cleaning in four existing airport restrooms, governed from seller/integrator, manufacturer, and airport owner/operator perspectives.

Each scenario has an executive dashboard with scope, acceptance results, schedule, budget and Total Cost of Ownership (TCO), top risks, team accountability, browser-playable operations evidence, completed project artifacts, and formal closeout.

Below the robotics work, two enterprise transformation sections show additional real-world program leadership:

6. An anonymized M&A IT integration modeled in Agile and Predictive / Waterfall delivery, covering Day 1 onboarding, identity, network, collaboration-platform migration, application rationalization, cutover, hypercare, and closeout.
7. A 360-device, four-site hardware refresh modeled in Kanban, Scrum, Predictive / Waterfall, and Hybrid delivery, covering procurement, build, data and application readiness, deployment waves, security, asset custody, sanitization, service transition, and benefits.

The enterprise cases include six interactive dashboards, 100+ editable source artifacts, two polished field guides, and two formula-driven control workbooks. The M&A dashboards operate as five-workstream command centers, with executive status, accountable teams, next decisions, color/evidence legends, and sectioned plans and registers for onboarding, network/server/cloud infrastructure, collaboration platforms, application/data consolidation, and vendor/MSP governance. Company ABC and Company XYZ, project results, dates, quantities, and costs are explicitly labeled as fictional assumptions; verified experience and primary-source research are identified separately.

## Repository map

- `docs/` — generated GitHub Pages website.
- `scenarios/` — completed scenario documents and data.
- `portfolio/scenario_dashboard_data.json` — dashboard source data.
- `enterprise-programs/` — complete M&A and hardware-refresh playbooks, registers, templates, guides, and workbooks.
- `portfolio/enterprise_dashboard_data.json` — six enterprise-dashboard source models.
- `media/videos/` — four MuJoCo operations demonstrations plus productization and support workflow animations.
- `simulations/` — MuJoCo source for the four simulator-backed case studies, including the two-scene retail inbound-to-fulfillment story.
- `tools/` — robotics support data lab, tool research, and reference architecture.
- `pm-operating-system/` — reusable Word, Excel, CSV, and AI-assisted program-management tools.
- `quality-control/` — independent Claude and Grok review packages with manifests and response schemas.
- `governance/` — selected cross-program controls and the generated public artifact register.
- `scripts/` — repeatable site builder and privacy/link validator.

Internal career prompts, resume tailoring, publishing instructions, blank templates, local installation files, and working notes are intentionally maintained in a separate private repository.

## Scenario notice

These simulations and enterprise cases are fictitious generic scenarios for demonstration purposes only.

All company names, customer names, project results, and operational data within the scenarios are fictional. Public standards, vendor, and government references are identified in the source registers. Scenario cost inputs that require real procurement evidence are marked accordingly.

## Build and validation

The published site is already included in `docs/`. Maintainers can rebuild it with:

```text
python scripts/build_portfolio_site.py
python scripts/validate_portfolio.py
```

Visitors do not need Python, MuJoCo, Git, or a command line. The website renders every source artifact in the browser and provides the guides and workbooks as direct downloads.
