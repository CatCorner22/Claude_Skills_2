---
name: algebra-and-formulas
description: >-
  Translates word problems into symbols (name the unknown in words, define every quantity,
  state the relation that holds), solves linear equations step by step with the balance
  principle, rearranges formulas to isolate any variable (simple interest, breakeven
  quantity, rate formulas), verifies every solution by substituting back, handles
  inequalities and the sign flips they demand, solves two-unknown systems by substitution,
  and reads or debugs spreadsheet formulas as algebra — operator precedence, parentheses
  discipline, the hidden order-of-operations error. Use when a stated problem needs
  translating into math, a formula needs solving or rearranging for a different variable,
  or a spreadsheet formula returns a number that looks wrong. Triggers: solve for x,
  rearrange the formula, algebra, linear equations, word problem, isolate the variable,
  breakeven, two unknowns, order of operations, PEMDAS.
metadata:
  version: "1.1.1"
---

# Algebra and formulas

## When to use
- A word problem needs translating into symbols: define the unknown, name every quantity,
  state what relation holds between them.
- A linear equation needs solving, or a formula needs rearranging to isolate a different
  variable — simple interest, breakeven quantity, a rate formula, any solve-for-x on a
  formula you actually use.
- A candidate answer needs checking, an inequality needs handling (and you want to know
  what flips its direction), or two unknowns are linked and a small two-equation system
  by substitution will untangle them.
- A spreadsheet formula returns a number that looks wrong and needs reading as algebra:
  operator precedence, parentheses discipline, the hidden order-of-operations error.
- Not for: building spreadsheet models — structure, assumptions tabs, scenario switches
  → see `data-analytics-bi-skills:spreadsheet-modeling`. This skill reads a single
  formula as algebra; that one builds the workbook around it.
- Not for: the accounting equation, debits/credits, and normal balances — that is
  double-entry bookkeeping, an accounting-domain topic this library does not carry, not
  solve-for-x.
- Siblings: unit-check every rearranged formula with
  `math-foundations-skills:units-and-dimensional-analysis`; rough-size the answer before
  solving with `math-foundations-skills:number-sense-and-estimation`.

## Do it
The full solve-for-x ladder (one-step through formula rearrangement, each with its
substitute-back check) is in `references/solving-and-rearranging.md`.

1. **Name the unknown in words, with units.** "Let h = hours worked (hours)" — never a
   bare "let x". The words are the guard rail: most wrong answers to word problems are
   set up wrong, not solved wrong, and a variable that carries its meaning is hard to
   misuse.
2. **Name every other quantity the same way,** including the ones the problem states
   outright ("flat fee F = $40", "hourly rate = $15/hour"). A quantity without a name
   tends to get dropped or double-counted.
3. **State the relation as two descriptions of the same quantity.** An equation is a
   claim that both sides describe one number. "The invoice is the flat fee plus the
   hourly charge" becomes `40 + 15h = 145` — left side built from the story, right side
   the known total.
4. **Rough-size the answer before solving** (see the sibling
   `math-foundations-skills:number-sense-and-estimation`). Here: the fee leaves about
   $100 of hourly work at $15/hour, so h should land near 7. A pre-solve figure this
   coarse still catches sign errors and dropped terms.
5. **Solve with the balance principle: one operation, both sides, written down.** Undo
   operations in reverse order — the equation was built additions-last, so strip
   additions first:
   `40 + 15h = 145` → subtract 40 from both sides → `15h = 105` → divide both sides by
   15 → `h = 7`.
6. **Substitute back into the original equation** (not into your rearranged line, which
   may carry the same error): `40 + 15(7) = 40 + 105 = 145`. Matches, so both the setup
   and the algebra survived. This check costs seconds and catches both kinds of mistake.
7. **Rearrange a formula with exactly the same moves** — treat the variable you want as
   the unknown and every other symbol as a known number.
   - Simple interest `I = P·r·t`, solve for r: divide both sides by `P·t` →
     `r = I/(P·t)`. Check with numbers: P = $12,000, r = 0.04/yr, t = 1.5 yr gives
     I = 12,000 × 0.04 × 1.5 = $720; then r = 720/(12,000 × 1.5) = 720/18,000 = 0.04. ✓
   - Breakeven `Q = F/(p − v)`, solve for p: multiply both sides by (p − v) →
     `Q(p − v) = F` → divide by Q → `p − v = F/Q` → add v → `p = v + F/Q`. Check:
     F = $9,000, p = $25, v = $13 gives Q = 9,000/12 = 750 units; then
     p = 13 + 9,000/750 = 13 + 12 = 25. ✓
8. **Unit-check the rearranged form** with
   `math-foundations-skills:units-and-dimensional-analysis`: r = I/(P·t) has units
   $/($·yr) = 1/yr — a rate per year, as it should be. A rearrangement that survives the
   algebra but fails the unit check is still wrong.
9. **Inequalities: same balance moves, one exception.** Multiplying or dividing both
   sides by a negative number flips the direction (so does swapping the sides). Budget
   example: `200 − 12x ≥ 80` → subtract 200 → `−12x ≥ −120` → divide by −12 and flip →
   `x ≤ 10`. Check the boundary (x = 10: 200 − 120 = 80 ✓) and one point beyond
   (x = 11: 200 − 132 = 68, which violates the original ✓).
10. **Two linked unknowns: substitution.** Write both relations, solve the simpler one
    for one variable, substitute into the other. Tickets: adult $9, child $5, 20 tickets,
    $132 total. `a + c = 20` and `9a + 5c = 132`. From the first, `a = 20 − c`;
    substitute: `9(20 − c) + 5c = 132` → `180 − 4c = 132` → `4c = 48` → `c = 12`,
    `a = 8`. Check in both originals: 8 + 12 = 20 ✓ and 72 + 60 = 132 ✓.
11. **Debug a spreadsheet formula by rewriting it as algebra.** Copy the formula out,
    write it in math notation with explicit parentheses per the app's precedence rules,
    substitute the actual cell values, and recompute by hand. The two classics:
    `=A1+B1/2` intending the midpoint of A1 and B1 computes `A1 + (B1/2)` — with A1 = 10,
    B1 = 20 that is 20, not the intended (10 + 20)/2 = 15. And Excel's unary minus binds
    tighter than `^`, so `=-2^2` returns (−2)² = 4 where written math reads −(2²) = −4.
    Protocol and precedence table in `references/solving-and-rearranging.md`.

## Why / learn
**An equation is a claim, and solving is preserving it.** Both sides describe the same
quantity, so any operation applied to both descriptions keeps the claim true — that is
the whole of the balance principle. Every legal move follows from it, and every classic
error (subtracting from one side, dividing only one term of a sum) is a way of silently
changing the claim. Seeing it this way also explains why rearranging a formula is not a
separate skill: `Q = F/(p − v)` is just an equation whose unknown happens to be p today.

**Substitute-back verification is free insurance on two policies at once.** Plugging the
answer into the *original* equation checks the algebra; asking whether the answer makes
sense in the *story* (7 hours on a $145 invoice — plausible) checks the setup. The two
failures are independent, common, and each caught in seconds. Work that skips the check
isn't faster; it just moves the error downstream to somewhere expensive.

**Naming variables in words prevents the reversal error.** The best-studied setup bug:
"there are six times as many students as professors" is routinely written `6s = p` —
the sentence order transcribed as symbols. Name in words first — s = number of students,
p = number of professors; students are the bigger group — and the relation can only come
out `s = 6p` (p = 10 professors gives s = 60 ✓). Translation is meaning-to-symbols, not
word-order-to-symbols, and named variables force the meaning step.

**The inequality flip is a mirror, not a rule to memorize.** Multiplying by a negative
reflects the number line, so order reverses: 2 < 3, but −2 > −3. Addition slides both
values without reordering them, which is why only multiplication and division by
negatives flip. And a spreadsheet formula is just algebra with invisible parentheses —
the app inserts them by its precedence table whether or not you meant them, so debugging
means making them visible again.

## Common mistakes
- Transcribing sentence order into symbols ("six times as many students" → `6s = p`) →
  name variables in words, then ask which quantity is bigger before writing the relation.
- Operating on one side only, or on only one term of a side — `(6x + 9)/3` is `2x + 3`,
  not `2x + 9` → the divisor applies to every term of the sum.
- Skipping the substitute-back check → it costs seconds and is the only step that
  catches setup and algebra errors together.
- Forgetting the flip when dividing an inequality by a negative → check the boundary and
  one point beyond it; the numbers will confess.
- Rearranging a formula correctly but never unit-checking it →
  `math-foundations-skills:units-and-dimensional-analysis`; units are a second,
  independent proof.
- Trusting spreadsheet precedence to match written math → `=-2^2` is 4 in Excel;
  `=A1+B1/2` halves only B1. Parenthesize what you mean.
- Solving before rough-sizing → an answer of 700 hours on a $145 invoice should never
  survive first contact with the pre-solve figure.

## Tailor to your environment
List the formulas you actually rearrange — your pricing rule, interest conventions,
breakeven inputs, commission structure — in `references/your-environment.md`, each with
its symbols named in words and units. Keep committed content structural: real rates,
client terms, or anything sensitive belongs in `your-environment.private.md`
(git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/algebra-and-formulas.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/solving-and-rearranging.md — the solve-for-x ladder from one-step to formula
  rearrangement (each with its substitute-back check), the word-problem translation
  protocol, inequality flip rules, and spreadsheet formulas read as algebra
- references/your-environment.md — your recurring formulas, symbols, and conventions
