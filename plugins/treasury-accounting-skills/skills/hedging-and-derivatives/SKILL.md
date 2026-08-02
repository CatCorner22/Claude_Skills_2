---
name: hedging-and-derivatives
description: >-
  Runs a corporate hedging program — choosing and pricing the workhorse instruments (FX forwards
  and swaps, interest-rate swaps, caps/collars), sizing hedges against measured exposures,
  executing through the trade lifecycle (quote, execute, confirm, settle), monitoring
  mark-to-market and counterparty exposure, and understanding hedge accounting (cash flow vs fair
  value designation, effectiveness, documentation) well enough to keep hedges from whipsawing
  earnings. Use when hedging an FX or interest-rate exposure, evaluating a forward or swap quote,
  rolling or unwinding a hedge, or setting up hedge accounting documentation. Triggers: hedge,
  FX forward, forward points, interest rate swap, cap, collar, hedge accounting, cash flow hedge,
  mark to market, unwind hedge, hedge effectiveness, ISDA, notional, hedge ratio.
---

# Hedging and derivatives for treasury

## When to use
- Converting a measured FX or interest-rate exposure into an executed hedge: instrument choice,
  sizing, quote evaluation, execution, confirmation, and settlement.
- Managing a live book: MTM monitoring, rolls, unwinds, counterparty exposure, and the hedge
  accounting that keeps derivative results in the right place in the statements.
- Not for: identifying and measuring the FX exposure in the first place → see
  `finance-skills:fx-risk-basics`. For the floating-rate debt being hedged → see
  `treasury-accounting-skills:debt-facilities-and-covenants`.

## Do it
1. **Start from a measured exposure and a written policy.** A hedge answers a specific exposure
   (forecast EUR revenue, a USD loan's floating coupon) with a stated objective, horizon, and
   hedge ratio (often 50–80% of forecast exposure, layered by tenor — not 100%, because the
   forecast itself is uncertain). No exposure measurement, no trade.
2. **Pick the simplest instrument that fits:**
   - **FX forward** — lock a rate for one date. Forward rate = spot ± **forward points**, which
     are the interest-rate differential between the currencies, *not* a market forecast.
   - **FX swap** — move existing currency liquidity across dates (spot leg + forward leg);
     the treasury tool for funding, not for new exposure.
   - **Interest-rate swap** — pay fixed / receive floating to fix a loan's coupon.
   - **Cap** — premium up front, keeps upside; **collar** — cap funded by selling a floor,
     cheap or zero-cost but gives up downside.
   - Options beyond caps (vanilla FX options) buy flexibility for a premium; use when the
     exposure itself is uncertain (contingent bids). Avoid exotic structures whose payoff you
     can't draw by hand.
3. **Evaluate quotes against the arithmetic, and compete them.** Forwards price off covered
   interest parity; swaps off the fixed rate that equates the two legs' PV — so an indicative
   mid is computable, and the bank's margin is the deviation from it. Get two or more quotes
   for anything sizeable; `references/hedging-toolkit.md` has the pricing arithmetic and quote
   checklists.
4. **Execute with the full lifecycle, not just the trade.** Pre-trade: ISDA (with CSA if
   collateralized) in place, counterparty within limits (see
   `treasury-accounting-skills:investment-policy-compliance` for the limit discipline),
   dealing mandate covers the trader. Trade: record time-stamped details. Post-trade: **match
   the confirmation against your record same day** — confirmation errors found at settlement
   are expensive; then diarize fixings, settlements, and maturities.
5. **Designate hedge accounting on day one if you want it.** Default accounting sends all
   derivative MTM through earnings each period, while the hedged item (forecast revenue, future
   interest) isn't in earnings yet — that mismatch is the whipsaw. **Cash flow hedge**
   designation (for forecast transactions / floating rates) parks effective MTM in OCI until
   the hedged item hits earnings; **fair value hedge** (for fixed-rate assets/liabilities)
   marks the hedged item too. The price: contemporaneous documentation (risk, item, instrument,
   effectiveness method) at inception — it cannot be backdated — plus ongoing effectiveness
   assessment and prospective-transaction probability.
6. **Monitor the book monthly.** MTM per trade (bank statements or your own valuation),
   counterparty exposure = positive MTM (what you'd lose if they defaulted), hedge ratio vs
   updated forecast (re-layer as forecasts firm up), and hedge accounting effectiveness. For a
   collar or cap, track where rates sit vs the strikes.
7. **Roll and unwind deliberately.** Rolling a forward = settle (or swap) the maturing leg and
   lay on the next — the realized gain/loss is the old hedge doing its job, not new P&L to
   chase. Unwind when the exposure disappears (order cancelled, debt repaid): terminate at MTM,
   and if hedge-accounted, follow the de-designation rules (OCI amounts stay parked until the
   forecast transaction occurs — or recycle immediately if it's no longer probable).

## Why / learn
Corporate hedging done right is *insurance arithmetic*: you pay (points, premium, or foregone
upside) to swap an uncertain outcome for a certain one, and the test of a hedge is whether it
offset the exposure — never whether the hedge "made money." That reframe dissolves most hedging
confusion: forward points aren't a prediction (they're interest differentials, so hedging a
high-rate currency's revenue costs carry); a hedge that lost money while the exposure gained is
a *success*; and hedging 100% of a forecast is speculating on the forecast. The instrument menu
is really one distinction — forwards/swaps lock both directions for free, options lock one
direction for a price — and everything else is packaging. Hedge accounting exists because
accounting timing, not economics, creates the whipsaw: the derivative marks every quarter, the
hedged item doesn't hit earnings until later, so designation is the bridge that lines the two
up. Its documentation burden is the fee for that bridge, and the reason it must exist at
inception is that regulators won't let you decide *after seeing the outcome* which trades were
"hedges." Counterparty exposure completes the picture: a deeply in-the-money hedge is exactly
when your bank's credit starts to matter, because the hedge is now an asset they owe you.

## Common mistakes
- Judging hedges by their standalone P&L → evaluate hedge + exposure together; the offset is the product.
- Reading forward points as a market view → they're rate differentials (covered interest parity); the "expensive" direction is carry, not prophecy.
- Hedging 100% of a forecast exposure → over-hedged the moment the forecast slips; layer 50–80% by tenor.
- Skipping same-day confirmation matching → errors surface at settlement as disputes; match on trade date.
- Trading first, documenting hedge accounting later → designation can't be backdated; earnings whipsaw is locked in.
- Zero-cost collar treated as free → you sold the floor; price the give-up, don't just admire the zero premium.
- Ignoring counterparty exposure on winning trades → positive MTM is unsecured credit to the bank absent a CSA.
- Exotic structures for yield/cheapness → if you can't draw the payoff, you can't manage the risk.

## Tailor to your environment
Record your program in `references/your-environment.md` (live positions and ISDA specifics in
`your-environment.private.md`, git-ignored): policy objectives and hedge ratios, approved
instruments and tenors, counterparties with ISDAs/CSAs and limits, dealing mandates, who
confirms and who books, and your hedge accounting elections. **Never commit live positions,
rates, or ISDA terms.**

## References
- references/hedging-toolkit.md — instrument cheat sheet, pricing arithmetic, lifecycle and hedge-accounting checklists
- references/your-environment.md — your policy, instruments, counterparties, elections (fill in)
