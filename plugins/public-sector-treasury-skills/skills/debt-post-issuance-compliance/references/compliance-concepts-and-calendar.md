# Post-issuance compliance concepts and calendar (reference)

This file teaches the structure of the federal tax and disclosure regimes for tax-exempt debt.
Thresholds, safe harbors, and event lists are set by Treasury regulations and SEC Rule 15c2-12
and are amended over time — **confirm current specifics with bond counsel and your rebate
consultant before relying on any figure here.**

## Contents
- Vocabulary that prevents confusion
- Arbitrage: yield restriction vs rebate
- Spending exceptions to rebate (structure)
- Private business use: the two-part test, sources, measurement
- Continuing disclosure: annual filings and event notices
- Record retention map
- Compliance calendar template
- Who decides what (escalation map)

## Vocabulary that prevents confusion
- **Proceeds / gross proceeds:** sale proceeds plus investment earnings plus amounts treated as
  proceeds (e.g. sinking funds, pledged funds). Arbitrage rules attach to *gross proceeds*,
  which is broader than "the construction fund."
- **Bond yield:** the discount rate equating debt-service payments to the issue price —
  computed at issuance (fixed-rate) or over computation periods (variable). The benchmark for
  both yield restriction and rebate.
- **Temporary period:** a window during which gross proceeds may be invested without yield
  restriction (e.g. a multi-year window for project funds spent with due diligence).
- **Computation date:** a date as of which cumulative rebate liability is calculated.
- **Refunding:** new bonds retiring old bonds; transferred proceeds and record-retention chains
  follow the refunding.

## Arbitrage: yield restriction vs rebate
Two separate tests; passing one does not pass the other.

| | Yield restriction | Rebate |
|---|---|---|
| Question | May these proceeds be invested above bond yield *at all*? | Of the excess earnings that were allowed, how much is owed to the IRS? |
| Applies to | Gross proceeds outside temporary periods / allowances | Cumulative excess earnings across the issue |
| Timing | Continuous — status of each fund at each moment | Periodic — computation dates (structurally at least every 5 years and at final redemption) |
| Cure/mechanics | Restrict investments; yield-reduction payments where permitted | Rebate payments with the IRS filing (Form 8038-T family) |

Analyst's role: maintain issue-level, fund-level investment records (security, purchase price,
income, disposition) so the consultant can compute; calendar the computation dates; budget for
potential liability in high-rate environments. In low-rate periods liability is often zero —
the *computation obligation* is not.

## Spending exceptions to rebate (structure)
The regulations reward fast spenders with exceptions from rebate on certain funds. The classic
patterns (elect/qualify per issue — confirm which applies):
- **6-month exception:** substantially all proceeds spent within 6 months.
- **18-month exception:** benchmarks at 6/12/18 months (roughly 15% / 60% / 100%).
- **2-year construction exception:** for qualifying construction issues, benchmarks at
  6/12/18/24 months (roughly 10% / 45% / 75% / 100%).
Missing a benchmark generally forfeits the exception (some de-minimis/reasonable-retainage
relief exists). This is why the spend-down schedule is a compliance document, not just a
project-management report.

## Private business use: the two-part test, sources, measurement
Governmental bonds generally lose their status only if **both** limbs are exceeded:
1. **Private business use test:** more than the permitted share (structurally 10%, tighter —
   5% — for unrelated/disproportionate use) of proceeds/financed property is used in a trade or
   business of a non-governmental person. For 501(c)(3) ("qualified 501(c)(3) bond") financings
   the analysis differs — the borrower's exempt use matters; confirm the framework per issue.
2. **Private payment/security test:** more than the corresponding share of debt service is
   secured by or derived from private payments/property.

**What creates PBU (screen all of these):**
- Leases and subleases of financed space to non-governmental users.
- **Management/service contracts** for financed facilities (dining, bookstore, parking, energy,
  athletics operations) — compensation-structure safe harbors exist; route terms to counsel.
- **Sponsored research** in financed labs — safe harbors for federally sponsored and qualifying
  basic research exist; the killer detail is who gets rights to resulting IP on what terms.
- Naming rights / sponsorship with use rights attached; cell towers, antennas, rooftop space.
- Sales of output/capacity, special parking arrangements, joint ventures, priority-use deals.
- General public use on equal terms is *not* PBU (short-term equal-access arrangements have
  their own safe-harbor structure).

**Measurement:** PBU % is measured against the issue over the measurement period, weighting
space and time (square footage × time of private use, and cost allocation of the financed
portion). Practical machinery: an annual questionnaire to every department occupying financed
space, plus a contract-review gate so new agreements touching financed facilities get screened
*before* signature. If a limit will be exceeded from a **change in use**, prompt **remedial
action** (redemption/defeasance of nonqualified bonds, alternative use of proceeds or facility)
can preserve the exemption — timing matters, so escalate immediately.

## Continuing disclosure: annual filings and event notices
Source: the issue's **continuing disclosure agreement/undertaking**, written to satisfy SEC
Rule 15c2-12 (the underwriter's rule — it binds the issuer via contract).
- **Annual filing:** audited financial statements plus the specific operating data tables the
  CDA promises (enrollment, revenues by source, etc. for a university credit), due within the
  CDA's stated window after fiscal year end. File on **EMMA** (MSRB's portal), correctly
  indexed to every CUSIP.
- **Event notices:** the rule enumerates events — payment delinquencies, rating changes,
  defeasances, bond calls, substitution of credit/liquidity providers, certain
  financial-obligation incurrences and defaults (added in later amendments), bankruptcy,
  merger/sale events, trustee changes, and more — filed within the rule's short window
  (structurally **10 business days** of occurrence). Pull the exact list from each CDA; the
  rule has been amended and older CDAs enumerate shorter lists.
- **Failure handling:** a missed or late filing must itself be disclosed (and surfaces in
  diligence on the next offering). Log filings with dates and EMMA confirmations; run an annual
  self-check of filing completeness against every outstanding CUSIP.

## Record retention map
Keep, per issue, for life of the bonds + all refundings + the audit tail (~3 years — confirm):
- **Transcript:** authorizing documents, tax certificate, 8038-G/8038 filings, opinions, CDA.
- **Expenditure records:** requisitions, invoices, allocation of proceeds to projects,
  final-allocation documentation.
- **Investment records:** every fund holding gross proceeds — trades, income, balances.
- **Rebate:** computations, consultant reports, IRS filings and payments.
- **Use records:** PBU questionnaires, leases, management/research contracts, counsel analyses.
- **Disclosure:** annual filings, event notices, EMMA confirmations.

## Compliance calendar template
| Frequency | Item | Owner |
|-----------|------|-------|
| Annual | CDA annual filing (deadline = FYE + CDA window) | Debt/disclosure officer |
| Annual | PBU questionnaire to departments in financed space | Treasury analyst |
| Annual | Spend-down schedule refresh per unspent-proceeds issue | Treasury analyst |
| Annual | Records-vault completeness check | Treasury analyst |
| Ongoing | Event-notice watch (ratings, defeasances, new financial obligations) | Named watcher |
| Ongoing | Contract-review gate for financed facilities | Treasury + counsel |
| Per issue, ≥ every 5 yrs | Rebate/yield-restriction computation date | Rebate consultant |
| At redemption/refunding | Final computations; extend record chains | Consultant + analyst |

## Who decides what (escalation map)
- **Analyst/treasury:** data, calendars, questionnaires, schedules, filings logistics, flags.
- **Rebate consultant:** rebate and yield-reduction computations, IRS payment filings.
- **Bond counsel:** safe-harbor conclusions, PBU determinations, remedial actions, anything
  touching the tax opinion.
- **Disclosure counsel/municipal advisor:** CDA interpretation, event-notice judgment calls.
