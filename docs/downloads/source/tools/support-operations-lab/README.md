# Support Operations Workflow Lab - Data Only

> **Evidence-confidence key:** Synthetic events and results are fictional scenario assumptions [SA-L]. Routing logic and arithmetic are deterministic derived calculations [DC-L]. A production workflow requires approved service design, customer data, security review, and platform configuration [UPV].

This data-only lab supports Case 04 without a physics simulator. It turns synthetic robot events into a deduplicated support-case register, severity assignment, owner queue, next action, and operational scorecard. It demonstrates the information handoffs among fleet telemetry, customer cases, installed-product data, Robotics Level 2, field service, engineering, and customer communication.

## Windows run

```bat
.venv\Scripts\python.exe tools\support-operations-lab\build_cases.py
```

The command reads `sample_robot_events.csv` and writes `support_case_register.csv`, `support_scorecard.csv`, and `support_workflow_summary.json` into `outputs/support_workflow/`.

**Table 1. Lab inputs and outputs - Evidence: synthetic [SA-L] and deterministic [DC-L]; Confidence: see evidence key and row/source notes**

| Item | Purpose | Production replacement |
|---|---|---|
| sample_robot_events.csv | Safe synthetic event input | Approved telemetry/event contract |
| build_cases.py | Deduplication and routing demonstration | Governed automation in the service platform |
| support_case_register.csv | Traceable case record | System-of-record cases and work orders |
| support_scorecard.csv | Evidence completeness and severity view | Service dashboard with approved definitions |

The lab never authorizes a remote robot action. A human retains safety, severity, recovery, dispatch, engineering-escalation, and customer-communication authority.
