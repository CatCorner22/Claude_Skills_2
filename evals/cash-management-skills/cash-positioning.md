# Evals — cash-management-skills:cash-positioning

## 1. Positive trigger (should load the skill)
> "I need to know how much cash we actually have available across our three USD accounts today
> before I decide how much to sweep to the concentration account. The AP run posts this afternoon."

Expected: skill loads; sets scope and cutoff; takes opening from the prior-day statement and uses the
available (not ledger) balance; layers confirmed vs. projected flows including the AP run; computes a
projected closing per account; compares to the target balance to size the sweep.

## 2. Near-miss (should NOT load this skill)
> "Build me a rolling 13-week cash flow forecast so I can see whether we'll have enough liquidity to
> cover the debt maturity in week 10."

Expected: this is a forward projection beyond the actuals horizon — a forecast, not a position. The
`cash-management-skills:cash-forecasting` skill should handle it. If this skill loads, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** positions to the available balance, keeps currencies/entities separate, tags
  actual vs. projected flows, computes opening + in − out = projected closing, and reads the gap to
  the target balance to size the sweep/funding move.
- **Teaches:** explains *why* positioning uses bank truth and available (not ledger) balance, why
  currencies and entities aren't netted, and how a position differs from a forecast (certainty vs.
  horizon) — not just the arithmetic.
- **Safe:** does not overstate cash by using the ledger balance or treating projected receipts as
  confirmed; does not net a shortfall in one currency against a surplus in another.
