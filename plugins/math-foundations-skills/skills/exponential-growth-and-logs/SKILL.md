---
name: exponential-growth-and-logs
description: >-
  Does the math of anything that grows or shrinks by a roughly constant percent per period —
  growth-factor form (up r% means ×(1+r); n periods means ×(1+r)^n), CAGR from two endpoints,
  doubling time exactly (ln 2/ln(1+r)) and via the rule of 72 with its accuracy range, halving
  time for decay, solving how-long-until-it-reaches-X with logs (t =
  ln(target/current)/ln(1+r)), honest log scales, and averaging growth rates with the geometric
  mean, not the arithmetic. Teaches why percent changes multiply, not add, and why +10% then
  −10% ends below the start. Use when a quantity changes by a percent each period — revenue,
  users, prices — and the question is a rate, a horizon, or a fair per-period figure; not for
  discounting money across dates or fitting trend models to history. Triggers: exponential
  growth, CAGR, doubling time, rule of 72, logarithm, log scale, growth rate math, geometric
  average, how long until it doubles, decay rate.
metadata:
  version: "1.3.0"
---

# Exponential growth and logarithms

An exponential process is multiplication repeated: up r% per period means ×(1+r) per
period, and n periods means ×(1+r)^n. Everything about such a process therefore lives
in ratios and logarithms. This skill does that arithmetic — rates, horizons, fair
averages, honest charts — and teaches the intuition that linear thinking gets wrong.

## When to use
- A quantity changes by a roughly constant percent per period — revenue, users,
  prices, data volume, transaction counts — and you need a rate, a horizon, or a total.
- Computing a growth rate from two endpoints (CAGR), a doubling or halving time, or
  "how long until it reaches X."
- Averaging a series of period growth rates or returns into one fair per-period figure.
- Choosing or reading a log-scale chart for a fast-changing series.
- Not for: valuing money across time — PV/FV/NPV/IRR and discount rates are
  time-value-of-money work, a finance-domain topic this library does not carry; same (1+r)^n
  machinery, but the question there is worth, not size.
- Not for: fitting trend or seasonality models to a history → see
  `machine-learning-skills:time-series-forecasting`.
- Not for: sizing a system against projected load to an exhaustion date → see
  `safety-and-reliability-skills:weight-of-the-books`; its exhaustion-date relation
  t = ln(F/F_floor)/ln(1+g) is this skill's solve-for-time method applied to a
  capacity margin.
- Not for: single-period percent moves, percent vs percentage points, and mix
  effects → see sibling `math-foundations-skills:percentages-and-proportions`.

## Do it
1. **Convert every percent change to a growth factor.** Up 12% → ×1.12; down 15% →
   ×0.85. Factors are the working currency; percents are only the display format.
2. **Chain periods by multiplying factors.** n periods at rate r gives ×(1+r)^n, and
   mixed periods multiply their individual factors. This is why +10% then −10% ends
   below the start: 1.10 × 0.90 = 0.99, one percent under.
3. **CAGR from two endpoints:** CAGR = (end/start)^(1/n) − 1, where n counts the
   *periods between* the endpoints, not the data points. Worked: 40,000 → 58,564 over
   4 years: 58,564/40,000 = 1.4641; 1.4641^(1/4) = 1.10; CAGR = 10.0%. Check by
   recompounding: 40,000 × 1.10^4 = 40,000 × 1.4641 = 58,564 — it must reproduce the
   endpoint exactly, so always run this check.
4. **Doubling time.** Exact: t = ln 2 / ln(1+r). At 8% per year:
   0.6931/0.07696 ≈ 9.0 years. Shortcut: the rule of 72 — 72 ÷ rate-in-percent —
   gives 72/8 = 9. The rule stays within about ±2% of exact for rates of roughly
   4–12% (and within ±1% over 6–10%); it overshoots at lower rates and undershoots at
   higher ones (accuracy table in references/growth-math-worked.md).
5. **Any target, not just double:** t = ln(target/current) / ln(1+r). Worked:
   5,000 → 20,000 at 12% per year: ln(4)/ln(1.12) = 1.3863/0.11333 ≈ 12.2 years.
   Consistency check: quadrupling is two doublings, and 2 × ln 2/ln(1.12) =
   2 × 6.12 = 12.2 — same answer. Dimensional check: the numerator is the log of a
   pure ratio (units cancel), the denominator is per-period, so t lands in periods of
   whatever r is quoted in.
6. **Shrinking quantities.** A decay of d% per period is ×(1−d); the halving time is
   ln 2 / |ln(1−d)|. At 15% decay per year: 0.6931/0.16252 ≈ 4.3 years. Note that
   72/15 = 4.8 overstates it — the rule of 72 is calibrated for growth, and a decay
   factor sits farther from 1 than the same-percent growth factor.
7. **Average growth rates geometrically, never arithmetically.** The one fair
   per-period rate is (product of factors)^(1/n) − 1. Worked: returns +20%, −10%,
   +15%: 1.20 × 0.90 × 1.15 = 1.242, so 1.242^(1/3) − 1 ≈ 7.49% per year. The
   arithmetic average (20 − 10 + 15)/3 = 8.33% lies: compounding 8.33% for 3 years
   gives ×1.2714, but the actual outcome was ×1.242. Full table in the reference.
8. **Pick the chart scale to match the question.** A linear axis answers "how much";
   a log axis answers "how fast." On a log axis a straight line means a constant
   growth rate and equal vertical distances mean equal ratios. Say which axis you
   chose and why; the honesty guide is in references/growth-math-worked.md.

## Why / learn
**Exponential is repeated multiplication.** Each period's change acts on the previous
period's result, not on the original amount — so successive changes multiply, and
percents never add across periods. That is also why +10% then −10% loses ground: the
−10% acted on the larger, post-gain base. Logs make the asymmetry visible:
ln(1.10) = +0.0953 but ln(0.90) = −0.1054, so the down-leg is bigger in log space and
the sum is negative.

**A logarithm answers "what exponent."** log_b(x) is the exponent b needs to reach x.
Time enters exponential growth as the exponent in (1+r)^t, so every "how long until"
question is a log question: (1+r)^t = target/current, take logs, and
t = ln(target/current)/ln(1+r). The log turns repeated multiplication into division —
that is the whole trick. It is also why the geometric average is the fair one: it is
the ordinary average taken in log space, where compounding is additive.

**Linear intuition underestimates runaway.** Intuition extrapolates by adding: 1% a
day "should" give about +365% in a year (×4.65). The real answer is 1.01^365 ≈ ×37.8 —
an eightfold intuition gap in a single year, because growth compounds on growth and
the error compounds with it. When a compounding series looks flat early and explosive
late, nothing changed; that is what the same rate looks like on a linear axis.

**Why the rule of 72 works, and where.** For small r, ln(1+r) ≈ r, so
t = ln 2/ln(1+r) ≈ 0.693/r = 69.3/rate-in-percent. The bump from 69.3 to 72 partly
buys clean divisibility (2, 3, 4, 6, 8, 9, 12) and partly offsets ln(1+r) sitting
below r — which is exactly why the rule is at its best mid-range (about 4–12%) and
drifts at both ends.

## Common mistakes
- Adding percent changes across periods ("+10% and +10% is +20%") → multiply factors:
  1.10² = 1.21, so +21%.
- Averaging returns arithmetically → the geometric average is the one that reproduces
  the endpoint; the arithmetic one overstates whenever rates vary.
- CAGR with n = count of data points → n is periods *between* endpoints; five annual
  observations span four years (fencepost).
- Taking a CAGR across a zero or negative endpoint → end/start has to be positive.
  A sign change makes the ratio negative, which a spreadsheet answers with #NUM! and a
  math library with a complex number; two negative endpoints are worse, because they
  hand back a healthy-looking rate for a quantity that got worse (−100 to −400 over two
  years computes as (−400/−100)^(1/2) − 1 = +100% a year). Report the absolute change
  instead.
- Feeding a percent into the log (ln(1+12) instead of ln(1.12)) → r is the decimal
  rate; the dimensional check in step 5 catches this.
- Reading a solve-for-time answer without checking that r points at the target →
  t = ln(target/current)/ln(1+r) is undefined at r = 0 and goes negative when the rate
  runs away from the target (5,000 reaching 20,000 at −5% a year returns
  ln(4)/ln(0.95) = −27.0, which is the same law extrapolated backwards, not a
  forecast). Confirm the direction before reading the number as a horizon.
- Using the rule of 72 far outside 4–12% → compute ln 2/ln(1+r) instead.
- Reading a straight line on a log chart as constant amounts → it means constant
  rate; the amounts are accelerating.
- Choosing a log axis to flatten an alarming rise (or a linear axis to dramatize a
  routine one) → pick the axis for the question being asked, and label the choice.
- Treating the projected rate as a fact → the formula assumes r stays constant;
  whether it does is a claim about the world, so state it as an assumption.

## Tailor to your environment
Record in `references/your-environment.md`: which quantities you track that behave
exponentially (and their typical rates), your period conventions (calendar vs fiscal
year, month vs 4-week cycle), house rounding and display rules for rates, and your
default chart-axis policy. Keep committed content structural — real figures, client
names, or internal projections belong in `your-environment.private.md` (git-ignored),
never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/exponential-growth-and-logs.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/growth-math-worked.md — worked CAGR, doubling-time, and solve-for-time
  examples with every step recomputed; the rule-of-72 accuracy table; the
  geometric-vs-arithmetic averaging table; the log-chart reading guide
- references/your-environment.md — your compounding quantities, period conventions,
  and chart norms (fill in)
