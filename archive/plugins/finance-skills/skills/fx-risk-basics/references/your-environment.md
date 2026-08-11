# Your FX-risk environment (sanitized template)

Fill in your real setup. If it names real counterparties, entities, or amounts, keep it in
`your-environment.private.md` instead — that suffix is git-ignored, so raw data never gets committed.
Commit only sanitized, structural examples.

- **Reporting / functional currency:** <e.g. USD>
- **Currency pairs you are exposed to:** <e.g. EUR/USD, GBP/USD, USD/MXN — and typical direction>
- **Exposure types in scope:** <transaction | translation | economic — which you actively manage>
- **Hedging policy:** <which exposures you hedge, target hedge ratio, tenor limits>
- **Approved instruments:** <forwards | FX swaps | options — and any prohibited ones>
- **Approved counterparties / banks:** <dealer list; credit limits>
- **Netting arrangement:** <intragroup netting cycle; netting center; see intercompany-cash-netting>
- **Hedge accounting:** <do you apply cash-flow / net-investment hedge designation; documentation rules>
- **Authorization & segregation:** <who may transact; who confirms/settles; who reports>
