# Evals — finance-skills:working-capital-management

## 1. Positive trigger (should load the skill)
> "Our DSO crept from 42 to 55 days this year and inventory is piling up. Walk me through our cash
> conversion cycle and how much cash we'd free up if we got DSO back to 45 and stretched payables by
> a week."

Expected: skill loads; computes DSO/DIO/DPO and `CCC = DSO + DIO − DPO`; translates the day changes
into cash via `Δdays × daily driver`; flags the trade-offs (customer goodwill on DSO, supplier strain
and forfeited discounts on DPO); reads the numbers against the trend, not as a bare level.

## 2. Near-miss (should NOT load this skill)
> "Build me a 13-week cash flow forecast so I can see when we'll dip below our minimum cash balance
> and need to draw on the revolver."

Expected: this is day-by-day cash-position projection and funding-gap planning — the
`cash-management-skills:cash-forecasting` skill should handle it. Working-capital metrics inform a
forecast but are not the deliverable here. If this skill loads as primary, tighten the "Not for" line.

## 3. Quality rubric
A good response:
- **Does the task:** computes the three day-metrics on the right bases (credit sales for DSO, COGS for
  DIO/DPO), builds CCC correctly, and converts day changes into a cash figure.
- **Teaches:** explains that CCC is how long cash is trapped in the operating cycle and that shortening
  it releases cash you already own — and that the levers are trade-offs against customers and suppliers.
- **Safe:** does not recommend maximizing DPO blindly (notes the ~37% cost of a forfeited 2/10 net 30),
  and does not read a negative or improving CCC as automatically healthy.
