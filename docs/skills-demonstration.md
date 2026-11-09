# Skills demonstration — reproducible fictional investigation

**Purpose:** Show what the project author can explain and practice, without presenting AI-assisted code as independently mastered programming.

## Demonstration 1: Evidence provenance
**Explain:** Why an event has a source reference and why a timeline row is not sufficient evidence by itself.
**Show:** Open `examples/case-study-2024/evidence_index.csv`; find ART-001, then trace F-001's `ART-001:row-2` source pointer.
**Practice question:** What would you do if a source pointer did not match an indexed artifact?

## Demonstration 2: Timestamp normalization and corrections
**Explain:** Why `2024-05-14T03:02:00-07:00` is `2024-05-14T10:02:00Z`.
**Show:** Compare the raw and UTC columns for F-001, then open `correction_log.csv`.
**Practice question:** Why retain the old value instead of overwriting the record without an audit trail?

## Demonstration 3: Correlation versus attribution
**Explain:** Why F-001/F-002 are five minutes apart and why this does not prove compromise or a second physical device.
**Show:** Run `python demo/case_study_report.py`; verify three same-account pairs, and confirm F-004 is excluded.
**Practice question:** Which independent provider record would be needed to assess authorization?

## Demonstration 4: Test and publish
**Explain:** What automated tests do and do not establish.
**Show:** Run `python -m unittest discover -s demo -v`, then `python demo/publish_report.py --output fictional_case_report.pdf` after installing `reportlab`.
**Practice question:** How would you debug a failing UTC conversion test?

## Career positioning
**Current strengths:** evidence organization, cross-provider comparison, source traceability, correction handling, careful analytical reasoning, and clear technical documentation.

**Developing skills:** Python, automated testing, GitHub Actions, reproducible report generation, and security-tooling implementation. The published code was developed with AI assistance; proficiency should be demonstrated through hands-on explanation, modification, and troubleshooting.

**Interview-ready phrasing:**
"I developed an evidence-focused investigation methodology and am learning to implement it with Python and automated tests. I can explain the investigation logic, trace findings to their sources, and identify where conclusions need further verification. I actively seek feedback and am comfortable learning the tools a team uses."

## Honest progress checklist
- [ ] I can explain the source-reference model without notes.
- [ ] I can reproduce the timezone correction.
- [ ] I can run the correlation demo and explain its output.
- [ ] I can run tests and explain one failure.
- [ ] I can regenerate the PDF report.
- [ ] I can make a small code change and verify it.

**Do not mark items completed until personally demonstrated.**
