#!/usr/bin/env python3
"""Simulate the Claude Code skill-listing character budget against this library.

Why this exists
---------------
`docs/live-routing-and-degradation-2026-08-18.md` originally reported the degradation
mechanism from a *model introspecting its own system reminder* ("101 of 121 NAMEONLY").
That instrument did not reproduce, and the account it produced was wrong: it described
an install-order fill with a hard cutoff and explicitly denied usage was involved.

The mechanism below was instead read out of the shipped CLI binary (v2.1.235) and is
reimplemented here so the numbers in that document are checkable by anyone, offline,
without introspection and without spending money on eval runs.

The mechanism, as shipped
-------------------------
Budget:
    SLASH_COMMAND_TOOL_CHAR_BUDGET            if set, wins outright
    else max(1, floor(context_tokens * 4 * skillListingBudgetFraction))
      * 4    = the harness's chars-per-token constant
      * 0.01 = skillListingBudgetFraction default
      * 200000 = default context, so the default budget is 8,000 characters
    skillListingMaxDescChars default 1536 caps each description.

Selection:
    1. every candidate starts rendered name-only as "- {name}"  (len(name) + 2)
    2. bundled skills are PROTECTED: always full, never candidates
    3. candidates sort DESCENDING by
           usageCount * max(0.5 ** (daysSinceUse / 7), 0.1)
       and a skill never used scores exactly 0
    4. walk that order, upgrading name-only -> full whenever the incremental cost
       fits the remaining budget; otherwise SKIP IT AND CONTINUE (there is no cutoff)

Consequence worth remembering: in a fresh session every score is 0, so the sort is
stable and candidates keep listing order. The install-order pattern that was observed
live is that degenerate all-zero-usage case -- not a separate algorithm.

Usage
-----
    python3 scripts/simulate-listing-budget.py
    python3 scripts/simulate-listing-budget.py --context 1000000
    python3 scripts/simulate-listing-budget.py --budget 8000 --list
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

CHARS_PER_TOKEN = 4          # harness constant (fgf)
DEFAULT_CONTEXT = 200_000    # harness default (F7v)
DEFAULT_FRACTION = 0.01      # skillListingBudgetFraction default (B7v)
MAX_DESC_CHARS = 1536        # skillListingMaxDescChars default (U7v)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_skills() -> list[tuple[str, str]]:
    """Return [(qualified_name, description)] for every skill in the library."""
    out = []
    pattern = os.path.join(REPO, "plugins", "*", "skills", "*", "SKILL.md")
    for path in sorted(glob.glob(pattern)):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+?)\s*$", fm, re.M)
        if not name:
            continue
        # description is a YAML folded scalar (">-"); take the indented block after it
        desc_m = re.search(r"^description:\s*>-?\s*\n((?:[ \t]+.*\n?)+)", fm, re.M)
        if desc_m:
            desc = " ".join(desc_m.group(1).split())
        else:
            flat = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
            desc = " ".join(flat.group(1).split()) if flat else ""
        plugin = path.split(os.sep)[-4]
        out.append((f"{plugin}:{name.group(1)}", desc[:MAX_DESC_CHARS]))
    return out


def budget_for(context_tokens: int, fraction: float) -> int:
    env = os.environ.get("SLASH_COMMAND_TOOL_CHAR_BUDGET")
    if env and env.strip().isdigit():
        return int(env.strip())
    return max(1, int(context_tokens * CHARS_PER_TOKEN * fraction))


def name_only_cost(name: str) -> int:
    return len(name) + 2                      # "- {name}", exactly as the code computes it


def full_cost(name: str, desc: str) -> int:
    return len(name) + len(desc) + 4          # "- {name}: {desc}"


def simulate(skills, budget, usage=None):
    """Return (baseline_chars, upgraded_indices, slack_left)."""
    n = len(skills)
    baseline = sum(name_only_cost(nm) for nm, _ in skills) + max(0, n - 1)
    slack = budget - baseline
    scores = usage if usage else [0.0] * n
    order = sorted(range(n), key=lambda i: -scores[i])   # stable: ties keep listing order
    upgraded = set()
    for i in order:
        nm, desc = skills[i]
        inc = full_cost(nm, desc) - name_only_cost(nm)
        if inc <= slack:
            upgraded.add(i)
            slack -= inc
    return baseline, upgraded, slack


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--context", type=int, default=None,
                    help=f"context window in tokens (default {DEFAULT_CONTEXT})")
    ap.add_argument("--fraction", type=float, default=DEFAULT_FRACTION,
                    help=f"skillListingBudgetFraction (default {DEFAULT_FRACTION})")
    ap.add_argument("--budget", type=int, default=None,
                    help="override the computed budget with an explicit character count")
    ap.add_argument("--list", action="store_true",
                    help="list which skills keep a description")
    args = ap.parse_args()

    skills = load_skills()
    if not skills:
        print("no skills found — run from the repo", file=sys.stderr)
        return 1

    full_listing = sum(full_cost(nm, d) for nm, d in skills) + len(skills) - 1
    name_listing = sum(name_only_cost(nm) for nm, _ in skills) + len(skills) - 1

    print(f"library: {len(skills)} skills")
    print(f"  full listing (every description):  {full_listing:>8,} chars")
    print(f"  name-only listing (bare names):    {name_listing:>8,} chars")
    print(f"  full listing as % of a 200K window's char equivalent: "
          f"{full_listing / (DEFAULT_CONTEXT * CHARS_PER_TOKEN) * 100:.2f}%")
    print()

    if args.budget is not None:
        rows = [("explicit", args.budget)]
    elif args.context is not None:
        rows = [(f"{args.context:,} tok", budget_for(args.context, args.fraction))]
    else:
        rows = [(f"{c:,} tok", budget_for(c, args.fraction))
                for c in (DEFAULT_CONTEXT, 750_000, 1_000_000)]

    print(f"{'context':>14}  {'budget':>9}  {'full desc':>10}  {'name-only':>10}  {'slack':>7}")
    for label, budget in rows:
        baseline, upgraded, slack = simulate(skills, budget)
        if baseline > budget:
            note = f"  <-- bare names alone exceed budget by {baseline - budget:,}"
        else:
            note = ""
        print(f"{label:>14}  {budget:>9,}  {len(upgraded):>10}  "
              f"{len(skills) - len(upgraded):>10}  {slack:>7,}{note}")
        if args.list:
            keep = sorted(skills[i][0] for i in upgraded)
            print("      keeps a description: " + (", ".join(keep) if keep else "(none)"))
    print()
    print("All zero usage assumed (a fresh session). Because the real sort key is")
    print("usageCount * max(0.5**(days/7), 0.1), a returning user's frequently-used")
    print("skills win the budget instead -- the arbitrary case is the first session.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # piping into `head` closes stdout early; exit quietly like any unix filter
        try:
            sys.stdout.close()
        finally:
            os._exit(0)
