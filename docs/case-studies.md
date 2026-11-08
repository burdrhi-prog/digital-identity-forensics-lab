# Synthetic Investigation Case Studies

These scenarios are **fictional**. They illustrate methods inspired by independent research; they are not anonymized excerpts of a real investigation.

## Case 1 — 2024 Account Recovery Timeline
**Question:** Do recovery-method changes and authentication events form a supported sequence?

**Method:** Join provider-export events by source IDs and UTC timestamps; record whether each event reflects a request, confirmation, or completed change. Compare with device registrations without assuming device ownership.

**Limit:** Temporal proximity is not proof that one event caused another. A recovery event does not identify its operator.

**Deliverable:** Source-linked event timeline and unresolved-questions register.

## Case 2 — Logical Client vs Physical Device
**Question:** Do two client registrations establish two handsets?

**Method:** Compare provider namespaces, user agents, session IDs, first-seen/last-seen times, and explicit hardware identifiers where available.

**Limit:** Separate registrations may reflect reinstallations, browser profiles, or different devices; attribution remains unresolved absent independent linkage.

**Deliverable:** Identifier crosswalk with evidence-backed and candidate edges.

## Case 3 — Carrier Change and Account Activity
**Question:** Do carrier account events coincide with security-setting changes?

**Method:** Preserve carrier-recorded authorization status, channel, SIM event timestamps, and independent provider events. Compare time windows while separating documented changes from authorization disputes.

**Limit:** Correlation does not prove unauthorized access, a specific mechanism, or an actor.

**Deliverable:** Correlation table and prioritized provider clarification questions.

## Case 4 — Financial Account Activity
**Question:** Can account, transaction, and authentication records be reliably linked?

**Method:** Keep payment instrument aliases, merchant references, authorization events, account identities, and settlement/refund records separate until matching keys exist.

**Limit:** A charge, login, and network observation near the same time do not automatically share an operator or causal chain.

**Deliverable:** Source-linked transaction review with missing-bridge flags.
