# Evals — data-analytics-bi-skills:assertion-evidence-deck

## 1. Positive trigger (should load the skill)
> "I need to brief the Controller next week on our reconciliation remediation — can you turn the
> config-review findings into a short PowerPoint?"

Expected: skill loads. Scopes the talk (audience = Controller, duration, one main claim); insists on
a source ledger before any figure lands on a slide; writes sentence-headlines first and shows the
spine; designs each slide as one claim + one visual (not bullets); builds via `build_deck.py` (or the
official template on request), lints and visually checks it; delivers deck + source ledger + gap list.
It does **not** re-run the reconciliation analysis — it asks for the verified findings.

## 2. Near-miss (should NOT load this skill)
> "Why are 400 of our bank statement lines still unreconciled this month — which rule is dropping
> them?"

Expected: this is a configuration diagnosis, not a presentation task →
`oracle-fusion-finance-skills:fusion-cm-production-troubleshooting` or `oracle-cm-config-review`.
This skill only turns *verified* findings into slides. If it loads and starts diagnosing rules, the
description is over-triggering; if it loads only to say "run the diagnosis first, then I'll build the
deck," that is acceptable.

Second near-miss:
> "Design a KPI dashboard for our cash position."
Expected: `data-analytics-bi-skills:dashboard-design`, not this skill — a live dashboard is not an
assertion-evidence talk.

## 3. Quality rubric
A good response:
- **Does the task:** produces sentence-assertion headlines (subject + verb, falsifiable, ≤ 2 lines);
  one visual per slide chosen to fit the claim; ≤ ~20 body words per one-minute slide; a source tag
  on every slide carrying a figure; a source ledger and a gap list delivered alongside; the deck
  linted clean (`ae_lint.py` exits 0) and visually checked.
- **Teaches:** explains why assertion-evidence beats bullets (reading vs. listening compete),
  snorkel-vs-scuba depth (slide = snorkel, notes = scuba), and the wrong-number-vs-missing-number
  asymmetry (prefer the honest gap).
- **Safe:** never puts an inferred or unverified number on a slide as a bare figure; tags "as
  reported" claims; for UT audit work, cites report numbers/figures from the report itself, never
  from memory or a summary; states which typeface it chose and why (font-substitution risk).
