# Growth math, worked and recomputed

Every number below is computed step by step and then checked by an independent
recomputation (usually by reproducing the endpoint). If you change an input, rerun
both directions.

## Contents
1. Growth factors and chaining
2. CAGR — two worked examples
3. Doubling and halving time; rule-of-72 accuracy table
4. Solving for time (and the dimensional check)
5. Geometric vs arithmetic averaging of growth rates
6. Reading log charts honestly

## 1. Growth factors and chaining
A percent change is a multiplication in disguise:

| Change | Factor |
|---|---|
| +12% | ×1.12 |
| −15% | ×0.85 |
| +100% (doubles) | ×2.00 |
| −50% (halves) | ×0.50 |

Chaining periods multiplies factors:
- +10% then −10%: 1.10 × 0.90 = 0.99 → down 1% overall.
- +50% then −50%: 1.50 × 0.50 = 0.75 → down 25% overall.
- Three years at +7%: 1.07³ = 1.07 × 1.07 × 1.07 = 1.1449 × 1.07 = 1.225043 → +22.5%,
  not +21%. The extra 1.5 points is growth acting on growth.

The order never matters (multiplication commutes), but the *base* of each percent is
always the running value — that is why the +10%/−10% pair loses ground.

## 2. CAGR — two worked examples
CAGR = (end/start)^(1/n) − 1, with n = the number of periods **between** the
endpoints (five annual observations span four years).

**Exact example.** 40,000 grows to 58,564 in 4 years.
- Ratio: 58,564 / 40,000 = 1.4641.
- Fourth root: 1.4641^(1/4). Since 1.10² = 1.21 and 1.21² = 1.4641, the fourth root
  of 1.4641 is exactly 1.10.
- CAGR = 1.10 − 1 = **10.0% per year**.
- Endpoint check: 40,000 × 1.10⁴ = 40,000 × 1.4641 = 58,564 ✓.

**Non-exact example.** 120 grows to 195 in 5 years.
- Ratio: 195 / 120 = 1.625.
- ln(1.625) = 0.48551; divide by 5 → 0.09710; exponentiate → e^0.09710 = 1.10197.
- CAGR ≈ **10.2% per year**.
- Endpoint check: 1.10197⁵ — 1.10197² = 1.21434; squared again = 1.47462;
  × 1.10197 = 1.62500 → 120 × 1.625 = 195 ✓.

CAGR is a *smoothing* summary: it is the single constant rate that connects the two
endpoints. It says nothing about the path between them — a series that went
+38%, −12% (1.38 × 0.88 = 1.2144) has the same CAGR as one that went +10.2% twice
(1.10197² = 1.2143).

## 3. Doubling and halving time; rule-of-72 accuracy
Exact doubling time at per-period rate r: **t = ln 2 / ln(1+r)** (ln 2 ≈ 0.6931).
The rule of 72 approximates this as 72 ÷ rate-in-percent.

| Rate r | Exact ln2/ln(1+r) | Rule of 72 | Rule error |
|---|---|---|---|
| 1%  | 69.66 periods | 72.0 | +3.4% |
| 2%  | 35.00 | 36.0 | +2.9% |
| 4%  | 17.67 | 18.0 | +1.9% |
| 6%  | 11.90 | 12.0 | +0.9% |
| 8%  | 9.01  | 9.0  | −0.1% |
| 10% | 7.27  | 7.20 | −1.0% |
| 12% | 6.12  | 6.0  | −1.9% |
| 18% | 4.19  | 4.0  | −4.5% |
| 24% | 3.22  | 3.0  | −6.9% |

Reading: the rule is excellent between roughly 4% and 12% (within ~2%), overshoots at
low rates (where 69.3 would be the better constant), and undershoots at high rates.
Outside that band, compute the exact form.

**Halving time** for a quantity decaying d% per period: t = ln 2 / |ln(1−d)|.
- At 15% decay per year: ln(0.85) = −0.16252, so t = 0.6931 / 0.16252 = **4.27 years**.
- Check: 0.85^4.27 → 4.27 × ln(0.85) = 4.27 × (−0.16252) = −0.6940 → e^−0.694 ≈ 0.4996
  ≈ ½ ✓.
- The rule of 72 gives 72/15 = 4.8 — noticeably too slow, because |ln(1−d)| > ln(1+d)
  for the same d: decay factors sit farther from 1 than their mirror-image growth
  factors. Use the exact form for decay.

## 4. Solving for time
Any "how long until it reaches X" question:

**t = ln(target/current) / ln(1+r)**

Worked: 5,000 growing at 12% per year; when does it reach 20,000?
- Ratio: 20,000 / 5,000 = 4.
- ln(4) = 1.38629; ln(1.12) = 0.11333.
- t = 1.38629 / 0.11333 = **12.23 years**.
- Consistency check: quadrupling is two doublings; doubling at 12% is
  0.6931/0.11333 = 6.116 years; 2 × 6.116 = 12.23 ✓.
- Endpoint check: 1.12^12.23 → 12.23 × 0.11333 = 1.3860 → e^1.386 ≈ 3.999 ≈ 4 ✓.

**Dimensional check** (run it every time):
- ln(target/current): a log of a pure ratio — the units of target and current cancel,
  leaving a dimensionless number.
- ln(1+r): r is per-period, so this term carries "per period."
- Dimensionless ÷ per-period = periods. The answer is in whatever period r is quoted
  in — a monthly rate gives months, an annual rate gives years. If your formula does
  not survive this check, it is not a time.

This same relation, applied to capacity margins, is the exhaustion-date formula in
`safety-and-reliability-skills:weight-of-the-books`: t = ln(F/F_floor)/ln(1+g), where
the "target/current" ratio is how far the current safety factor F can erode before it
hits the written floor F_floor while load grows at rate g.

## 5. Geometric vs arithmetic averaging of growth rates
The fair per-period rate is the **geometric** average of the factors:
(product of factors)^(1/n) − 1. It is the only average that reproduces the actual
endpoint when compounded.

Worked series: three annual returns +20%, −10%, +15%.

| Year | Return | Factor | Running product |
|---|---|---|---|
| 1 | +20% | 1.20 | 1.2000 |
| 2 | −10% | 0.90 | 1.0800 |
| 3 | +15% | 1.15 | 1.2420 |

- Actual 3-year outcome: ×1.242 (+24.2%).
- Geometric average: 1.242^(1/3) − 1. ln(1.242) = 0.21672; ÷3 = 0.07224;
  e^0.07224 = 1.07491 → **7.49% per year**.
  Check: 1.07491³ = 1.07491² (=1.15544) × 1.07491 = 1.24200 ✓.
- Arithmetic average: (20 − 10 + 15)/3 = 25/3 = **8.33% per year**.
  Compounded: 1.08333³ = 1.17361 × 1.08333 = 1.27141 → claims +27.1%, but the actual
  outcome was +24.2%. The arithmetic figure overstates by nearly 3 points of factor.

Extreme case: +50% then −50%. Actual: 1.5 × 0.5 = 0.75 (down 25%). Arithmetic
average: 0% ("flat"). Geometric: √0.75 − 1 = 0.86603 − 1 = **−13.4% per year**
(check: 0.86603² = 0.75 ✓). The arithmetic average of returns is always ≥ the
geometric, with equality only when every period's return is identical — so quoting
the arithmetic figure for a volatile series always flatters it.

## 6. Reading log charts honestly
On a log-scaled value axis:
- **Equal vertical distances are equal ratios** — the step from 10 to 100 is as tall
  as the step from 100 to 1,000.
- **A straight line is a constant growth rate**; its slope is the rate. Two parallel
  lines grow at the same rate no matter how far apart their levels are.
- **Bending down** means the rate is slowing even while the amounts still rise.

A log chart is the honest choice when:
- the series spans several orders of magnitude (a linear axis would crush the early
  history into the baseline);
- the question is about *rates* — comparing how fast two series grow, or spotting a
  change in rate;
- the process is multiplicative by nature, so ratio distance is the meaningful one.

It misleads when:
- the audience will read it as linear — the visual "slowing" of a perfectly steady
  exponential is the most common misread, so label the axis loudly;
- it is chosen to flatten an alarming rise (the same data that looks explosive on a
  linear axis looks tame on log — sometimes that is honest context, sometimes it is
  concealment; the difference is whether the question is about rate or about amount);
- the data contain zeros or negatives — a log axis cannot show them, and truncating
  or nudging them silently distorts the picture.

State which axis you chose and why. When both questions matter (how much AND how
fast), show both charts rather than making one axis do both jobs.
