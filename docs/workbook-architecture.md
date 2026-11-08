# Workbook Architecture — Portfolio Abstraction

The private investigation workbook evolved into a structured evidence management and correlation system. Earlier inspected historical snapshots included a master timeline, evidence index, identifier crosswalk, overlap analysis, and attribution workflow. The latest version has not been verified in this repository; **do not present historical sheet counts as current**.

## Demonstration worksheets (synthetic)
| Sheet | Intended grain | Key fields |
|---|---|---|
| Evidence Index | One original artifact | artifact_id, provider, date_received, filename_alias, integrity_note |
| Raw Event Register | One source event | event_id, artifact_id, source_pointer, raw_time, record_type |
| Normalized Timeline | One normalized event | event_id, utc_time, timezone_rule, event_type |
| Identifier Crosswalk | One typed identifier occurrence | namespace, value_alias, event_id, first_seen |
| Correlation Candidates | One candidate event pair | left_event, right_event, join_basis, time_delta, limitations |
| Attribution Review | One hypothesis or question | hypothesis_id, evidence_for, evidence_against, missing_bridge, status |
| Corrections Log | One correction | changed_field, old_value, new_value, reason, source_reference |

## Quality controls
- Preserve original raw values; normalization creates additional fields.
- Use event IDs for deduplication, not simply matching timestamps.
- Flag missing source references and ambiguous date conversions.
- Treat IP address, device labels, and client IDs as different identifier types.
- Never collapse provider records into a physical device or operator without verification.
- Keep summary and correlation sheets concise: only meaningful new findings, not copied filler.
- Corrections must preserve provenance and prior classification.

## Publication boundary
The actual workbook, provider exports, financial data, IPs, phone numbers, and third-party identifiers remain outside this repository. Demonstrations use fabricated records and aliases.
