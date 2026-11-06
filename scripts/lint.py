#!/usr/bin/env python3
"""Lint the skill against AUTHORING.md.

Usage: python3 -I scripts/lint.py [skill root]

Checks: SKILL.md frontmatter (name matches folder, description length, line budget), every bullet in a
topic reference ends with an evidence tag and is at most 35 words, no shouted ALWAYS/NEVER/MUST, file line
budgets, TOC presence over 100 lines, and that every local link points at a file that exists.
"""
import re
import sys
from pathlib import Path

TAG = re.compile(r"\[(study|data|practitioner|opinion)(;[^\]]*)?\]\s*(\([^)]*\))?\s*$")
SHOUT = re.compile(r"\b(ALWAYS|NEVER|MUST)\b")
LINK = re.compile(r"`?((?:references|assets|scripts)/[\w\-./]+\.md)`?")
TOPIC_FILES_EXEMPT = {"sources.md", "claims-audit.md", "benchmarks.md"}
MAX_WORDS = 35
MAX_SCRIPT_WORDS = 75  # written scripts; spoken ones should stay under 40


def words(text: str) -> int:
    text = TAG.sub("", text)
    return len(text.split())


def lint_skill_md(root: Path, problems: list[str]) -> None:
    path = root / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 150:
        problems.append(f"SKILL.md: {len(lines)} lines, budget 150")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        problems.append("SKILL.md: no frontmatter")
        return
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != root.name:
        problems.append(f"SKILL.md: name '{name.group(1).strip() if name else None}' != folder '{root.name}'")
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not desc:
        problems.append("SKILL.md: no description")
    elif len(desc.group(1)) > 1024:
        problems.append(f"SKILL.md: description {len(desc.group(1))} chars, max 1024")
    if SHOUT.search(text):
        problems.append("SKILL.md: shouted ALWAYS/NEVER/MUST")


def lint_reference(path: Path, problems: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    n = len(lines)
    if n > 300:
        problems.append(f"{path.name}: {n} lines, budget 300")
    if n > 100 and path.name not in ("sources.md", "benchmarks.md") and not any(re.match(r"^## (Contents|Table of contents)", l) for l in lines):
        problems.append(f"{path.name}: over 100 lines without a TOC")
    in_code = False
    in_scripts = False
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            in_scripts = line.lower().startswith("## script")
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if SHOUT.search(line):
            problems.append(f"{path.name}:{i}: shouted word")
        if path.name in TOPIC_FILES_EXEMPT:
            continue
        stripped = line.strip()
        if stripped.startswith("- ") and not stripped.startswith("- ["):
            if not TAG.search(stripped):
                # Allow pure navigation or template bullets that carry no claim.
                if not re.search(r"`[^`]+\.md`", stripped) and "[NEEDS INPUT]" not in stripped:
                    problems.append(f"{path.name}:{i}: bullet without evidence tag")
            else:
                cap = MAX_SCRIPT_WORDS if in_scripts else MAX_WORDS
                if words(stripped[2:]) > cap:
                    problems.append(f"{path.name}:{i}: {words(stripped[2:])} words, max {cap}")


def lint_links(root: Path, problems: list[str]) -> None:
    for path in [root / "SKILL.md", *sorted((root / "references").glob("*.md")), *sorted((root / "assets").glob("*.md"))]:
        for m in LINK.finditer(path.read_text(encoding="utf-8")):
            if not (root / m.group(1)).exists():
                problems.append(f"{path.relative_to(root)}: link to missing {m.group(1)}")


def main(root: Path) -> int:
    problems: list[str] = []
    lint_skill_md(root, problems)
    for path in sorted((root / "references").glob("*.md")):
        lint_reference(path, problems)
    lint_links(root, problems)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main((Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent).resolve()))
