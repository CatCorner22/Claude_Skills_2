# SEC codes, return codes, NOCs, reversals, and ODFI/RDFI duties (reference)

Timeframes and limits below describe the **structure** of the NACHA rules and the historical
figures analysts know by heart. NACHA amends the rules regularly — **confirm current numbers
with your ODFI or the current NACHA Operating Rules before acting on a deadline.**

## Contents
- Common SEC codes and what they imply
- Return codes: families and the ones you will actually see
- Return timeframes: how the clocks work
- Notifications of change (NOCs / C-codes)
- Reversal checklist
- Prenote flow
- Same Day ACH notes
- ODFI vs RDFI responsibilities

## Common SEC codes and what they imply

| Code | Name | Parties | Typical use | Authorization implied |
|------|------|---------|-------------|----------------------|
| PPD | Prearranged Payment & Deposit | Company ↔ consumer | Payroll direct deposit, student refunds, recurring consumer debits | Written (or similarly evidenced) standing authorization |
| CCD | Corporate Credit or Debit | Company ↔ company | Vendor payments, tax payments, cash concentration | Agreement between companies; receiver monitors own account |
| CTX | Corporate Trade Exchange | Company ↔ company | Vendor payments with full remittance detail | Like CCD, plus up to 9,999 addenda records (EDI 820-style remittance) |
| WEB | Internet-Initiated/Mobile Entry | Company → consumer (debit) | Online one-time or recurring consumer debits (e.g. online tuition/fee payment by bank draft) | Authorized via internet/mobile; originator owes account-validation and security duties |
| TEL | Telephone-Initiated Entry | Company → consumer (debit) | Debit authorized during a phone call | Oral authorization, recorded or confirmed in writing |
| COR | Notification of Change | RDFI → ODFI | Carries a NOC (see below) | n/a — zero-dollar administrative entry |
| IAT | International ACH Transaction | Cross-border leg | Any entry funded from / destined to an account outside the US | Extra data for OFAC/BSA screening |

Rule of thumb: **consumer vs company picks the family (PPD vs CCD/CTX); the authorization
channel picks the consumer code (PPD vs WEB vs TEL); remittance-detail needs pick CCD vs CTX.**

## Return codes: families and the ones you will actually see

R-codes group into families; read the family first, then the specific code.

**Funds problems (retryable within limits)**
- **R01 — Insufficient funds.** May be re-initiated a limited number of times (historically up
  to two more attempts). Most common return in collections.
- **R09 — Uncollected funds.** Balance present but not yet collected; same retry treatment.

**Account problems (fix data before any retry)**
- **R02 — Account closed.** Stop originating; get new instructions.
- **R03 — No account / unable to locate.** Name and number don't match any account.
- **R04 — Invalid account number structure.** Data entry problem on your side.
- **R12 — Account sold to another DFI.**
- **R13 / R28 — Invalid or bad routing number / check digit.**
- **R16 — Account frozen.** Legal hold or OFAC-related; involve your bank before retrying.
- **R20 — Non-transaction account.** Account type doesn't permit ACH.

**Authorization problems (never re-initiate without new authorization)**
- **R05 — Unauthorized debit to consumer account using corporate SEC code.** Extended window.
- **R07 — Authorization revoked by customer.** Extended window.
- **R10 — Customer advises: not authorized / no relationship.** The classic consumer
  unauthorized claim; requires the RDFI to hold a Written Statement of Unauthorized Debit.
- **R11 — Customer advises: entry not in accordance with the authorization.** Error in an
  otherwise-authorized entry (wrong amount/date); correctable and may be re-originated once
  corrected, unlike R10.
- **R29 — Corporate customer advises not authorized.** The corporate analog to R10, but on the
  short two-banking-day clock.

**Receiver / bank action**
- **R06 — Returned per ODFI's request.** The result of your bank asking for the entry back.
- **R08 — Payment stopped.** A stop-payment order at the RDFI.
- **R23 — Credit entry refused by receiver.**
- **R24 — Duplicate entry.**
- **R31 — Permissible return (CCD/CTX).** RDFI returning a corporate entry late *with the
  ODFI's agreement.*

## Return timeframes: how the clocks work
- **Standard returns** (funds, account, most administrative): must be *received by the ODFI* by
  opening of business on the **second banking day following settlement**. This is why a Monday
  origination that settles Tuesday can still bounce Thursday morning.
- **Consumer unauthorized/revoked (R05, R07, R10, R11):** extended window — the RDFI must
  transmit the return within a window historically framed as **60 calendar days from
  settlement**, backed by the consumer's written statement. Regulation E gives the *consumer*
  separate, longer rights against their own bank; don't confuse the two.
- **Corporate unauthorized (R29):** the short two-banking-day clock. After it lapses, remedies
  are contractual (indemnity, breach-of-warranty claims), not returns.
- Clocks run from the **settlement date**, not the file-creation or origination date.

## Notifications of change (NOCs / C-codes)
A NOC arrives as a zero-dollar **COR** entry: the RDFI posted your entry but is telling you to
fix a data element before the next one.

| Code | Fix |
|------|-----|
| C01 | Account number |
| C02 | Routing number |
| C03 | Routing number **and** account number |
| C05 | Account type (checking ↔ savings) |
| C06 | Account number and account type |
| C07 | Routing number, account number, and account type |
| C09 | Individual ID number |

Originator duties: apply the change within the rules' window (historically six banking days or
before the next entry, whichever is later) and stop transmitting the old data. Route NOCs to
whoever owns the master data (payroll, vendor file), not just the treasury inbox.

## Reversal checklist
A reversing entry is permitted **only** for:
1. a **duplicate** of a previously originated entry;
2. the **wrong dollar amount**;
3. the **wrong receiver / account**;
4. a payment date **earlier than intended** (and certain other date errors — confirm current).

Mechanics:
- Transmit within the rule window — historically **five banking days from settlement** of the
  erroneous entry (and within 24 hours of discovering the error for files).
- Batch/company entry description must read **REVERSAL**; the original entry's details are
  echoed so the receiver can pair them.
- **Notify the receiver** of the reversal and the reason.
- If you reversed a payment someone was owed, re-originate the correct entry promptly.
- A reversal has no special standing — it can return R01/R02 like any debit. Failed reversal →
  direct recovery (call, letter, indemnity via your ODFI), not another reversal.

## Prenote flow
1. Send a **zero-dollar prenotification** with the live entry's account data.
2. Wait the validation period (historically three banking days) before the first live entry.
3. A return on the prenote = do not go live; a NOC on the prenote = fix data first, then go live.
Prenotes are optional under the rules but standard practice for new payroll accounts and vendor
bank-detail changes (pair them with callback verification — a prenote validates the *account*,
not the *identity* of who gave you the details).

## Same Day ACH notes
- Eligibility: domestic entries at or under the **per-payment dollar limit** (raised over the
  years; confirm the current limit). IATs are excluded.
- Multiple same-day **processing windows** exist with morning/afternoon cutoffs; your ODFI's
  cutoffs will be earlier than the network's.
- Costs more per entry (network fee plus bank pricing); use it for genuinely date-critical
  items, not as a default.
- A same-day-settled entry is still returnable on the normal clocks — speed ≠ finality.

## ODFI vs RDFI responsibilities
| | ODFI (origination side) | RDFI (receiving side) |
|---|---|---|
| Warrants | Entry is authorized, timely, accurate — the ODFI warrants this to the network and indemnifies RDFIs | — |
| Must | Vet originators, enforce exposure limits, monitor return rates (unauthorized-return-rate thresholds exist), pass NOCs to originators | Post entries by settlement date, make funds available per rules, return timely, send NOCs instead of silently fixing data |
| Your seat | As an **originator**, your duties flow through your ODFI agreement — authorization records, prenote discipline, honoring NOCs, staying under return-rate thresholds | As a **receiver**, watch your accounts daily: your practical protection on corporate accounts is the two-day return window plus ACH debit blocks/filters (see `cash-management-skills:cash-management-controls`) |
