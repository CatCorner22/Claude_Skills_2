# Netting cycle and structures (reference)

## Contents
- Bilateral vs. multilateral netting
- The netting cycle (calendar)
- FX in netting
- In-house bank (POBO/COBO)
- Cash pooling types

## Bilateral vs. multilateral netting
- **Bilateral** — two entities offset their mutual balances into a single net payment. Simple; scales
  poorly as entities multiply (each pair nets on its own).
- **Multilateral** — all participants net through a central **netting center**; each makes or receives
  **one** net payment to/from the center per cycle. Cuts the number of payments from ~n² pairs to n.
- The netting center may be a treasury entity or an in-house bank, often run on a netting system/module.

## The netting cycle (calendar)
1. **Invoice cutoff** — last date intercompany invoices are included this cycle.
2. **Matching / dispute window** — participants match AR to AP; disputed items are pulled and deferred.
3. **Netting calculation** — the center computes each participant's net position at the cutoff FX rates.
4. **Settlement advices** — the center publishes each participant's single net pay/receive; a short
   confirmation window follows.
5. **Settlement date** — each participant settles its one net amount; entries and FX are posted.
6. **Post-cycle** — reconcile the netting clearing account to zero; carry disputes to the next cycle.
Everyone must book to the **same cutoff**, or positions won't tie out.

## FX in netting
- Group balances **by currency**; net the **exposure per currency first**, then convert only the
  residual — this avoids paying the bid-offer spread on offsetting amounts that never needed to move.
- Fix a **settlement currency** per participant and a **rate source/timestamp** in the advice; the
  **netting center typically bears the FX** and can hedge the residual net exposure once (see
  `finance-skills:fx-risk-basics`).

## In-house bank (POBO/COBO)
- An **in-house bank (IHB)** is a central treasury entity that runs **internal accounts** for
  subsidiaries and acts as their bank.
- **POBO** (payments-on-behalf-of) — the IHB pays external vendors on a subsidiary's behalf; the
  subsidiary's obligation becomes an intercompany balance on its internal account.
- **COBO** (collections-on-behalf-of) — the IHB collects customer receipts on a subsidiary's behalf.
- Effect: most intercompany and many external flows settle on **internal** accounts, shrinking the
  number of external bank accounts, payments, float, and FX conversions.

## Cash pooling types
- **Notional pooling** — the bank **offsets balances** across accounts for interest calculation
  **without moving cash**; requires a legal right of set-off and cross-guarantees. No intercompany
  loans created by the sweep itself.
- **Physical / ZBA pooling** — cash is **physically swept** to a header account; the sweeps **create
  intercompany loans** between participants and the header, with interest and tax consequences.
- Both need **tax and legal sign-off** (thin-capitalization, transfer pricing on interco interest,
  set-off enforceability). Choose based on legal/tax feasibility and how centralized you want cash.
