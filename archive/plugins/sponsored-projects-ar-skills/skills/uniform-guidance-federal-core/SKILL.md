---
name: uniform-guidance-federal-core
description: >-
  Provides core educational knowledge of 2 CFR Part 200 (Uniform Guidance) for federal awards —
  the subpart structure, post-2024 thresholds (15% de minimis F&A on MTDC, $1,000,000 Single
  Audit, $10,000 equipment), financial management standards (§200.302), payment standards
  (§200.305), cost principles and always-unallowable costs (Subpart E), and refund obligations —
  as context for sponsored projects billing and receivables analysis. Use for any question
  involving federal awards, Uniform Guidance, 2 CFR 200, cost principles, Single Audit, or when
  analyzing AR data for federal sponsors. Triggers: uniform guidance, 2 CFR 200, federal award
  compliance, cost principles, single audit, de minimis rate, MTDC, unallowable costs,
  allowability, federal grant rules, questioned costs, F&A rate.
---

# Uniform Guidance (2 CFR 200) federal core

## When to use
- Any sponsored-AR analysis touching federal sponsors: the compliance frame that decides what
  is billable, what must be refunded, and what an auditor will test.
- Answering "is this allowable," "what threshold applies," or "what does 2 CFR 200 say about X"
  at an educational level.
- Not for: how federal money actually moves (draws, advances, reimbursement) → see
  `sponsored-projects-ar-skills:federal-billing-cash-management`. For personnel-cost standards →
  see `sponsored-projects-ar-skills:federal-effort-reporting-basics`. Enter sponsored-AR
  analysis via `sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`.

## Do it
1. **State the scope honestly, every time.** This skill teaches the *public text* of 2 CFR
   Part 200 and official summaries — it is **not a substitute for the regulation itself, the
   Notice of Award (NOA), or institutional policy**, and agency-specific terms (NIH Grants
   Policy Statement, NSF PAPPG, agency 2 CFR adoptions) can be stricter. Every deliverable
   carries that disclaimer and cites the CFR sections it leans on.
2. **Classify the instrument first.** **Grants and cooperative agreements** run under Uniform
   Guidance; **federal contracts** run primarily under the FAR (and Cost Accounting Standards
   for larger contractors) — different rules, different audit regimes. Misclassifying the
   instrument invalidates the whole analysis; check the award document.
3. **Navigate by subpart.** 2 CFR 200's structure *is* the index: **Subpart A** acronyms and
   definitions; **B** general provisions; **C** pre-award; **D** post-award requirements
   (financial management §200.302, payment §200.305, program income, cost sharing, closeout);
   **E** cost principles (allowability, direct vs indirect, selected items of cost);
   **F** audit requirements (Single Audit). Route any question to its subpart before answering.
4. **Apply the current thresholds — and date them.** For awards under the revised guidance
   (effective for federal awards issued on/after October 1, 2024; earlier awards may carry old
   terms): **de minimis F&A = 15% of MTDC**; **Single Audit threshold = $1,000,000** of federal
   expenditures in a fiscal year; **equipment capitalization = $10,000**. **MTDC** includes
   salaries/wages, fringe, materials and supplies, services, travel, and **up to the first
   $50,000 of each subaward**; it excludes equipment, capital expenditures, patient care,
   rental costs, scholarships/participant support, and the portion of each subaward beyond
   $50,000. Awards straddling the change keep their award-term rates — check the NOA.
5. **Know the financial-management floor (§200.302):** identification of federal awards,
   accurate/current/complete expenditure records, records that support amounts charged
   (source documentation), effective internal control, comparison of expenditures to budget,
   and written procedures for payments and allowability. For AR analysis this is the standard
   the *billing data itself* must meet.
6. **Carry the cost-principles essentials (Subpart E):** allowability = reasonable + allocable
   + consistently treated + adequately documented + within award terms. Always-unallowable
   examples: **bad debts (§200.426)** — critically, a federal sponsor's non-payment can never
   be charged back to the award — alcohol, entertainment, lobbying, fines and penalties.
   **Unallowable costs already collected must be refunded (§200.410)**, often with interest —
   which is how a compliance finding becomes an AR event (a negative one).
   `references/ug-quick-tables.md` has the threshold and unallowable-cost tables with citations.
7. **Deliver in the standard form:** glossary of the terms in play, the applicable threshold
   table (dated), key CFR citations, the analysis itself, and the disclaimer. Route billing/
   cash mechanics onward to `sponsored-projects-ar-skills:federal-billing-cash-management`.

## Why / learn
Uniform Guidance is best read as *the terms and conditions of the federal government as a
customer* — and it's a customer that writes its own rules, audits your books, and can demand
money back with interest. That reframe explains why a receivables analyst needs it at all:
every dollar of federal AR is conditional revenue, collectible only to the extent the
underlying costs were allowable, allocable, and documented to §200.302 standards. The
always-unallowable list isn't trivia — bad debts (§200.426) mean the normal commercial reflex
("reserve it, write it off against the account") is *prohibited* against federal awards, so
federal AR risk management has to work upstream, in billing timeliness and cost hygiene, not
downstream in write-offs. The thresholds matter because they set which machinery switches on
(a Single Audit at $1M of expenditures, equipment treatment at $10k, the 15% de minimis for
institutions without a negotiated rate), and dating them matters because the 2024 revision
means two awards side by side can run under different numbers. And the instrument distinction
(UG vs FAR) is the deepest gate: it decides which rulebook applies at all, which is why it's
step one and not a footnote.

## Common mistakes
- Treating this knowledge as authority → the regulation, NOA, and institutional policy govern; this is orientation, always disclaimed.
- Applying Uniform Guidance to a federal *contract* → FAR/CAS territory; classify the instrument first.
- Using post-2024 thresholds on older awards (or vice versa) → award terms control; date every threshold.
- Computing MTDC with full subaward values → only the first $50,000 of each subaward counts.
- Writing off federal AR as bad debt against the award → §200.426 prohibits it; the loss lands on institutional funds.
- Ignoring agency-specific rules → NIH GPS / NSF PAPPG can be stricter; check the agency layer.
- Forgetting that collected-then-disallowed costs must be refunded → §200.410; billed and collected is not final for federal AR.

## Tailor to your environment
Record your institution's federal posture in `references/your-environment.md` (award-level
specifics in `your-environment.private.md`, git-ignored): negotiated F&A rate vs de minimis,
your Single Audit status, institutional policy deltas stricter than UG, and your major agency
mix. **Never commit award numbers, NOA terms, or audit findings.**

## References
- references/ug-quick-tables.md — threshold table (dated), subpart map, unallowable-cost examples with citations
- references/your-environment.md — your rates, audit status, policy deltas, agency mix (fill in)
