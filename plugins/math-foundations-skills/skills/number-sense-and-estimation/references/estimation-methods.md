# Estimation methods — toolkit, benchmarks, worked Fermi examples, and the check protocol

Contents:
1. [Mental-math toolkit, expanded](#1-mental-math-toolkit-expanded)
2. [Anchor quantities (benchmark tables)](#2-anchor-quantities-benchmark-tables)
3. [Worked Fermi example A — dental office appointments](#3-worked-fermi-example-a--dental-office-appointments)
4. [Worked Fermi example B — school buses in a city of one million](#4-worked-fermi-example-b--school-buses-in-a-city-of-one-million)
5. [The five-question sanity-check protocol](#5-the-five-question-sanity-check-protocol)
6. [Rounding and significant figures](#6-rounding-and-significant-figures)

Every worked number below shows its arithmetic. If a figure looks off, recompute it — that is
the habit this skill exists to build.

## 1. Mental-math toolkit, expanded

These are exact transformations — they trade a hard computation for an equivalent easy one.

| Move | How it works | Example (verify each) |
|---|---|---|
| Decomposition | Split one factor by place value, distribute | 7 × 480 = 7 × 400 + 7 × 80 = 2,800 + 560 = 3,360 |
| Compensation (add) | Round up, subtract the excess | 297 + 458 = 300 + 458 − 3 = 758 − 3 = 755 |
| Compensation (multiply) | Round a factor, correct with one more product | 98 × 47 = 100 × 47 − 2 × 47 = 4,700 − 94 = 4,606 |
| Nearby squares | (a − b)(a + b) = a² − b² | 19 × 21 = 400 − 1 = 399; 48 × 52 = 2,500 − 4 = 2,496 |
| Double-and-halve | Halve one factor, double the other | 16 × 35 = 8 × 70 = 560; 4.5 × 24 = 9 × 12 = 108 |
| Percent benchmarks | 10% shifts the decimal one place; 1% two; 5% = half of 10% | 3% of 3,420 = 3 × 34.2 = 102.6; 15% of 62 = 6.2 + 3.1 = 9.3 |
| Percent swap | a% of b = b% of a (both are ab/100) | 16% of 25 = 25% of 16 = 4; 4.8% of 2,500 = 2,500% of 4.8 = 25 × 4.8 = 120 |
| Factor via 10 | ×5 = ×10 ÷ 2; ×50 = ×100 ÷ 2; ×25 = ×100 ÷ 4 | 68 × 5 = 680 ÷ 2 = 340; 84 × 25 = 8,400 ÷ 4 = 2,100 |

Division moves:
- Divide by 5 → multiply by 2, divide by 10: 435 ÷ 5 = 870 ÷ 10 = 87.
- Divide by 25 → multiply by 4, divide by 100: 900 ÷ 25 = 3,600 ÷ 100 = 36.
- Rough division by decomposing the dividend: 1,032 ÷ 8 = (800 + 232) ÷ 8 = 100 + 29 = 129.

Scientific-notation drill (mantissas times, exponents add):
- 47,000 × 0.002 = (4.7 × 10⁴)(2 × 10⁻³) = 9.4 × 10¹ = 94.
- (3.2 × 10⁴)(2 × 10³) = 6.4 × 10⁷.
- Division subtracts exponents: (8 × 10⁶) ÷ (4 × 10²) = 2 × 10⁴ = 20,000.

## 2. Anchor quantities (benchmark tables)

Time (stable — memorize these):

| Quantity | Value | Arithmetic |
|---|---|---|
| Seconds per day | 86,400 | 24 × 3,600 = 86,400 |
| Seconds per year | ~3.15 × 10⁷ | 365 × 86,400 = 31,536,000 |
| Hours per year | 8,760 | 365 × 24 = 8,760 |
| Weeks per year | 52 | 364 ÷ 7 = 52, plus a day |
| Working days per year | ~250 | 52 × 5 = 260, minus ~10 holidays |
| Work hours per year (full time) | ~2,000 | 50 weeks × 40 h = 2,000 |

Everyday physical anchors (stable):

| Quantity | Working value |
|---|---|
| 1 liter of water | 1 kg |
| Walking pace | ~5 km/h (~3 mph) |
| Brisk reading speed | ~200–250 words/minute |
| A ream of paper (500 sheets) | ~5 cm thick, ~2.5 kg |
| Single-file people per meter of queue | ~2 |

Percent shortcuts:

| Fact | Check |
|---|---|
| 1% of 1 million = 10,000 | 1,000,000 ÷ 100 = 10,000 |
| 10% of anything = shift decimal once | 10% of 3,420 = 342 |
| A part-per-thousand is 0.1% | 1 ÷ 1,000 = 0.001 = 0.1% |

Population-style anchors drift over the years — keep your own current working figures in
`your-environment.md` rather than trusting a stale table, and refresh them when they matter
to a real decision.

## 3. Worked Fermi example A — dental office appointments

**Question:** how many patient appointments does a 3-chair dental office run per year?

**Decompose.** Appointments per year = chairs × appointments per chair per day × working days
per year.

**Judge each factor.**
- Chairs: 3 (given).
- Appointments per chair per day: the office is open about 8 hours; a hygiene visit runs about
  an hour and some visits are shorter, so call it 7 per chair per day (range 5–9).
- Working days: 5 days × 52 weeks = 260, less holidays and closures → call it 250 (range
  230–260).

**Central figure.** 3 × 7 = 21 appointments per day across the office; 21 × 250 = 5,250 per
year.

**Bound.** Push every factor the same direction:
- Pessimistic: 3 × 5 × 230 → 3 × 5 = 15; 15 × 230 = 3,450.
- Optimistic: 3 × 9 × 260 → 3 × 9 = 27; 27 × 260 = 7,020.
- Bracket check: 3,450 < 5,250 < 7,020 — the central figure sits inside the bounds. If it
  did not, a factor judgment or a multiplication is wrong; stop and find it.

**Triangulate** by a different decomposition: appointments per year = active patients × visits
per patient per year. A 3-chair practice plausibly carries about 2,000 active patients; two
hygiene recalls a year plus occasional treatment gives about 2.5 visits per patient:
2,000 × 2.5 = 5,000. That lands inside 3,450–7,020 and near the first route's 5,250 — two
independent routes agree.

**Report.** "About five thousand appointments a year, plausibly 3,500–7,000." Not "5,250":
the trailing digits are artifacts of round inputs, and the range is the honest part of the
answer. Order of magnitude: thousands — not hundreds, not tens of thousands.

## 4. Worked Fermi example B — school buses in a city of one million

**Question:** roughly how many school buses does a city of 1,000,000 people need?

**Decompose.** Buses = (school-age children × share who ride the bus) ÷ children carried per
bus per day.

**Judge each factor.**
- School-age children: about 15% of the population → 1,000,000 × 0.15 = 150,000 (range
  10–18%).
- Share who ride a school bus: call it half → 150,000 × 0.5 = 75,000 riders (range 30–60%).
- Children per bus per day: about 50 seats, and each bus runs two routes a morning →
  50 × 2 = 100 riders per bus (range 60–120).

**Central figure.** 75,000 ÷ 100 = 750 buses.

**Bound.**
- Pessimistic (fewest buses needed): 10% children, 30% ride, 120 per bus:
  1,000,000 × 0.10 = 100,000; × 0.30 = 30,000; ÷ 120 = 250 buses.
- Optimistic (most buses): 18% children, 60% ride, 40 seats × 1.5 runs = 60 per bus:
  1,000,000 × 0.18 = 180,000; × 0.60 = 108,000; ÷ 60 = 1,800 buses.
- Bracket check: 250 < 750 < 1,800 — holds.

**Triangulate.** A different route: buses per school. 150,000 children at roughly 500 per
school is 300 schools; a typical school is served by 2–3 buses → 300 × 2.5 = 750. Agreement
with route 1 is strong evidence the order of magnitude (hundreds to low thousands) is right.

**Report.** "Several hundred to a couple thousand; call it around 750."

## 5. The five-question sanity-check protocol

Run these against any number you are about to trust, in order of cheapness:

1. **Sign.** Should this quantity be positive, negative, or is either possible? A negative
   per-unit cost, a negative headcount, a probability outside 0–1 — each one ends the check
   immediately: the machinery is miswired.
2. **Magnitude.** Is the power of ten plausible? Compare against an anchor: monthly payroll
   of $840,000 implies annual pay of 840,000 × 12 = 10,080,000 ≈ $10.1M. A model printing
   $100M is off by a factor of ten — a classic sign of a units slip (cents vs dollars) or a
   double-counted total.
3. **Units.** Push the units through the formula and confirm they come out as the units of
   the answer (dollars ÷ people = dollars per person, not people per dollar). The full method
   is the `units-and-dimensional-analysis` sibling skill.
4. **Independent re-derivation.** Rebuild the number by a different rough route — different
   inputs, different decomposition. Re-running the same formula, or eyeballing the same
   spreadsheet cell, re-tests the typing but not the thinking. This step is where estimation
   earns its keep.
5. **Edge behavior.** Feed the formula boundary inputs — zero, one, something enormous. A
   pricing formula that returns a discount above 100%, or an allocation that explodes when a
   group is empty, fails here before it fails in production.

Interpretation discipline: passing all five means "plausible," not "verified." Failing any
one means the number is not yet usable — even if it later turns out right, you did not yet
have a reason to believe it.

## 6. Rounding and significant figures

- **Precision inherits from the weakest input.** A product or quotient is only as precise as
  its least precise factor. 2.5 × 3.1415926 = 7.8539815 by calculator, but if the 2.5 is a
  two-significant-figure measurement the defensible answer is 7.9.
- **Round once, at the end.** Intermediate rounding compounds: 1.4 × 1.4 × 1.4 = 2.744, but
  rounding each step to one figure (1.4 → 1.4 × 1.4 = 1.96 → round to 2 → 2 × 1.4 = 2.8)
  drifts from the true 2.744. Carry digits through; trim when you report.
- **Spurious precision markers.** Long decimal tails on divided round numbers ($1,000 ÷ 7 =
  142.857142857…), percentages quoted to hundredths from a sample of 30, totals to the cent
  from inputs estimated to the thousand — each tail claims knowledge the inputs never had.
- **When exactness is the point** (ledgers, invoices, anything that must tie to the cent),
  precision is not spurious — it is the requirement. The rule is not "always round"; it is
  "match reported precision to actual knowledge and purpose."
