#!/usr/bin/env python3
"""Generate docs/SKILLS.md — a trigger & capability catalog — from every skill's SKILL.md frontmatter.

Usage: python3 scripts/gen-catalog.py   (run from anywhere; paths resolve relative to the repo root)
Re-run this whenever skills are added, removed, or their descriptions change.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "SKILLS.md"
MARKET = "treasury-analyst-skills"


def parse_frontmatter(md_path):
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fm = []
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        fm.append(ln)
    name, desc_lines, mode = None, [], None
    for ln in fm:
        if re.match(r"^name:", ln):
            name = ln.split(":", 1)[1].strip().strip('"').strip("'")
            mode = None
        elif re.match(r"^description:", ln):
            rest = ln.split(":", 1)[1].strip()
            if rest in (">-", ">", "|", "|-", ">+", "|+", ""):
                rest = ""
            desc_lines.append(rest)
            mode = "desc"
        elif mode == "desc" and re.match(r"^[a-zA-Z_-]+:\s", ln):
            mode = None  # a new top-level key ended the description
        elif mode == "desc":
            desc_lines.append(ln.strip())
    desc = re.sub(r"\s+", " ", " ".join(desc_lines)).strip()
    return name, desc


def split_desc(desc):
    """Return (what_and_when, [triggers])."""
    m = re.search(r"\bTriggers:\s*", desc)
    if not m:
        return desc.rstrip(". "), []
    what = desc[:m.start()].strip().rstrip(". ") + "."
    triggers = [t.strip() for t in desc[m.end():].strip().rstrip(".").split(",") if t.strip()]
    return what, triggers


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main():
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    plugins = [(p["name"], p.get("description", "")) for p in market["plugins"]]

    total = 0
    by_plugin = {}
    for pname, pdesc in plugins:
        entries = []
        for sk in sorted(p for p in (ROOT / "plugins" / pname / "skills").iterdir() if p.is_dir()):
            fm = parse_frontmatter(sk / "SKILL.md")
            if not fm:
                continue
            name, desc = fm
            what, triggers = split_desc(desc)
            entries.append((name, what, triggers))
            total += 1
        by_plugin[pname] = (pdesc, entries)

    out = []
    w = out.append
    w("# Treasury Analyst Skills — trigger & capability catalog\n")
    w(f"Auto-generated from every skill's `SKILL.md` frontmatter by `scripts/gen-catalog.py`. "
      f"**{total} skills across {len(plugins)} plugins.**\n")

    w("## How to trigger a skill\n")
    w("There are two ways every skill fires:\n")
    w("1. **Automatically** — just describe your task in plain language. Claude matches your "
      "request against each skill's description and **trigger phrases** (listed below) and loads "
      "the right one on its own. You don't need to name it.\n")
    w("2. **Manually** — type the slash command `/{plugin}:{skill}` "
      "(e.g. `/cash-management-skills:bank-reconciliation`) to invoke a specific skill on demand.\n")
    w("Ask **\"what skills are available?\"** any time to list them.\n")

    w("## Install\n")
    w("```")
    w("/plugin marketplace add blakereaganlaw-droid/claude_skills_2")
    w(f"/plugin install <plugin>@{MARKET}      # e.g. cash-management-skills@{MARKET}")
    w("```")
    w("Install only the plugins you want; each is independent. Skills are namespaced "
      "`<plugin>:<skill>` so they never collide.\n")

    w("## Plugins\n")
    for pname, (pdesc, entries) in by_plugin.items():
        w(f"- [`{pname}`](#{slug(pname)}) ({len(entries)}) — {pdesc}")
    w("")

    for pname, (pdesc, entries) in by_plugin.items():
        w(f"## `{pname}`\n")
        w(f"{pdesc}\n")
        w(f"Install: `/plugin install {pname}@{MARKET}`\n")
        for name, what, triggers in entries:
            w(f"### `{pname}:{name}`\n")
            w(f"**Invoke:** `/{pname}:{name}` — or just describe the task.\n")
            w(f"**What it does:** {what}\n")
            if triggers:
                w("**Triggers:** " + ", ".join(f"`{t}`" for t in triggers) + "\n")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {total} skills across {len(plugins)} plugins.")


if __name__ == "__main__":
    main()
