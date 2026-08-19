---
name: number-sense-and-estimation
description: >-
  Does trustworthy mental math and back-of-the-envelope figuring: decomposes hard arithmetic
  into easy pieces (10% and 1% benchmarks, compensation, round-then-correct), keeps only honest
  digits (significant figures, spotting spurious calculator and spreadsheet precision), works in
  orders of magnitude and scientific notation, builds Fermi estimates by decompose → bound →
  triangulate (an optimistic and a pessimistic bound that bracket the answer), and gut-checks
  any computed number — sign, magnitude, units, an independent rough re-derivation — before
  trusting it. Use when a rough number is needed fast, before accepting the output of a long
  calculation or model, or when a figure smells wrong. Triggers: mental math, Fermi estimate,
  back-of-the-envelope, order of magnitude, rough number, ballpark, does this number make
  sense, significant figures, rounding, quick math, eyeball the math.
metadata:
  version: "1.1.0"
---

# Number sense and estimation

Estimation is not a worse version of calculation — it is a second, independent way of reaching
a number. Calculation produces digits; estimation tells you whether those digits could
possibly be right.

## When to use
- Doing arithmetic in your head or on paper, fast, without reaching for a calculator.
- Producing a rough figure for a quantity nobody has measured — a Fermi / back-of-the-envelope
  question ("how many appointments does a 3-chair dental office run per year?").
- Gut-checking a number that a spreadsheet, model, or another person just handed you, before
  trusting it or passing it on.
- Deciding how many digits of a result are real and how many are calculator theater.
- Not for: disciplining a material estimate against a distribution of comparable past outcomes
  — that is formal outside-view work → see `decision-science-skills:reference-class-forecasting`.
- Not for: summarizing a dataset you already have (typical value, spread, shape) → see
  `data-analytics-bi-skills:descriptive-statistics`.
- Companion legs: the units half of a full number check lives in
  `math-foundations-skills:units-and-dimensional-analysis`; percent arithmetic and its traps in
  `math-foundations-skills:percentages-and-proportions`.

## Do it

### 1. Estimate before you calculate — and before you look
Write down your own rough answer before running the formula, opening the spreadsheet, or
reading the number you were given. Once a figure is in view it anchors you, and the
"independent check" quietly becomes a rationalization of it. Thirty seconds of rough figuring
first is what keeps the check independent.

### 2. Do mental arithmetic with structure, not strain
Each move below is exact, not approximate:
- **Decomposition** — split by place value: 7 × 480 = 7 × 400 + 7 × 80 = 2,800 + 560 = 3,360.
- **Benchmarks** — 10% moves the decimal one place, 1% moves it two, 5% is half of 10%.
  For 3,420: 10% = 342 and 1% = 34.2, so 3% = 3 × 34.2 = 102.6. A 15% tip on $62:
  10% = $6.20, plus half of that ($3.10) = $9.30.
- **Compensation** — round to something easy, then correct:
  297 + 458 = (300 + 458) − 3 = 755; 98 × 47 = 100 × 47 − 2 × 47 = 4,700 − 94 = 4,606.
- **Nearby squares** — (a − b)(a + b) = a² − b²: 19 × 21 = 20² − 1 = 399.
- **Double-and-halve** — 16 × 35 = 8 × 70 = 560.
- **Percent swap** — a% of b = b% of a: 16% of 25 = 25% of 16 = 4.

### 3. Work orders of magnitude in scientific notation
For rough multiplication, one significant digit plus a power of ten is enough: multiply the
mantissas, add the exponents. 47,000 × 0.002 = (4.7 × 10⁴) × (2 × 10⁻³) = 9.4 × 10¹ = 94.
Getting the exponent right is the whole game — a mantissa off by 30% is still a useful
estimate, but an exponent off by one is a wrong answer. Keep a small stock of anchor
quantities (86,400 seconds in a day; roughly 2,000 work hours and 250 working days in a year);
benchmark tables live in `references/estimation-methods.md`.

### 4. Fermi-estimate the unmeasured: decompose → bound → triangulate
1. **Decompose** the quantity into factors you can each roughly judge on their own.
2. **Bound** it: compute a central figure, then a high and a low version by pushing every
   factor to the plausible extreme that moves *the result* the same way — which means the
   opposite extreme for any factor in a denominator (more riders raises the bus count; more
   seats per bus lowers it). Then check the bounds bracket the central figure.
3. **Triangulate**: re-derive the number through a *different* decomposition and check it
   lands inside the same bounds. Agreement between independent routes is the evidence.

Compact example — appointments per year at a 3-chair dental office:
- Route 1: 3 chairs × 7 appointments per chair-day × 250 working days = 5,250.
- Bounds: low 3 × 5 × 230 = 3,450; high 3 × 9 × 260 = 7,020 — they bracket 5,250.
- Route 2: roughly 2,000 active patients × 2.5 visits per year = 5,000 — inside the bounds.
- Report "about five thousand, plausibly 3,500–7,000," not "5,250."
Fully worked examples, every multiplication shown: `references/estimation-methods.md`.

### 5. Round honestly — precision is a claim
A result carries no more precision than its shakiest input. If a budget of "about $1,000" is
split seven ways, the spreadsheet's 142.857142857 is fiction past the first two digits — say
"roughly $140 each." Carry extra digits through intermediate steps, round once at the end,
and report only digits you can defend: 2.5 × 3.1415926 with the 2.5 known to two figures
is 7.9, not 7.8539815.

### 6. Sanity-check a computed number before trusting it
Run the five questions (expanded protocol in `references/estimation-methods.md`):
1. **Sign** — should this be positive or negative? A negative per-unit cost is a wiring error.
2. **Magnitude** — right power of ten? Monthly payroll of $840k makes annual pay about $10.1M
   (840,000 × 12 = 10,080,000); a model reporting $100M is off by a factor of ten.
3. **Units** — does the formula's unit algebra actually deliver the units of the answer?
   (This leg belongs to `math-foundations-skills:units-and-dimensional-analysis`.)
4. **Independent re-derivation** — reach the number by a different rough route. Re-running
   the original formula only rechecks the typing, not the thinking.
5. **Edge behavior** — feed the formula 0, 1, or something huge; does it respond sensibly?
A number that passes all five is not proven right; a number that fails any one is not yet
trustworthy.

## Why / learn

**A wrong exact answer looks exactly like a right one.** Calculation is a high-precision,
low-redundancy channel: it emits eight confident digits whether the model behind it is sound
or broken, and a dropped minus sign or a ×1,000 unit slip passes straight through. Estimation
is the redundancy — low precision, but its errors are of a completely different kind, so the
two channels rarely fail the same way. When they agree, trust the digits; when they disagree,
trust neither until you know why.

**Ranges beat points.** A point estimate hides its own uncertainty; a range confesses it. The
bounds also do real work later: if a subsequent "exact" figure falls outside them, either the
calculation or the bounds contains a wrong assumption — and either way you have learned
something a point estimate could never have told you.

**Why Fermi decomposition works.** One wild guess becomes several tame ones, and in a product
the factor errors partially cancel — being 40% high on one factor and 30% low on another
nearly nets out. That cancellation is also why triangulation is strong evidence: two routes
built from *different* factors agreeing near 5,000 is far harder to achieve by luck than
either route alone.

**Anchoring is the quiet failure.** An estimate made after seeing a number is not an estimate
— it is an adjustment away from that number, and people adjust too little. The discipline of
step 1 (your figure first, in writing) is the only reliable countermeasure, which is why it is
the first step and not a footnote.

**Spurious precision is a confidence claim.** Digits communicate certainty whether you intend
it or not: "142.86" asserts you know the answer to one part in ten thousand. Rounding to what
you actually know is not sloppiness — it is honesty about the measurement, and it stops
readers from building on precision that was never there.

## Common mistakes
- Reading the given number before making your own → anchored; estimate first, then compare.
- Reporting a Fermi result to three digits ("5,250") → the digits overstate what you know;
  give one significant figure and the range.
- Bounding by varying only one factor, or pushing every factor to the same numeric
  extreme regardless of where it sits in the formula → falsely narrow bounds. Push each
  factor to the extreme that moves the *result* the same way; denominators reverse.
- Verifying a calculation by re-running it → catches typos only; re-derive by a different route.
- Rounding at every intermediate step → rounding error compounds; keep digits, round once at
  the end.
- Losing the exponent while juggling mantissas → track powers of ten separately; the exponent
  is the answer.
- Treating "passed the sanity check" as "verified" → passing makes a number plausible, not
  proven; say which checks it passed.

## Tailor to your environment
The benchmarks that make you fast are the ones from your own world. Record in
`references/your-environment.md` the anchor quantities of your domain — headcounts, typical
transaction sizes, daily volumes, rough revenue per working day — plus your house rounding
conventions and the figures you are most often asked to gut-check. Keep committed entries
structural and sanitized; real dollar figures or client specifics go in
`your-environment.private.md`, which is git-ignored.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/number-sense-and-estimation.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/estimation-methods.md — the mental-math toolkit expanded, anchor-quantity
  benchmark tables, two fully worked Fermi examples (decompose → bound → triangulate with
  every multiplication shown), the five-question protocol, and rounding rules
- references/your-environment.md — your own benchmark numbers and conventions
