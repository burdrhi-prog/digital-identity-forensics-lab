# Investigation Methodology — Independent Research

## Purpose
Document a repeatable approach to reviewing multi-provider digital identity, authentication, account-recovery, device, network, and financial-account records. This is an **independent analytical portfolio**, not a claim of professional forensic certification or legal proof of wrongdoing.

## Source-of-truth rule
The private master investigation workbook is the authoritative *structured index*, but conclusions must trace back to provider exports, records, or other original artifacts. A workbook row alone is not independent confirmation. The most recent workbook version must be verified before citing current counts or findings. Older versions are historical snapshots.

## Workflow
1. **Acquire and preserve:** Record source provider, export date, original filename, record ID, original timestamp and time zone. Keep source records unchanged.
2. **Normalize:** Parse UTC and local time without overwriting originals. Document DST, uncertain clock accuracy, and date-only events.
3. **Namespace:** Keep account, client, browser, session, device, IP, SIM, and payment identifiers in separate typed fields.
4. **Index:** Link every derived event to the original artifact and its precise location (row, page, JSON path, or event ID).
5. **Correlate:** Use exact identifiers first, then carefully bounded time windows. A shared IP or close timestamp alone cannot establish a common actor.
6. **Reconcile:** Track duplicate exports, contradictory provider records, user-reported corrections, and missing joins without silently merging.
7. **Classify:** Distinguish provider-recorded observation, user-reported observation, technical correlation, hypothesis, disputed ownership, and unresolved attribution.
8. **Report:** Describe what is known, alternative explanations, missing evidence, and the next verification step.

## Attribution ladder
Logical client registration ≠ physical device ≠ operator identity. Multiple logical identifiers do not establish multiple physical handsets. Historical account association does not establish present control.

## 2024 preservation priority
Focus on authentication, account recovery, device registration, and financial-account activity in 2024. Preserve original dates and identifiers in the **private** record; demonstrate the approach publicly with fictional cases.

## Research boundaries
Do not assert hacking, SIM-swap causation, device cloning, or a particular operator without a verified evidence bridge. Provider disclosure gaps are unresolved questions, not proof of concealment. Avoid merging independent records solely because their labels resemble one another.
