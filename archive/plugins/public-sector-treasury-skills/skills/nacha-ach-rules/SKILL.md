---
name: nacha-ach-rules
description: >-
  Applies NACHA ACH operating-rule fundamentals from both the originator's and the receiver's
  seat: choosing and interpreting SEC codes (PPD, CCD, CTX, WEB, TEL), reading return codes and
  their timeframes, handling notifications of change (NOCs), running compliant reversals and
  prenotes, Same Day ACH eligibility and windows, and ODFI/RDFI responsibilities. Use when
  interpreting an ACH return or NOC, originating or reversing an entry, choosing an SEC code,
  or investigating an ACH exception on a bank statement. Triggers: NACHA, ACH rules, return
  code, R01, NOC, notification of change, SEC code, PPD, CCD, WEB, ACH reversal, prenote,
  ODFI, RDFI, ACH return timeframe, unauthorized ACH.
---

# NACHA ACH rules

## When to use
- Interpreting an ACH return (R-code) or a notification of change (NOC / C-code) that appears on
  a bank statement, returns report, or origination platform.
- Originating entries: choosing the right SEC code, running a prenote, or deciding whether a
  reversal is allowed and how to send it.
- Explaining who is responsible for what between the ODFI (originating bank) and RDFI (receiving
  bank), or whether an entry qualifies for Same Day ACH.
- Not for: deciding whether to pay by ACH versus wire, RTP, or check → see
  `banking-skills:payment-rails`. For locating returns/NOCs inside a raw BAI2/CSV statement file
  → see `banking-skills:bank-statement-parsing`.

## Do it
1. **Identify your seat and the entry.** Are you the **Originator** (you or your ODFI sent the
   entry) or the **Receiver** (someone debited/credited your account)? Is the entry a **debit**
   (pull) or **credit** (push), and is the counterparty a **consumer** or a **company**? These
   three facts determine which rules, timeframes, and rights apply to everything below.
2. **Interpreting a return:** look up the R-code and read it as *family + specifics* — funds
   problems (R01 insufficient, R09 uncollected), account problems (R02 closed, R03 no account,
   R04 invalid number), authorization problems (R05/R07/R10/R11/R29 unauthorized or revoked),
   and receiver-action returns (R08 stopped, R06 ODFI request). See
   `references/sec-codes-returns-and-nocs.md` for the table. Then check **timeliness**: most
   returns must reach the ODFI within about two banking days of settlement, while consumer
   unauthorized claims travel on an extended window (~60 calendar days) — confirm the exact
   current deadlines in the NACHA rules before disputing one as late.
3. **Decide the response to the return.** Fix-and-resend is allowed only in narrow cases: an
   entry returned for insufficient/uncollected funds may be re-initiated a limited number of
   times (historically two more attempts), and a corrected entry may follow certain
   administrative returns. An entry returned as *unauthorized* must **not** be re-initiated
   without a new authorization. Log every return as an exception with an owner.
4. **Handling a NOC (C-code):** a NOC rides in on a COR entry and tells the Originator "your
   entry posted, but fix this detail" — wrong account number (C01), routing number (C02),
   account type (C05), etc. Update the master record before the next entry (the rules give a
   short window, ~six banking days or prior to the next entry — confirm current). Repeatedly
   ignoring NOCs is itself a rules violation and invites future returns.
5. **Choosing an SEC code when originating:** the code declares *who authorized the entry and
   through what channel*, so pick it from the authorization, not from convenience: **PPD**
   consumer, standing written authorization; **WEB** consumer debit authorized over the
   internet/mobile; **TEL** consumer debit authorized by phone; **CCD** company-to-company;
   **CTX** company-to-company carrying full remittance addenda (up to 9,999 records). Each code
   carries its own authorization, retention, and (for WEB) account-validation duties.
6. **Reversals:** allowed only for the enumerated errors — duplicate entry, wrong amount, wrong
   receiver/account, or wrong (earlier-than-intended) date. Send within the short rule window
   (about five banking days from settlement), label the batch description **REVERSAL**, and
   notify the receiver. A reversal is an ordinary debit with no priority: if the money is gone,
   the reversal returns R01 and you are into recovery by phone and letter, not by rule.
7. **Prenotes:** before the first live entry to a new account you may send a zero-dollar
   prenotification, then wait the rule's short validation period (historically three banking
   days) and act on any return or NOC it draws. Prenotes are optional but cheap insurance for
   payroll and vendor master changes.
8. **Same Day ACH:** eligible domestic entries under the per-payment limit can settle same day
   through the extra processing windows, at a premium fee. The limit and window cutoffs have
   changed several times — confirm the current figures with your ODFI before promising same-day
   settlement.
9. **Close the loop.** Tie the return/NOC back to the statement line and your ledger entry,
   record the resolution, and update the exception log so patterns (one department's bad vendor
   data, one recurring R10 counterparty) become visible.

## Why / learn
ACH is a **batch network run on rules instead of real-time verification** — nobody checks that
the account exists or the money is there when the file is submitted. The rules substitute for
that missing verification, and almost every mechanism above is one of the substitutes.
**Authorization is the spine**: the SEC code is a declaration of who authorized the entry and
how, and that declaration drives everything downstream — corporate entries (CCD/CTX) get only a
~two-banking-day return window because companies are expected to monitor their accounts daily,
while consumers get an extended unauthorized-return window because consumer-protection law
(Regulation E) sits behind the rules. **Returns are the network's error-correction channel** and
NOCs are its maintenance channel: a return says "this entry failed," a NOC says "it worked, but
fix your data." **Reversals are deliberately narrow** because ACH has no recall right — the
network lets you attempt to claw back only clerical errors, and even then the reversal is just
another entry that can itself bounce. The operational consequence to internalize: an ACH credit
you received is provisional until the return windows lapse, and an ACH debit you originated is
never "collected" on settlement day. Hold the model "declared authorization in, rule-bounded
error-correction out" and every R-code, C-code, and deadline slots into place.

## Common mistakes
- Treating settlement as final → return windows are still open; don't release goods or refunds
  against a same-day ACH credit.
- Re-initiating an entry returned as unauthorized (R05/R07/R10/R29) → prohibited without a new
  authorization; obtain one or pursue the claim outside ACH.
- Ignoring NOCs → data never gets fixed, future entries return, and repeated NOC neglect is a
  rules violation. Route every NOC to the master-data owner.
- Picking WEB vs PPD by habit → the authorization channel dictates the code; the wrong code
  voids your proof-of-authorization posture in a dispute.
- Using a reversal to unwind a business dispute → reversals cover clerical errors only; a
  disputed-but-authorized payment is a negotiation, not a reversal.
- Assuming the consumer 60-day unauthorized window applies to corporate accounts → corporate
  receivers have ~two banking days; after that the fight moves to indemnities and agreements.
- Counting return deadlines from origination date → windows run from the settlement date, in
  banking days (or calendar days for the consumer window). Verify which clock applies.

## Tailor to your environment
Record your real ACH setup in `references/your-environment.md`: your ODFI(s) and origination
platform, the SEC codes you actually originate (e.g. PPD payroll and refunds, CCD/CTX vendor
payments), where returns and NOCs surface (returns report, statement addenda, portal), who owns
each exception type, and your prenote and re-initiation policies. Keep anything sensitive —
company IDs, bank names tied to account details, counterparty specifics — in
`your-environment.private.md`, which is git-ignored; never commit real identifiers. NACHA
amends the rules on a rolling schedule (limits, windows, validation duties), so record *where
you confirm current rules* (your ODFI's bulletin, NACHA publications) rather than pinning
numbers here.

## References
- references/sec-codes-returns-and-nocs.md — SEC code table, return-code families and common
  codes, NOC codes, reversal/prenote checklists, ODFI vs RDFI duties
- references/your-environment.md — your ODFI, SEC codes, exception routing (add when supplied)
