#!/usr/bin/env python3
"""Measure what installing this library costs a context window.

Claude sees every installed skill's `name` and `description` on every turn,
whether or not any of them is used. That listing is the library's standing tax,
and it is the number that decides how many plugins a person should install.

Prints the per-plugin table and the bundle table exactly as README.md carries
them, so the README can be refreshed instead of re-derived. The figure went
stale within a day of being measured by hand, which is why it is a script.

Tokens are estimated at 3.7 characters/token — measured against this library's
own prose, not assumed. Treat the percentages as accurate to a tenth.

    python3 scripts/measure-listing-cost.py
"""
import collections
import glob
import re
import sys

CHARS_PER_TOKEN = 3.7
CONTEXT = 200_000

BUNDLES = {
    "Analyst": ["data-analytics-bi-skills", "data-tools-skills", "math-foundations-skills"],
    "Developer": ["full-stack-dev-skills", "coding-agent-skills"],
    "Operations / process": ["continuous-improvement-skills", "safety-and-reliability-skills"],
    "Management / communication": ["collaboration-skills", "writing-skills",
                                   "decision-science-skills"],
}


def listing_chars(path: str) -> int:
    """Characters Claude sees for one skill: its name plus its description."""
    text = open(path, encoding="utf-8", errors="replace").read()
    end = text.find("\n---", 3)
    front = text[3:end]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"description:\s*>-\s*\n((?:[ \t]{2,}.*\n)+)", front)
    if not name or not desc:
        raise SystemExit(f"{path}: cannot read name/description")
    body = " ".join(line.strip() for line in desc.group(1).splitlines())
    return len(name.group(1).strip()) + len(body)


def main() -> int:
    per = collections.Counter()
    count = collections.Counter()
    for path in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
        plugin = path.split("/")[1]
        per[plugin] += listing_chars(path)
        count[plugin] += 1

    total = sum(per.values())
    skills = sum(count.values())
    print(f"Measured across all {skills} skills: **{total:,} characters ≈ "
          f"{round(total / CHARS_PER_TOKEN):,} tokens ≈ "
          f"{total / CHARS_PER_TOKEN / CONTEXT * 100:.1f}% of a 200K context**\n")

    print("| Plugin | Skills | ~Tokens | % of 200K |")
    print("|---|---|---|---|")
    for plugin, chars in sorted(per.items(), key=lambda kv: -kv[1]):
        print(f"| `{plugin}` | {count[plugin]} | {round(chars / CHARS_PER_TOKEN):,} "
              f"| {chars / CHARS_PER_TOKEN / CONTEXT * 100:.2f}% |")
    print(f"| **all {len(per)}** | **{skills}** | **{round(total / CHARS_PER_TOKEN):,}** "
          f"| **{total / CHARS_PER_TOKEN / CONTEXT * 100:.2f}%** |")

    print("\n| Bundle | Plugins | Skills | ~Tokens | % of 200K |")
    print("|---|---|---|---|---|")
    for label, plugins in BUNDLES.items():
        missing = [p for p in plugins if p not in per]
        if missing:
            print(f"| {label} | MISSING: {', '.join(missing)} | — | — | — |")
            continue
        chars = sum(per[p] for p in plugins)
        n = sum(count[p] for p in plugins)
        names = " + ".join(f"`{p}`" for p in plugins)
        print(f"| {label} | {names} | {n} | {round(chars / CHARS_PER_TOKEN):,} "
              f"| {chars / CHARS_PER_TOKEN / CONTEXT * 100:.2f}% |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
