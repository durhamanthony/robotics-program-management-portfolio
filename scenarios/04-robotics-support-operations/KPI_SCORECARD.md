# Robotics Service KPI Scorecard

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


## Fleet/customer outcomes

Fleet availability; mission success; planned versus completed missions; mean missions between intervention; human interventions per 100 missions; customer workflow throughput; safety events/near misses; Customer Satisfaction (CSAT).

## Support flow

Mean Time to Detect (MTTD); Mean Time to Acknowledge (MTTA); time to safe state; time to restore; time to permanent correction; first-contact resolution; first-time fix; reopen/repeat rate; backlog age; Service-Level Agreement (SLA) compliance; communication compliance; escalation quality/evidence completeness.

## Product/reliability

Incidents by subsystem/version/site; fault recurrence; mean time/distance/missions between failure; alert precision/recall; top known errors; escaped defects; rollback rate; update success; defect-to-release lead time.

## Field/parts/economics

Dispatch/onsite/repair duration; parts fill; Return Material Authorization (RMA) cycle/no-fault-found; service labor/parts/travel/cloud cost; cost per robot/month; warranty reserve; support contacts per robot; remote-resolution rate.

## Day-180 operating scorecard

**Table 1. Day-180 operating scorecard — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Metric | Target | Actual | Trend | Segment/root cause | Owner/action |
|---|---:|---:|---|---|---|
| Installed-product data completeness | 100% | 100% | Up from 86% at day 75 | All 250 robots linked to site/version/entitlement/owner | Service data owner: monthly audit |
| Diagnostic evidence completeness | >= 95% | 96% | Up | Coaching improved Level 1 bundles | Robotics Level 2: sample 20 cases/week |
| Remote resolution for eligible cases | >= 65% | 68% | Up | Strongest on configuration and software faults | Robotics Level 2: expand two safe runbooks |
| First-time field fix | >= 85% | 87% | Up | Parts mapping and pre-dispatch evidence | Field Service: monitor actuator repeat repairs |
| Severity 1 acknowledgement | <= 15 minutes | 12-minute median | Stable | Two events; both drills reviewed | Duty Manager: retain monthly on-call drill |
| Severity 1 customer updates | Every 30 minutes | 100% compliant | Stable | Communication owner assigned at incident start | Service Operations: quarterly audit |
| Critical-parts fill | >= 95% | 97% | Up | Depot minimums and serialized transfers | Supply Chain: recalculate quarterly |
| Repeat incident rate | <= 8% | 7.1% | Down | Known-error and release linkage | Problem Manager: top-three review monthly |

The scorecard is the accepted day-180 baseline. Production targets must be replaced by executed customer agreements and actual product-risk requirements where those are more stringent.
