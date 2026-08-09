# Evals — math-foundations-skills:algebra-and-formulas

## 1. Positive trigger (should load the skill)
> "Two things. First: our breakeven formula is Q = F/(p − v) and I always look up Q —
> rearrange it so I can solve for the price p instead, and walk me through it so I can
> do the next one myself. Second: this spreadsheet cell was supposed to show the
> midpoint of B2 and B3 but the number looks wrong — the formula is =B2+B3/2."

Expected: skill loads and does both. For the rearrangement it treats p as the unknown
and every other symbol as a known, shows the balance moves one at a time (multiply both
sides by (p − v), divide by Q, add v) to reach p = v + F/Q, then substitutes numbers
back through the *original* formula to verify (e.g. F = 9,000, v = 13, Q = 750 →
p = 13 + 12 = 25, and 9,000/(25 − 13) = 750 ✓), reads the result's meaning (price =
unit variable cost plus each unit's share of fixed cost), and points at the sibling
units skill for a dimension check of the rearranged form. For the spreadsheet it
rewrites the formula as algebra with the app's precedence made explicit — B2 + (B3/2),
not (B2 + B3)/2 — demonstrates the difference with the actual cell values, and gives
the corrected parenthesized formula. Throughout it teaches the balance principle rather
than just emitting the answer.

## 2. Near-miss (should NOT load this skill — adjacent skill owns it)
> "Build me a pricing workbook: an assumptions tab, a calculations sheet with breakeven
> and margin outputs, scenario toggles for three price points, and check cells so we
> catch errors."

Expected: `data-analytics-bi-skills:spreadsheet-modeling` loads instead — the ask is
model *structure* (input/calc/output separation, scenario switches, check cells), not
reading or rearranging a formula as algebra. If algebra-and-formulas loads on a
workbook-construction request, its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Walk me through the accounting equation — if assets go up and liabilities are
> unchanged, which side is the debit?"

Expected: `accounting-skills:double-entry-fundamentals` loads instead. "Equation" and
"which side" sound algebraic, but the accounting equation, debits/credits, and normal
balances are that skill's scope; this one owns solve-for-x, not A = L + E.

## 3. Quality rubric
A good response:
- **Does the task:** names the unknown in words with units before any symbol pushing;
  states the relation as two descriptions of one quantity; applies one balance move at a
  time, both sides, written down; substitutes the answer back into the *original*
  equation and sanity-reads it against the story; for rearrangements, verifies with a
  concrete numeric round-trip; for inequalities, checks the boundary and one point
  beyond; for spreadsheet formulas, rewrites them in math notation with the app's real
  precedence and re-verifies with the actual cell values. Arithmetic in worked steps is
  correct and shown, not asserted.
- **Teaches:** explains that an equation claims two descriptions agree and solving
  preserves the claim; why substitute-back is free insurance against two independent
  failure modes (setup vs algebra); why word-order transcription causes the reversal
  error and naming-in-words prevents it; why multiplying an inequality by a negative
  flips it (reflection reverses order); why spreadsheet precedence is algebra with
  invisible parentheses.
- **Stays honest:** flags an unsolvable or contradictory setup as a fact about the
  problem instead of forcing an answer; routes workbook architecture to
  `data-analytics-bi-skills:spreadsheet-modeling` and accounting-equation questions to
  `accounting-skills:double-entry-fundamentals` rather than absorbing them; recommends
  the sibling unit check on rearranged formulas instead of claiming algebra alone
  proves correctness; and never presents an unchecked number as checked.
