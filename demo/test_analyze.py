"""Run with: python -m unittest discover -s demo -v"""
import csv
import tempfile
import unittest
from pathlib import Path
from analyze import load_events, correlate, report


class CorrelationTests(unittest.TestCase):
    def setUp(self):
        self.sample = Path(__file__).with_name("events.csv")

    def test_expected_correlations(self):
        result = report(self.sample)
        self.assertEqual(result["event_count"], 4)
        self.assertEqual(len(result["candidate_pairs"]), 3)
        self.assertTrue(any(pair["different_logical_clients"] for pair in result["candidate_pairs"]))

    def test_different_accounts_not_joined(self):
        pairs = correlate(load_events(self.sample), 120)
        self.assertEqual(len(pairs), 3)

    def test_duplicate_ids_rejected(self):
        rows = list(csv.DictReader(self.sample.open(encoding="utf-8")))
        rows[1]["event_id"] = rows[0]["event_id"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                load_events(path)

    def test_naive_time_rejected(self):
        rows = list(csv.DictReader(self.sample.open(encoding="utf-8")))
        rows[0]["timestamp"] = "2024-05-14T10:02:00"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "naive.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "timezone"):
                load_events(path)


if __name__ == "__main__":
    unittest.main()
