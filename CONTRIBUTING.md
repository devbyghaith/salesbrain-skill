# Contributing

Thanks for helping. This skill is a set of Markdown files that an AI agent reads, so contributions are
mostly writing, and every line has to earn its place.

## Ground rules

- Read `AUTHORING.md` first. It holds the rules the linter enforces: evidence tags on every bullet, 35-word
  bullets, no shouted ALWAYS/NEVER/MUST, file line budgets, working links.
- Every rule needs an evidence tag: `[study]`, `[data]`, `[practitioner]` or `[opinion]`. Every number needs
  a row in `references/benchmarks.md` with its source, date and sample.
- Do not add a claim because a well-known sales author says it. Check `references/claims-audit.md` first;
  several popular claims are there because the research contradicts them.
- Prompts in `evals/*/prompt.md` are frozen once labelled. Add a new case for a new failure instead of
  editing an old prompt.

## Workflow

1. Fork and branch.
2. Make the change. Run the linter:

   ```bash
   python3 -I scripts/lint.py .
   ```

3. If you touched `SKILL.md` or a reference file, run the eval case closest to your change at one run,
   no ablation. It costs a few cents and needs Claude Code installed:

   ```bash
   claude plugin eval . --case objection-too-expensive --runs 1 --ablation none --output-dir /tmp/salesbrain-evals
   ```

4. Open a pull request. Say which rule you changed, what evidence backs it, and paste the eval line if you
   ran one.

## Good first contributions

- A new eval case for a sales situation the skill handles badly, with a grader anchored to a rule in
  `references/`.
- A near-miss negative case (a prompt that sounds like sales but is not) to guard against over-triggering.
- A missing source for a number already in `references/benchmarks.md`.
- A correction to a claim in `references/claims-audit.md`, with the DOI or dataset that settles it.

## Reporting problems

Use the issue templates. For wrong advice, quote the bullet and the evidence that contradicts it. For a
triggering problem, paste the prompt that should (or should not) have fired the skill.
