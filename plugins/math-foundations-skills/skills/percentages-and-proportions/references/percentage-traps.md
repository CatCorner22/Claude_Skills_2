# Percentage traps — the catalog, with verified worked numbers

Contents:
1. [Gain/loss asymmetry and the recovery table](#1-gainloss-asymmetry-and-the-recovery-table)
2. [Percentage points vs percent](#2-percentage-points-vs-percent)
3. [Basis points](#3-basis-points)
4. [Markup vs margin conversion tables](#4-markup-vs-margin-conversion-tables)
5. [Weighted vs plain averages of rates](#5-weighted-vs-plain-averages-of-rates)
6. [Mix effects (Simpson's paradox, everyday form)](#6-mix-effects-simpsons-paradox-everyday-form)
7. [Reversing changes and tax-inclusive amounts](#7-reversing-changes-and-tax-inclusive-amounts)
8. [Successive changes and discount stacking](#8-successive-changes-and-discount-stacking)
9. [Rates, per-1,000, and per capita](#9-rates-per-1000-and-per-capita)
10. [Small, zero, and negative bases](#10-small-zero-and-negative-bases)

Every number here shows its arithmetic so you can recompute it. That is the point: a percent
claim you cannot rebuild from its base is a claim you have not yet checked.

## 1. Gain/loss asymmetry and the recovery table

Changes are scale factors, so a loss of L (factor 1 − L) needs a recovery gain of
L ÷ (1 − L) to return to the starting value — always bigger than L:

| Loss | Factor left | Recovery gain needed | Arithmetic |
|---|---|---|---|
| −10% | 0.90 | +11.1% | 0.10 ÷ 0.90 = 0.111 |
| −20% | 0.80 | +25% | 0.20 ÷ 0.80 = 0.25 |
| −25% | 0.75 | +33.3% | 0.25 ÷ 0.75 = 0.333 |
| −33.3% | 0.667 | +50% | (1/3) ÷ (2/3) = 0.50 |
| −50% | 0.50 | +100% | 0.50 ÷ 0.50 = 1.00 |
| −75% | 0.25 | +300% | 0.75 ÷ 0.25 = 3.00 |
| −90% | 0.10 | +900% | 0.90 ÷ 0.10 = 9.00 |

The demonstration everyone should run once: start at 100, drop 50% → 50, rise 50% →
50 × 1.50 = 75. Order does not matter (1.50 × 0.50 = 0.50 × 1.50 = 0.75): any −X% and +X%
pair leaves you below the start, because (1 − x)(1 + x) = 1 − x² < 1 for any x ≠ 0.

## 2. Percentage points vs percent

The difference of two percentages has two honest descriptions and one misleading one:

| Move | In percentage points | Relative (% change) | Arithmetic |
|---|---|---|---|
| Interest 4% → 6% | +2 pp | +50% | 2 ÷ 4 = 0.50 |
| Unemployment 5% → 4% | −1 pp | −20% | 1 ÷ 5 = 0.20 |
| Conversion 2% → 3% | +1 pp | +50% | 1 ÷ 2 = 0.50 |

The reporting trap runs both directions. "Rates rose 2%" understates 4% → 6% (which is a 50%
relative rise); "conversions jumped 50%!" oversells a one-point move from 2% to 3%. The
honest sentence carries both: "up one point, from 2% to 3% — a 50% relative increase."

## 3. Basis points

One basis point = 0.01 percentage points = 0.0001 in decimal. Finance quotes rate moves in
bp precisely to dodge the points-vs-percent ambiguity above.

| Basis points | Percentage points | Decimal | On $10,000,000 |
|---|---|---|---|
| 1 bp | 0.01 pp | 0.0001 | $1,000 |
| 10 bp | 0.10 pp | 0.0010 | $10,000 |
| 25 bp | 0.25 pp | 0.0025 | $25,000 |
| 50 bp | 0.50 pp | 0.0050 | $50,000 |
| 100 bp | 1.00 pp | 0.0100 | $100,000 |

Checks: 10,000,000 × 0.0001 = 1,000; × 0.0025 = 25,000. A yield of 4.00% raised 50 bp is
4.50%; cut 25 bp it is 3.75%.

## 4. Markup vs margin conversion tables

Same profit dollars, two bases: markup = profit ÷ cost; margin = profit ÷ price.
Conversions: margin = markup ÷ (1 + markup); markup = margin ÷ (1 − margin).

Markup → margin:

| Markup | Margin | Arithmetic |
|---|---|---|
| 10% | 9.1% | 0.10 ÷ 1.10 = 0.0909 |
| 20% | 16.7% | 0.20 ÷ 1.20 = 0.1667 |
| 25% | 20.0% | 0.25 ÷ 1.25 = 0.20 |
| 30% | 23.1% | 0.30 ÷ 1.30 = 0.2308 |
| 50% | 33.3% | 0.50 ÷ 1.50 = 0.3333 |
| 100% | 50.0% | 1.00 ÷ 2.00 = 0.50 |

Margin → markup:

| Margin | Markup | Arithmetic |
|---|---|---|
| 10% | 11.1% | 0.10 ÷ 0.90 = 0.1111 |
| 20% | 25.0% | 0.20 ÷ 0.80 = 0.25 |
| 25% | 33.3% | 0.25 ÷ 0.75 = 0.3333 |
| 30% | 42.9% | 0.30 ÷ 0.70 = 0.4286 |
| 40% | 66.7% | 0.40 ÷ 0.60 = 0.6667 |
| 50% | 100.0% | 0.50 ÷ 0.50 = 1.00 |

Concrete check: cost 100, priced at cost + 50% markup → price 150 → margin 50 ÷ 150 = 33.3%.
The expensive version of this trap: a shop targeting a 25% margin that prices at cost + 25%
actually earns 0.25 ÷ 1.25 = 20% margin. On cost 100 that is price 125 and profit 25 — where
the intended price was 100 ÷ 0.75 = 133.33 with profit 33.33. The shortfall is
8.33 ÷ 33.33 = 25% of the intended profit, given up on every sale.

## 5. Weighted vs plain averages of rates

Rates of 2% (on 9,000 units) and 10% (on 1,000 units):

- Plain average: (2% + 10%) ÷ 2 = 6%.
- True overall: defects = 0.02 × 9,000 = 180 and 0.10 × 1,000 = 100; total 280 defects on
  10,000 units → 280 ÷ 10,000 = 2.8%.

The plain average overstates by more than double because it gives the 1,000-unit segment the
same weight as one nine times its size. The rule: a rate is a fraction — combine numerators
and denominators separately, then divide once. A plain average of rates equals the weighted
one only when all denominators match.

## 6. Mix effects (Simpson's paradox, everyday form)

The overall rate is a share-weighted blend of segment rates: overall = Σ (share × rate).
It therefore moves for two reasons — rates changing, or shares changing — and the second can
overwhelm the first.

| Period | Segment | Volume | Share | Defect rate | Defects |
|---|---|---|---|---|---|
| Year 1 | A | 8,000 | 80% | 2.0% | 160 |
| Year 1 | B | 2,000 | 20% | 10.0% | 200 |
| Year 1 | **Total** | **10,000** | 100% | **3.6%** | **360** |
| Year 2 | A | 4,000 | 40% | 1.5% | 60 |
| Year 2 | B | 6,000 | 60% | 9.0% | 540 |
| Year 2 | **Total** | **10,000** | 100% | **6.0%** | **600** |

Checks: 8,000 × 0.020 = 160; 2,000 × 0.100 = 200; 360 ÷ 10,000 = 3.6%.
4,000 × 0.015 = 60; 6,000 × 0.090 = 540; 600 ÷ 10,000 = 6.0%.

Both segments improved; the blend worsened by 2.4 points. Decompose the +2.4 pp move by
holding one thing constant at a time:

- **Rate effect** — Year 1 mix at Year 2 rates: 0.80 × 1.5% + 0.20 × 9.0% =
  1.2% + 1.8% = 3.0%. So improving rates alone: 3.6% → 3.0% = **−0.6 pp**.
- **Mix effect** — moving to the Year 2 mix at Year 2 rates: 6.0% − 3.0% = **+3.0 pp**.
- Sum: −0.6 + 3.0 = +2.4 pp = the observed 3.6% → 6.0%. ✓

Reading: quality genuinely improved (−0.6), but the product mix shifted toward the
high-defect segment (+3.0). The honest headline names both; either alone misleads.

## 7. Reversing changes and tax-inclusive amounts

To undo a change, divide by its factor:

| Known | Question | Wrong way | Right way |
|---|---|---|---|
| Price 150 after +25% | Original price? | 150 − 25% = 112.50 | 150 ÷ 1.25 = 120 |
| Receipt 121.00, VAT 21% | Net and tax? | 121 × 0.21 = 25.41 tax | 121 ÷ 1.21 = 100 net; tax 21.00 |
| Salary 46,000 after +15% raise | Before the raise? | 46,000 − 15% = 39,100 | 46,000 ÷ 1.15 = 40,000 |

Checks: 120 × 1.25 = 150 ✓; 100 × 1.21 = 121 ✓; 40,000 × 1.15 = 46,000 ✓. The wrong way
always overshoots because it takes the percent of the *new*, larger base.

## 8. Successive changes and discount stacking

Convert to factors, multiply, convert back:

| Sequence | Factors | Net | Not |
|---|---|---|---|
| +20% then +30% | 1.20 × 1.30 = 1.56 | +56% | +50% |
| −20% then −30% | 0.80 × 0.70 = 0.56 | −44% | −50% |
| −50% then +50% | 0.50 × 1.50 = 0.75 | −25% | 0% |
| +10% then −10% | 1.10 × 0.90 = 0.99 | −1% | 0% |

Order never matters for the net result (multiplication commutes): a 20% discount then 7% tax
is 0.80 × 1.07 = 0.856, identical to taxing first and discounting after. Note the boundary of
this skill: two or three steps compose by hand; a *series* of periodic changes (monthly for a
year, annually for a decade) is exponential-growth territory → the
`math-foundations-skills:exponential-growth-and-logs` sibling.

## 9. Rates, per-1,000, and per capita

Counts measure size; rates measure intensity. Normalize to a common exposure before ranking:

| Site | Incidents | Exposure | Rate per 1,000 |
|---|---|---|---|
| Plant A | 12 | 400 people | 12 ÷ 400 × 1,000 = 30 |
| Plant B | 18 | 900 people | 18 ÷ 900 × 1,000 = 20 |

Plant B has 50% more incidents (18 vs 12) and a 33% lower rate (20 vs 30: 10 ÷ 30 = 0.333).
Which is "worse" depends on the question — but ranking by raw count silently assumes equal
exposure. The same shape appears with cities (crimes per 1,000 residents), portfolios (losses
per $1M), and pipelines (failures per 1,000 runs). Choose the denominator that matches the
exposure actually generating the events, and say it out loud: "per person-year" and "per
visit" can rank the same two hospitals differently.

## 10. Small, zero, and negative bases

Percent change divides by the base, so it degrades as the base shrinks:

- Small base: going from 4 users to 10 is (10 − 4) ÷ 4 = +150% — arithmetically true and
  practically empty. Quote the absolutes ("from 4 to 10").
- Zero base: from 0 to anything is undefined (division by zero). Say "new" rather than "∞%."
- Negative base: from −50 to +50 gives (50 − (−50)) ÷ (−50) = −200% — a nonsense sign for an
  improvement. For quantities that cross zero (profit, net cash flow), report the absolute
  change ("improved by 100, from −50 to +50") and drop the percent entirely.

A useful reflex: whenever a percent change looks spectacular, ask for the base. Spectacular
percents on tiny bases are how weak results get dressed up.
