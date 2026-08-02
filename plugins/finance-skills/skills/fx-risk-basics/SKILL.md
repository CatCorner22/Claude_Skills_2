---
name: fx-risk-basics
description: >-
  Identifies transaction, translation, and economic foreign-exchange exposure and applies basic hedges
  — forward contracts, natural or operational hedging, and netting exposures before hedging externally.
  Use when handling multi-currency exposure, deciding whether or how to hedge a foreign-currency cash
  flow, distinguishing the three types of FX risk, or reading spot/forward quotes. Triggers: FX risk,
  foreign exchange risk, currency exposure, hedging, forward contract, transaction exposure,
  translation exposure, economic exposure, natural hedge, hedge ratio, currency netting.
---

# FX risk basics

## When to use
- Classifying a company's currency exposure into transaction, translation, or economic.
- Deciding whether and how to hedge a known foreign-currency cash flow with a forward or naturally.
- Reading spot/forward/swap quotes and computing a simple hedge ratio.
- Not for: the mechanics of pooling and settling intragroup balances across entities → see
  `cash-management-skills:intercompany-cash-netting`. For discounting foreign cash flows to present
  value → see `finance-skills:time-value-of-money`.

## Do it
1. **Classify the exposure before touching a hedge** (see `references/exposures-and-hedges.md`):
   - **Transaction** — a known, dated foreign-currency cash flow (an FX receivable or payable). Rate
     moves change the home-currency amount you actually settle. This is what forwards hedge.
   - **Translation (accounting)** — restating a foreign subsidiary's financials into the reporting
     currency on consolidation. Hits equity via the cumulative translation adjustment, **not cash**.
   - **Economic (operating)** — the long-run effect of rate moves on competitiveness and future,
     not-yet-contracted cash flows. Managed operationally, not with a single forward.
   The right response depends entirely on which of these you have — name it first.
2. **Measure the exposure per currency and per date.** For transaction risk, list each foreign-currency
   inflow and outflow with its amount and settlement date. Group by currency and tenor.
3. **Net before you hedge.** Within a currency and tenor, offset inflows against outflows and hedge only
   the **net** exposure. Netting across the group first (see the intercompany-netting cross-link) shrinks
   the notional you must transact externally and cuts spread and fees.
4. **Read the quote correctly.** For a pair quoted `BASE/QUOTE` (e.g. `EUR/USD = 1.08` means 1 EUR =
   1.08 USD), know which currency you are long/short. A **forward** rate is the spot adjusted for the
   interest-rate differential between the two currencies (covered interest parity) — it is *not* a
   forecast of the future spot. A forward premium/discount just reflects that differential.
5. **Choose the hedge for the exposure type:**
   - Transaction: sell/buy the net amount forward to lock the home-currency value; or use a natural
     hedge if one exists. Options cost a premium but keep upside — mention when asymmetry matters.
   - Economic: shift operations — source costs in the revenue currency, diversify markets, reprice.
   - Translation: usually left unhedged or hedged sparingly (e.g. net-investment hedge) since it is
     non-cash; hedging it with cash instruments can create real cash risk to smooth an accounting line.
6. **Set the hedge ratio deliberately.** `Hedge ratio = notional hedged / total exposure`. Full hedge
   (1.0) removes rate uncertainty on that exposure; a partial ratio keeps some. State the ratio and the
   residual open position — do not imply a partial hedge is fully covered.
7. **Document the hedge against the exposure.** Record exposure, currency, tenor, hedge instrument,
   rate locked, hedge ratio, and residual. The hedge exists to remove volatility on a known exposure —
   tie each hedge to its underlying, not to a rate view.

## Why / learn
The first and most important move in FX is **naming the exposure**, because the three types are
different animals and a tool that fixes one does nothing for another. Transaction exposure is real
cash: you will hand over or receive a foreign amount on a date, and the home-currency value of that
amount swings with the rate — a forward nails it down. Translation exposure is an **accounting**
artifact of consolidation; it moves equity through the cumulative translation adjustment but no cash
changes hands, so hedging it with real forwards can introduce genuine cash risk purely to smooth a
reported number. Economic exposure is the slow, structural one — a sustained rate shift that erodes
your competitiveness or the value of future business you haven't even booked yet — and no single
forward touches it; you manage it by changing where you earn and spend. The second idea is that
**hedging is risk management, not a bet**. A forward removes uncertainty by locking a rate; it does not
try to beat the market, and a forward that "loses" relative to where spot ended up did its job — it
delivered certainty, which is what you paid for. That is why you net exposures before hedging (hedging
offsetting flows separately just pays spread twice for no benefit) and why you set an explicit hedge
ratio (the honest statement of how much uncertainty you removed and how much you kept). Treating a
forward as a directional trade — over-hedging, or leaving exposures open because you "think" the rate
will move your way — is speculation wearing a hedge's clothes.

## Common mistakes
- Hedging before classifying the exposure → the wrong tool for the type. Name transaction/translation/economic first.
- Hedging translation exposure with cash forwards → creates real cash risk to smooth a non-cash line.
- Hedging each flow separately → net offsetting inflows/outflows first, then hedge the residual.
- Misreading the quote direction → confirm base/quote and whether you are long or short the currency.
- Treating the forward rate as a spot forecast → it is spot adjusted for the interest-rate differential.
- Over-hedging or hedging a view → that is speculation; hedge only identified exposure, to a stated ratio.
- Calling a partial hedge "covered" → always state the hedge ratio and the residual open position.

## Tailor to your environment
Record your setup in `references/your-environment.md` (or `your-environment.private.md`, git-ignored, if
it names real counterparties or amounts — never commit real data). Capture your reporting currency, the
currency pairs you are exposed to, your hedging policy (which exposures you hedge and to what ratio),
approved instruments and counterparties, netting arrangements, and any hedge-accounting designation you
apply. The generic classify-net-hedge process then runs against your real exposures.

## References
- references/exposures-and-hedges.md — the three exposure types, spot/forward/swap mechanics, hedge instruments, and netting
- references/your-environment.md — your reporting currency, pairs, hedging policy, and counterparties (add when supplied)
