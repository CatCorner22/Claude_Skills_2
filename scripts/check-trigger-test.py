#!/usr/bin/env python3
"""Guard the trigger-test protocol against measuring the wrong thing.

Tier D's middle column asks whether a persona skill is reachable by someone who
does NOT know its name. A prompt in that column that contains one of the
target's own trigger phrases asks a different question — is this string in the
description? — and passes for the wrong reason. That defect shipped once and
made the tier report a clean result it had not earned.

This checks the invariant mechanically: no Tier D in-scope prompt may contain
any trigger phrase of its target skill. Run from the repo root.
"""
import re
import sys

PROTOCOL = "docs/trigger-test.md"
MIN_PHRASE = 4          # below this, a "trigger" is a fragment that matches by accident


def triggers(skill: str):
    plugin, name = skill.split(":")
    path = f"plugins/{plugin}/skills/{name}/SKILL.md"
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        return None
    end = text.find("\n---", 3)
    m = re.search(r"description:\s*>-\s*\n((?:[ \t]{2,}.*\n)+)", text[3:end])
    if not m:
        return []
    desc = " ".join(line.strip() for line in m.group(1).splitlines())
    i = desc.lower().rfind("triggers:")
    if i < 0:
        return []
    return [t.strip().strip(".").lower()
            for t in desc[i + len("triggers:"):].split(",")
            if len(t.strip()) >= MIN_PHRASE]


def main() -> int:
    text = open(PROTOCOL, encoding="utf-8").read().split("\n## Log")[0]
    tier_d = re.search(r"## Tier D.*?(?=\n## |\Z)", text, re.S)
    if not tier_d:
        print(f"{PROTOCOL}: no Tier D section found — check the protocol's headings")
        return 2

    rows = re.findall(r"^\| (D\d+) \| `([^`]*)` \| `([^`]*)` \| `([^`]*)` \| `([^`]*)` \|",
                      tier_d.group(0), re.M)
    if not rows:
        print(f"{PROTOCOL}: Tier D table did not parse — check its column layout")
        return 2

    problems = []
    for rid, _by_name, in_scope, _out, skill in rows:
        tl = triggers(skill)
        if tl is None:
            problems.append(f"{rid}: target skill `{skill}` does not exist")
            continue
        leaked = [t for t in tl if t in in_scope.lower()]
        if leaked:
            problems.append(f"{rid}: in-scope prompt contains {skill}'s own trigger(s): "
                            + ", ".join(repr(t) for t in leaked))

    for p in problems:
        print("TRIGGER-TEST: " + p)
    print(f"== trigger-test protocol: {len(rows) - len(problems)}/{len(rows)} Tier D in-scope "
          f"prompts are free of their target's trigger phrases ==")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
