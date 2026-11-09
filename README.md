# Digital Identity Forensics Lab 🔎

**Independent Digital Forensics Research · Identity & Access Analysis · Fraud Investigation Methods · Cross-Provider Event Correlation**

> **Status:** Independent investigation methodology documented; synthetic case-study specifications prepared. This repository does **not** contain the original investigation workbook, actual personal records, or a completed interactive dashboard.

## From unanswered questions to a structured investigation
This project began as an independent investigation portfolio. Comparing account records across providers required more than a list of suspicious events: it required a defensible evidence index, timestamp normalization, identifier crosswalks, correction tracking, and careful separation of observations from hypotheses.

The resulting methodology supports review of authentication and account-recovery histories, logical client and device registrations, network observations, carrier account changes, and financial-account events. The **private master workbook** remains the structured reference, while each substantive conclusion must be traceable to original source records.

## What this project demonstrates
| Competency | Portfolio evidence |
| --- | --- |
| Evidence organization | Proposed evidence index and raw/derived event model |
| Timeline reconstruction | Timestamp preservation and normalization rules |
| Cross-provider correlation | Typed identifiers, time-window comparisons, missing joins |
| Identity and access reasoning | Logical client vs physical device vs operator distinctions |
| Data quality | Duplicate control, provenance, contradiction and correction logs |
| Technical reporting | Explicit findings, limitations, alternative explanations |

## ▶ Try the working demonstration

**[Open the Python demo](demo/README.md)** · [Inspect the script](demo/analyze.py) · [View synthetic events](demo/events.csv) · [Review tests](demo/test_analyze.py)

This small, standard-library Python example validates fictional events, normalizes timezone-aware timestamps, and identifies same-account event pairs within 15 minutes. Its expected output is **4 events and 3 candidate pairs**, with explicit limitations on device and operator attribution.

```bash
python demo/analyze.py
python -m unittest discover -s demo -v
```

**Verification status:** Initial demo and case-study code and tests are committed. GitHub Actions is configured; check the Actions tab for confirmed hosted results. This is a teaching demonstration, not a deployed forensic platform.

## Read the documentation
- [Investigation methodology](docs/investigation-methodology.md)
- [Workbook architecture](docs/workbook-architecture.md)
- [Four fictional case studies](docs/case-studies.md)
- [Project evolution and employer relevance](docs/project-evolution.md)

## Investigation reasoning
```text
Original provider record
        ↓
Source-linked evidence index
        ↓
Raw event + UTC-normalized timeline
        ↓
Typed identifier crosswalk
        ↓
Correlation candidates + alternative explanations
        ↓
Confirmed / Correlated / Disputed / Unresolved
        ↓
Reviewable finding + missing verification bridge
```

**Key principle:** Multiple logical registrations do not automatically prove multiple physical devices or people. Shared network context does not identify an operator.

## Case-study focus
The portfolio prioritizes **2024 account recovery, authentication, device registration, and financial-account activity** as a preservation and correlation period, alongside fictional examples of carrier changes and session attribution.

## What is built vs planned
**Documented:** An independently developed research methodology, a workbook-based analytical approach, and four synthetic case-study designs.

**Implemented as an initial demonstration:** Synthetic CSV events, a Python correlation script, and unit tests (execution verification pending). **Next:** A fabricated workbook, independently verified test results, and visualizations.

**Not claimed:** Professional forensic certification, forensic acquisition of devices, verified chain of custody, a completed dashboard, proof of compromise, or confirmed actor attribution.

## Privacy
This repository is designed for eventual public presentation. It excludes original provider exports, personal identifiers, private account records, and allegations about individuals. Do not commit the private master workbook.

## Related projects
- [Security Event Correlation Portfolio](https://github.com/burdrhi-prog/security-event-correlation-portfolio) — executable analysis tooling.
- [Human–AI Collaboration Lab](https://github.com/burdrhi-prog/human-ai-collaboration-lab) — human-in-the-loop evaluation.
- [Identity Fairy](https://github.com/burdrhi-prog/identity-fairy) — privacy-aware consumer product concept.

*Independent, self-directed technical research. Evidence first; attribution only when supported.*

## New: reproducible fictional 2024 case study

The [fictional 2024 case study](docs/fictional-2024-case-study.md) now has five inspectable CSV source tables: events, evidence index, identifier crosswalk, correction log, and candidate findings. It demonstrates source-pointer validation, UTC normalization, same-account correlation, and preserving a documented correction.

```bash
python demo/case_study_report.py
python -m unittest discover -s demo -v
```

Expected: **4 fictional events, 2 fictional source artifacts, 3 candidate correlations**. The case-study report is generated from the CSV data rather than manually claimed results. [GitHub Actions](.github/workflows/tests.yml) is configured to test the demonstrations on each push. Hosted test results should be checked in the Actions tab.

### Professional positioning

This work showcases independent evidence organization, structured investigative questions, data-quality controls, correction tracking, cross-provider correlation, and careful documentation. Python and automation are developing skills supported by AI-assisted implementation and review. It does **not** claim professional forensic certification, independent software-engineering experience, or verified real-world attribution.
