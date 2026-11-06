# Eval suite

Eight cases in the Claude Code plugin-evaluation format: five positive (the skill should fire and the output should meet
the graders) and three near-miss negatives (the skill should stay silent and the task should still get done).
Each positive case has a `skill-fired` grader (unscored under ablation) plus one or two `llm` graders anchored
to a rule in `references/`. Each negative case has a `skill-not-fired` grader (`min: 0, max: 0, arm: both`)
and a task-done grader.

Run from the repo root:

```bash
claude plugin eval . --ablation with-without --max-cost-usd 15 --output-dir /tmp/salesbrain-evals
```

## Baseline run, 2026-11-06 (skill v0.1.0, Claude Code 2.1.305, 3 runs per arm)

Cost $4.74, 324 seconds, 48 runs.

| Case | With skill | Without | Delta | Note |
|---|---|---|---|---|
| cold-email-first-touch | 0.67 | 0.00 | +0.83 | baseline wrote 150+ word emails with invented stats; one with-run failed on judge noise (fixed grader wording) |
| discovery-first-call | 1.00 | 0.00 | +0.83 | baseline front-loaded situation questions and skipped next steps |
| went-dark-after-quote | 1.00 | 0.33 | +0.67 | prompt never says "sales"; skill still fired 3/3 |
| objection-too-expensive | 1.00 | 0.67 | +0.17 | baseline sometimes discounted before diagnosing |
| objection-think-it-over | 1.00 | 1.00 | 0.00 | grader did not discriminate; tightened to require the indecision diagnosis and two de-risking moves |
| neg-internal-offsite-email | 1.00 | 1.00 | 0.00 | skill silent 3/3 |
| neg-landing-page-copy | 1.00 | 1.00 | 0.00 | skill silent 3/3 |
| neg-support-invoice-reply | 0.33 | 1.00 | −0.33 | skill silent 3/3; judge flipped on a correct reply that asked for the address (grader wording fixed) |

Triggering: fired in 15 of 15 positive runs, 0 of 9 negative runs.

## Re-run of the three rewritten cases, same day (cost $1.69)

| Case | With skill | Without | Delta | Note |
|---|---|---|---|---|
| objection-think-it-over | 1.00 | 0.00 | +1.00 | tightened grader now discriminates: baseline never names indecision vs status quo or two de-risking moves |
| neg-support-invoice-reply | 1.00 | 1.00 | 0.00 | grader wording fixed; skill silent 3/3 |
| cold-email-first-touch | 0.67 | 0.00 | +0.67 | email text clean in all three with-runs; one judge vote split (PASS FAIL FAIL) because the explanation after the email quotes Gong percentages. Grader reworded again to ignore the explanation; not yet re-run |

Combined picture after both runs: skill fired 24 of 24 positive runs, 0 of 18 negative runs. Mean delta over
the five positive cases is about +0.6 pass-rate points; every negative case holds at parity.

## Full re-run, 2026-11-06 afternoon (all eight cases, 3 runs per arm)

Cost $4.66, 1154 seconds, 48 runs. Skill fired 15 of 15 positive runs, 0 of 18 negative runs.

| Case | With skill | Without | Delta | Note |
|---|---|---|---|---|
| cold-email-first-touch | 1.00 | 0.17 | +0.83 | reworded grader holds; no judge splits |
| discovery-first-call | 1.00 | 0.17 | +0.83 | |
| went-dark-after-quote | 1.00 | 0.67 | +0.33 | |
| objection-too-expensive | 0.67 | 0.50 | +0.17 | `one-reason-next-step` judged the explanation under the email and read "by [day]" as no date; emails themselves were correct in all three with-runs. Grader reworded to judge the email only and accept placeholder dates |
| objection-think-it-over | 1.00 | 0.00 | +1.00 | |
| neg-internal-offsite-email | 1.00 | 1.00 | 0.00 | |
| neg-landing-page-copy | 1.00 | 1.00 | 0.00 | |
| neg-support-invoice-reply | 1.00 | 1.00 | 0.00 | |

Single-case re-run of objection-too-expensive after the grader fix (cost $0.62): with 1.00, without 0.33,
delta +0.67, all nine with-arm judge votes PASS. Mean delta over the five positive cases is now about +0.73.

Re-run a single case after editing its grader:

```bash
claude plugin eval . --case cold-email-first-touch --ablation with-without --output-dir /tmp/salesbrain-evals
```

## Adding a case

One folder per case: `prompt.md` (frontmatter plus the user's words), `graders/*.md`. Keep prompts frozen once
labelled; add a new case for a new failure rather than editing an old prompt. A grader that passes in both
arms is not measuring the skill; tighten it or drop it.
