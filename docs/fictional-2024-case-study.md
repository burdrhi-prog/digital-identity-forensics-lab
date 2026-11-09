# Fictional 2024 recovery and session case study

**Purpose:** Demonstrate investigative reasoning and workbook design using wholly fictional records. The 2024 dates are illustrative and are not copied from private records.

## Question
Which recovery and authentication events on the same account fall within a 15-minute window, and what do they establish?

## Source preservation
Two fictional provider exports are indexed as ART-001 and ART-002. Each normalized event carries a source pointer. The original timestamp and the UTC-normalized timestamp are separate fields. A synthetic correction log documents one timezone-conversion correction without erasing the prior value.

## Observations
- F-001 authentication at 10:02 UTC and F-002 recovery change at 10:07 UTC are five minutes apart on the same fictional account.
- F-003 session registration occurs at 10:11 UTC.
- F-004 belongs to another fictional account and is not paired.
- Three same-account event pairs fall within 15 minutes.

## Interpretation and limits
The records show temporal correlation, not that the recovery event was unauthorized or that a particular person acted. Logical client labels do not establish physical-device count. The source label "disputed" is a simulated report, not an independently verified finding.

## Evidence gaps
- Provider-side semantics of recovery and registration actions.
- Reliable source-clock documentation and original export provenance.
- Independent verification of authorization and practical account control.

## Reproduce
```bash
python demo/case_study_report.py
python -m unittest discover -s demo -v
```

The script reads [fictional source tables](../examples/case-study-2024/events.csv) and writes a Markdown report to standard output. These CSV files are the portable, inspectable source of the demonstration workbook.
