# Forecast model and accuracy (reference)

## Contents
- Direct vs. indirect method
- The 13-week structure
- Drivers and timing rules
- Accuracy metrics

## Direct vs. indirect method
- **Direct method** — sum projected **receipts** and **disbursements** by category on the dates cash
  moves. Bottom-up, bank-aligned, short-horizon. The treasury standard for liquidity management.
- **Indirect method** — start from projected **net income**, add back non-cash items (depreciation,
  amortization), adjust for **working-capital** changes (Δ AR, Δ inventory, Δ AP) and financing/
  investing. Ties to the P&L and balance sheet; suited to 12-month+ planning. Poor at telling you
  *which week* is tight.
- Rule of thumb: **direct for treasury (days–weeks), indirect for FP&A (months–years)**. They should
  reconcile in total over a long horizon.

## The 13-week structure
- 13 weekly buckets ≈ one quarter — long enough to see a debt maturity or seasonal trough, short
  enough to model from real drivers. Common in treasury and standard in liquidity monitoring / turnaround.
- Layout: rows = receipt and disbursement categories; columns = weeks 1–13. Each week:
  `opening + total receipts − total disbursements = closing`, carried to next week's opening.
- Add a **minimum/target balance** row and a **surplus/(shortfall)** row so covenant or overdraft
  breaches surface by week.
- **Roll weekly:** drop the elapsed week, add week 14, and reforecast the near weeks with actuals so the
  horizon stays 13.

## Drivers and timing rules
| Line | Driver | Timing rule |
|------|--------|-------------|
| AR collections | Open AR aging × collection curve (or DSO) | When customers actually pay, by cohort |
| Card / lockbox | Sales × settlement lag | Settlement date, not sale date |
| AP disbursements | Payment-run calendar × terms | Scheduled run date |
| Payroll | Headcount × pay cycle | Pay dates (incl. off-cycle, taxes) |
| Debt service | Loan/bond schedule | Contractual interest/principal dates |
| Tax | Estimated-tax / VAT calendar | Statutory payment dates |
| Capex / dividends | Project & board schedules | Committed payment dates |

Forecast the **driver and its timing**, not a straight line of the total — cash timing is lumpy and
causal, so a modeled driver captures the week-to-week shape that an average erases.

## Accuracy metrics
- **Variance %** = (actual − forecast) / forecast, per period/category. Sign shows direction.
- **MAPE** (mean absolute percentage error) = average of |actual − forecast| / |actual| across
  periods. Magnitude of error; lower is better.
- **Bias** = average signed error. Non-zero bias means a systematic over/under to fix at the driver.
- **Accuracy by horizon** — week 1 should beat week 13; track separately so you know how far out the
  forecast is trustworthy.
- Use variance analysis as a **feedback loop**: diagnose the miss to a driver (curve, lag, calendar)
  and correct the rule — do not just overwrite the number.
