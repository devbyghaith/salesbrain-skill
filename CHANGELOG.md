# Changelog

## 0.1.0 (2026-11-06)

First release.

- `SKILL.md` router with the rules models most often get wrong, guardrails and a deliverable footer that
  states what was assumed, what evidence backs the advice, and what was not checked.
- Eleven reference files: discovery, objections, closing, outreach, offer positioning, pitching, rapport,
  persuasion psychology, personal branding, sales process and team, mindset.
- `references/benchmarks.md`: every number with value, source, date, sample, evidence tag and caveat.
- `references/claims-audit.md`: 41 popular sales claims checked against sources; 14 verified, 12 overstated,
  4 misattributed, 2 failed replication, 9 unverifiable.
- `references/sources.md`: register of 55 talks and 26 studies with evidence grades.
- Four output templates in `assets/`.
- Eval suite of eight `claude plugin eval` cases (five positive, three near-miss negatives). On the
  2026-11-06 run the skill fired in 15 of 15 positive runs and 0 of 18 negative runs; mean pass-rate delta
  over the positive cases about +0.73 against the no-skill baseline.
- `scripts/lint.py` enforcing `AUTHORING.md`; `scripts/build_sources.py` regenerating the source register.
