# Account analysis and bank fees (reference)

Reserve requirements, earnings-credit conventions, and carry-forward rules are bank- and
period-specific — **confirm current terms for your bank/region.**

## Contents
- Account analysis statement anatomy
- The earnings credit math
- Hard charges vs balance compensation
- AFP Service Codes
- EDI 822 vs ISO 20022 camt.086
- Analysis techniques
- Negotiation levers

## Account analysis statement anatomy
A typical monthly account analysis statement has three parts:
1. **Balance summary** — average **ledger** balance, average **collected (available)** balance,
   float, a **reserve factor** deduction, and the resulting **investable balance**.
2. **Earnings credit** — investable balance × **ECR** × day-count; the notional credit that offsets
   charges.
3. **Service charges** — per-service lines, each with **volume**, **unit price**, and **charge**,
   grouped by service category, then a **net settlement**: total charges − earnings credit = amount
   billed (a hard debit) or a credit surplus.

## The earnings credit math
```
investable balance = average collected balance − reserve factor − float
earnings credit    = investable balance × ECR × (days in period / 360 or 365)
net due (hard)     = total service charges − earnings credit      (if positive, debited)
credit surplus     = earnings credit − total service charges      (carry-forward? confirm)
```
- **ECR (earnings credit rate):** a notional rate the bank sets; it discounts fees, it is **not**
  interest paid to you.
- **Reserve factor:** the share of balances the bank treats as non-investable; a higher factor
  lowers the credit. (US statutory reserve requirements have changed over time — the bank may still
  apply an analysis reserve factor regardless; **confirm.**)
- **Day count:** banks use 360 or 365; check which, as it changes the credit.

## Hard charges vs balance compensation
- **Hard charge:** the fee is billed and debited from the account. Simple, transparent, and the cash
  you would otherwise leave as a compensating balance is free to be invested.
- **Balance compensation:** you leave a **compensating balance** whose earnings credit offsets the
  fees; no cash leaves, but the balance earns only the ECR.
- **The decision:** compare the **ECR** to your **marginal short-term investment yield**.
  - Investment yield **>** ECR → pay hard fees, invest the cash (balances under-earn at the ECR).
  - ECR **≥** investment yield (or the balance is required anyway) → compensate with balances.
- Many firms do a mix and true it up as rates move — when short rates rise, held balances often
  become expensive relative to investing, favoring hard fees.

## AFP Service Codes
- Standardized codes maintained by the **Association for Financial Professionals** that classify
  bank treasury-management services into a common taxonomy, so the *same* service carries the *same*
  code across banks.
- Purpose: make unit prices and volumes **comparable** across banks and statements — essential for
  benchmarking and RFPs. Map every billed line to its AFP code; investigate any line you can't map
  (it may be a proprietary bundle or a mis-billed item).
- The codes group services (e.g. general account services, depository, paper/ACH disbursement, wire
  and other funds transfer, information reporting, lockbox) — **confirm the current code list** with
  AFP; codes are periodically revised.

## EDI 822 vs ISO 20022 camt.086
- **EDI 822 (ANSI X12 Account Analysis):** the legacy US electronic account-analysis format. Machine
  readable; widely used domestically; carries balances, services, volumes, unit prices, and charges.
- **ISO 20022 camt.086 (BankServicesBillingStatement, "BSB"):** the global standard for electronic
  bank service billing — richer, structured XML, supports multi-currency and international banks, and
  aligns service identification with AFP codes.
- Prefer either machine-readable file over PDF: line-item data enables trending, benchmarking, and
  variance detection that a PDF total hides. Many banks emit both during a transition — **confirm
  what your banks support.**

## Analysis techniques
- **Rank by dollars:** sort charges high-to-low; the top handful usually drives most of the bill.
- **Decompose cost = volume × unit price:** a rising charge is either more volume or a higher unit
  price — the fix differs (process/volume vs negotiation).
- **Trend month over month** per AFP code to catch **price creep** and new/removed services.
- **Benchmark unit prices** across your banks (same AFP code) and against market/RFP data.
- **Hunt waste:** services you no longer use, duplicate per-account charges, one-off setup fees still
  recurring, minimums you trip, and float assumptions that understate your collected balance.
- **Check the ECR utilization:** are you leaving far more balance than needed to cover charges? That
  excess should be invested (see the trade-off above).

## Negotiation levers
- **Unit price reductions** on high-volume services (biggest dollar impact).
- **Higher ECR** and **lower reserve factor** (improves the balance offset).
- **Volume tiers / commitments** in exchange for lower per-item pricing.
- **Bundling / account consolidation** to drop per-account minimums and duplicate charges.
- **Waivers** of setup, maintenance, or legacy service fees.
- **RFP / benchmarking** using AFP codes as the common yardstick.
- Take the largest-dollar items first, set target prices, and verify on the next statement.
