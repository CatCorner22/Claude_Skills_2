# FX exposures and basic hedges (reference)

## The three exposures
| Type | What is at risk | Cash or accounting | Typical response |
|---|---|---|---|
| **Transaction** | Home-currency value of a known, dated foreign cash flow (FX receivable/payable) | Cash | Forward (or natural hedge) on the net amount |
| **Translation (accounting)** | Reported equity when a foreign sub is consolidated into the reporting currency | Accounting (CTA in equity) | Usually unhedged; occasionally a net-investment hedge |
| **Economic (operating)** | Long-run competitiveness and value of future, uncontracted cash flows | Cash (future, structural) | Operational: source/sell/finance in matching currencies |

Classify first — the tool that fixes one type does nothing for another. A forward that hedges a
transaction exposure has no effect on economic exposure, and hedging translation (a non-cash accounting
figure) with cash forwards can *introduce* real cash risk.

## Quotes: spot, forward, swap
- **Quote convention:** a pair `BASE/QUOTE` states the price of one unit of the base in the quote
  currency. `EUR/USD = 1.08` → 1 EUR = 1.08 USD. Know which side you are long vs short.
- **Spot:** rate for near-immediate delivery (typically T+2).
- **Forward:** rate agreed now for delivery on a future date. By covered interest parity,
  `Forward = Spot × (1 + i_quote) / (1 + i_base)` for the tenor's interest rates `i`. The forward is
  spot adjusted for the **interest-rate differential**, not a forecast of future spot. When the quote
  currency's rate exceeds the base's, the base trades at a forward **premium**, and vice versa.
- **FX swap:** a spot leg plus an offsetting forward leg (e.g. buy spot, sell forward) — used to roll or
  shift the timing of a currency position, not to take new directional risk.

## Hedge instruments (basics)
- **Forward contract:** obligation to exchange a set amount at a set rate on a set date. Locks the
  home-currency value of a transaction exposure. No upfront premium; both sides are committed. A forward
  that ends "worse" than spot still did its job — it bought certainty.
- **Natural / operational hedge:** offset exposure inside the business — match foreign-currency revenue
  with foreign-currency costs, borrow in the currency of foreign assets, or invoice in your home
  currency. Cheapest and most durable where feasible; addresses economic exposure too.
- **Currency option:** right, not obligation, to exchange at a strike; keeps favorable moves for a
  premium. Use when the exposure is uncertain or asymmetry matters. (Mention; full pricing is out of scope.)
- **Netting first:** offset inflows against outflows within a currency and tenor and hedge only the net.
  Group-wide netting (see `cash-management-skills:intercompany-cash-netting`) shrinks external notional
  and saves spread/fees.

## Hedge ratio
`Hedge ratio = notional hedged / total exposure`.
- 1.0 = fully hedged: rate uncertainty on that exposure removed.
- Between 0 and 1 = partially hedged: state the residual open position explicitly.
- Set the ratio from policy and the certainty of the exposure — not from a rate view. Over-hedging
  (ratio > 1, or hedging exposure you don't have) is speculation, not hedging.

## A minimal workflow
1. List each foreign-currency flow with amount, currency, and settlement date.
2. Net inflows against outflows per currency and tenor.
3. Classify the residual (transaction / economic; translation handled separately).
4. Choose the instrument, set the hedge ratio, lock and document against the underlying.
