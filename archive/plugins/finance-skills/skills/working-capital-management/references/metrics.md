# Working-capital metrics (reference)

`D` = days in the period (365 for a year, 90/91 for a quarter, actual days for a month). Use average
balances — `(opening + closing) / 2` — unless you deliberately want a point-in-time snapshot, and use
the *same* `D` across all three metrics so the CCC is coherent.

## The three day-metrics
| Metric | Formula | Driver base | Reads as |
|---|---|---|---|
| DSO (days sales outstanding) | `Average AR / Credit Sales × D` | credit sales | days to collect a sale |
| DIO (days inventory outstanding) | `Average Inventory / COGS × D` | COGS | days inventory sits before sale |
| DPO (days payable outstanding) | `Average AP / COGS × D` | COGS (or purchases) | days you take to pay suppliers |

- DSO uses **credit** sales, not total revenue — cash sales never create a receivable, so including
  them understates true collection speed. If credit sales are unavailable, note the approximation.
- DIO and DPO sit at **cost**, so both use COGS (some analysts use purchases for DPO — `purchases =
  COGS + ending inventory − beginning inventory`; disclose which you used).
- Turnover ratios are the reciprocals scaled by `D`: `receivables turnover = Credit Sales / Avg AR`,
  `inventory turnover = COGS / Avg Inventory`, `payables turnover = COGS / Avg AP`. `DSO = D /
  receivables turnover`, and so on.

## Cycles
- Operating cycle = `DSO + DIO` — total days from buying inventory to collecting the resulting sale.
- Cash conversion cycle: `CCC = DSO + DIO − DPO`. DPO is subtracted because supplier credit finances
  part of the operating cycle at no cash cost to you.
- A **negative CCC** means you collect from customers before you pay suppliers — the business runs on
  supplier float and throws off cash as it grows. Confirm it is structural, not just stretched payables.

## Translating days into cash
Cash freed by a sustained improvement ≈ `Δdays × daily driver`:
- Reduce DSO by `x` days → releases `x × (Credit Sales / D)`.
- Reduce DIO by `x` days → releases `x × (COGS / D)`.
- Increase DPO by `x` days → releases `x × (COGS / D)`.
The release is a one-time cash unlock that persists while the new level holds; it is not recurring
profit. Always report the currency amount alongside the day change.

## Cost of forfeiting an early-payment discount
Terms like "2/10 net 30" mean 2% off if paid within 10 days, else full amount by day 30. The implied
annualized cost of *not* taking the discount (i.e. of stretching to day 30):

`cost ≈ (discount / (1 − discount)) × (D / (net days − discount days))`

For 2/10 net 30: `(0.02 / 0.98) × (365 / 20) ≈ 37.2%`. Because that vastly exceeds normal short-term
borrowing rates, taking the discount usually beats stretching DPO — the classic trade-off in step 6.

## Levers, in brief
- **Collections (DSO ↓):** invoice promptly and accurately, tighten credit terms and screening,
  automate dunning, offer (well-priced) early-pay discounts, resolve disputes fast.
- **Inventory (DIO ↓):** demand forecasting, JIT/replenishment, SKU rationalization, consignment,
  reducing safety stock where service allows.
- **Payables (DPO ↑):** negotiate longer terms, standardize payment runs, but weigh discounts and
  supplier health — do not simply pay late.
