# Intercompany reconciliation toolkit (reference)

## Contents
- The IC matrix
- Difference-resolution playbook
- Settlement and interest conventions
- Elimination checklist

## The IC matrix
Rows = reporting entity's due-from (receivable); columns = counterparty's due-to (payable),
all in group currency at the agreed closing rate:

|            | Payable: A | Payable: B | Payable: C |
|---|---|---|---|
| **Receivable: A** | — | 1,250.0 | 310.5 |
| **Receivable: B** | 0.0 | — | 88.0 |
| **Receivable: C** | 42.7 | 90.0 | — |

Mirror test: A's receivable from B (1,250.0) must equal B's payable to A. Compare cell (A,B) to
the counterparty's reported payable; differences go on a per-pair difference schedule. Build it
from trial-balance extracts by counterparty dimension — not from emails.

## Difference-resolution playbook
| Cause | Signature | Fix |
|---|---|---|
| Timing — one side unbooked | Difference = one identifiable invoice/entry | Receiving side accrues (or books) in the same period; root-cause late IC invoicing |
| FX — different rates | Difference ≈ balance × rate delta | Both sides restate at the group rate source/date; difference disappears or becomes explained FX |
| Error — wrong amount/account/counterparty | Odd amounts; one-sided entries in IC accounts | Correct at the entity that erred, with a reference to the original entry |
| Dispute — sides disagree on the charge | Persistent, documented disagreement | Escalate per policy (e.g. both CFOs, then group controller); don't let it age silently |
Order matters: check timing first (most common), then FX (mechanical), then error, then dispute.
Materiality floor: auto-write-off tiny residuals per policy, logged.

## Settlement and interest conventions
- Settlement calendar: e.g. all IC trade balances settle monthly on WD5 via the netting run;
  IC loans per their agreements.
- Interest on IC loans: rate per agreement (arm's length; often benchmark + spread set by tax
  policy), accrued monthly by *both* sides from the same schedule.
- "Permanent" funding balances: designate explicitly (affects FX treatment — CTA vs P&L) and
  agree with auditors; review the designation annually.

## Elimination checklist
- [ ] IC due-from/due-to eliminated pairwise; residual = zero (differences resolved *before* this step)
- [ ] IC revenue vs IC expense eliminated by flow (management fees, royalties, recharges)
- [ ] Unrealized profit in ending inventory from IC transfers eliminated (margin × IC inventory on hand)
- [ ] IC interest income vs expense eliminated
- [ ] IC dividends eliminated against the receiving entity's income
- [ ] FX differences on IC balances explained (P&L or CTA per designation), not plugged
- [ ] Elimination entries documented with the matrix version they were built from
