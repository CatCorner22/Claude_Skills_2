# Bank account structures (reference)

Legal and tax treatment of sweeps and pooling varies by country and bank — **confirm for your bank
and region** before implementing.

## Contents
- Account roles
- Hierarchy pattern
- ZBA vs target-balance sweeps
- Physical vs notional pooling
- Account rationalization checklist
- Bank account management (BAM) and eBAM

## Account roles
- **Concentration / header account** — top of the hierarchy per currency (and often per entity);
  where cash is pooled, made visible, and invested. Sweeps flow into and out of it.
- **Collection (receipts) sub-account** — receives customer/AR inflows (lockbox, card settlement,
  incoming ACH/wires); swept up to the header.
- **Disbursement (payables) sub-account** — funds AP runs, supplier payments, wires out; funded down
  from the header. Often paired with **positive pay** for fraud control.
- **Payroll sub-account** — isolates payroll for confidentiality and control; funded per pay cycle.
- **Special-purpose accounts** — tax, escrow, restricted, or regulatory accounts kept separate by
  requirement (not swept if the balance is legally restricted).

## Hierarchy pattern
```
                 [ Concentration / header account ]  (per currency/entity)
                  /            |                 \
   [ Collections ]      [ Disbursements ]     [ Payroll ]        [ Special-purpose ]
   swept up (ZBA)       funded down (ZBA)     funded per run     kept separate, not swept
```
Cash flows **up** from collections and **down** to disbursements, so idle balances collapse into one
investable pool and each sub-account keeps a clean, single-purpose transaction history.

## ZBA vs target-balance sweeps
| | ZBA (zero-balance) | Target-balance |
|---|---|---|
| End-of-day balance | Zero | A set target amount |
| What moves | Entire balance to/from header | Only the amount above/below target |
| Use for | Most collection/disbursement sub-accounts | Accounts needing a local minimum or compensating balance |
| Effect | No idle cash at all | Leaves exactly the required cushion |

- Sweeps are usually **end-of-day**, automated by the bank per standing instruction; some banks
  offer intraday or threshold-triggered sweeps.
- A **two-way** sweep both concentrates surplus and funds shortfalls; a **one-way** sweep only
  concentrates (the sub-account must be pre-funded). Confirm which your bank runs.

## Physical vs notional pooling
- **Physical pooling (cash concentration):** real transfers move balances into a master account.
  - Pros: one investable balance; simple to deploy; works across banks via sweeps.
  - Cons: cross-entity sweeps create **intercompany loans** — must be documented, interest-bearing at
    arm's length, and tracked; withholding-tax and thin-cap rules can apply.
- **Notional pooling:** no money moves; the bank **offsets** debit and credit balances across
  accounts to compute net interest (and sometimes to cover overdrafts against credit balances).
  - Pros: no intercompany loans; entities keep their own balances; efficient interest.
  - Cons: **not permitted or not legally enforceable in some jurisdictions** (e.g. restricted in the
    US); needs cross-guarantees; single-bank, single-currency (or multicurrency overlay) constructs.
  - **Confirm availability and enforceability for your bank/region.**
- Many groups combine both: notional within a country/bank, physical sweeps across banks/regions.

## Account rationalization checklist
- Close **dormant** accounts (no activity over your policy window).
- Merge **same-purpose, same-currency, same-entity** accounts.
- Replace stray local operating accounts with **sub-accounts** under the concentration structure.
- Challenge every account: what breaks if it is closed? If nothing, close it.
- Track the score: account count, total idle balance, annual fees, and reconciliation hours — before
  and after. Fewer accounts = less idle cash, fewer fees, less recon, smaller fraud surface.

## Bank account management (BAM) and eBAM
- **BAM** is the system of record for the account estate: every account's entity, bank, currency,
  purpose, status, **signatories and mandates** (who may transact and to what limit), and KYC/renewal
  dates. It underpins opening/closing workflow, audit, and regulatory reporting (e.g. FBAR/foreign
  account reporting where applicable).
- **eBAM** uses ISO 20022 `acmt` messages to exchange account-opening, closing, and mandate-change
  instructions electronically with banks, reducing paper and turnaround — **confirm your banks
  support it**; adoption is uneven.
- Keep mandates current: stale signatory lists are both a fraud risk and an audit finding.
