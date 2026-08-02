# Evals — cash-management-skills:cash-management-controls

## 1. Positive trigger (should load the skill)
> "We just had a near-miss where someone almost paid a supplier's 'updated' bank details from an
> email. I need to review our cash controls — segregation of duties on payments, our approval limits,
> whether Positive Pay is set up right, and how we should verify bank-detail changes going forward."

Expected: skill loads; frames the four control objectives; builds/reviews the SoD matrix across
initiate/approve/record/reconcile; sets authorization limits and dual control enforced at the bank;
recommends Payee Positive Pay and ACH filters; and centers BEC defense on out-of-band verification
against a known-good contact plus dual approval on bank-detail changes.

## 2. Near-miss (should NOT load this skill)
> "Reconcile last month's bank statement to the GL and find what's making up the $2,450 difference."

Expected: this is performing the reconciliation, not designing controls over it. The
`cash-management-skills:bank-reconciliation` skill should handle it. If this skill loads, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** ties controls to authorization/completeness/accuracy/safeguarding, separates
  initiate/approve/record/reconcile with toxic combinations flagged, sets limits + dual control
  enforced at the bank, enables Positive Pay/ACH filters, and defines an out-of-band BEC verification
  procedure.
- **Teaches:** explains *why* SoD splits the "move money" and "conceal it" tasks, why you need both
  preventive and detective layers, and why no approval workflow stops BEC (the payment is
  "authorized") — only out-of-band verification does.
- **Safe:** does not suggest verifying bank-detail changes using contact info from the request, does
  not treat reconciliation as the sole control, and defaults payment exceptions to "no pay."
