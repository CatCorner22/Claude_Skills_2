---
name: cash-management-controls
description: >-
  Designs and reviews controls over cash processes — segregation of duties, payment authorization and
  dual approval, positive pay and ACH filters, reconciliation as a detective control, bank mandate
  management, and business-email-compromise prevention — mapped to the control objectives of
  authorization, completeness, accuracy, and safeguarding. Use when designing or auditing cash
  controls, building a segregation-of-duties matrix, or responding to a payment-fraud risk. Triggers:
  cash controls, segregation of duties, SOD, dual approval, payment authorization, positive pay, ACH
  filter, payment fraud, BEC, business email compromise, audit trail, bank mandate.
---

# Cash management controls

## When to use
- Designing or reviewing controls over payments, receipts, bank accounts, and reconciliation.
- Building a segregation-of-duties matrix for cash, or setting payment authorization limits and dual control.
- Responding to a payment-fraud risk (BEC, altered bank details, check/ACH fraud).
- Not for: performing the reconciliation itself → see `cash-management-skills:bank-reconciliation`. For
  documenting and standardizing the control procedure → see
  `continuous-improvement-skills:standard-work`.

## Do it
1. **State the control objectives for cash.** Every control here serves one of four: **authorization**
   (only approved payments go out), **completeness** (all cash activity is recorded), **accuracy**
   (recorded correctly), and **safeguarding** (assets protected from loss/fraud). Tie each control you
   design back to an objective — see `references/sod-and-control-catalog.md`.
2. **Build the segregation-of-duties matrix.** Separate the four incompatible roles: **initiate**,
   **approve**, **record**, and **reconcile** a payment. No one person should hold two that let them
   both move money and hide it. Flag toxic combinations (e.g. create vendor + approve payment;
   release wire + reconcile bank).
3. **Set payment authorization and dual control.** Define approval **limits by amount and payment
   type**, require **dual approval** on wires/ACH above a threshold and on all first-time payees, and
   make sure **bank-side entitlements match the policy** — a limit that isn't enforced at the bank is
   not a control.
4. **Turn on bank fraud tools.** Enable **Positive Pay** (bank matches presented checks to your issued
   file — use **Payee** Positive Pay to catch altered payees) and **ACH debit filters/blocks** (only
   authorized originators may debit). Set exception decisions to **default to "no pay."**
5. **Use reconciliation as the detective control.** Timely, independent bank reconciliation is what
   catches an unauthorized or erroneous payment after the fact — schedule it, and keep the reconciler
   separate from anyone who initiates or approves. Run the rec with `cash-management-skills:bank-reconciliation`.
6. **Manage bank mandates and prevent BEC.** Keep authorized-signer and entitlement lists current —
   **remove leavers immediately**. For any request to change vendor **bank details** or make an urgent
   payment, **verify out-of-band via a known-good phone number** (never the contact details in the
   request), require dual approval on bank-detail changes, and train staff on the pattern.
7. **Preserve the audit trail and review.** Ensure every payment and master-data change is logged
   (who, what, when, before/after) and immutable; review exceptions, overrides, and SoD conflicts on a
   cadence. A control you cannot evidence is a control you cannot rely on.

## Why / learn
Cash is the asset thieves and errors reach first, so its controls all trace back to the same four
objectives — **authorization, completeness, accuracy, safeguarding** — and the art is placing controls
so that defeating one requires defeating another held by a *different person*. That is why
**segregation of duties** is the backbone: the danger is never one task, it is one person holding the
task that *moves* money and the task that *conceals* it. Split initiate/approve/record/reconcile and a
single actor can no longer both pay themselves and hide it — collusion becomes necessary, which is far
harder. **Preventive** controls (authorization limits, dual approval, positive pay, ACH filters) stop
the bad payment before it leaves; **detective** controls (reconciliation, exception review, the audit
trail) catch what slipped through — you need both, because prevention is never perfect and detection
without prevention just documents losses. The modern reason this matters is that the biggest cash
losses today are not forged checks but **social engineering**: a convincing email redirecting a
supplier payment or changing bank details. No approval workflow stops that, because the payment is
"authorized" — the only control that does is **out-of-band verification against a known-good contact**,
which is why it sits at the center of BEC defense. Think in objectives and in prevent-plus-detect
layers, and the specific tools become obvious rather than a checklist to memorize.

## Common mistakes
- One person initiates and reconciles → they can pay and conceal it. Separate initiate/approve/record/reconcile.
- Approval limits set in policy but not at the bank → unenforced. Mirror the limits in bank entitlements.
- Amount-only Positive Pay → misses altered payees. Use Payee Positive Pay and default exceptions to "no pay."
- Verifying a bank-detail change using the contact info in the request → that is the fraudster's number. Call a known-good number.
- Leaving ex-employees on signer/entitlement lists → open door. Remove leavers immediately.
- Treating reconciliation as the only control → it only detects after the fact. Pair it with preventive controls.

## Tailor to your environment
Drop your real control setup into `references/your-environment.md` (keep sensitive specifics — signer
lists, limits, bank entitlements — in `your-environment.private.md`, which is git-ignored): your
approval limits by amount and payment type, your SoD assignments and any accepted conflicts with
compensating controls, which bank fraud tools are enabled (Positive Pay type, ACH filters), your bank
mandate/entitlement review cadence, and your BEC verification procedure. Once the controls are set,
standardize the procedures with `continuous-improvement-skills:standard-work` and run the detective
reconciliation with `cash-management-skills:bank-reconciliation`.

## References
- references/sod-and-control-catalog.md — the SoD matrix, control objectives, and a catalog of preventive/detective cash controls
- references/your-environment.md — your limits, SoD assignments, fraud tools, and BEC procedure (add when supplied)
