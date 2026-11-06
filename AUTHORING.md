# Authoring rules for salesbrain-skill

These rules govern every line in `SKILL.md`, `references/` and `assets/`. They come from two reports in the
notes layer (kept outside this repo): a review of how skills change agent behaviour (what knowledge actually
moves outputs) and an evidence review of the sales corpus (what popular sales advice gets wrong).

## 1. The one test every line must pass: the delta

The model is already a competent generalist. A line earns its place only if a fresh session without the skill
would get it wrong, omit it, or say the opposite. Concretely, include:

- Counter-intuitive findings the model will contradict by default (e.g. "fear and urgency make indecisive
  buyers more indecisive", "the best talk ratio is a diagnostic, not a target", "'did I catch you at a bad
  time?' is the worst cold-call opener").
- Decision rules with an observable condition and a threshold ("if the buyer has not named an explicit need,
  do not present the solution yet").
- Numbers with their source and sample ("11–14 questions spread through the call, Gong 2017, 519k calls").
- Exact wording worth reusing: scripts of at most 40 words spoken, 75 words written.
- Diagnostic questions that classify a situation before responding.
- Named frameworks ONLY as a selection rule (when to use which) and as the few steps the model gets wrong.
- Common mistakes, each paired with the replacement behaviour.

Exclude:

- Definitions of things the model knows (what BANT is, what a value proposition is, what SPIN stands for).
- Generic advice ("personalize", "listen actively", "build trust", "be confident", "know your customer").
- Motivational content, anecdotes that do not carry a rule, speaker biographies.
- Any claim in the do-not-cite list (`references/claims-audit.md`).
- Speakers' self-reported business figures (close rates, revenue, show rates). They may appear only as
  "<Name> reports…" and only when a rule depends on them; prefer to cut.

## 2. Line format

One idea per bullet, at most 35 words, action first. Every bullet ends with an evidence tag:

| Tag | Meaning |
|---|---|
| `[study]` | Peer-reviewed experiment, field study or meta-analysis |
| `[data]` | Large vendor or proprietary dataset (Gong, JOLT, Bridge Group, Belkins, Lavender). Correlational. |
| `[practitioner]` | Operator with a track record, or researcher writing a how-to |
| `[opinion]` | Neither of the above |

Add a replication flag when relevant: `[study; replicated]`, `[study; mixed replication]`. Failed replications
and retracted work go to `claims-audit.md`, never into a topic file as advice.

Add a context flag when a rule holds in only one sales motion: `(small-ticket, single-call)` or
`(complex B2B, committee)`. A rule with no flag is claimed to hold in both.

When two sources disagree, never leave both as peers. Resolve at authoring time into:

```
- Default: X. Exception: when <observable condition>, Y. [tag]
```

Default first (primacy). Study beats data beats practitioner beats opinion when they conflict and the
conditions are the same. Dedupe at the claim level: the same idea from five speakers is one bullet.

Numbers: include the short source inline, e.g. `(Gong 2018, 28,833 deals)`, `(Petrowsky 2025 meta-analysis)`.
Full entries with URL, date, sample and caveat live in `references/benchmarks.md`. Never round a number in the
persuasive direction; use the "safe statement" wording from the claims audit where one exists.

Attribution: no per-line speaker names, except (a) a framework the user may ask for by name, (b) "<Name>
reports…" for an unverifiable figure a rule depends on. The named frameworks are: SPIN, MEDDICC, BANT, JOLT,
Challenger, Voss labels and calibrated questions, the Mom Test, JTBD / demand-side forces, strategic narrative
(Raskin), Obviously Awesome positioning (Dunford), SUCCESs, WOOP. Any other speaker is described by the move,
not the name.

## 3. File shape

- Headers are situations, written the way a seller meets them: `## Prospect says "send me some info"`,
  `## First call with a VP: how many questions`, `## Pricing a three-tier proposal`. Headers are the retrieval
  key; the model greps and skims them.
- Each topic file: 80–300 lines. Table of contents at the top when over 100 lines.
- Order inside a file: (1) the 3–6 rules the model most often violates, (2) situation sections, (3) scripts,
  (4) 2–4 worked examples, (5) common mistakes → replacement.
- Worked examples are short (under 120 words each) and show the rule applied, not a full transcript.
- Tables for comparisons and selection rules; bullets for everything else; no prose paragraphs over 3 lines.
- No nested reference chains. A topic file may point to `benchmarks.md`, `claims-audit.md`, an `assets/`
  template, or another topic file in a single line ("see references/closing.md, Concessions"). Each rule has
  one home file; every other file carries at most that one pointer line, never a copy.
- Never write "ALWAYS", "NEVER", "MUST" in capitals. State the rule and, in a few words, why.
- Prohibitions are written as "mistake → do this instead", never as a bare "don't".

## 4. What goes in SKILL.md versus references

`SKILL.md` (at most 150 lines, first 60 lines are the ones that survive context compaction):

1. Non-blocking context questions (work with what you have; mark gaps `[NEEDS INPUT]`).
2. Routing table: situation → `references/<file>.md`. The `##` headers inside the file are the anchors; the
   agent greps them, so they stay phrased as situations.
3. The 10–12 counter-intuitive rules with evidence anchors, one line each.
4. Guardrails: never invent customers, metrics, quotes or case studies; vendor data is correlational; end
   every deliverable with a one-line self-report (assumptions, evidence level, what was not checked).
5. Output pointers to `assets/`, "when not to use this skill", related skills.

Everything else lives in `references/`. A section that every task ends up reading gets promoted into SKILL.md.

## 5. Sources of truth, in order

1. `sources/studies/*/notes.md` and the claims-audit "safe statement" column: the only place a number may come from.
2. `research_notes/Salesbrain expert sources by topic/*.md`: the researched evidence per topic, with URLs.
3. `reports/Salesbrain expert sources by topic.md`: the synthesis and the contradictions table.
4. `sources/videos/*/notes.md`: practitioner tactics and scripts. Use for wording, question banks and
   step sequences; grade as `[practitioner]` unless the speaker is reporting a study.

All of these live in the notes layer, a separate folder outside this repo. They are never shipped
inside the skill.

## 6. Self-check before a file is done

- Every bullet has a tag. Every number has a source. No bullet exceeds 35 words.
- No two bullets say the same thing. No two bullets contradict without a Default/Exception.
- No line in the do-not-cite list survives as advice.
- A reader who knows nothing about the speakers can act on every line.
- The file answers "what should I do now?" for the situations in its headers, not "what is X?".
