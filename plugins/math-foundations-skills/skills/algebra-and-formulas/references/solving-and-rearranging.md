# Solving and rearranging — the ladder, the translation protocol, flips, and spreadsheets

Contents: §1 The solve-for-x ladder · §2 The word-problem translation protocol ·
§3 Inequality flip rules · §4 Two unknowns by substitution · §5 Spreadsheet formulas as
algebra

Every rung shows the balance move and the substitute-back check. The check always goes
into the *original* equation — a rearranged line can carry the very error you are
checking for.

## §1 The solve-for-x ladder

**Rung 1 — one step (undo an addition).**
`x + 9 = 31` → subtract 9 from both sides → `x = 22`.
Check: 22 + 9 = 31 ✓

**Rung 2 — one step (undo a multiplication).**
`4x = 52` → divide both sides by 4 → `x = 13`.
Check: 4 × 13 = 52 ✓

**Rung 3 — two steps, in reverse order of operations.**
`5x − 7 = 33`. Building the left side, x was multiplied by 5 first, then 7 was
subtracted; undoing runs in reverse: add 7 → `5x = 40` → divide by 5 → `x = 8`.
Check: 5 × 8 − 7 = 40 − 7 = 33 ✓

**Rung 4 — variable on both sides.**
`7x − 4 = 3x + 24` → subtract 3x from both sides → `4x − 4 = 24` → add 4 → `4x = 28` →
divide by 4 → `x = 7`.
Check: left 7 × 7 − 4 = 45; right 3 × 7 + 24 = 45 ✓

**Rung 5 — a fraction.**
`x/4 + 5 = 12` → subtract 5 → `x/4 = 7` → multiply both sides by 4 → `x = 28`.
Check: 28/4 + 5 = 7 + 5 = 12 ✓

**Rung 6 — parentheses.**
`3(x − 2) = 21`. Two routes, same answer: divide both sides by 3 first → `x − 2 = 7` →
`x = 9`; or distribute → `3x − 6 = 21` → `3x = 27` → `x = 9`.
Check: 3 × (9 − 2) = 3 × 7 = 21 ✓

**Rung 7 — a formula with letters as the knowns.**
Distance `d = r·t`, solve for t: divide both sides by r → `t = d/r`.
Check with numbers: 330 miles at 55 mph → t = 330/55 = 6 hours; 55 × 6 = 330 ✓

**Rung 8 — simple interest.**
`I = P·r·t`, solve for r: divide both sides by `P·t` → `r = I/(P·t)`.
Check: P = $12,000, r = 0.04/yr, t = 1.5 yr → I = 12,000 × 0.04 × 1.5 = $720.
Rearranged: r = 720/(12,000 × 1.5) = 720/18,000 = 0.04 ✓
Unit check: $/($·yr) = 1/yr, a per-year rate — the right kind of thing.

**Rung 9 — the unknown inside a denominator.**
Breakeven `Q = F/(p − v)`, solve for p. The unknown is trapped under the bar, so free it
first: multiply both sides by (p − v) → `Q(p − v) = F` → divide by Q → `p − v = F/Q` →
add v → `p = v + F/Q`.
Check: F = $9,000, p = $25, v = $13 → Q = 9,000/(25 − 13) = 9,000/12 = 750 units.
Rearranged: p = 13 + 9,000/750 = 13 + 12 = $25 ✓
Read the result: price must cover unit variable cost v plus each unit's share of fixed
cost F/Q — the rearrangement *means* something, which is a bonus check in itself.

**Rung 10 — solve for a rate buried in a structure.**
Price at a target margin m (margin as a fraction of price): `p = c/(1 − m)`, solve
for m: multiply by (1 − m) → `p(1 − m) = c` → divide by p → `1 − m = c/p` → `m = 1 − c/p`.
Check: c = $48, m = 0.20 → p = 48/0.8 = $60. Rearranged: m = 1 − 48/60 = 1 − 0.8 = 0.20 ✓

## §2 The word-problem translation protocol
1. **Read for the question first** — what quantity, in what units, is being asked for?
   That quantity is the unknown; name it in words with units ("let h = hours worked").
2. **Name every stated quantity** the same way, including units, even the obvious ones.
3. **Find the sentence that equates two descriptions of one number** — a total, a
   balance, a "the same as". That sentence is the equation; everything else is data.
4. **Write the equation from meaning, not word order.** Ask which side is bigger, which
   quantities add, which multiply. ("Six times as many students as professors": students
   are the bigger count, so s = 6p.)
5. **Rough-size the answer** before solving; then solve; then substitute back into the
   original equation *and* the original story.

Worked end-to-end: a service charges a $40 flat fee plus $15 per hour, and the invoice
is $145. Unknown: h = hours worked (hours). Relation: invoice = fee + rate × hours →
`40 + 15h = 145`. Pre-solve size: about $100 of hourly work at $15/hour → h near 7.
Solve: `15h = 105` → `h = 7`. Check: 40 + 15 × 7 = 145 ✓, and 7 hours is a sane visit.

## §3 Inequality flip rules
All balance moves work on inequalities; only these change the direction:

| Move | Direction |
|---|---|
| Add or subtract anything, both sides | keeps |
| Multiply or divide by a **positive**, both sides | keeps |
| Multiply or divide by a **negative**, both sides | **flips** |
| Swap the two sides | **flips** |
| Multiply by a variable of unknown sign | unsafe — split into cases instead |

Why: multiplying by a negative reflects the number line, and reflection reverses order
(2 < 3 but −2 > −3). Addition slides values without reordering them.

Worked: `−3x + 5 > 20` → subtract 5 → `−3x > 15` → divide by −3 and flip → `x < −5`.
Check a point inside: x = −6 → −3(−6) + 5 = 23 > 20 ✓. Check the boundary is excluded:
x = −5 → 15 + 5 = 20, not > 20 ✓.

Boundary-and-beyond is the standard verification for any inequality: test the boundary
value and one value past it, and the direction confirms or convicts itself.

## §4 Two unknowns by substitution
Use when two quantities are linked by two independent relations. Solve the simpler
relation for one variable, substitute into the other, finish with the ladder.

Worked — a blend: 12 lb of a coffee blend priced at $8.50/lb, mixed from beans at $7/lb
and $10/lb. Let a = pounds of the $7 bean, b = pounds of the $10 bean.
Relations: `a + b = 12` (weight) and `7a + 10b = 12 × 8.50 = 102` (cost).
From the first: `a = 12 − b`. Substitute: `7(12 − b) + 10b = 102` → `84 + 3b = 102` →
`3b = 18` → `b = 6`, so `a = 6`.
Check both originals: 6 + 6 = 12 ✓ and 7 × 6 + 10 × 6 = 42 + 60 = 102 ✓, and
102/12 = $8.50/lb ✓.

If substitution produces a true statement with no variable (e.g. `0 = 0`), the two
relations were the same fact twice — infinitely many solutions. A false statement
(e.g. `0 = 5`) means the relations contradict — no solution. Both outcomes are answers
about the problem, not algebra failures.

## §5 Spreadsheet formulas as algebra
A spreadsheet formula is an equation's right-hand side with invisible parentheses that
the app inserts by its precedence table. Debugging means making them visible.

**The debug protocol.**
1. Copy the formula text out of the cell.
2. Rewrite it in math notation, inserting explicit parentheses exactly where the app's
   precedence puts them (not where you intended them).
3. Substitute the actual cell values.
4. Recompute by hand and compare with the cell's displayed result — they will match,
   which localizes the bug in the formula's *structure*, not the data.
5. Write the formula you meant, with parentheses, and re-verify.

**Excel/Sheets precedence, highest first:** range/space operators; unary minus (`-x`);
percent (`%`); exponent (`^`); multiply/divide (`*` `/`); add/subtract (`+` `-`); text
join (`&`); comparisons. Two departures from written math worth memorizing by example:
- **Unary minus beats the exponent:** `=-2^2` returns 4, because Excel reads (−2)²,
  while written math reads −(2²) = −4. `=0-2^2` returns −4 — the binary minus has normal
  (low) precedence.
- **Division beats addition (the hidden order-of-operations error):** `=A1+B1/2`
  intending a midpoint computes `A1 + (B1/2)`. With A1 = 10, B1 = 20: 10 + 10 = 20
  instead of the intended (10 + 20)/2 = 15.

**Worked debug — a weighted unit cost.** Intended:
`=(Q1*P1 + Q2*P2)/(Q1 + Q2)`. Typed without parentheses: `=Q1*P1 + Q2*P2/Q1 + Q2`.
With Q1 = 10, P1 = $2, Q2 = 30, P2 = $4:
- Intended: (10×2 + 30×4)/(10 + 30) = (20 + 120)/40 = 140/40 = **$3.50/unit**.
- As typed, precedence inserts: `(Q1·P1) + (Q2·P2/Q1) + Q2` = 20 + (120/10) + 30 =
  20 + 12 + 30 = **62** — not even a cost per unit (the trailing `+ Q2` adds a
  *quantity* to *dollars*, which a unit check catches instantly; see
  `math-foundations-skills:units-and-dimensional-analysis`).

Parentheses discipline that prevents the whole class: parenthesize every numerator and
every denominator that contains an operation, even when precedence would happen to save
you — the formula then reads the same to you, the app, and the next person.
