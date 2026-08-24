# Anthony Durham — Robotics Program Management Portfolio

This is the public source repository for Anthony Durham's robotics deployment, open-source productization, and service-operations portfolio.

Public website: `https://durhamanthony.github.io/robotics-program-management-portfolio/`

## What visitors can review

The GitHub Pages website opens with five complete operating scenarios:

1. Two humanoids piloted for employee-facing retail-backroom fulfillment in an unchanged legacy store.
2. Three quadrupeds deployed for human-supervised night security.
3. An open-source quadruped reference design productized as a supported, supervised Robotics-as-a-Service (RaaS) offer.
4. A robotics support and field-operations model for 250 robots at 60 sites.
5. Two humanoids piloted for controlled routine cleaning in four existing airport restrooms, governed from seller/integrator, manufacturer, and airport owner/operator perspectives.

Each scenario has an executive dashboard with scope, acceptance results, schedule, budget and Total Cost of Ownership (TCO), top risks, team accountability, browser-playable operations evidence, completed project artifacts, and formal closeout.

## Repository map

- `docs/` — generated GitHub Pages website.
- `scenarios/` — completed scenario documents and data.
- `portfolio/scenario_dashboard_data.json` — dashboard source data.
- `media/videos/` — four MuJoCo operations demonstrations plus productization and support workflow animations.
- `simulations/` — MuJoCo source for the four simulator-backed case studies, including the two-scene retail inbound-to-fulfillment story.
- `tools/` — robotics support data lab, tool research, and reference architecture.
- `pm-operating-system/` — reusable Word, Excel, CSV, and AI-assisted program-management tools.
- `quality-control/` — independent Claude and Grok review packages with manifests and response schemas.
- `governance/` — selected cross-program controls and the generated public artifact register.
- `scripts/` — repeatable site builder and privacy/link validator.

Internal career prompts, resume tailoring, publishing instructions, blank templates, local installation files, and working notes are intentionally maintained in a separate private repository.

## Scenario notice

These simulations are fictitious generic scenarios for demonstration purposes only.

All company names, customer names, results, and operational data within the five scenarios are fictional. Public vendor and government references are identified in the research-and-assumptions documents. Scenario cost inputs that require real procurement evidence are marked accordingly.

## Build and validation

The published site is already included in `docs/`. Maintainers can rebuild it with:

```text
python scripts/build_portfolio_site.py
python scripts/validate_portfolio.py
```

Visitors do not need Python, MuJoCo, Git, or a command line. All six evidence videos play directly in the website.
