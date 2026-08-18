# Lean review checklist (reference)

## Contents
- PR review checklist
- Signs of over-engineering
- Deletion opportunities
- Net-lines discipline
- What a finished lean review contains (deliverable contract)
- Worked example: the review artifact

## PR review checklist
- [ ] Could a stdlib/framework feature replace any hand-rolled logic here?
- [ ] Does every new parameter/option have a caller who needs it *today*?
- [ ] Any abstraction with only one implementation? (Inline it.)
- [ ] Any helper called exactly once that doesn't clarify? (Inline it.)
- [ ] Public surface: did anything become exported/optional/configurable without need?
- [ ] Are there tests for behavior, not for implementation details that block refactors?
- [ ] Is the diff's *net* line count justified by the behavior change?
- [ ] Anything in this PR that could be deleted instead of modified?

## Signs of over-engineering
| Sign | Smell | Lean fix |
|---|---|---|
| Interface/ABC with one implementation | Speculative polymorphism | Concrete class; extract when the second impl exists |
| `utils.py` growing unrelated helpers | Abstraction landfill | Move helpers next to their single caller |
| Deep config objects / factory factories | Flexibility nobody used | Default args; hard-code until needed |
| Wrapper around a library "to swap it later" | Vendor-change insurance you'll never claim | Use the library directly; migrations are rewrites anyway |
| Generic event bus for two functions | Architecture cosplay | A function call |
| Feature flags older than a quarter | Shipped or dead | Delete flag + dead branch |
| Comments explaining clever code | Cleverness tax | Rewrite boring; delete the comment |

## Deletion opportunities (hunt monthly)
- Unused dependencies — `deptry` or `pipreqs` for Python, `depcheck` for Node. Not `pip-audit`
  (CVEs) and not `npm ls` (prints the installed tree): neither answers "which declared
  dependency is never imported", so both report clean on a project full of unused deps.
- Dead endpoints/routes (access logs say nobody calls them)
- Commented-out code and TODOs older than 6 months (do or delete)
- Duplicate near-copies that drifted (merge or delete one)
- Tests that test mocks, not behavior

## Net-lines discipline
Track per PR: `+added / −deleted / net`. Healthy mature codebases trend near zero net while
shipping features. Celebrate the negative-net feature PR in review — it's the strongest
signal the discipline is working. Celebrate it as an outcome, never set it as a target:
see the last tell in `earning-abstractions.md`, where the deleted retry that was absorbing
a real flake is a negative diff and a worse system.

## What a finished lean review contains (deliverable contract)

A lean review is not a set of opinions in a PR thread. It is an artifact with eight parts,
and a reviewer who leaves out parts 6–8 has produced the failure mode this skill exists to
prevent: a smaller codebase that is worse.

1. **Net-lines line per file group** — added, deleted, net. Per group, not one repo-wide
   number, so a large deletion cannot hide a large addition somewhere else.
2. **Each proposed deletion with its evidence.** Not "this looks unused" — the actual
   proof: a callers grep that returns nothing, an access-log window with the number of days
   and zero hits, the date a feature flag reached 100%. A deletion without evidence is a
   guess with a merge button.
3. **Each proposed inline, with before/after and the count** — including the test lines the
   inline removes, which are usually where most of the saving is.
4. **Each abstraction kept, with the gate it passes** — name the gate and the evidence
   (the four gates are in the sibling reference `earning-abstractions.md`). "Seems fine"
   is not a gate.
5. **Each abstraction removed, with the gate it fails.** Naming the failed gate is what
   makes the review teachable and what stops the same extraction being re-proposed next
   quarter.
6. **A "not touched, and why" list.** Code that looks redundant but sits on the
   irreversible-cost list, or duplication that fails gate 1 deliberately. Without this
   section, everything the review left alone reads as something the reviewer missed.
7. **Behaviour-preservation evidence.** Which tests cover the changed lines, run before and
   after, with the result. If no test covers them, writing one is the first item of work,
   not the last — a simplification with no test is a rewrite with no test.
8. **What was not done, and why.** Scope you found and deliberately did not take, so it is
   a filed item rather than a thing everyone assumed the other person saw.

## Worked example: the review artifact

Against the three-CSV-export change in `earning-abstractions.md`. The shape is the
deliverable; the log windows, commit ratios, and flag ages below are an illustration of
what evidence looks like when written down, not measurements from a real project.

```
Lean review — PR 214, "CSV exports"

1. Net lines
     app/exports/     +35  −240  net −205
     tests/exports/   +14  −33   net −19
     total                       net −224

2. Deletions, with evidence
     exports/legacy_xlsx.py (183 lines) — no route registers it since the
       /exports/v2 cutover; 90 days of access logs, zero hits on any path in it.
     FEATURE_CSV_STREAMING flag (11 lines, the dead branch included) — set true in every
       environment for 7 months; last toggle in config history is the enable.

3. Inlines
     _fmt_money(v) -> f"{v:.2f}" — one call site after this change.
       −4 lines in the module, −6 in the test that asserted f-string behaviour.

4. Abstractions kept
     csv_response(filename, header, rows) — gate 1: 4 of the last 11 commits
       touching any export handler touched two of them, every one an envelope
       change (disposition quoting, media type, BOM). Gates 2–4: 3 params, none
       behaviour-selecting, call sites readable without opening it.

5. Abstractions removed
     export_csv(db, model, columns, filename, date_field, since, money_fields,
       enum_fields, relation_fields) — gate 3: 5 of 9 params select behaviour, and
       3 of them shape each row independently: 2^3 = 8 reachable paths in the row
       loop, 3 exercised by tests. Gate 2: the docstring needed "or".

6. Not touched, and why
     The per-row f"{r.total:.2f}" rounding is duplicated in all three handlers.
       Left alone: gate 1 fails (never edited in the same commit), and a shared
       rounding helper changes three externally-visible artifacts at once, which
       is on the irreversible list — customers reconcile against these files.

7. Behaviour evidence
     tests/exports/test_csv.py covers all three routes; run before and after,
       byte-identical output against the golden fixtures.

8. Not done
     Export with no `since` scans the whole table. Filed separately: adding a cap
       is a behaviour change, not a simplification, and does not belong in a diff
       whose claim is "no behaviour changed".
```

The group totals reconcile, and this is the part a reviewer should re-add rather than
trust. The `app/exports/` deletions are 42 (the three Version A handlers the rewrite
replaces) + 183 (`legacy_xlsx.py`) + 11 (the flag and its dead branch) + 4 (`_fmt_money`)
= 240, against 35 added, so 35 − 240 = −205. Tests are 14 − 33 = −19. Total:
−205 + −19 = −224. A net-lines line that does not survive this re-addition means the
deletion inventory and the diff have drifted apart — which is the most common way a lean
review overstates what it did.

Read what the artifact makes arguable. Every claim in it can be checked by someone who
disagrees — the log window, the commit ratio, the parameter count, the golden files. That
is the difference between a lean review and a preference.
