# Deliverable footer

Every deliverable the skill produces ends with this three-line block. It keeps the agent honest about
what it invented, what it assumed, and how strong the evidence behind its advice is.

```
---
Assumed: <the 1–3 facts about the prospect, deal or product you had to assume>
Evidence: <study | data | practitioner | opinion> for the main rule applied; any number used is from <source>
Not checked: <what you could not verify; items marked [NEEDS INPUT]>
```

Rules:

- Never fill a gap with an invented customer name, metric, quote, case study or statistic. Write
  `[NEEDS INPUT]` instead.
- If a number came from vendor data, say "vendor data, correlational" in the Evidence line.
- If the user's own guru claim was contradicted by `references/claims-audit.md`, say so in one line.
