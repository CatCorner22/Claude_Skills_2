#!/usr/bin/env python3
"""Guard the trigger-test protocol against measuring the wrong thing.

A positive prompt asks whether a skill is reachable by someone who does NOT know
its name. A prompt that contains one of the target's own trigger phrases asks a
different question — is this string in the description? — and passes for the
wrong reason. That defect has now shipped twice: once in Tier D, and once in
Tier F, where a row pasted two of its target's twelve triggers verbatim.

The second time is why this script no longer looks only at Tier D. **It walks
every tier**, because an invariant enforced in one section is an invariant that
quietly fails everywhere else. Tables are matched by their header cells rather
than by position, so a layout change surfaces as a skipped table rather than as
a silent pass.

Negative-control tiers are exempt by design: where the column says "must NOT
load", a prompt sitting near a trigger phrase *is* the test.

Some overlaps are also legitimate in a positive prompt, and pretending otherwise
would make the gate noise. A user really does paste a database error verbatim,
and a skill whose trigger is an ordinary word ("prompt", "forecast") cannot be
asked about in words that avoid it. Those need an exemption **with a written
reason**, recorded in the protocol itself as:

    <!-- trigger-overlap-ok: E4 "too many connections" — why this one is real -->

An exemption without a reason, or for a row that no longer leaks, is itself a
failure: the point is that the justification is reviewable, not that the number
goes green.

Run from the repo root.
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


def _cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _tables(section: str):
    """Yield (header_cells, [row_cells, ...]) for every markdown table in a section."""
    lines = section.splitlines()
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("|") and set(lines[i + 1].replace("|", "").strip()) <= {"-", ":"}:
            header = _cells(lines[i])
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                rows.append(_cells(lines[j]))
                j += 1
            yield header, rows
            i = j
        else:
            i += 1


def _column(header, *needles, exclude=()):
    for idx, cell in enumerate(header):
        low = cell.lower().replace("*", "")
        if any(n in low for n in needles) and not any(x in low for x in exclude):
            return idx
    return None


def main() -> int:
    text = open(PROTOCOL, encoding="utf-8").read().split("\n## Log")[0]
    sections = re.split(r"\n(?=## )", text)

    exempt = {}
    marker = re.compile(r'<!--\s*trigger-overlap-ok:\s*(\S+)\s+"([^"]+)"\s*[—-]+\s*(.+?)\s*-->')
    for rid, phrase, reason in marker.findall(text):
        exempt[(rid.strip(), phrase.strip().lower())] = reason.strip()

    checked = 0
    problems = []
    skipped = []
    used_exemptions = set()
    for section in sections:
        title = section.splitlines()[0].strip("# ").strip() if section.strip() else ""
        if not title.lower().startswith("tier"):
            continue
        for header, rows in _tables(section):
            # The target skill: a "Must load" column, or Tier D's trailing "Skill" column.
            skill_idx = _column(header, "must load", exclude=("must not",))
            if skill_idx is None:
                skill_idx = _column(header, "skill")
            # The positive prompt, never a near-miss or out-of-scope column.
            prompt_idx = _column(header, "prompt", "in-scope",
                                 exclude=("near-miss", "out-of-scope", "must not"))
            if skill_idx is None or prompt_idx is None:
                # A negative-control table has no positive prompt to guard; anything else
                # is a layout change worth reporting rather than passing silently.
                if _column(header, "must not load") is None:
                    skipped.append(f"{title}: no prompt/skill column pair found")
                continue
            for row in rows:
                if len(row) <= max(skill_idx, prompt_idx):
                    continue
                rid = row[0]
                if "~~" in rid:          # retired row
                    continue
                prompt = row[prompt_idx].strip("`")
                skill = row[skill_idx].strip("`").strip()
                if ":" not in skill or not prompt:
                    continue
                tl = triggers(skill)
                if tl is None:
                    problems.append(f"{rid}: target skill `{skill}` does not exist")
                    continue
                checked += 1
                leaked = []
                for t in tl:
                    if t not in prompt.lower():
                        continue
                    if (rid, t) in exempt:
                        used_exemptions.add((rid, t))
                        continue
                    leaked.append(t)
                if leaked:
                    problems.append(f"{rid}: positive prompt contains {skill}'s own trigger(s): "
                                    + ", ".join(repr(t) for t in leaked))

    for p in problems:
        print("TRIGGER-TEST: " + p)
    for sk in skipped:
        print("TRIGGER-TEST: SKIPPED " + sk)
    for key in sorted(set(exempt) - used_exemptions):
        problems.append(f"{key[0]}: stale exemption for {key[1]!r} — that prompt no longer "
                        "contains the phrase, so remove the marker")
        print(f"TRIGGER-TEST: {problems[-1]}")
    for key in sorted(used_exemptions):
        print(f"TRIGGER-TEST: exempt {key[0]} {key[1]!r} — {exempt[key]}")
    if not checked:
        print(f"{PROTOCOL}: no rows parsed — check the tier table layouts")
        return 2
    print(f"== trigger-test protocol: {checked - len(problems)}/{checked} positive prompts "
          f"across all tiers are free of their target's trigger phrases ==")
    return 1 if problems or skipped else 0


if __name__ == "__main__":
    sys.exit(main())
