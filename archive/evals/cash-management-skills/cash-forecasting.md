# Evals — cash-management-skills:cash-forecasting

## 1. Positive trigger (should load the skill)
> "Help me build a rolling 13-week cash forecast. I want to project collections off our AR aging and
> the AP payment runs, and I need to see if we dip below our minimum balance before the tax payment
> in week 7."

Expected: skill loads; selects the direct method for the horizon; sets weekly buckets; forecasts
receipts from the aging/collection curve and disbursements from the run calendar, payroll, tax, and
debt service on their payment dates; nets to a projected balance per week and flags the breach; sets
up rolling reforecast and variance tracking.

## 2. Near-miss (should NOT load this skill)
> "How much cash is actually available in our operating account right now so I can release today's
> wires?"

Expected: this is same-day availability — a cash position, not a projection. The
`cash-management-skills:cash-positioning` skill should handle it. If this skill loads, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** uses the direct method, models receipts and disbursements from drivers on their
  payment/collection dates, nets to a weekly projected balance, flags the minimum-balance breach, and
  establishes rolling reforecast plus variance/MAPE tracking.
- **Teaches:** explains *why* the direct method suits short-term treasury (vs. indirect for planning),
  why timing follows the driver rather than the invoice date, and how variance analysis and bias
  detection tighten accuracy — not just the layout.
- **Safe:** does not straight-line history in place of drivers, does not present a one-shot forecast
  as final without a reforecast cadence, and diagnoses misses to a driver rather than plugging numbers.
