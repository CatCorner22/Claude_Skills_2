# Evals — math-foundations-skills:units-and-dimensional-analysis

## 1. Positive trigger (should load the skill)
> "Our utility rate is $0.032 per kWh and we used 41,500 kWh last month — annualize
> that cost for the budget. Also, this formula from the old workbook looks off to me:
> days of liquidity = balance × monthly outflow / 30. Can you check whether the units
> even work?"

Expected: skill loads and does both with visible unit cancellation. The cost chain:
41,500 kWh/month × $0.032/kWh = $1,328/month (kWh cancels), then × 12 months/year =
$15,936/year — and it notes this ×12 is valid because a cost is a *flow*, distinguishing
it from a rate of return, which compounds and belongs to
`math-foundations-skills:exponential-growth-and-logs`.
The formula check writes the units of every term: balance ($) × monthly outflow
($/month) / 30 gives $²/month — not days, so the formula is refuted before any number
is computed. It then supplies the dimensionally sound form — days = balance ÷ (monthly
outflow ÷ 30 days/month) — and demonstrates it (e.g. $450,000 ÷ ($300,000/mo ÷ 30 d/mo)
= 450,000 ÷ 10,000 $/day = 45 days), teaching that units are algebra and a failed
dimension check refutes a formula regardless of how plausible its output looks.

## 2. Near-miss (should NOT load this skill — adjacent skill owns it)
> "We're sizing the new invoice-processing system before go-live. Peak is about 4× the
> daily volume and the document store grows every year — run the design review so we
> know it will hold at real volumes."

Expected: `safety-and-reliability-skills:weight-of-the-books` loads instead — sizing a
system against its payload, peak, growth curve, and outlier lot is the Load Manifest
method. Volumes and growth rates sound unit-flavored, but the ask is the design review,
not a conversion or a dimension check. If units-and-dimensional-analysis loads here,
its description is over-triggering. (The right division of labor: that skill runs the
review; this one checks that the sizing formulas inside it are dimensionally sound.)

## 2b. Near-miss (closer — should NOT load this skill)
> "Two reviewers keep disagreeing on the same exception queue — one calls a line a
> match, the other doesn't. Can we measure whether our measurement process itself is
> reliable before we trust the exception counts?"

Expected: `continuous-improvement-skills:measurement-systems-analysis` loads instead —
inter-rater agreement and gauge trustworthiness are Gage R&R / attribute-agreement
territory. "Measurement" is shared vocabulary, but wrong units are a translation
defect; noisy or inconsistent measurers are a measurement-system defect.

## 3. Quality rubric
A good response:
- **Does the task:** writes every starting quantity with its unit; writes each
  conversion factor as a fraction equal to 1 oriented so the unwanted unit cancels;
  shows the cancellation before computing numbers; confirms the surviving unit answers
  the question asked; converts rates to a common time base before dividing them; uses
  ×12 only on flows and routes compounding rates to the exponential-growth sibling; for
  formula checks, assigns units to every symbol, derives the units of every term,
  applies all three laws (added terms share a unit, sides match, exp/ln/exponent
  arguments dimensionless), and states the verdict before touching numbers. All shown
  arithmetic is correct and reproducible from the page.
- **Teaches:** explains that units multiply, divide, and cancel like symbols, so a
  carried unit is a free structural proof; why a conversion factor equals 1 and
  therefore preserves value; why a dimensional check is the cheapest formula review
  (fails with certainty, passes only provisionally); why flows add but growth
  compounds; and cites the library's own weight-of-the-books formula catch as evidence
  the check works on authors too.
- **Stays honest:** treats a *passed* dimension check as "worth testing numerically,"
  never as proof of correctness (a dimensionless constant can still be wrong); refutes
  a broken formula outright instead of patching its output to look plausible; keeps
  compound-growth math with `math-foundations-skills:exponential-growth-and-logs`
  rather than improvising it; routes system
  sizing to `safety-and-reliability-skills:weight-of-the-books` and gauge reliability
  to `continuous-improvement-skills:measurement-systems-analysis`; and flags any
  quantity it cannot assign a unit to as a finding rather than guessing one.
