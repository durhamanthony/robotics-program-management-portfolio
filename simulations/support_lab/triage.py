from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


ROUTING = {
    "COMMS_DEGRADED": ("S2", "Robotics L2", "Network diagnostics and safe-state validation"),
    "NETWORK_LOSS": ("S2", "Robotics L2", "Confirm geofence safe state and restore approved communications"),
    "GRIPPER_FORCE_VARIANCE": ("S2", "Robotics L2", "Review force telemetry; field inspection if repeatable"),
    "THERMAL_CAMERA_DEGRADED": ("S3", "Robotics L2", "Suspend dependent alert capability; inspect/calibrate sensor"),
    "LOW_BATTERY_RETURN": ("S3", "Fleet Operations", "Verify dock/coverage rotation and battery health"),
    "INJECTED_STOP": ("S2", "Test & Validation", "Validate controlled stop and authorized resume evidence"),
}


def load_fault_rows(output_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for csv_path in sorted(output_dir.glob("*_telemetry.csv")):
        with csv_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row.get("fault_code"):
                    row["source_file"] = csv_path.name
                    rows.append(row)
    return rows


def build_tickets(fault_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    tickets: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for row in fault_rows:
        key = (row["scenario"], row["robot_id"], row["fault_code"])
        if key in seen:
            continue
        seen.add(key)
        default_severity, queue, next_action = ROUTING.get(
            row["fault_code"], (row.get("severity") or "S3", "Robotics L2", "Review evidence")
        )
        tickets.append(
            {
                "ticket_id": f"RBT-{len(tickets) + 1:04d}",
                "correlation_id": row.get("correlation_id") or f"AUTO-{len(tickets) + 1:04d}",
                "severity": row.get("severity") or default_severity,
                "customer_site": row["site_id"],
                "robot_id": row["robot_id"],
                "software_version": row["software_version"],
                "fault_code": row["fault_code"],
                "safety_state": row["safety_state"],
                "assigned_queue": queue,
                "summary": row["message"],
                "evidence": row["source_file"],
                "next_action": next_action,
                "status": "New",
            }
        )
    return tickets


def write_outputs(tickets: list[dict[str, str]], output_dir: Path) -> dict[str, str]:
    ticket_path = output_dir / "support_lab_tickets.csv"
    fields = list(tickets[0].keys()) if tickets else ["ticket_id", "status"]
    with ticket_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(tickets)

    severity_counts = Counter(ticket["severity"] for ticket in tickets)
    queue_counts = Counter(ticket["assigned_queue"] for ticket in tickets)
    scorecard = {
        "unique_tickets": len(tickets),
        "by_severity": dict(sorted(severity_counts.items())),
        "by_queue": dict(sorted(queue_counts.items())),
        "evidence_complete_pct": 100.0
        if tickets and all(ticket["evidence"] and ticket["robot_id"] for ticket in tickets)
        else 0.0,
        "note": "Portfolio rule-based triage; production routing requires approved service design and human oversight.",
    }
    scorecard_path = output_dir / "support_lab_scorecard.json"
    scorecard_path.write_text(json.dumps(scorecard, indent=2, sort_keys=True), encoding="utf-8")

    report_path = output_dir / "support_lab_report.md"
    lines = [
        "# Support Lab Triage Report",
        "",
        f"Unique tickets: {len(tickets)}",
        "",
        "| Ticket | Severity | Robot | Fault | Queue | Safe/next action |",
        "|---|---|---|---|---|---|",
    ]
    for ticket in tickets:
        lines.append(
            f"| {ticket['ticket_id']} | {ticket['severity']} | {ticket['robot_id']} | "
            f"{ticket['fault_code']} | {ticket['assigned_queue']} | {ticket['next_action']} |"
        )
    lines.extend(
        [
            "",
            "This is a portfolio demonstration of evidence normalization, deduplication, severity, routing, and system linkage. It does not autonomously authorize remote robot actions.",
        ]
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"tickets": str(ticket_path), "scorecard": str(scorecard_path), "report": str(report_path)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs")
    args = parser.parse_args()
    fault_rows = load_fault_rows(args.output_dir)
    if not fault_rows:
        raise SystemExit("No fault telemetry found. Run the three MuJoCo demos first.")
    tickets = build_tickets(fault_rows)
    print(write_outputs(tickets, args.output_dir))


if __name__ == "__main__":
    main()

