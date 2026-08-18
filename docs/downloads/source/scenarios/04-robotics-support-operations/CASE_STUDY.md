# Case Study 4 — Build Robotics Support Operations

## Scenario

A growing robotics company supports 250 humanoid and quadruped robots across 60 customer sites but lacks a scalable support mechanism. Salesforce is the CRM (Customer Relationship Management) platform, Jira is used by engineering, and the company has either ServiceNow or Zendesk. The program manager must stand up frontline customer support, remote robotics support, field service, incident/problem management, knowledge, training, parts/RMA (Return Material Authorization), telemetry, and governance.

## Target operating outcome

Create one traceable service chain from customer/telemetry signal to safe restoration, field work or engineering fix, with clear ownership and customer communication. Make support readiness a release and deployment gate, not a post-sale afterthought.

## Principles

- Safety first; support tools never bypass independent safety controls.
- One installed-product identity and one correlation ID across systems.
- Evidence before escalation; no screenshot-only “robot broken” tickets.
- Customer communication and technical diagnosis run in parallel.
- Known errors, fixes, and telemetry improve product and support continuously.
- Field service, spares, RMA, and serviceability are part of product design.

## 180-day rollout

### Days 0–30 — stabilize

Name service owner and on-call; define severity and safety escalation; create single intake; inventory customers/sites/robots/versions/contracts; establish daily incident review; publish initial safe-response SOPs; identify critical spares and field contacts.

### Days 31–60 — standardize

Implement case/work-order/Jira linkage; evidence bundle; queues/routing; customer communication templates; knowledge ownership; remote-access approval; support-readiness checklist; RMA (Return Material Authorization)/parts records; weekly KPI (Key Performance Indicator) review.

### Days 61–90 — instrument

Standardize robot telemetry/logging; MCAP evidence; Grafana/fleet dashboards; health alerts; correlation IDs; version/configuration views; alert-to-case automation for high-confidence conditions; controlled remote-diagnostic workflow.

### Days 91–120 — scale field operations

Territories, skills, dispatch, tools, vans/depots, parts min/max, contractors, certification, return-to-service tests, first-time-fix and repeat-repair analysis.

### Days 121–180 — improve product/service economics

Problem management; known-error database; defect/release feedback; reliability and intervention trends; cost per robot/month; contract/SLA (Service-Level Agreement) alignment; workforce forecast; QBRs (Quarterly Business Reviews); serviceability design reviews; release/deployment readiness gates.
