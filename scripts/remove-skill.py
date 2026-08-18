#!/usr/bin/env python3
"""Report everything that breaks if a skill is removed, and optionally remove it.

Deleting a skill directory is the easy part. What breaks is everything pointing at
it: sibling skills' `Not for:` seams, the eval, the catalogs, and any prose that
names it. A pointer to a skill that no longer exists is worse than no pointer —
it sends a reader somewhere that is gone — so this script refuses to delete
silently and prints every inbound reference for a human to rewrite.

    python3 scripts/remove-skill.py <plugin>:<skill> [more...]        # dry run
    python3 scripts/remove-skill.py --apply <plugin>:<skill> [more...]

--apply removes the skill directory and its eval, then re-prints the inbound
references that now need rewriting BY HAND. It deliberately does not attempt an
automatic rewrite: each seam says something specific about why this is not the
skill for that job, and that sentence has to survive the edit.
"""
import glob
import os
import re
import shutil
import subprocess
import sys


def all_skills():
    return {f"{p.split('/')[1]}:{p.split('/')[3]}": os.path.dirname(p)
            for p in glob.glob("plugins/*/skills/*/SKILL.md")}


def searchable():
    files = (glob.glob("plugins/**/*.md", recursive=True)
             + glob.glob("docs/**/*.md", recursive=True)
             + glob.glob("evals/**/*.md", recursive=True)
             + ["README.md", "CONTRIBUTING.md", "MEMORY.md"])
    return [f for f in files if os.path.isfile(f)]


def inbound(target, skip_dir):
    """Every file:line naming this skill, outside the skill's own directory."""
    out = []
    for f in searchable():
        if os.path.abspath(f).startswith(os.path.abspath(skip_dir) + os.sep):
            continue
        for n, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            if target in line:
                out.append((f, n, line.strip()))
    return out


def main(argv) -> int:
    apply = "--apply" in argv
    targets = [a for a in argv if not a.startswith("--")]
    if not targets:
        print(__doc__)
        return 2

    known = all_skills()
    unknown = [t for t in targets if t not in known]
    if unknown:
        print(f"unknown skill(s): {', '.join(unknown)}")
        return 2

    plugins = sorted({t.split(":")[0] for t in targets})
    print(f"Removing {len(targets)} skill(s) from {len(plugins)} plugin(s): {', '.join(plugins)}\n")

    total_refs = 0
    for t in targets:
        d = known[t]
        ev = f"evals/{t.split(':')[0]}/{t.split(':')[1]}.md"
        # references from OTHER skills being removed in the same batch do not count:
        # they are going away too.
        refs = [r for r in inbound(t, d)
                if not any(os.path.abspath(r[0]).startswith(os.path.abspath(known[o]) + os.sep)
                           for o in targets if o != t)]
        total_refs += len(refs)
        print(f"── {t}")
        print(f"   dir   {d}  ({len(glob.glob(d + '/**/*', recursive=True))} paths)")
        print(f"   eval  {ev}  {'✓' if os.path.exists(ev) else 'MISSING'}")
        if refs:
            print(f"   {len(refs)} inbound reference(s) — each needs a hand-written replacement:")
            for f, n, line in refs:
                print(f"      {f}:{n}")
                print(f"         {line[:150]}")
        else:
            print("   no inbound references")
        print()

    if not apply:
        print(f"DRY RUN — nothing removed. {total_refs} reference(s) would need rewriting.")
        print("Re-run with --apply once you have a replacement in mind for each one.")
        return 0

    for t in targets:
        d = known[t]
        ev = f"evals/{t.split(':')[0]}/{t.split(':')[1]}.md"
        for path in (d, ev):
            if not os.path.exists(path):
                continue
            rc = subprocess.run(["git", "rm", "-r", "-q", path],
                                capture_output=True).returncode
            if rc != 0:                       # untracked; fall back to the filesystem
                shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
        print(f"removed {t}")

    print(f"\n{total_refs} inbound reference(s) are now DANGLING. Rewrite each to name the "
          f"capability or domain instead of the skill, keeping the boundary the line was drawing.")
    print("Then: bump each touched plugin, run scripts/validate.sh and scripts/gen-catalog.py.")
    return 1 if total_refs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
