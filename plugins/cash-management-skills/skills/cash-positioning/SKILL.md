---
name: cash-positioning
description: >-
  Builds and reads a daily cash position — opening, available, and projected closing balances
  across bank accounts, currencies, and entities — from actual cash flows (bank statement
  balances, AP payments, AR receipts, payroll) to drive funding, sweep, and investing decisions.
  Use when determining how much cash is available today, sizing a sweep, funding a disbursement
  account before a payment run, or building a cash position worksheet. Triggers: cash position,
  daily cash, available balance, cash worksheet, opening balance, closing balance, position the
  cash, sweep decision, how much cash today, funding decision.
---

# Cash positioning

## When to use
- Determining how much cash you actually control today/tomorrow across accounts, currencies, and
  entities before a funding, sweep, or investment decision.
- Building or reading a daily cash position worksheet from actual balances and known flows.
- Sizing a sweep to a concentration account, or funding a disbursement account ahead of a payment run.
- Not for: projecting liquidity out for weeks or months → see `cash-management-skills:cash-forecasting`.
  For setting the target/minimum balance a sweep aims at → see `cash-management-skills:liquidity-management`.

## Do it
1. **Fix the scope and cutoff.** State which accounts, currencies, and entities you are positioning,
   and the as-of business/value date. Positioning is a same-day / next-day exercise, so define the
   **cutoff time** after which incoming items roll to tomorrow's position.
2. **Take opening balances from the bank, not the ledger.** Use each account's *prior-day closing
   balance* from the final prior-day statement (BAI2 / MT940 / CAMT.053) as today's opening. Position
   to the **available (collected) balance**, not the ledger balance, wherever float or holds apply —
   see `references/cash-position-worksheet.md`.
3. **Layer today's flows in by certainty.** Add **confirmed/settled** items first (intraday postings
   from MT942 / BAI2 intraday, wires released), then **scheduled-today** items (AP payment run,
   payroll file, debt service, tax), then **expected receipts** (lockbox, card settlement, direct
   debits). Tag every line **actual vs. projected**.
4. **Compute the position per account and currency.** `Opening + inflows − outflows = projected
   closing (and available) balance`. Keep each currency **separate** — never net across currencies;
   convert to a reporting currency only for a consolidated view, at a stated rate.
5. **Compare to the target/minimum balance and read the gap.** Surplus above target → candidate to
   sweep or invest. Shortfall below minimum → fund it (sweep in, draw a facility, or defer a
   disbursement). The target level itself is a liquidity-management decision, not a positioning one.
6. **Act and document.** Execute the sweep / funding / investment, record the amount, rate, and the
   assumptions (which flows were projected). Next day, replace projections with actuals and check the
   variance — that feedback is what sharpens your intraday judgment over time.

## Why / learn
A cash position answers exactly one question — *"how much money do I actually control right now, and
where is it?"* — and it is built from **bank truth, not book truth**, because funding decisions settle
at the bank, not in the GL. This is the mirror image of forecasting: a position trades **horizon for
certainty**. You only look a day or two ahead, but you insist on real balances and confirmed flows, so
the number is accurate enough to move money against. The **available-vs-ledger** distinction is the
crux — the ledger balance counts money that has posted but may not yet be collected, and paying
against uncollected funds is precisely how a "positive" account gets overdrawn. Keeping **currencies
and entities separate** matters for the same underlying reason: cash is not fungible across them
without an FX trade or an intercompany loan. A EUR surplus does not cover a USD shortfall, and Entity
A's cash does not fund Entity B's payroll without a real transaction. The worksheet is just the ledger
of that reasoning — it lines up opening, in, out, and closing so the **gap to your target balance** is
visible, and that gap is the number every sweep, draw, and short-term investment is sized against.

## Common mistakes
- Positioning off the ledger balance → overstates available cash and risks overdraft. Use the available/collected balance.
- Netting across currencies → hides a real single-currency shortfall. Position each currency on its own.
- Treating projected receipts as confirmed → the position looks funded when it is not. Tag actual vs. projected; lean conservative on inflows.
- Ignoring the cutoff → late items land in the wrong day and the position ties out wrong. Set and honor a cutoff time.
- Positioning only at the group level → an entity or account can be short while the group looks flush. Position at the account/entity grain.
- Pushing the position out for weeks → that is a forecast, not a position. Beyond the actuals horizon, forecast instead.

## Tailor to your environment
Drop your real setup into `references/your-environment.md` (keep anything sensitive — account numbers,
real balances — in `your-environment.private.md`, which is git-ignored). Capture your account /
currency / entity structure, which balance you position to (available vs. ledger), your cutoff times,
your statement feeds and their timing (prior-day vs. intraday), your target balances, and how AP / AR /
payroll flows reach you. If you run Oracle Fusion, its Cash Positioning module builds **Cash Position
Worksheets** from an Essbase cube fed by bank statements, external transactions, AP / AR, and payroll —
see `references/cash-position-worksheet.md`. Report actuals with
`oracle-otbi-skills:otbi-cash-management-reports`; parse raw statements with
`banking-skills:bank-statement-parsing`.

## References
- references/cash-position-worksheet.md — worksheet structure, available vs. ledger, intraday feeds, and Oracle Fusion specifics
- references/your-environment.md — your accounts, balances, cutoffs, and feeds (add when supplied)
