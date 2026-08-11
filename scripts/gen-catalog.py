#!/usr/bin/env python3
"""Generate the library's two catalogs from every skill's SKILL.md frontmatter:

- docs/SKILLS.md — the full trigger & capability catalog (per plugin, per skill)
- docs/INDEX.md  — the quick router: when to use / optimized for / how to trigger,
                   grouped by marketplace category, plus the archived-plugins manifest

Usage: python3 scripts/gen-catalog.py   (run from anywhere; paths resolve relative to the repo root)
Re-run this whenever skills are added, removed, or their descriptions change.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_CATALOG = ROOT / "docs" / "SKILLS.md"
OUT_INDEX = ROOT / "docs" / "INDEX.md"
ARCHIVE = ROOT / "archive" / "plugins"
MARKET = "treasury-analyst-skills"

# Fixed display order + labels for marketplace categories.
CATEGORY_ORDER = ["research", "operations", "development", "data", "writing", "finance", "reporting"]
CATEGORY_LABELS = {
    "research": "Research & decision-making",
    "operations": "Operations, safety & collaboration",
    "development": "Development & coding agents",
    "data": "Data, analytics & math",
    "writing": "Writing & communication",
    "finance": "Finance",
    "reporting": "Reporting",
}


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
        elif mode == "desc" and re.match(r"^[a-zA-Z_-]+:(\s|$)", ln):
            mode = None  # a new top-level key (incl. bare 'metadata:') ends the description
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


def sentences(text):
    """Naive sentence split that tolerates the em-dash-heavy house style."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", text)
    return [p.strip() for p in parts if p.strip()]


def index_fields(what):
    """Derive (optimized_for, when_to_use) deterministically from the what-part.

    optimized_for = the first sentence (the lead capability clause).
    when_to_use   = the first sentence starting with 'Use ' (the house 'Use when...'
                    convention); falls back to the second sentence, then the first.
    """
    sents = sentences(what)
    if not sents:
        return "", ""
    optimized = sents[0]
    when = next((s for s in sents if re.match(r"^Use\b", s)), None)
    if when is None:
        when = sents[1] if len(sents) > 1 else sents[0]
    return optimized, when


def cell(text, limit=240):
    """Make text safe and scannable inside a markdown table cell."""
    text = text.replace("|", "\\|").strip()
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def collect():
    """Parse the marketplace + every active skill.

    Returns (plugins, total) where plugins is a list of dicts:
    {name, description, category, entries: [(skill, what, triggers)]}
    """
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    plugins = []
    total = 0
    for p in market["plugins"]:
        pname = p["name"]
        entries = []
        for sk in sorted(d for d in (ROOT / "plugins" / pname / "skills").iterdir() if d.is_dir()):
            fm = parse_frontmatter(sk / "SKILL.md")
            if not fm:
                continue
            name, desc = fm
            what, triggers = split_desc(desc)
            entries.append((name, what, triggers))
            total += 1
        plugins.append({
            "name": pname,
            "description": p.get("description", ""),
            "category": p.get("category", "uncategorized"),
            "entries": entries,
        })
    return plugins, total


def collect_archived():
    """Read archived plugins (if any) for the index's manifest section."""
    rows = []
    if not ARCHIVE.is_dir():
        return rows
    for pdir in sorted(d for d in ARCHIVE.iterdir() if d.is_dir()):
        manifest = pdir / ".claude-plugin" / "plugin.json"
        desc, version = "", ""
        if manifest.is_file():
            try:
                data = json.loads(manifest.read_text())
                desc = data.get("description", "")
                version = data.get("version", "")
            except json.JSONDecodeError:
                pass
        n_skills = len([d for d in (pdir / "skills").iterdir() if d.is_dir()]) if (pdir / "skills").is_dir() else 0
        rows.append((pdir.name, n_skills, version, desc))
    return rows


def emit_catalog(plugins, total):
    out = []
    w = out.append
    w("# Skills Library — trigger & capability catalog\n")
    w(f"Auto-generated from every skill's `SKILL.md` frontmatter by `scripts/gen-catalog.py`. "
      f"**{total} skills across {len(plugins)} plugins.** "
      f"For the quick when-to-use router, see [INDEX.md](INDEX.md).\n")

    w("## How to trigger a skill\n")
    w("There are two ways every skill fires:\n")
    w("1. **Automatically** — just describe your task in plain language. Claude matches your "
      "request against each skill's description and **trigger phrases** (listed below) and loads "
      "the right one on its own. You don't need to name it.\n")
    w("2. **Manually** — type the slash command `/{plugin}:{skill}` "
      "(e.g. `/decision-science-skills:pre-mortem`) to invoke a specific skill on demand.\n")
    w("Ask **\"what skills are available?\"** any time to list them.\n")

    w("## Install\n")
    w("```")
    w("/plugin marketplace add blakereaganlaw-droid/claude_skills_2")
    w(f"/plugin install <plugin>@{MARKET}      # e.g. decision-science-skills@{MARKET}")
    w("```")
    w("Install only the plugins you want; each is independent. Skills are namespaced "
      "`<plugin>:<skill>` so they never collide.\n")

    w("## Plugins\n")
    for p in plugins:
        w(f"- [`{p['name']}`](#{slug(p['name'])}) ({len(p['entries'])}) — {p['description']}")
    if ARCHIVE.is_dir():
        w("")
        w("Archived plugins (delisted, preserved, restorable) are documented in "
          "[archive/README.md](../archive/README.md) and indexed in [INDEX.md](INDEX.md).")
    w("")

    for p in plugins:
        w(f"## `{p['name']}`\n")
        w(f"{p['description']}\n")
        w(f"Install: `/plugin install {p['name']}@{MARKET}`\n")
        for name, what, triggers in p["entries"]:
            w(f"### `{p['name']}:{name}`\n")
            w(f"**Invoke:** `/{p['name']}:{name}` — or just describe the task.\n")
            w(f"**What it does:** {what}\n")
            if triggers:
                w("**Triggers:** " + ", ".join(f"`{t}`" for t in triggers) + "\n")

    return "\n".join(out) + "\n"


def emit_index(plugins, total):
    archived = collect_archived()
    out = []
    w = out.append
    w("# Skill Index — when to use, what it's optimized for, how to trigger\n")
    w(f"Auto-generated by `scripts/gen-catalog.py` from the same frontmatter as "
      f"[SKILLS.md](SKILLS.md) (the full catalog). **{total} active skills across "
      f"{len(plugins)} plugins**" +
      (f", plus {len(archived)} archived plugins (see [bottom](#archived-plugins))." if archived else ".") + "\n")
    w("Every skill fires two ways: **describe the task** in words like its trigger phrases, "
      "or **invoke directly** with `/{plugin}:{skill}`.\n")

    # Group plugins by category, in fixed order.
    by_cat = {}
    for p in plugins:
        by_cat.setdefault(p["category"], []).append(p)
    cats = [c for c in CATEGORY_ORDER if c in by_cat] + sorted(set(by_cat) - set(CATEGORY_ORDER))

    w("## Contents\n")
    for cat in cats:
        label = CATEGORY_LABELS.get(cat, cat.title())
        names = ", ".join(f"`{p['name']}`" for p in by_cat[cat])
        w(f"- [{label}](#{slug(label)}) — {names}")
    if archived:
        w("- [Archived plugins](#archived-plugins)")
    w("")

    for cat in cats:
        label = CATEGORY_LABELS.get(cat, cat.title())
        w(f"## {label}\n")
        for p in by_cat[cat]:
            w(f"### `{p['name']}`\n")
            w(f"{p['description']}\n")
            w("| Skill | Optimized for | When to use | Say (or `/invoke`) |")
            w("|---|---|---|---|")
            for name, what, triggers in p["entries"]:
                optimized, when = index_fields(what)
                say = ", ".join(f"`{t}`" for t in triggers[:4]) + (", …" if len(triggers) > 4 else "")
                if not say:
                    say = f"`/{p['name']}:{name}`"
                w(f"| **{name}** | {cell(optimized)} | {cell(when)} | {cell(say, 200)} |")
            w("")

    if archived:
        w("## Archived plugins\n")
        w("Delisted from the marketplace but preserved in `archive/plugins/` with full git "
          "history — see [archive/README.md](../archive/README.md) for the why and the "
          "restore procedure. Locally installed copies keep working as version-pinned "
          "snapshots; they simply no longer receive updates.\n")
        w("| Plugin | Skills | Last version | What it covered |")
        w("|---|---|---|---|")
        for name, n_skills, version, desc in archived:
            w(f"| `{name}` | {n_skills} | {version or '—'} | {cell(desc, 200)} |")
        w("")

    return "\n".join(out) + "\n"


def main():
    plugins, total = collect()
    OUT_CATALOG.parent.mkdir(parents=True, exist_ok=True)
    OUT_CATALOG.write_text(emit_catalog(plugins, total), encoding="utf-8")
    OUT_INDEX.write_text(emit_index(plugins, total), encoding="utf-8")
    archived = collect_archived()
    arch_note = f" (+{len(archived)} archived)" if archived else ""
    print(f"Wrote docs/SKILLS.md and docs/INDEX.md — {total} skills across {len(plugins)} plugins{arch_note}.")


if __name__ == "__main__":
    main()
