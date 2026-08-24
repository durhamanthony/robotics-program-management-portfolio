# AI-Assisted Robotics PM Workflow Playbook

> **Evidence-confidence key:** [PB-H] public benchmark or authoritative source/high confidence; [RBE-M] range-based estimate/medium confidence; [SA-L] scenario assumption/low confidence; [DC-L] disclosed derived calculation/confidence inherits the weakest input; [UPV] unverified production value/block commitment until approved.


AI may accelerate drafting, cross-file comparison, arithmetic checks, meeting synthesis, and quality review. It does not own facts or authorize safety, security, privacy, finance, employment, supplier, customer, or release decisions.

## Control loop

**Table 1. Control loop — Evidence: disclosed row/source notes; Confidence: see evidence key and row/source notes**

| Step | AI use | Required human control | Evidence output |
|---|---|---|---|
| 1. Frame | Convert approved objective and constraints into a draft work breakdown | Program owner confirms scope and exclusions | Dated brief with assumptions labeled |
| 2. Retrieve | Summarize only the supplied or linked source set | Record owner checks source identity, date, and applicability | Source register with URLs or file paths |
| 3. Draft | Propose artifacts, tests, risks, and decisions | Functional owners edit and accept their content | Versioned draft with owner names |
| 4. Reconcile | Compare numbers, dates, identifiers, and definitions across files | Finance/test/program owners resolve discrepancies | Exception report and corrected baselines |
| 5. Challenge | Run adversarial review for missing evidence and unsupported claims | Approver disposition is recorded | QC report with severity and confidence |
| 6. Release | Generate a publication candidate | Human privacy, security, safety, legal, and executive review | Signed release checklist |

## Reusable prompt — evidence-first review

```text
Role: independent robotics program assurance reviewer.
Inputs: only the attached controlled files and explicitly linked primary sources.
Task: identify contradictions, arithmetic errors, missing dependencies, unsupported claims,
unlabeled assumptions, acceptance tests without thresholds, and decisions without owners.
For every finding return severity, file, section/row, exact claim, available evidence,
calculation or reasoning, proposed correction, and confidence. Do not invent a pass result.
Treat [UPV] as unverified and block commitments that depend on it.
```

## Reusable prompt — weekly synthesis

```text
Using the approved schedule, RAID, budget, evidence, and benefits registers, draft a one-page
weekly status. Preserve identifiers and numbers exactly. Separate observed results [RBE/PB]
from scenario assumptions [SA], derived calculations [DC], and unverified production values
[UPV]. List decisions needed with owner and due date. End with a reconciliation table showing
which source rows were used. A human program lead will approve the final status.
```

## Prohibited use

- Never accept generated citations, prices, laws, safety thresholds, or test results without checking the primary source.
- Never paste credentials, private customer data, biometric data, export-controlled material, or unredacted logs into an unapproved model.
- Never let AI execute robot commands, change a production configuration, close an incident, accept a test, approve spend, or sign a gate.
- Never hide uncertainty: use the evidence class and confidence fields in every output.

## Minimum review checklist

1. Sources resolve and publication dates are recorded.
2. Units, currencies, periods, and rounding are explicit.
3. Totals reconcile across dashboard, narrative, spreadsheet, and CSV.
4. Every table has a title; every material value has an evidence label and confidence.
5. Every requirement has an owner, method, threshold, result, status, and evidence location.
6. A named human retains approval authority.
