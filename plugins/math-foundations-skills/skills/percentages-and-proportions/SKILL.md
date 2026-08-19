---
name: percentages-and-proportions
description: >-
  Does percent arithmetic without falling into its classic traps: percent of, percent change
  vs percent difference, the asymmetry of gains and losses (down 50% needs up 100% to get
  back), percentage points vs percent, basis points, markup vs margin, per-unit rates and
  per-1,000 normalization, index numbers and rebasing, weighted averages when a plain average
  of rates would mislead, and mix effects where a total moves opposite to every subgroup.
  Names the base first — percent OF WHAT — because most percent errors are base errors, and
  successive changes multiply rather than add. Use when computing or checking a percent
  change, comparing rates across groups of different sizes, converting markup to margin,
  quoting basis points, or when a percent-based claim looks off. Triggers: percent change,
  percentage points, percent vs percentage points, basis points, weighted average, markup vs
  margin, proportion, per capita, rate per, of what base, index and rebase.
---

# Percentages and proportions

A percentage is a fraction wearing a disguise: the numerator is on display and the
denominator is hidden. Nearly every percent error — and most percent-based spin — lives in
that hidden denominator, so the first question is always the same: *percent of what?*

## When to use
- Computing or checking percent of, percent change, or percent difference; converting among
  percent, percentage points, and basis points.
- Comparing rates across groups of different sizes: normalizing per-1,000 or per capita,
  weighting a combined rate, or explaining why a total moved against its subgroups.
- Converting markup to margin (or back); building, reading, or rebasing an index series.
- Not for: liquidity, leverage, and profitability ratios as company diagnostics — that
  is financial-statement ratio analysis, a finance-domain skill this library does not carry.
  The percentage machinery here is the same; the interpretation is not.
- Not for: summarizing a dataset (typical value, spread, shape) → see
  `data-analytics-bi-skills:descriptive-statistics`.
- Multi-period growth math — CAGR, doubling time, log scales — belongs to the sibling
  `math-foundations-skills:exponential-growth-and-logs`; single-step percent moves live here.
- Gut-checking whether the resulting number is even plausible → sibling
  `math-foundations-skills:number-sense-and-estimation`.

## Do it

### 1. Name the base before touching the numbers
Write every percent as "p% of B" with B explicit. "Sales fell 30%" is incomplete until you
can say from what — last quarter? last year? plan? Chained shares multiply against shrinking
bases: if 40% of respondents chose product X, and 25% *of those* would pay more, that is
0.40 × 0.25 = 0.10 → 10% of all respondents, not 25% and not 65%.

### 2. The three core computations
- **Percent of:** (p ÷ 100) × B. 12% of 450 = 0.12 × 450 = 54.
- **Percent change** (directional; base = the starting value): (new − old) ÷ old.
  100 → 120 is +20%; 120 → 100 is −16.7% (20 ÷ 120). Same gap, different base — percent
  changes are not symmetric.
- **Percent difference** (symmetric; base = the midpoint): |a − b| ÷ ((a + b) ÷ 2).
  120 vs 100 → 20 ÷ 110 = 18.2%. Use it when neither value is the natural "before."

### 3. Reverse a change by dividing, never subtracting
A change is a scale factor: +25% is ×1.25, and undoing ×1.25 is ÷1.25. A price of 150 after
a 25% increase started at 150 ÷ 1.25 = 120 — not 150 − 25% = 112.50. Tax-inclusive amounts
work the same way: a 121.00 receipt at 21% VAT contains 121 ÷ 1.21 = 100.00 net and 21.00
tax; computing 121 × 0.21 = 25.41 taxes the tax.

### 4. Successive changes multiply
Convert each change to its factor and multiply: +20% then +30% is 1.20 × 1.30 = 1.56 →
+56%, not +50%. Stacked discounts of 20% and 30% are 0.80 × 0.70 = 0.56 → 44% off, not 50%.
The gain/loss asymmetry falls straight out: down 50% then up 50% is 0.50 × 1.50 = 0.75 —
still 25% below the start. Recovering from a loss of L requires a gain of L ÷ (1 − L):
−20% needs +25%, −50% needs +100% (full recovery table in `references/percentage-traps.md`).

### 5. Percentage points vs percent — and basis points
A move from 4% to 6% is **+2 percentage points** (absolute difference of two percentages)
and **+50% relative** (2 ÷ 4). These are different quantities; the honest sentence quotes
both: "up two points, from 4% to 6% — a 50% relative increase." One basis point is 0.01
percentage points: 4.00% + 50 bp = 4.50%, and 25 bp on a $10M balance is
10,000,000 × 0.0025 = $25,000.

### 6. Markup vs margin
Markup is profit over **cost**; margin is profit over **price** — the same dollars against
two different bases. With cost 100 and price 150: markup = 50 ÷ 100 = 50%, margin =
50 ÷ 150 = 33.3%. Conversions: margin = markup ÷ (1 + markup); markup = margin ÷ (1 − margin).
Pricing for a 25% margin therefore needs a 0.25 ÷ 0.75 = 33.3% markup — pricing "cost + 25%"
delivers only a 0.25 ÷ 1.25 = 20% margin. Conversion table in `references/percentage-traps.md`.

### 7. Rates: normalize before comparing
Counts compare sizes; rates compare performance. Divide by the exposure denominator and quote
per-unit: 12 safety incidents at a 400-person site is 12 ÷ 400 = 30 per 1,000; 18 incidents
at a 900-person site is 18 ÷ 900 = 20 per 1,000. More incidents, lower rate — the raw counts
rank the sites backwards. Pick the per-what (per 1,000, per capita, per FTE, per transaction)
to fit the exposure that actually drives the events.

### 8. Combine rates as a weighted average — weight by the denominator
Defect rates of 2% on 9,000 units and 10% on 1,000 units: the plain average says
(2 + 10) ÷ 2 = 6%, but the true overall rate is (0.02 × 9,000 + 0.10 × 1,000) ÷ 10,000 =
(180 + 100) ÷ 10,000 = 2.8%. A plain average of rates is only correct when every denominator
is equal; otherwise recompute from the underlying totals.

### 9. Mix effects: a total can move against every subgroup
Because the overall rate is a share-weighted blend, it shifts when the *mix* shifts — even
if every subgroup improves:

| Period | Segment | Volume | Defect rate | Defects |
|---|---|---|---|---|
| Year 1 | A | 8,000 | 2.0% | 160 |
| Year 1 | B | 2,000 | 10.0% | 200 |
| Year 1 | **Total** | **10,000** | **3.6%** | **360** |
| Year 2 | A | 4,000 | 1.5% | 60 |
| Year 2 | B | 6,000 | 9.0% | 540 |
| Year 2 | **Total** | **10,000** | **6.0%** | **600** |

Both segments got better (2.0% → 1.5%; 10.0% → 9.0%), yet the total worsened from 3.6% to
6.0% because volume shifted from the clean segment (80% → 40% of the mix) to the dirty one.
Before declaring improvement or decline from a blended rate, check whether the mix moved;
the rate-effect vs mix-effect decomposition is worked in `references/percentage-traps.md`.

### 10. Index numbers and rebasing
An index restates a series relative to a base period set to 100: index_t = 100 × value_t ÷
value_base. The series 80, 100, 120 indexed on its first period reads 100, 125, 150. To
rebase onto the middle period, divide by that period's index and rescale: 100 ÷ 125 × 100 =
80; 125 ÷ 125 × 100 = 100; 150 ÷ 125 × 100 = 120. Index *points* are not percent: a move
from 150 to 165 is +15 points but 15 ÷ 150 = +10%.

## Why / learn

**The base is the whole game.** Percent errors are rarely arithmetic errors; they are base
errors — the right operation applied to the wrong denominator. That is why step 1 is naming
the base, why percent change and percent difference disagree (different bases for the same
gap), and why markup and margin disagree (same profit, cost base vs price base). When a
percent claim is confusing or fishy, recover the underlying fraction and both mysteries and
spin usually dissolve.

**Why changes multiply.** A percent change is a scale factor — +20% means ×1.20 — and
applying changes in sequence composes the factors. Adding them is a linearization that only
approximates when changes are small (1.05 × 1.03 = 1.0815, close to the added 8%); at
everyday magnitudes it fails badly (1.20 × 1.30 = 1.56, not 1.50). The gain/loss asymmetry is
the same fact seen from the other side: after a loss the base is smaller, so the recovery
percent must be larger — the −50%/+100% pair is not a paradox, it is ÷2 followed by ×2.

**Why reversing needs division.** "Undo ×1.25" is ÷1.25, and ÷1.25 = ×0.80 — a 20% cut, not
25%. Subtracting the same percent takes it from the *new*, bigger base and overshoots.

**Why weighting matters.** A rate is a fraction, and fractions combine by adding numerators
and denominators separately — never by averaging the quotients. The plain average hands a
1,000-unit segment the same voice as a 9,000-unit one; weighting by the denominator restores
each observation's actual share of the evidence. Mix effects are the same mathematics run in
time: the blend moved because the weights moved. This is Simpson's paradox in its everyday
form, and the resolution is always to show the subgroup rates and the mix side by side.

## Common mistakes
- Adding successive percent changes → convert to factors and multiply (1.20 × 1.30 = 1.56).
- Reversing a change by subtracting the same percent → divide by the factor
  (150 ÷ 1.25 = 120).
- Saying "percent" when the move is percentage points (or vice versa) → quote both: "up 2
  points, from 4% to 6% — a 50% relative rise."
- Pricing with markup where margin is meant → convert first; cost + 25% yields a 20% margin,
  not 25%.
- Taking a plain average of rates over different-sized groups → weight by the denominator or
  recompute from totals.
- Ranking groups by raw counts → normalize to a rate per common exposure first.
- Quoting percent change from a tiny, zero, or negative base → the figure explodes or loses
  meaning; give the absolute change instead.
- Treating a total that moves against every subgroup as a data error → usually a mix shift;
  decompose rate effect vs mix effect before escalating.
- Reading index points as percent → points are absolute on the index scale; divide by the
  level for the percent move.

## Tailor to your environment
Record your house conventions in `references/your-environment.md`: whether rate moves are
quoted in basis points or percentage points, whether pricing is stated as markup or margin,
standard index base periods, default rate denominators (per-1,000, per FTE, per transaction),
and rounding conventions for quoted percents. Keep committed entries structural; real prices,
rates, or client figures go in `your-environment.private.md`, which is git-ignored.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/percentages-and-proportions.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/percentage-traps.md — the trap catalog with verified worked numbers: the
  gain/loss recovery table, points-vs-percent examples, basis-point table, markup↔margin
  conversion table, weighted-average and mix-effect worked tables with the rate/mix
  decomposition, reversal and inclusive-tax examples, and small-base warnings
- references/your-environment.md — your quoting, pricing, and base-period conventions
