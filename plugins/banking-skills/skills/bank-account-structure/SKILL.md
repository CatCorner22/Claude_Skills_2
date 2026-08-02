---
name: bank-account-structure
description: >-
  Designs bank account hierarchies and automated sweep structures — concentration/header accounts,
  zero-balance (ZBA) and target-balance sub-accounts, and physical vs notional cash pooling — and
  rationalizes account counts to cut idle cash, fees, and risk. Use when structuring, opening, or
  rationalizing bank accounts, or designing sweeps or cash pooling. Triggers: bank account
  structure, account hierarchy, ZBA, zero balance account, concentration account, target balance,
  sweeps, cash pooling, notional pooling, account rationalization, BAM, bank account management.
---

# Bank account structure

## When to use
- Designing a bank account hierarchy (collection, disbursement, payroll, concentration) for an entity or group.
- Setting up ZBA / target-balance sweeps or evaluating physical vs notional pooling.
- Rationalizing an existing account estate — cutting redundant accounts and idle balances.
- Not for: choosing the target/minimum balance *level* a sweep aims at → see
  `cash-management-skills:liquidity-management`. For settling intercompany balances created by
  concentration → see `cash-management-skills:intercompany-cash-netting`.

## Do it
1. **Inventory the current estate.** List every account: entity, bank, currency, purpose
   (collections/disbursements/payroll/tax/escrow), average balance, monthly fees, and signatories.
   You cannot rationalize what you have not counted. Flag dormant and single-purpose accounts.
2. **Group by purpose and currency.** Separate **collection** (money in), **disbursement** (money
   out), and **special-purpose** (payroll, tax, escrow, restricted) accounts, per currency and per
   legal entity. Mixing flows in one account defeats control and clean reconciliation.
3. **Design the hierarchy.** Put a **concentration (header) account** per currency/entity at the
   top; hang collection and disbursement **sub-accounts** beneath it. Cash flows up to the
   concentration account, where it is visible and investable, and down to fund disbursements.
4. **Choose the sweep type per sub-account** (see `references/account-structures.md`):
   - **ZBA (zero-balance):** sub-account swept to **zero** each day into/out of the header — nothing
     sits idle in it. Standard for disbursement and collection sub-accounts.
   - **Target-balance:** sub-account swept to leave a fixed **target** (e.g. a local minimum or
     compensating balance); only the excess/shortfall moves.
5. **Decide concentration method: physical vs notional pooling.**
   - **Physical (cash concentration):** real sweeps move funds into one account — simplest to invest,
     but creates **intercompany loans** between entities that must be tracked and priced.
   - **Notional:** the bank offsets credit and debit balances for **interest** without moving money;
     no intercompany loans, but availability and legal enforceability vary by country (restricted in
     the US) — **confirm for your bank/region**.
6. **Rationalize.** Close dormant and redundant accounts; consolidate same-purpose, same-currency
   accounts; replace stray local accounts with sub-accounts under the concentration structure. Fewer
   accounts means less idle cash, fewer fees, less reconciliation, and a smaller fraud surface.
7. **Formalize with bank account management (BAM).** Maintain a system of record for every account:
   opening/closing workflow, **signatories and mandates** (who can transact and up to what limit),
   KYC refresh, and regulatory reporting (e.g. FBAR where applicable). eBAM (ISO 20022 `acmt`
   messages) can automate opening/closing/mandate changes with banks — **confirm bank support**.

## Why / learn
Structure exists to solve one problem: **cash spread across many accounts is idle, invisible, and
expensive.** A dollar sitting in a local sub-account earns little, can't be invested, and still
attracts fees and reconciliation effort. A concentration hierarchy fixes this by **pulling balances
up to one visible pool** while still letting each sub-account do its job. The sweep is the mechanism:
**ZBA** empties a sub-account to zero every day so no cash is stranded, while **target-balance**
leaves exactly what a local requirement demands and sweeps the rest — the difference is just *how
much you insist stays behind*. Pooling is the next lever, and the physical-vs-notional choice is
really a trade between simplicity and legal cleanliness: **physical** pooling actually moves the
money (easy to invest, but every sweep across entities is a loan you must document and price at
arm's length), whereas **notional** pooling leaves balances in place and only nets them for interest
(no intercompany loans, but not permitted or enforceable everywhere). Rationalization ties it
together: **every extra account is idle cash, a fee line, a reconciliation, and an attack surface**,
so the default is the *fewest accounts that still separate flows and satisfy local/legal needs.* Hold
"concentrate the cash, separate the flows, keep only the accounts you truly need" and the design
follows.

## Common mistakes
- Mixing collections and disbursements in one account → breaks control and reconciliation. Separate by purpose.
- Leaving balances in local sub-accounts → idle cash and fees. Sweep to zero (ZBA) or to a set target.
- Physical pooling without tracking intercompany loans → tax and legal exposure. Document and price every sweep.
- Assuming notional pooling is allowed everywhere → it is restricted/unavailable in some jurisdictions. Confirm for your bank/region.
- Opening an account per need and never closing any → estate sprawl. Rationalize on a schedule.
- No mandate/signatory record → fraud and audit risk. Keep BAM current for every account.

## Tailor to your environment
Drop your real structure into `references/your-environment.md` (keep account numbers, balances, and
signatory names in `your-environment.private.md`, which is git-ignored). Capture your legal-entity
and currency map, current accounts and their purposes, your concentration banks, existing sweep
rules and targets, whether you pool physically or notionally, and your BAM system of record and
mandate approval workflow. Pooling legality, eBAM support, and regulatory reporting differ by
country and bank — **confirm for your bank/region** before designing to them.

## References
- references/account-structures.md — hierarchy patterns, ZBA vs target-balance sweeps, physical vs notional pooling, and BAM/eBAM
- references/your-environment.md — your entities, accounts, banks, sweep rules, and BAM setup (add when supplied)
