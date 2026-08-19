---
name: units-and-dimensional-analysis
description: >-
  Converts quantities across units with the factor-label method — conversion factors written as
  fractions so units cancel visibly — chains multi-step conversions (time, volume, currency as a
  unit), treats per-unit rates (cost per unit, items per hour) as first-class quantities that
  multiply and divide, annualizes and de-annualizes (×12 for flows; compound growth routes to
  the exponential-growth sibling), and dimension-checks any formula: write the units of every
  term, and if the two sides disagree the formula is wrong however plausible its numbers look.
  Catches the classic traps — per-month vs per-year mixups, thousands vs millions scale errors,
  percent as a dimensionless unit. Use when converting units, checking whether a formula's units
  balance, or annualizing a monthly figure. Triggers: unit conversion, convert units,
  dimensional analysis, units don't match, per unit, annualize, factor-label, cancel the units,
  unit check, thousands vs millions.
metadata:
  version: "1.2.0"
---

# Units and dimensional analysis

## When to use
- Converting any quantity between units — single-step or a chain across time, volume,
  currency, and scale (thousands, millions).
- Working with per-unit rates (cost per unit, items per hour, $ per kWh) as first-class
  quantities: building them, multiplying them, dividing by them.
- Annualizing or de-annualizing a monthly figure — and deciding whether ×12 is even the
  right move.
- Checking a formula's dimensional consistency *before* trusting it: yours, a
  colleague's, or one inherited inside a spreadsheet.
- Not for: sizing a system against its payload and growth curve (the Load Manifest
  method) → see `safety-and-reliability-skills:weight-of-the-books`. This skill checks
  that the sizing formulas are dimensionally sound; that one runs the design review.
- Not for: measurement instrument error — repeatability, reproducibility, Gage R&R →
  see `continuous-improvement-skills:measurement-systems-analysis`. Wrong units are a
  translation defect; noisy gauges are a measurement defect.
- Siblings: `math-foundations-skills:algebra-and-formulas` (unit-check every formula it
  rearranges) and `math-foundations-skills:number-sense-and-estimation` (units confirm
  the kind of thing; that skill confirms the size of it).

## Do it
Worked chains, the full check protocol, and the trap catalog are in
`references/factor-label-and-unit-checks.md`.

1. **Write the starting quantity with its unit attached.** `45 mi/hr`, never `45`. A
   number without a unit cannot be checked, converted, or safely combined.
2. **Write each conversion factor as a fraction equal to 1,** oriented so the unit you
   want to remove sits on the opposite side of the bar: `5280 ft / 1 mi` kills miles in
   a numerator; `1 mi / 5280 ft` kills feet. Orientation comes from cancellation, not
   memory — there is nothing to memorize.
3. **Chain the factors and cancel units before touching the numbers.**
   ```
   45 mi     5280 ft     1 hr        45 × 5280
   ------ × --------- × --------  =  ---------  ft/s  =  66 ft/s
    1 hr      1 mi      3600 s         3600
   ```
   Miles cancel, hours cancel, feet-per-second survives. Only then compute:
   45 × 5280 = 237,600; ÷ 3600 = 66.
4. **Confirm the surviving unit is the unit the question asked for.** If it isn't, a
   factor is missing or upside down — fix the chain, not the number.
5. **Treat "per" as division and per-unit rates as ordinary quantities.** A carton of
   24 boxes × 500 sheets/box costs $54, so
   $54/carton × (1 carton/24 boxes) × (1 box/500 sheets) = 54/12,000 = $0.0045/sheet.
   Rates divide, too: $900/day at 480 invoices/day is 900/480 = $1.875/invoice — but
   only because both rates share the same time base (see step 8).
6. **Currency is a unit.** An FX rate is a conversion factor: 8,400 EUR × 1.08 USD/EUR
   = 9,072 USD — EUR cancels, USD survives. The same discipline that stops mi/km errors
   stops paying an invoice in the wrong currency's magnitude.
7. **Annualize flows by ×12; hand rates that compound to the growth sibling.** A
   *flow* adds across months: $2,350/month × 12 months/year = $28,200/year, and
   $46,800/year ÷ 12 = $3,900/month. A *rate of return* does not add — 1% per month is
   (1.01)¹² − 1 ≈ 12.68% per year, not 12%. This skill's job is the distinction and the
   ×12 case; the (1+r)ⁿ math belongs to `math-foundations-skills:exponential-growth-and-logs`.
8. **Dimension-check any formula before trusting it.** Write the units of every symbol;
   work out the units of every term; every pair of added or subtracted terms shares a
   unit, both sides match, and anything inside exp, ln, or an exponent is dimensionless.
   A formula that fails is wrong no matter how plausible its output looks — and one
   whose units merely *resolve* still owes you the question of which law joins the
   terms. This library's own `safety-and-reliability-skills:weight-of-the-books` had
   its margin-exhaustion formula corrected in adversarial review by exactly that pair
   of questions: the draft's units came out as years, and writing them down was what
   exposed that nothing in it said how the quantity actually moved with time (the
   worked catch is in the reference file). Numbers can look right by luck; writing the
   units out is what makes the structure you actually wrote visible.
9. **Scan for the standing traps:** per-month and per-year figures added in one sum;
   "$ thousands" columns read as raw dollars (a 1,000× error — write k$ and M$ as real
   units: 2,340 k$ = $2,340,000 = 2.34 M$); percent used as if it were a count
   (5% = 5/100 = 0.05, a dimensionless ratio); two rates divided on different time
   bases ($900/day ÷ 60 invoices/hour is not $15/invoice — convert to a common base
   first: 60/hr × 8 hr/day = 480/day, so 900/480 = $1.875).

## Why / learn
**Units are algebra.** They multiply, divide, and cancel exactly like symbols, because
a unit *is* a symbol — "45 mi/hr" is the product 45 × mi × hr⁻¹. That is why the
factor-label method works: each conversion factor equals 1 (5280 ft and 1 mi are the
same length), so multiplying by it changes the representation and never the quantity.
Carrying units through a calculation is therefore a check that travels with the work —
but be precise about what it proves. **Units resolving does not make the structure
correct.** It is a one-way test: wrong units prove the formula wrong, while right units
leave a formula that can still carry a wrong constant, a wrong sign, a missing factor of
two, or the right dimensions assembled the wrong way round. Treat a clean dimensional
check as "not yet refuted", never as "verified". Dropping units doesn't simplify the
work — it deletes the half of the answer that can catch the other half.

**A dimensional check is the cheapest formula review that exists.** It needs no data,
no test cases, and no domain expertise beyond knowing what each symbol measures — yet it
refutes a wrong formula outright. It is asymmetric in the useful direction: passing
doesn't prove a formula right (a constant can still be wrong), but failing proves it
wrong with certainty. That asymmetry is why it runs *before* trusting any formula, not
after the numbers disappoint — plausible-looking output is precisely what a
dimensionally broken formula produces, since nothing else constrains it. It works on
authors, too: the weight-of-the-books catch above was an author's own formula, in this
library, found when a reviewer wrote out the units of every term and asked what law
joined them — the units came out as years, and the question they provoked was what
convicted the formula.

**Flows add; growth compounds.** Twelve months of a $2,350 cost is genuinely
12 × 2,350, because dollars spent in different months pile up in one heap. Twelve months
of 1% growth is not 12%, because each month's growth acts on a base the previous months
already enlarged — multiplication, not addition. The unit lens makes the distinction
visible: a flow's unit is $/month (multiply by months and months cancel — the ×12 is
itself factor-label), while a growth rate is dimensionless-per-period and lives in an
exponent, where only dimensionless things belong.

## Common mistakes
- Conversion factor upside down (multiplying by 3600 s/hr when seconds should cancel) →
  orient by cancellation: the unit to remove goes on the other side of the bar.
- Computing the numbers before the units resolve → cancel first; arithmetic on an
  unchecked chain just launders the error.
- Dividing rates on different time bases ($/day ÷ items/hour) → convert both to one
  base, then divide.
- Annualizing a growth rate with ×12 → ×12 is for flows; rates compound — route to
  `math-foundations-skills:exponential-growth-and-logs`.
- Adding per-month and per-year figures in one total ($1,800/mo rent + $2,400/yr
  insurance ≠ $4,200 of anything; it is $21,600 + $2,400 = $24,000/yr) → convert to a
  common period before any sum.
- Reading a "$ thousands" report column as raw dollars → treat k$ and M$ as units and
  convert explicitly; 1,000× errors survive plausibility review because both magnitudes
  can look reasonable.
- Using 5% as the number 5 → percent is a dimensionless unit meaning /100; write 0.05.
- Trusting a formula because its output looks reasonable → run the units of every term;
  plausible numbers are what broken formulas emit.

## Tailor to your environment
Record your recurring conversions and house conventions in
`references/your-environment.md`: the units your systems report in, standard reporting
scales (k$, M$), period conventions (which figures arrive monthly vs annually), and the
formulas you have dimension-checked with their verdicts. Keep committed content
structural — real rates, balances, or counterparty details belong in
`your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/units-and-dimensional-analysis.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/factor-label-and-unit-checks.md — worked conversion chains with visible
  cancellation, the formula dimensional-check protocol with the worked
  weight-of-the-books catch, and the trap catalog with verified numbers
- references/your-environment.md — your units, scales, period conventions, and checked
  formulas
