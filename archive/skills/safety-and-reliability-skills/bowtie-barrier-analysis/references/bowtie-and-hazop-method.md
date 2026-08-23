# Bowtie and HAZOP method (reference)

## Contents
- Bowtie anatomy
- HAZOP guideword × parameter matrix
- Barrier quality tests
- Escalation-factor catalog
- Assurance tests — owner + test per barrier
- Worked example: the BEC bowtie
- Lineage and evidence notes (with provenance)

## Bowtie anatomy
```
 THREAT 1 --[P]--[P]--\                          /--[M]--[M]-- CONSEQUENCE 1
 THREAT 2 --[P]-------- >  ( TOP EVENT )  ------<---[M]------- CONSEQUENCE 2
 THREAT 3 --[P]--[P]--/                          \--[M]------- CONSEQUENCE 3
              |                                        |
        escalation factor                        escalation factor
        (+ its control)                          (+ its control)
```
- **Hazard** — the standing activity with harm potential (kept above the diagram as a title).
- **Top event** — the single moment control is lost. Not the harm itself: "fraudulent instruction
  accepted as genuine" is the top event; "funds unrecoverable" is a consequence.
- **[P] preventive barriers** sit on threat lines, left; **[M] mitigative/recovery barriers** sit on
  consequence lines, right. Escalation factors hang off individual barriers and get controls of
  their own.

## HAZOP guideword × parameter matrix
Run each guideword over each parameter of the process description; keep credible deviations as
threat lines. Payment-process parameters shown; substitute your own (for a clinical process:
patient, instrument, dose, timing, handoff).

| Guideword | Approval | Instruction / file | Beneficiary | Amount | Timing | Posting |
|---|---|---|---|---|---|---|
| **NO / NOT** | no approval obtained | no instruction on file | no beneficiary validation | — | never sent | never posted |
| **MORE** | extra approvals rubber-stamped | duplicate file transmitted | — | amount inflated | sent twice | posted twice |
| **LESS** | partial approval (one of two) | truncated file | — | amount short | late release | partial posting |
| **REVERSE** | approval after release | return/credit treated as original | — | debit/credit flipped | — | credit-return posted as receipts |
| **AS WELL AS** | approver also initiator | extra records appended | additional payee inserted | fee added | — | posted to extra account |
| **PART OF** | only some lines approved | truncated addenda | partial name match | split under threshold | — | subset posted |
| **OTHER THAN** | wrong approver role | wrong template/rail | wrong beneficiary / changed bank details | wrong currency | wrong value date | wrong account/period |

Reading the matrix: each filled cell is a candidate threat ("MORE × file = duplicate file
transmitted"). Empty cells are fine — not every combination is credible. The discipline is having
*considered* each cell, not filling it.

## Barrier quality tests
A candidate barrier must pass all three, or it is not drawn as a barrier:

1. **Independent** — it works even when the threat's cause is active, and it does not share a
   person, system, or data source with another barrier on the same line. The initiator's own
   diligence is never a barrier on a threat the initiator causes.
2. **Effective** — on its own, it can stop the threat (preventive) or materially reduce the
   consequence (mitigative). "Reduces likelihood somewhat" is a supporting measure, not a barrier.
3. **Auditable** — you can test whether it works and whether it worked: it leaves evidence
   (platform logs, callback records, exception queues) and can be exercised deliberately.

Instant fails: *training*, *policy*, *awareness*, *culture*, *management commitment* — these shape
whether barriers get built and maintained, but they stop nothing by themselves. Model them as
controls on escalation factors (e.g. training keeps the callback discipline from decaying), never as
barriers on a threat line.

## Escalation-factor catalog
Common degraders, by barrier type:
- **Human verification barriers** (callback, review, dual approval): key person absent → delegate
  rubber-stamps; volume spike → verification shortened; familiarity → "known vendor" skips the
  callback; urgency framing by the attacker → pressure to bypass.
- **System barriers** (positive pay, ACH filters, platform-enforced dual control): exception queue
  defaults to pay; filter rules stale after account changes; admin rights can disable the control;
  cutoff pressure releases before the check completes.
- **Data barriers** (vendor master, callback phone list): master data changed via the same channel
  the attacker controls (email); stale entries; no re-verification window after a change.
- **Mitigative barriers** (recall, AML chain, insurance): recall window expires over weekends;
  receiving-bank cooperation varies by rail and jurisdiction; policy exclusions for "authorized"
  push payments.

Each escalation factor gets its own control (delegation rules with equal training, queue default =
no-pay, out-of-band verification for master-data changes, recall runbook with rail-specific clocks).

## Assurance tests — owner + test per barrier
Every barrier row in the register carries: **owner** (a named role, not a department), **assurance
test** (how you prove it works), and **cadence**. Patterns:
- *Exercise*: submit a controlled fake — a test payee change, a mismatched check — and confirm the
  barrier catches it (coordinate with the bank; never test on production rails without agreement).
- *Evidence sampling*: pull N callback records / dual-approval logs per period; verify performed as
  designed, not just recorded.
- *Configuration check*: confirm the platform still enforces the rule (thresholds, queue defaults,
  filter lists) after every change.
An untested barrier is scenery. A barrier that fails its test is a finding — treat it as such.

## Worked example: the BEC bowtie
**Hazard:** the treasury moves money on instruction. **Top event:** fraudulent payment instruction
accepted as genuine.

Threat lines (guideword-generated):
- *OTHER THAN — impersonated sender* (spoofed/compromised executive or vendor email):
  [P] out-of-band callback to a number from the vendor master, never from the instruction —
  [P] dual approval enforced in the bank platform. Escalation factors: urgency framing ("CEO needs
  this before close"), approver absence → delegate; controls: no-exception callback rule, trained
  delegates. The callback and the challenge are *human* barriers — assertiveness under pressure is
  what makes them real; grade and rehearse that (PACE-style graded assertiveness — see
  `safety-and-reliability-skills:sbar-structured-communication`).
- *OTHER THAN — changed bank details* (real vendor, attacker-supplied account):
  [P] master-data change requires out-of-band verification + [P] re-verification hold on first
  payment after any change. Escalation factor: change requested via the compromised channel itself.
- *PART OF / MORE — manipulated file* (truncated addenda, duplicate or appended records):
  [P] file-level totals/hash check + [P] platform duplicate-file detection.

Consequence lines (right side): funds released to attacker →
[M] recall/return request with rail-specific clocks (wire vs. ACH) — [M] receiving-bank KYC/AML
detection and freeze — [M] fraud insurance / law-enforcement
referral (IC3-style reporting) — [M] incident response and counterparty notification.

Every barrier above gets an owner and an assurance test before the bowtie is called done.

## Lineage and evidence notes (with provenance)
- **Origin** [snippet-only]: bowtie-style cause–consequence diagrams appear in ICI hazard-analysis
  course notes (1979); after the Piper Alpha disaster and the Cullen inquiry, Shell adopted bowties
  as a group standard in the early 1990s; CCPS and the Energy Institute standardized the method in
  *Bow Ties in Risk Management*.
- **HAZOP** [snippet-only]: developed at ICI in the late 1960s (associated with Trevor Kletz's
  hazard-studies program); the guideword technique is codified in IEC 61882.
- **Financial services** [snippet-only]: banks, insurers, and regulators use bowties for fraud,
  cyber, and operational risk (scenario analysis, control mapping). Adoption is strong;
  controlled-measurement evidence that bowtie use improves loss outcomes is thin — no
  surgical-checklist-style trial exists. Present the method on its structuring merits.

Provenance note: items marked [snippet-only] were verified against summaries and secondary accounts,
not full primary texts. Re-verify specifics before quoting in anything formal.
