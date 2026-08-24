from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Iterable


TELEMETRY_FIELDS = [
    "table_title",
    "timestamp_ns",
    "sim_time_s",
    "scenario",
    "site_id",
    "robot_id",
    "robot_model",
    "software_version",
    "mission_id",
    "operational_state",
    "safety_state",
    "battery_pct",
    "network_rssi_dbm",
    "x_m",
    "y_m",
    "z_m",
    "component",
    "fault_code",
    "severity",
    "correlation_id",
    "message",
    "evidence_class",
    "confidence",
    "source_or_validation",
]


def _normalized(record: dict[str, Any]) -> dict[str, Any]:
    return {field: record.get(field, "") for field in TELEMETRY_FIELDS}


def write_records(
    records: Iterable[dict[str, Any]], output_dir: Path, prefix: str
) -> dict[str, str]:
    """Write the same operational evidence to CSV, JSONL, and MCAP."""
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = [_normalized(row) for row in records]

    csv_path = output_dir / f"{prefix}_telemetry.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TELEMETRY_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    jsonl_path = output_dir / f"{prefix}_telemetry.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

    result = {"csv": str(csv_path), "jsonl": str(jsonl_path)}

    try:
        from mcap.writer import Writer

        mcap_path = output_dir / f"{prefix}_telemetry.mcap"
        schema = {
            "type": "object",
            "properties": {field: {} for field in TELEMETRY_FIELDS},
        }
        with mcap_path.open("wb") as handle:
            writer = Writer(handle)
            writer.start(profile="robotics-operations-portfolio")
            schema_id = writer.register_schema(
                name="robotics.ops.Telemetry",
                encoding="jsonschema",
                data=json.dumps(schema).encode("utf-8"),
            )
            channel_id = writer.register_channel(
                topic="/ops/telemetry",
                message_encoding="json",
                schema_id=schema_id,
            )
            for row in rows:
                timestamp_ns = int(row["timestamp_ns"])
                writer.add_message(
                    channel_id=channel_id,
                    log_time=timestamp_ns,
                    publish_time=timestamp_ns,
                    data=json.dumps(row, sort_keys=True).encode("utf-8"),
                )
            writer.finish()
        result["mcap"] = str(mcap_path)
    except ImportError:
        result["mcap"] = "not written; install mcap==1.4.0"

    return result


def write_summary(summary: dict[str, Any], output_dir: Path, prefix: str) -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{prefix}_summary.json"
    path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    return str(path)
