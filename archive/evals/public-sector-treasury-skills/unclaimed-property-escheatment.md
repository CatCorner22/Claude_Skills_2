# Evals — public-sector-treasury-skills:unclaimed-property-escheatment

## 1. Positive trigger (should load the skill)
> "Our outstanding-check report has about 240 checks over a year old — payroll, vendor
> payments, and student refunds. Can we just void them and write them off, or what do we
> actually have to do?"

Expected: skill loads; immediately corrects the write-off idea (liability, never income);
lays out the lifecycle — dormancy screen by property type under the current state table,
priority rules by owner address, statutory due-diligence letters, reissue-with-controls vs
report-and-remit, holder report in the state's format, retention; recommends a recurring
cycle plus source reduction (e-payments, payee data, early chase).

## 2. Near-miss (should NOT load this skill)
> "Help me reconcile last month's bank statement — there's a $12,400 unreconciled
> difference between the bank and the GL."

Expected: this is a bank reconciliation, not an escheatment task —
`cash-management-skills:bank-reconciliation` should handle it (stale checks merely *surface*
there). If this skill loads, tighten the description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** screens by property type and dormancy; applies the Texas v. New Jersey
  priority rules (owner's last-known-address state first, holder's domicile second); runs
  due diligence within the statutory window with documentation; shows the correct
  accounting (void → unclaimed-property liability → reissue or remit); covers the holder
  report, negative reports, and record retention; adds source reduction.
- **Teaches:** explains the custodial/derivative-rights model (the state takes custody, the
  owner's claim is perpetual, the money was never the holder's), why income write-offs are
  the classic audit finding, and why the address field is a compliance control.
- **Safe:** never hard-codes dormancy periods, thresholds, or deadlines — says to verify the
  current state table (Tennessee as example framing only); requires payee identity
  verification before reissue (fraud vector); flags that a public institution's status may
  be modified and must be confirmed; keeps owner-level data out of committed files.
