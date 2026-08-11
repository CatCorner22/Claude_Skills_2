# Hedging toolkit (reference)

## Contents
- Instrument cheat sheet
- Pricing arithmetic
- Trade lifecycle checklist
- Hedge accounting checklist

## Instrument cheat sheet
| Instrument | Locks | Cost | Typical corporate use |
|---|---|---|---|
| FX forward | Rate for one future date, both directions | Forward points (carry) | Forecast foreign revenue/costs, firm commitments |
| FX swap | Moves currency across dates | Points on the far leg | Funding a foreign account without FX exposure |
| NDF | Like a forward, cash-settled | Points | Restricted currencies (BRL, KRW, INR...) |
| IR swap (pay fixed) | Floating coupon → fixed | Embedded in fixed rate | Fixing revolver/term-loan interest |
| Cap | Ceiling on floating rate | Upfront premium | Keep downside protection + rate-fall upside |
| Collar | Ceiling, funded by floor | Low/zero premium | Cheap protection; gives up rate-fall benefit |
| FX option (vanilla) | One direction only | Premium | Contingent exposures (bids, M&A) |

## Pricing arithmetic
**Forward (covered interest parity):**
```
F = S × (1 + r_quote × t) / (1 + r_base × t)
EUR/USD spot 1.0800, USD 1y 4.5%, EUR 1y 3.0%:
F = 1.0800 × 1.045/1.030 ≈ 1.0957  → points ≈ +157 pips (USD yields more, EUR forward at premium)
```
The quote's fairness = distance from this mid. Points are carry: hedging exposure *into* the
higher-rate currency earns points; out of it costs points.

**Swap fixed rate:** the rate making PV(fixed leg) = PV(expected floating leg) off the current
curve. An indicative mid is on any terminal/bank run; your executed rate − mid = the bank's
margin. Compete quotes above a size threshold and record all quotes received.

**Collar sanity check:** price cap and floor separately (premiums offset); a "zero-cost" collar
with a suspiciously good cap means the floor you sold is worth more than you think.

## Trade lifecycle checklist
- [ ] Exposure measured, hedge within policy ratio/tenor bands
- [ ] Counterparty: ISDA (+CSA?) executed; exposure within limit *after* this trade
- [ ] Dealing mandate covers instrument, size, trader
- [ ] ≥2 quotes for size (record them); executed vs indicative mid noted
- [ ] Trade recorded same day: counterparty, notional, rate/strike, dates, direction
- [ ] Confirmation matched same day; discrepancies raised immediately
- [ ] Fixings/settlements/maturities diarized; settlement instructions verified (callback for new SSIs)
- [ ] Hedge accounting documentation executed at inception (if designating)

## Hedge accounting checklist (ASC 815 / IFRS 9 shape)
At inception, documentation states:
- [ ] Hedged item/transaction (specific, and "probable" for forecast transactions)
- [ ] Hedged risk (e.g. FX in forecast EUR revenues; benchmark rate on the loan)
- [ ] Hedging instrument (the specific trade)
- [ ] Type: cash flow (forecast/floating) vs fair value (fixed-rate item) vs net investment
- [ ] Effectiveness method (critical-terms match, regression) and assessment frequency
Ongoing:
- [ ] Effectiveness assessed each period; ineffectiveness handled per framework
- [ ] Forecast transaction still probable (if not: recycle OCI per rules; stop designation)
- [ ] De-designation/termination handled: OCI stays parked until the hedged item occurs
      (or recycles immediately when no longer probable)
Coordinate elections with the auditors *before* the first trade, not at the first close.
