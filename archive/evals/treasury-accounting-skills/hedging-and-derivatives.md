# Evals — treasury-accounting-skills:hedging-and-derivatives

## 1. Positive trigger (should load the skill)
> "We forecast €12M of EUR revenue next year and want to hedge it — evaluate this forward quote,
> tell me how much to hedge, and set it up so it doesn't whipsaw our earnings."

Expected: skill loads; sizes a layered partial hedge (not 100% of a forecast); checks the quote
against covered-interest-parity arithmetic and competes it; walks the lifecycle (ISDA, limits,
same-day confirmation); flags cash-flow-hedge designation with inception documentation as the
anti-whipsaw mechanism.

## 2. Near-miss (should NOT load this skill)
> "Which of our subsidiaries actually have FX exposure, and how do I measure our net position
> by currency?"

Expected: exposure identification/measurement — `finance-skills:fx-risk-basics`. If this skill
loads, tighten the execution/instruments framing.

## 3. Quality rubric
A good response:
- **Does the task:** appropriate instrument and hedge ratio, quote evaluated against the
  computable mid, full lifecycle covered, hedge accounting designated at inception.
- **Teaches:** hedges judged with the exposure (offset, not standalone P&L), forward points as
  rate differentials not forecasts, and why the accounting whipsaw is a timing artifact that
  designation bridges.
- **Safe:** warns against 100% forecast hedging, zero-cost collars treated as free, exotic
  payoffs, backdated designation, and ignoring counterparty exposure on in-the-money trades.
