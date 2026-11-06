#!/usr/bin/env python3
"""Build references/sources.md from the notes layer's meta.yaml files.

Usage: python3 -I scripts/build_sources.py <path to the notes layer sources/ folder>

Reads sources/videos/*/meta.yaml and sources/studies/*/meta.yaml (flat key: "value" plus
simple lists), and writes references/sources.md next to this script's parent directory.
The hand-written preamble below is the rating legend; the tables are generated.
"""
import sys
from pathlib import Path

PREAMBLE = """# Source register

Every rule in the topic files traces back to one of the sources below. Open this file when the user asks
"who says that?", when a bullet's `[tag]` needs a name behind it, or before quoting a speaker.

Evidence grades (from the notes layer's `meta.yaml`):

| Grade | Meaning | How to use it |
|---|---|---|
| study | Peer-reviewed experiment, field study or meta-analysis, or a vendor dataset with a stated method | Quote with the number and sample. Vendor datasets (Gong, Bridge Group, Huthwaite) are correlational: say so. |
| practitioner | Operator with a track record, or a researcher writing a how-to | Use for wording, question banks and step sequences. Their own business figures are unverifiable: "<Name> reports…" at most. |
| opinion | Neither | Only where nothing better exists, tagged `[opinion]`. |

Standing flags the agent applies on top of the grade:

- Hormozi, Priestley, Chris Do and other course or community sellers: tactics tuned to single-call,
  small-ticket or creator contexts. Never state their close rates, show rates or revenue as fact.
- Huthwaite whitepapers, Gong Labs, Bridge Group, Belkins, 6sense, Gartner, Forrester, Edelman: vendor or
  analyst data with a commercial interest; useful benchmarks, never causal claims.
- Anything in `claims-audit.md` overrides this register.
"""


def parse_meta(path: Path) -> dict:
    data: dict = {}
    key = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and key:
            data.setdefault(key, []).append(line[4:].strip().strip('"'))
            continue
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "null":
                value = ""
            if value in ("", "[]"):
                data[key] = [] if value == "[]" else data.get(key, [])
            elif value.startswith("[") and value.endswith("]"):
                data[key] = [v.strip().strip('"') for v in value[1:-1].split(",") if v.strip()]
            else:
                data[key] = value.strip('"')
    return data


def row(cells: list[str]) -> str:
    return "| " + " | ".join(c.replace("|", "/") for c in cells) + " |"


def main(src_root: Path) -> None:
    out = [PREAMBLE]
    videos = sorted(src_root.joinpath("videos").glob("*/meta.yaml"))
    studies = sorted(src_root.joinpath("studies").glob("*/meta.yaml"))

    out.append("## Studies and data reports\n")
    out.append(row(["Source", "Year", "Authors", "Grade", "Link"]))
    out.append(row(["---"] * 5))
    for meta in studies:
        d = parse_meta(meta)
        authors = d.get("authors", [])
        authors = ", ".join(authors) if isinstance(authors, list) else str(authors)
        link = d.get("doi") or d.get("url") or d.get("pdf_url") or ""
        if link and not link.startswith("http"):
            link = f"https://doi.org/{link}"
        out.append(row([d.get("title", meta.parent.name), str(d.get("year") or ""), authors,
                        d.get("evidence", "unrated"), link]))

    out.append("\n## Talks and interviews\n")
    out.append(row(["Source", "Speakers", "Grade", "Date", "Link"]))
    out.append(row(["---"] * 5))
    for meta in videos:
        d = parse_meta(meta)
        speakers = d.get("speakers", [])
        speakers = "; ".join(speakers) if isinstance(speakers, list) else str(speakers)
        out.append(row([d.get("title", meta.parent.name), speakers, d.get("evidence", "unrated"),
                        d.get("upload_date", ""), d.get("url", "")]))

    target = Path(__file__).resolve().parent.parent / "references" / "sources.md"
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {target}: {len(studies)} studies, {len(videos)} talks")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]))
