# SoD matrix and cash control catalog (reference)

## Contents
- Control objectives for cash
- Segregation-of-duties matrix
- Preventive controls
- Detective controls
- BEC / payment-fraud prevention

## Control objectives for cash
- **Authorization** — only approved, valid payments are made.
- **Completeness** — every cash transaction is captured and recorded.
- **Accuracy** — transactions are recorded at the right amount, account, and period.
- **Safeguarding** — cash and payment channels are protected from theft, loss, and fraud.
Map every control to at least one objective; a control that maps to none is ceremony.

## Segregation-of-duties matrix
Four roles must not concentrate in one person:

| Role | Task | Should NOT also hold |
|------|------|----------------------|
| Initiate | Create the payment / vendor | Approve, Reconcile |
| Approve | Authorize / release the payment | Initiate, Record |
| Record | Post to the ledger | Approve, Reconcile |
| Reconcile | Tie bank to book | Initiate, Approve |

**Toxic combinations** to flag: create/edit vendor master **+** approve payment; initiate payment
**+** reconcile bank; release wire **+** record; approve payment **+** edit bank details. Where head-
count forces a conflict, document a **compensating control** (independent review of every payment,
tighter monitoring).

## Preventive controls (stop the bad payment)
- **Authorization limits** — approval thresholds by amount and payment type; higher amounts need
  higher/added approvers.
- **Dual control / dual approval** — two people to release wires/ACH above a threshold and all
  first-time payees; enforced in the bank platform, not just internally.
- **Positive Pay** — bank matches presented checks to your issued-check file (number, amount, and —
  with **Payee Positive Pay** — payee name); mismatches are flagged for a pay/no-pay decision that
  **defaults to "no pay."**
- **ACH debit filters / blocks** — only pre-authorized originators may debit the account; all others
  are blocked or held.
- **Vendor master change controls** — restricted access, dual approval on bank-detail changes,
  independent verification.

## Detective controls (catch what slipped through)
- **Bank reconciliation** — independent, timely; the primary detective control for unauthorized/
  erroneous items. See `cash-management-skills:bank-reconciliation`.
- **Exception & override review** — review declined/held items, limit overrides, and SoD conflicts on
  a cadence.
- **Audit trail** — immutable log of who did what and when, including master-data before/after values.

## BEC / payment-fraud prevention
- **Out-of-band verification** — confirm any bank-detail change or urgent payment by calling a
  **known-good** number from your own records — never the contact details supplied in the request.
- **Beware the pressure pattern** — urgency, secrecy, a changed bank account, an executive "request"
  by email are the BEC signature.
- **Callback + dual approval** on all bank-detail changes; **training** so staff recognize the pattern.
- **Least-privilege access** to banking platforms and vendor master; prompt removal of leavers.
