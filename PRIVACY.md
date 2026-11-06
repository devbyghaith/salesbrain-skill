# Privacy

salesbrain-skill is a set of Markdown files that an AI agent reads. It has no runtime code, no network
calls, no connectors and no storage of its own.

- **What it reads.** Whatever you type into your agent while the skill is active, which may include
  prospect names, email addresses, company names and deal details. That text is processed by the agent
  you are using (for example Claude Code) under that agent's own privacy terms, not by this skill.
- **What it stores.** Nothing. The skill writes no files and keeps no record of your prompts or outputs.
- **What it sends elsewhere.** Nothing. No data leaves the agent you run it in.
- **Scripts.** `scripts/lint.py` and `scripts/build_sources.py` are developer tools run by hand on this
  repository. They read local files only and make no network requests. The agent never runs them.
- **Evals.** `claude plugin eval` sends the fixed prompts in `evals/` to Claude for grading. Those prompts
  contain no real personal data.
- **Children.** Not intended for users under 18.

Questions: open an issue at https://github.com/devbyghaith/salesbrain-skill/issues.
