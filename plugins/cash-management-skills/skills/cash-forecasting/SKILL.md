---
name: cash-forecasting
description: >-
  Builds direct-method short- and medium-term cash forecasts — projecting receipts and disbursements
  from operational drivers (AR collections, AP runs, payroll, debt service, tax) — and measures
  forecast-vs-actual variance to improve accuracy. Use when projecting liquidity, building a rolling
  13-week or monthly cash forecast, choosing the direct vs. indirect method, or reviewing forecast
  accuracy. Triggers: cash forecast, liquidity forecast, direct method, indirect method, rolling
  forecast, 13-week forecast, forecast variance, forecast accuracy, receipts and disbursements,
  project cash flow.
---

# Cash forecasting

## When to use
- Projecting cash receipts and disbursements over a short (daily/weekly) or medium (monthly) horizon.
- Building a rolling forecast (the 13-week cash flow is the treasury standard) or reviewing its accuracy.
- Choosing the direct vs. indirect method, or diagnosing why a forecast keeps missing.
- Not for: knowing exactly how much cash is available *today* to move → see
  `cash-management-skills:cash-positioning`. For statistical/ML projection of a driver series (e.g.
  collections) → see `machine-learning-skills:time-series-forecasting`.

## Do it
1. **Pick the method for the horizon.** For treasury liquidity (days to ~13 weeks) use the **direct
   method** — forecast actual receipts and disbursements bottom-up. For 12-month+ planning that ties
   to the P&L, use the **indirect method** (net income adjusted for non-cash items and working-capital
   changes). See `references/forecast-model-and-accuracy.md`.
2. **Set the horizon and the buckets.** Choose the period grain (daily, weekly, monthly) and horizon
   (e.g. 13 weeks). Define receipt and disbursement categories that map to real drivers — not GL
   accounts — so each line has an owner and a timing rule.
3. **Forecast receipts from collection drivers.** Project AR collections from the open AR aging and a
   **collection curve** (what % of a cohort pays in week 1, 2, …), plus other inflows: card/lockbox
   settlement, interest/investment maturities, tax refunds, debt draws.
4. **Forecast disbursements from commitment drivers.** Project AP from the payment-run calendar and
   terms, payroll from the pay cycle, plus debt service (interest/principal schedule), tax payment
   dates, capex, dividends, and rent/lease. Anchor each to its actual **payment date**, not invoice date.
5. **Assemble the forecast and net to a projected balance.** For each period: `opening + receipts −
   disbursements = closing`, carried forward. Flag periods that breach a minimum/target balance — that
   is the liquidity signal the forecast exists to raise.
6. **Roll it forward on a fixed cadence.** Each period, drop the elapsed period and add one at the far
   end to keep a constant horizon, and **reforecast** near periods with fresh actuals. A rolling
   forecast that is never revised is just a stale budget.
7. **Measure variance and feed it back.** Compare each period's actual to what you forecast; compute
   variance % and MAPE by category and by horizon; look for **bias** (consistent over/under). Fix the
   driver, not the number — a recurring miss means a timing rule or curve is wrong.

## Why / learn
The **direct method** wins for short-term treasury because it forecasts the thing treasury actually
manages — money in and out of the bank on specific dates — so the output lines up one-to-one with the
cash position and with real funding decisions. The **indirect method** starts from accrual profit and
backs into cash; it ties cleanly to the financial statements and is right for annual planning, but it
tells you little about *which week* you might be short, which is the whole point of a liquidity
forecast. The reason forecasting is **driver-based** rather than a straight-line of history is that
cash timing is lumpy and causal: collections follow an aging and a payment behavior, disbursements
follow a run calendar and contractual terms. Model the driver and the timing falls out; model the
total and you will be right on average and wrong every week. **Rolling** discipline matters because a
forecast is a hypothesis with a short shelf life — reforecasting with actuals is how it stays a
decision tool instead of decaying into a budget. And **variance analysis is the engine of accuracy**:
a forecast you never check cannot improve. Watching MAPE fall and hunting down bias is how a treasury
team earns the right to make funding and investment calls on the forecast rather than on the position
alone.

## Common mistakes
- Using the indirect method for a weekly liquidity forecast → you learn the annual total, not which week is tight. Use the direct method short-term.
- Timing off the invoice/accrual date → cash moves on the payment/collection date. Anchor lines to when money actually moves.
- Straight-lining history instead of modeling drivers → misses lumpy, causal timing. Forecast the driver (aging, run calendar), not the total.
- Never reforecasting → a rolling forecast that isn't revised is a stale budget. Reforecast near periods with actuals every cycle.
- Skipping variance analysis → the forecast never gets better. Track variance %/MAPE and correct the driver, not the number.
- Ignoring bias → a forecast that is always 8% high is fixable. Measure direction, not just magnitude, of error.

## Tailor to your environment
Drop your real drivers into `references/your-environment.md` (keep sensitive figures in
`your-environment.private.md`, which is git-ignored): your horizon and period grain, your receipt and
disbursement categories, your collection curve / DSO assumptions, your payment-run and payroll
calendars, your debt-service and tax schedules, and the minimum/target balance the forecast is checked
against. Record your accuracy targets (e.g. MAPE by horizon) so reviews are consistent. If you run
Oracle Fusion, cash forecasting extends the Cash Positioning cube with projected sources — pair this
with `cash-management-skills:cash-positioning`. For statistical forecasting of a driver series, hand it
to `machine-learning-skills:time-series-forecasting` and feed the output back as a driver here.

## References
- references/forecast-model-and-accuracy.md — direct vs. indirect, the 13-week structure, drivers, and accuracy metrics
- references/your-environment.md — your horizon, drivers, calendars, and accuracy targets (add when supplied)
