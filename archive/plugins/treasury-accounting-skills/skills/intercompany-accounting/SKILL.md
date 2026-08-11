---
name: intercompany-accounting
description: >-
  Keeps intercompany accounting clean across entities — structuring IC transactions (billing,
  loans, allocations) with agreements behind them, booking both sides symmetrically, reconciling
  IC balances so they mirror each other, settling per policy, handling FX on cross-currency
  balances, and making consolidation eliminations net to zero. Use when booking or reconciling
  intercompany transactions, chasing an out-of-balance IC account, setting up an IC billing or
  loan arrangement, or preparing eliminations for consolidation. Triggers: intercompany,
  IC reconciliation, intercompany out of balance, elimination entries, IC billing, intercompany
  loan, transfer pricing entry, IC mismatch, consolidation eliminations, due to due from,
  intercompany settlement.
---

# Intercompany accounting

## When to use
- Booking intercompany activity (management fees, cost recharges, inventory transfers, IC
  loans and interest) and keeping due-to/due-from accounts mirrored across entities.
- Reconciling IC balances, clearing mismatches, running periodic settlement, and preparing
  consolidation eliminations.
- Not for: the cash settlement machinery (netting cycles, in-house bank) → see
  `cash-management-skills:intercompany-cash-netting`. For Fusion's intercompany balancing lines
  in GL → see `oracle-fusion-finance-skills:fusion-gl-and-journals`.

## Do it
1. **Give every IC flow a contract and a price.** Each recurring flow (management fee, shared
   services recharge, royalty, inventory transfer, IC loan) needs an intercompany agreement
   stating the service, pricing basis (cost, cost-plus X%, market), currency, billing cadence,
   and settlement terms. Pricing must follow the group's transfer-pricing policy (arm's length
   — set by tax advisors, not improvised by accounting); the agreement is what tax authorities
   and auditors ask for first.
2. **Book both sides symmetrically, ideally simultaneously.** Entity A's receivable from B must
   equal B's payable to A — same amount, same period, matching (mirrored) accounts. The
   strongest control is structural: one entry process that books both sides at once (ERP IC
   modules do this), so a mismatch cannot be *created*. Where entities book independently,
   standardize: the seller/provider initiates, the buyer books from the IC invoice within the
   same period, and late invoices get accrued by the receiving side (see
   `treasury-accounting-skills:accruals-and-prepaids`).
3. **Use dedicated IC accounts with counterparty detail.** Due-from/due-to accounts per
   counterparty entity (or a counterparty dimension/segment), never mixed with trade AR/AP.
   Consolidation can only eliminate what it can identify — IC activity hiding in trade accounts
   is the classic cause of eliminations that don't net.
4. **Reconcile pairwise on a matrix, monthly.** Build the IC matrix: rows = entity's
   receivable, columns = counterparty's payable; every off-diagonal pair must mirror.
   Differences decompose into a handful of causes — timing (one side booked, other not), FX
   (different rates on the same balance), errors (wrong amount/account/counterparty), and
   disputes — and each has a standard fix. `references/ic-recon-toolkit.md` has the matrix
   format and the difference-resolution playbook. Set a materiality floor for auto-clearing
   trivia and a hard deadline: mismatches must clear *before* consolidation, not in it.
5. **Handle FX with one rule set.** Cross-currency IC balances remeasure at the closing rate;
   both entities must use the *same* rate source and date. Long-term IC loans that are
   "permanent as equity" have special FX treatment (CTA rather than P&L) — flag them and agree
   treatment with the auditors. FX differences on IC balances are real (they hit P&L/CTA);
   don't force them to zero, explain them.
6. **Settle on a calendar.** IC balances that never settle become quasi-equity nobody intended:
   settle per agreement terms (monthly/quarterly), via the netting process where one exists
   (`cash-management-skills:intercompany-cash-netting`). Interest on IC loans accrues per the
   agreement — an interest-free "loan" is a transfer-pricing problem.
7. **Eliminate in consolidation and prove zero.** Eliminations reverse IC balances (due-from vs
   due-to), IC revenue vs expense, unrealized profit in inventory from IC transfers, and IC
   dividends. Because steps 2–5 kept the pairs mirrored, eliminations net to zero; when they
   don't, the difference is a specific broken pair — trace it on the matrix, don't book a plug.

## Why / learn
Intercompany accounting is bookkeeping for transactions with *yourself*, and that's exactly why
it decays without structure: no external counterparty ever complains about a wrong balance, so
errors accumulate silently until consolidation — the one process that must see the group as a
single entity — chokes on them. Every discipline in this skill is about restoring the pressure
an external party would provide. Symmetric booking replaces the vendor who'd chase the invoice;
the pairwise matrix replaces the customer statement; the settlement calendar replaces the
collector. The agreements-and-pricing layer answers a different audience: tax authorities on
*both* sides of every flow, each entitled to arm's-length pricing and each happy to tax the
same profit twice if documentation is missing. And eliminations are best understood as a proof,
not a procedure — if the group is one economic entity, then all internal claims must cancel;
an elimination that doesn't net isn't a consolidation problem, it's a ledger problem that two
entities created months earlier and consolidation merely discovered. Plugging it hides the
evidence; tracing it on the matrix finds the broken pair.

## Common mistakes
- IC activity booked in trade AR/AP → invisible to elimination; dedicated IC accounts with counterparty detail.
- Each side booking independently on its own schedule → structural mismatches; provider initiates, receiver books same period, or book both sides centrally.
- Clearing IC differences with a plug at consolidation → hides broken pairs; decompose (timing/FX/error/dispute) and fix at the pair.
- Different FX rates on the two sides of one balance → phantom differences; one rate source and date group-wide.
- IC flows without agreements or arm's-length pricing → transfer-pricing exposure on both sides; paper first, bill second.
- Balances that never settle → quasi-equity with FX and thin-cap side effects; settlement calendar, netting where available.
- Interest-free or undocumented IC loans → tax adjustments; rate and terms per the agreement.
- Ignoring unrealized profit in inventory from IC transfers → consolidated margin overstated; track and eliminate it.

## Tailor to your environment
Map your IC landscape in `references/your-environment.md` (agreements and entity specifics in
`your-environment.private.md`, git-ignored): entity list, the flows between them with pricing
bases, IC account ranges, rate source, settlement calendar, materiality floor, and who owns
each pairwise reconciliation. **Never commit real agreements, entity balances, or
transfer-pricing studies.**

## References
- references/ic-recon-toolkit.md — IC matrix format, difference-resolution playbook, elimination checklist
- references/your-environment.md — your entities, flows, accounts, calendar (fill in)
