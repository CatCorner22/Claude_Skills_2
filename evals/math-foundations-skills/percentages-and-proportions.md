# Evals — math-foundations-skills:percentages-and-proportions

## 1. Positive trigger (should load the skill)
> "Our conversion rate went from 2% to 3%. Marketing wants to announce 'conversions up 50%'
> and finance says it's only a 1% improvement — who's right? And how would I quote that move
> in basis points?"

Expected: the skill loads and shows both statements describe the same move on different
bases: +1 percentage point (absolute difference of two percentages) and +50% relative
(1 ÷ 2 = 0.50) — and that "a 1% improvement" is the one framing that is simply wrong. It
recommends the sentence that quotes both ("up one point, from 2% to 3% — a 50% relative
increase"), converts to basis points (1 pp = 100 bp), and teaches why the base is the source
of the disagreement. Bonus: it asks whether the denominator (traffic) shifted between
periods before certifying the improvement.

## 2. Near-miss (should NOT load this skill)
> "Here's the balance sheet and income statement. Compute the current ratio, quick ratio,
> debt-to-equity, and ROE, and tell me whether the company looks healthy."

Expected: should NOT trigger this skill. Liquidity, leverage, and profitability measures
read as company diagnostics — with benchmarks, trends, and DuPont — are financial
statement analysis (whose former owner is archived from this library), not percent
arithmetic. If percentages-and-proportions loads here, its description is over-triggering.

## 2b. Near-miss (closer — should also NOT load this skill)
> "Revenue went from $2M to $3.5M over four years. What's the annualized rate, and how long
> until it doubles at that pace?"

Expected: `math-foundations-skills:exponential-growth-and-logs` loads instead. Multi-period
compounding — CAGR, doubling time — is the exponential sibling's territory; this skill owns
single-step percent moves and their composition over two or three steps, not rate-over-time
math.

## 3. Quality rubric
A good response:
- **Does the task:** names the base of every percent before computing; converts changes to
  factors and multiplies for successive moves (1.20 × 1.30 = 1.56); reverses changes by
  division (150 ÷ 1.25 = 120), never subtraction; distinguishes percentage points, relative
  percent, and basis points and quotes the honest both-forms sentence; converts markup↔margin
  with the ÷(1 + m) / ÷(1 − m) formulas; weights combined rates by their denominators or
  recomputes from totals; normalizes counts to per-exposure rates before ranking; checks for
  a mix shift before interpreting a blended rate, decomposing rate effect vs mix effect when
  the total moves against subgroups.
- **Teaches:** explains that a percentage is a fraction with a hidden denominator and most
  percent errors are base errors; why changes multiply (scale factors) and when addition
  approximately works (small changes only); why recovering a loss takes a larger gain (the
  shrunken base); why plain-averaging rates over unequal groups misleads.
- **Stays honest:** every worked number is recomputable from its shown arithmetic; percent
  changes from tiny, zero, or negative bases are declined in favor of absolute changes;
  a spectacular percent claim triggers "what's the base?" rather than amplification; and the
  answer declines company-health ratio work as financial-statement analysis (not percent
  arithmetic), routes dataset summaries to `data-analytics-bi-skills:descriptive-statistics`,
  and CAGR/doubling-time asks to `math-foundations-skills:exponential-growth-and-logs`
  rather than absorbing them.
