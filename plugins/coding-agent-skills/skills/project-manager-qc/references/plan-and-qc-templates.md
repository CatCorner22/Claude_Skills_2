# Plan and QC templates — briefs, formats and the inline checklist

## Contents
- [The requirement ledger](#the-requirement-ledger)
- [Briefing the project-manager subagent](#briefing-the-project-manager-subagent)
- [Kickoff plan format (inline)](#kickoff-plan-format-inline)
- [The quality sweep as a checklist](#the-quality-sweep-as-a-checklist)
- [The punch-list bins](#the-punch-list-bins)
- [Acting on the gate's verdict](#acting-on-the-gates-verdict)

## The requirement ledger

Read the request or spec to the end, then write one line per requirement with its source words.
Later statements supersede earlier ones; strike the old line and point to the new one.
```
R1  outputs/kpis.csv, columns metric,value, no index column        (§4)
R2  period = September 2026                                         (§2)  → superseded by R9
R3  exclude internal accounts from signups AND orders               (§2)
...
R9  period boundaries in America/New_York, not UTC                 (§6 A1, supersedes R2)
R10 channel "partner" renamed "affiliate" in every output          (§6 A2)
Ambiguity: "sorted by the size of the difference" → absolute value, largest first (chosen; noted)
```
Each line becomes an acceptance check in the plan and a row in the sweep's first category.

## Briefing the project-manager subagent

Dispatch it as the `coding-agent-skills:project-manager` agent type when the plugin is installed;
otherwise paste the agent file's body as the prompt of a general-purpose subagent. Keep the brief
short: paths, not contents.

**PLAN**
```
MODE: PLAN
Goal: <one or two sentences, in the user's words>
Constraints: <deadline, budget, rules that must hold — e.g. never commit personal data>
Inputs (read as needed): <paths, URLs, existing notes>
Known decisions: <anything already settled, so it is not re-litigated>
Return the PLAN format, at most 60 lines.
```

**CHECKPOINT**
```
MODE: CHECKPOINT
Plan: <path to the plan, or the deliverables and budget in 5 lines>
Progress: <task list state in 5 lines>
Ledger: <path, or the usage figures so far>
Changed since the plan: <one or two lines>
Return the CHECKPOINT format, at most 40 lines.
```

**QC**
```
MODE: QC
Request or spec: <path>   (the subagent builds its own requirement ledger from it)
Acceptance criteria (if any beyond the request):
  1. <checkable criterion>
  2. ...
Deliverables: <paths>
Checks to run (read-only): <commands, e.g. bash scripts/validate.sh; python3 x.py --self-test>
Rails: <e.g. no personal data in committed files; every figure cited; repository git rules>
Do not modify anything. Return the QC format, at most 60 lines.
```

## Kickoff plan format (inline)

For a task of up to about ten steps, write this yourself in a few lines:
```
Outcome: <what done looks like>
Done when: <checkable test 1>; <test 2>
Steps: 1 <step> → 2 <step> → 3 <step> (parallel: 2a, 2b)
Delegate: <none | what and why>
Budget: <S/M/L>; cut first if short: <item>
```

## The quality sweep as a checklist

Walk every category to the end; the sweep is done when the list is, not when the findings feel
like enough. Re-open the request or spec rather than working from memory.
- [ ] **Requirements** — each ledger line, pass or fail, evidence from the artefact.
- [ ] **Numbers** — headline figures recomputed from source, independently of the code under review;
      totals that should agree across files agree.
- [ ] **Claims** — every statement in notes, summaries, changelogs, READMEs: true, false, unverifiable.
- [ ] **Code paths** — cleaned or filtered data actually used; boundaries; filters; joins; units.
- [ ] **Tests** — run; read what each asserts; does it exercise the shipped path? skipped or vacuous?
- [ ] **Files** — anything missing; anything that should not be there (debug dumps, personal data,
      secrets, a `.env` not covered by `.gitignore`).
- [ ] **Format** — headers and order, index columns, separators, decimals, line and word limits.
- [ ] **Examples** — documented commands run exactly as written.
- [ ] **Final message** — says what was done, what was verified, and what is left, in that order.

## The punch-list bins

Borrowed from The Foreman's draw inspection:
- **LOAD** — a criterion fails, a deliverable is missing, a claim is unsupported, or a rail is
  broken. Fix before delivery.
- **PUNCH** — real and worth fixing, but delivery does not rest on it. Fix soon; tell the user.
- **FUTURE** — never asked for and not needed now. Note it; do not build it into this delivery.

A list where everything is LOAD means the sort did not happen; a list where nothing is means the
inspection did not look.

## Acting on the gate's verdict
1. **PASS:** deliver, with the gate's evidence in one or two lines.
2. **HOLD:** fix every LOAD item, then send the subagent only the fixed items and their criteria
   for re-inspection — not the whole job again.
3. **Disagreement:** if you believe a LOAD item is wrong, show the evidence; do not overrule the
   gate silently. If it still stands, it is the user's call, asked once with both views.
