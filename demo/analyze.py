"""Small, deterministic correlation demo using entirely fictional records."""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = {"event_id", "timestamp", "account", "client_id", "event_type", "source_ref"}


def load_events(path):
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not REQUIRED.issubset(reader.fieldnames or []):
            raise ValueError("Missing required columns")
        rows = list(reader)
    ids = set()
    for row in rows:
        if not all(row.get(key, "").strip() for key in REQUIRED):
            raise ValueError("Empty required field")
        if row["event_id"] in ids:
            raise ValueError("Duplicate event_id")
        ids.add(row["event_id"])
        dt = datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00"))
        if dt.tzinfo is None or dt.utcoffset() is None:
            raise ValueError("Timestamp must contain a timezone")
        row["utc"] = dt.astimezone(timezone.utc)
    return sorted(rows, key=lambda row: (row["utc"], row["event_id"]))


def correlate(events, window_minutes=15):
    if window_minutes < 0:
        raise ValueError("window_minutes must be nonnegative")
    pairs = []
    for i, left in enumerate(events):
        for right in events[i + 1:]:
            if left["account"] != right["account"]:
                continue
            delta = abs((right["utc"] - left["utc"]).total_seconds()) / 60
            if delta <= window_minutes:
                pairs.append({
                    "left": left["event_id"],
                    "right": right["event_id"],
                    "minutes_apart": round(delta, 2),
                    "different_logical_clients": left["client_id"] != right["client_id"],
                    "source_refs": [left["source_ref"], right["source_ref"]],
                    "classification": "temporal correlation only",
                })
    return pairs


def report(path, window_minutes=15):
    events = load_events(path)
    return {
        "synthetic": True,
        "event_count": len(events),
        "candidate_pairs": correlate(events, window_minutes),
        "limitation": "Proximity and different logical client IDs do not prove separate physical devices, unauthorized access, or operator identity.",
    }


if __name__ == "__main__":
    print(json.dumps(report(Path(__file__).with_name("events.csv")), indent=2))
