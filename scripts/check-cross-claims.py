#!/usr/bin/env python3
"""Find prose that asserts a countable fact about another skill's internals.

`validate.sh` already checks that every `plugin:skill` reference *resolves*.
Nothing checked whether the sentence around it is still *true*. Deepening
reflective-learner turned its four-step protocol into five steps, and three
inbound references in two other files kept saying "the four-step protocol" —
resolving perfectly, describing something that no longer existed.

This flags every "<count>-<noun> ... `plugin:skill`" claim so the count can be
checked against the target, and prefers the durable fix: name the thing
("the correction protocol") rather than count it ("the four-step protocol"),
so the next revision cannot invalidate the sentence.

ADVISORY, NOT A GATE. This is deliberately not wired into validate.sh. Tightening
it from a 200-character proximity window (39 hits, nearly all noise) down to
grammatically attached forms leaves 2 hits on the current tree: one a true claim
worth re-checking when its target changes, one a genuine false positive where the
count attaches to an earlier reference in the same sentence ("`A` for the
four-question debrief, and `B` for the doctrine"). A 2-hit advisory is useful; a
2-false-positive build error would train authors to ignore the validator, which
is the failure this repo's own anomaly-detection skill warns about.

Run it when you change a skill's internal structure — the phases, steps, gates, or
fields another skill might be describing. Exit 1 if any claim is found.
"""
import glob
import os
import re
import sys

WORDS = r"(?:two|three|four|five|six|seven|eight|nine|ten|\d+)"
NOUNS = r"(?:step|phase|stage|field|gate|rule|part|lens|question|column|tier|pass|check|law)"
CLAIM = re.compile(rf"\b{WORDS}[- ]{NOUNS}s?\b", re.I)
REF = re.compile(r"`([a-z0-9-]+-skills):([a-z0-9-]+)`")
# The count must be grammatically ATTACHED to the reference, not merely nearby.
# A 200-character proximity window produced 39 hits of which nearly all were a
# count belonging to the *citing* skill with an unrelated reference beside it —
# the alert-fatigue failure this repo's own anomaly-detection skill describes.
# Same sentence, close, and in one of the three shapes English actually uses.
BEFORE_REF = re.compile(rf"\b(?:the\s+)?({WORDS}[- ]{NOUNS}s?)\b[^.`]{{0,40}}$", re.I)
AFTER_REF = re.compile(rf"^(?:'s|\u2019s)\s+({WORDS}[- ]{NOUNS}s?)\b", re.I)
OF_REF = re.compile(rf"\b(?:the\s+)?({WORDS}[- ]{NOUNS}s?)\s+(?:of|in|from)\s+$", re.I)


def targets():
    return {f"{p.split('/')[1]}:{p.split('/')[3]}" for p in glob.glob("plugins/*/skills/*/SKILL.md")}


def main() -> int:
    known = targets()
    files = [f for f in (glob.glob("plugins/**/*.md", recursive=True)
                         + glob.glob("evals/**/*.md", recursive=True)
                         + glob.glob("docs/**/*.md", recursive=True)
                         + ["README.md", "CONTRIBUTING.md", "MEMORY.md"]) if os.path.isfile(f)]
    hits = []
    for path in files:
        text = open(path, encoding="utf-8", errors="replace").read()
        own = None
        parts = path.split("/")
        if parts[0] == "plugins" and len(parts) > 3:
            own = f"{parts[1]}:{parts[3]}"
        for m in REF.finditer(text):
            ref = f"{m.group(1)}:{m.group(2)}"
            if ref not in known or ref == own:
                continue                      # a skill counting its own parts is self-consistent
            before = text[max(0, m.start() - 80):m.start()]
            after = text[m.end():m.end() + 60]
            found = None
            c = OF_REF.search(before) or BEFORE_REF.search(before)
            # "…`after-action-review` for the blameless four-question debrief, and
            # `extreme-ownership` for the doctrine" — the count belongs to the FIRST
            # reference. If another reference sits between the count and this one, it
            # is not this skill's claim.
            if c and REF.search(before[c.end(1):]):
                c = None
            if c:
                found = (c.group(1), "before")
            else:
                c = AFTER_REF.match(after)
                if c:
                    found = (c.group(1), "after")
            if found:
                line = text.count("\n", 0, m.start()) + 1
                hits.append((path, line, found[0], ref, found[1]))
    for path, line, claim, ref, side in hits:
        print(f"CROSS-CLAIM {path}:{line}: \"{claim}\" ({side} the reference) asserts a count "
              f"about `{ref}` — verify it, or name the thing instead of counting it")
    print(f"== cross-skill count claims: {len(hits)} to verify ==")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
