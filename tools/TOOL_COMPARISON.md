# Robotics Support and Troubleshooting Tool Comparison

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


Pricing checked: August 16, 2026. Public prices change; verify with the vendor before procurement. “Custom” means the vendor does not publish a complete production price.

Abbreviations used below are Return Material Authorization (RMA), Over-the-Air software delivery (OTA), Robot Operating System (ROS), Incident Response Management (IRM), Customer Service Management (CSM), Field Service Management (FSM), Customer Relationship Management (CRM), Continuous Integration (CI), Service-Level Objective (SLO), Configuration Management Database (CMDB), and Application Programming Interface (API). MCAP is the name of the robotics log-container format.

## Decision principle

Do not force one product to serve four different jobs. A robotics support stack needs: customer case management, field work/parts/RMA, robot telemetry and replay, infrastructure monitoring, secure remote access/OTA, and engineering defect escalation.

## Shortlist

**Table 1. Shortlist — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Layer | Tool | Primary use | Free/portfolio option | Public production price snapshot | Recommendation |
|---|---|---|---|---|---|
| Simulation | MuJoCo | Physics simulation and test scenarios | Free/open source | $0 | Portfolio standard |
| Robot data | MCAP | Multimodal robotics log container | Free/open source | $0 | Logging standard |
| Robot visualization | Foxglove | ROS/MCAP visualization, replay, devices, data | Free: 3 users, 5 devices, 10 GB storage | Pro starts at $20/month with 1 TB storage and 3 developer seats; additional devices are $20/device/month and data is usage-priced | Best portfolio visualization |
| Robot operations | InOrbit | Fleet observability, diagnostics, incident workflows, multi-vendor operations | Free Edition | Platform pricing custom; Premium Support advertised at $3,000/month with annual commitment | Strong multi-vendor fleet option |
| Robot operations | Formant | Fleet observability, teleoperation, data, workflows | Demo/assessment; no durable public free production tier found | Custom | Enterprise comparison candidate |
| Time-series diagnostics | PlotJuggler | Live/offline time-series visualization, ROS | Free/open source | $0 | Local troubleshooting tool |
| Metrics/logs | Grafana Cloud | Dashboards, logs, traces, alerts, IRM | $0 tier: 50 GB logs/traces/profiles, 14-day retention, limited active users | Pro: $19 platform fee plus usage; visualization and IRM seats separately priced | Portfolio and production observability |
| Metrics | Prometheus | Metrics collection and alert inputs | Free/open source | $0 self-hosted | Pair with Grafana |
| OTA/device management | Mender | Secure OTA software updates and device inventory | Open-source self-hosted; hosted enterprise trial excludes Service Provider features and Service-Level Agreement support | Basic $34/month for up to 50 standard devices; Professional $291/month for up to 250; Enterprise custom | Good OTA reference design |
| Edge fleet | balena | Container deployment and edge-device fleet management | First 10 devices free | Prototype $159/month/30 devices; Pilot $329/60; Production $1,439/110, plus overages | Strong lab/prototype choice |
| Secure access | Tailscale | Identity-based private network for remote diagnostics | Personal $0, noncommercial limits | Standard $8/user/month; Premium $18/user/month | Lab access; enterprise review required |
| Customer/IT service | Jira Service Management | Requests, incidents, knowledge, on-call, developer escalation | Free for 3 agents | Standard $20/agent/month; Premium $51.42/agent/month | Best free portfolio workflow |
| Customer support | Zendesk | Omnichannel cases, knowledge, routing, analytics | 14-day trial | Support Team $19; Suite Team $55; Suite Professional $115 per agent/month, annual billing | Strong customer-support option |
| Enterprise service | ServiceNow CSM/FSM | Cases, playbooks, work orders, dispatch, parts, assets, contractors | Developer learning instance may be available; production is not a free tier | Custom quote | Best when company already operates ServiceNow |
| CRM/field service | Salesforce Field Service | CRM-connected work orders, dispatch, technician mobile, assets | Service Cloud trial; no permanent production free tier | Dispatcher/Technician $175/user/month; Contractor $55/user/month or $22/login; Field Service Plus $230/user/month, annual | Best when Salesforce is system of customer record |
| Engineering work | Jira | Software/hardware backlog, defects, changes, releases | Free for up to 10 users | Standard $7.91/user/month; Premium $14.54/user/month | Use for L3 engineering escalation |
| Source/portfolio | GitHub | Code, issues, actions, evidence, Pages | Free unlimited public/private repos; 2,000 Actions minutes/month for private use and free standard Actions for public repos | Team $4/user/month | Portfolio system of record |

## Best-of-breed enterprise architecture

Assumptions: Salesforce is the CRM; Jira is used for software development; the organization owns either ServiceNow or Zendesk.

### Recommended system-of-record split

- **Salesforce:** accounts, installed products, contracts, entitlements, opportunities, customer/site master.
- **ServiceNow CSM + FSM** *or* **Zendesk + a field-service module:** customer cases, service contracts, dispatch, work orders, parts/RMA, knowledge, technician activity.
- **Jira:** reproducible L3 engineering defects, firmware/software changes, release linkage, known-error backlog.
- **Foxglove + MCAP:** robot evidence package, timeline replay, sensor/joint/log correlation.
- **InOrbit or Formant:** live fleet operations, robot health, mission status, remote interventions, multi-site/multi-vendor view.
- **Grafana/Prometheus/Loki:** service and infrastructure SLOs, alerting, trends, capacity, executive dashboards.
- **Mender or balena:** controlled OTA/device releases, rollout rings, rollback, configuration inventory.
- **Tailscale or enterprise zero-trust equivalent:** authenticated support path; no direct internet exposure of robot control interfaces.

### Choice between ServiceNow and Zendesk

- Choose **ServiceNow CSM/FSM** when field work, parts, contractors, asset history, CMDB, enterprise workflows, and scale dominate.
- Choose **Zendesk** when rapid customer-support setup, agent usability, omnichannel service, and knowledge are the priorities; add a robust field-service/asset/RMA capability.
- If Salesforce already has deep service adoption, assess **Salesforce Field Service** before buying a second field-dispatch platform. The CRM integration is valuable, but seat costs can grow quickly.

## Free portfolio stack

1. MuJoCo for simulated robots and operational events.
2. MCAP plus Foxglove Free for replay/visualization.
3. Grafana Cloud Free for KPI and incident dashboards.
4. Jira + Jira Service Management Free for the project backlog, service portal, incidents, change, and knowledge.
5. GitHub Free for source, documentation, issues, Actions, and recruiter-facing evidence.
6. Tailscale Personal only for a private noncommercial lab; do not present it as a production-commercial license.
7. Mender open source or the hosted limited trial for OTA workflow practice.

## Minimum data contract

Every robot event should carry: `timestamp`, `robot_id`, `model`, `site_id`, `software_version`, `mission_id`, `operational_state`, `battery_pct`, `network_rssi`, `joint_or_component`, `fault_code`, `severity`, `safety_state`, `location`, `correlation_id`, and `support_case_id` when escalated.

## Operational integration flow

```text
Robot/edge -> MCAP + metrics/logs -> Foxglove / fleet platform / Grafana
                                    |             |
                                    +--> Service case/work order --> field technician/RMA
                                                   |
                                                   +--> Jira engineering defect --> fixed release
CRM installed product/entitlement -----------------+
```
