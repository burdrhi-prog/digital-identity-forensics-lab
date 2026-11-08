# Run the synthetic event-correlation demo

Requires Python 3.9+; no third-party packages.

From the repository root:

```bash
python demo/analyze.py
python -m unittest discover -s demo -v
```

The four **fabricated** events are in `events.csv`. The program validates required fields, unique event IDs, and timezone-aware timestamps; then finds same-account events within a configurable 15-minute window. It preserves source references and flags when logical client IDs differ.

**Expected output:** 4 events and 3 candidate pairs. One separate-account event is excluded. No finding is labeled unauthorized.

This is a deterministic *teaching demonstration*, not a validated fraud detection system. It does not inspect real provider data, attribute operators, or infer physical-device count.
