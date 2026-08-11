---
name: working-capital-management
description: >-
  Analyzes days sales outstanding (DSO), days payable outstanding (DPO), days inventory outstanding
  (DIO), and the cash conversion cycle (CCC = DSO + DIO − DPO) to release cash tied up in operations,
  and weighs the levers and trade-offs for shortening it. Use when analyzing or improving working
  capital, the operating cycle, or the cash conversion cycle, or when quantifying cash freed by
  faster collections, leaner inventory, or longer payment terms. Triggers: working capital, cash
  conversion cycle, CCC, DSO, DPO, DIO, days sales outstanding, days payable outstanding, days
  inventory outstanding, receivables, payables, inventory days, operating cycle.
---

# Working capital management

## When to use
- Measuring DSO, DPO, DIO, or the cash conversion cycle for a business or a period.
- Diagnosing why cash is trapped in operations and quantifying what each lever would release.
- Comparing working-capital efficiency across periods, peers, or business units.
- Not for: projecting the actual day-by-day cash position and funding gaps → see
  `cash-management-skills:cash-forecasting`. For structuring liquidity buffers and facilities → see
  `cash-management-skills:liquidity-management`.

## Do it
1. **Pull the four inputs on a consistent basis.** Average accounts receivable, average inventory,
   average accounts payable (opening+closing)/2 for the period, plus credit sales (or revenue) and
   COGS for the same period, and the number of days in the period (`D`, e.g. 365 or 90).
2. **Compute the three day-metrics** (see `references/metrics.md` for the exact bases):
   - `DSO = Average AR / Credit Sales × D` — days to collect a sale.
   - `DIO = Average Inventory / COGS × D` — days inventory sits before sale.
   - `DPO = Average AP / COGS × D` — days you take to pay suppliers.
   Use the *same* `D`, and drive AR off **credit** sales, inventory and payables off **COGS**.
3. **Assemble the cash conversion cycle:** `CCC = DSO + DIO − DPO`. The operating cycle is
   `DSO + DIO`; DPO is subtracted because supplier credit funds part of that cycle for free.
4. **Interpret the number and its trend.** CCC is days of cash tied up in the operating cycle. Rising
   CCC means cash is draining into operations; falling (or negative) CCC means the cycle is releasing
   cash. Always read it against prior periods and peers — a level alone means little.
5. **Quantify each lever in cash, not just days.** Cash released ≈ `Δdays × daily driver`:
   - Cut DSO by `x` days → frees `x × (Credit Sales / D)`.
   - Cut DIO by `x` days → frees `x × (COGS / D)`.
   - Extend DPO by `x` days → frees `x × (COGS / D)`.
   Rank levers by cash freed against the cost/risk each carries (next step).
6. **Weigh the trade-offs before recommending.** Faster collections (lower DSO) can cost sales or
   goodwill if terms tighten too far; leaner inventory (lower DIO) risks stockouts and lost service;
   stretching DPO (higher DPO) strains suppliers and forfeits early-payment discounts — and a
   forfeited "2/10 net 30" discount costs ~37% annualized (see `references/metrics.md`). Recommend the
   levers whose cash gain beats their cost.
7. **Report the position and the plan.** Show current DSO/DIO/DPO/CCC, the trend, benchmark gaps, the
   cash each realistic lever frees, and the trade-off attached to it — with owners for the actions.

## Why / learn
Working capital is the cash locked inside the ordinary rhythm of the business: you buy or make
inventory, you sell it on credit, and only later do you collect — while suppliers finance part of the
wait by letting you pay late. The cash conversion cycle measures exactly how many days a dollar is
**trapped** in that loop before it comes back as cash. That framing is the whole point: DSO and DIO
are days cash is stuck out in receivables and stock, DPO is days you get to hold onto cash you owe, so
`CCC = DSO + DIO − DPO` is the net time your own cash is committed. Shortening the cycle **releases
cash** you already own without borrowing or raising equity — every day removed hands back roughly one
day of sales or COGS, permanently, as long as the improvement holds. That is why a negative CCC is so
powerful: firms that collect before they pay (some retailers and marketplaces) run operations on
suppliers' money and generate cash as they grow. But the levers are not free money — they are
**trade-offs against other parties**. Squeeze customers and you may lose them; starve inventory and you
stock out; stretch suppliers and you pay for it in relationships or in surrendered discounts that cost
far more than short-term financing. The skill is not "make CCC smaller"; it is finding the levers where
the cash released is worth more than what the squeeze costs.

## Common mistakes
- Driving DSO off total revenue when much of it is cash sales → overstates DSO; use credit sales.
- Using sales instead of COGS for DIO or DPO → inflates the metric; inventory and payables sit at cost.
- Mixing period lengths or period-end vs average balances → distorts the trend; be consistent.
- Reading CCC as a level with no benchmark → a number without a trend or peer says little.
- Maximizing DPO blindly → forfeited early-pay discounts and supplier strain can dwarf the cash gained.
- Treating a negative CCC as automatically healthy → confirm it is structural, not stretched payables.
- Reporting only days, never cash → translate day changes into currency so the size is visible.

## Tailor to your environment
Record your real setup in `references/your-environment.md` (or `your-environment.private.md`, which is
git-ignored, if it names real customers, suppliers, or figures — never commit real data). Capture your
standard credit terms and how much of sales are on credit, your inventory valuation basis, your target
DSO/DIO/DPO or CCC, peer benchmarks you compare to, and your early-payment-discount policy. The generic
formulas then run against your actual balances and terms.

## References
- references/metrics.md — exact formulas, credit-sales vs COGS bases, cash-release math, and discount-cost formula
- references/your-environment.md — your terms, targets, benchmarks, and discount policy (add when supplied)
