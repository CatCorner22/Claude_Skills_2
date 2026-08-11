---
name: fusion-ar-ppm-domain-knowledge
description: >-
  Provides the authoritative public-domain map of how sponsored projects data flows between
  Oracle Fusion PPM/Grants and Receivables — award and bill-plan types, the relevant OTBI
  subject areas on both sides, the PPM-to-AutoInvoice-to-AR integration and status flow, and a
  data-profiling routine for any uploaded sponsored-AR extract, with the standard gotchas
  flagged. Use as the first analytical step after the sponsored-AR router, or whenever the
  question is about data sources, subject areas, terminology, or column mapping. Triggers:
  PPM subject area, project billing subject area, where does unbilled AR come from, AutoInvoice
  PPM, sponsored AR data model, map these columns, grants data source, project invoice flow,
  bill plan type, confirm invoice acceptance.
---

# Fusion AR + PPM domain knowledge for sponsored projects

## When to use
- First analytical step in any sponsored-AR engagement: establish terminology, sources, and a
  data profile before computing anything.
- Answering "where does this number come from," "which subject area has X," or mapping an
  uploaded extract's columns to Fusion concepts.
- Not for: the analysis itself → return to the router
  (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`) for dispatch. For
  general subject-area selection outside sponsored AR → see
  `oracle-otbi-skills:otbi-subject-area-selection`.

## Do it
1. **Confirm the award/bill-plan type first.** **Cost-reimbursable** = bill actual incurred
   expenses (invoice amounts follow cost collection; unbilled AR is expense-driven and grows
   with spend). **Fixed-price / milestone** = bill pre-set amounts on dates or events (unbilled
   is schedule-driven; spend and billing can legitimately diverge). Everything downstream —
   unbilled definitions, burn metrics, aging expectations — depends on this split.
2. **Map the question to the public OTBI subject areas.** Receivables side:
   **Receivables - Transactions Real Time** (invoice/CM headers and lines),
   **Receivables - Payment Schedules Real Time** (due dates, balances — the aging source),
   **Receivables - Revenue Real Time** (AR-side revenue), aging analyses off payment schedules.
   PPM side: **Projects - Invoices Real Time** (draft/approved project invoices),
   **Projects - Revenue Real Time** (recognized project revenue),
   **Projects - Funding Real Time** (award/contract funding). The bridge:
   **Project Billing - Bill Transactions Real Time** — WIP/unbilled transactions with the
   **billing status** attribute (Ready to Bill, In Progress, Billed, Error).
   `references/subject-area-map.md` carries the full map with typical columns per question.
3. **Know the integration flow cold** (it explains every status a user will ask about):
   invoices are **generated in PPM** from bill plans → transferred through the **AutoInvoice**
   interface into Receivables → **Confirm Invoice Acceptance** updates the PPM invoice status
   once AR accepts. **Unbilled AR** (expenses incurred / revenue recognized in PPM but not yet
   invoiced) transitions to **billed AR** only after that flow completes — an amount can be
   "revenue" in PPM and invisible in Receivables, legitimately, until then.
4. **Profile any uploaded data before analysis:** map each column to its Fusion concept (flag
   unmappable ones), check completeness (nulls in key fields: project, contract, sponsor,
   amounts, dates), establish the date range and as-of date, and confirm the filters it was
   extracted with (sponsor, BU, project range). Deliver the profile as a table; unresolved
   mappings become questions, not assumptions.
5. **Flag the standard gotchas on every engagement:** project/task attributes appear on AR
   lines **only if the contract's invoice grouping rule includes them** (absent ≠ missing —
   join to PPM data instead); aging metrics can be **invoice-date or schedule-date** based
   (label which); pipeline/aging data is only as fresh as the extract — recommend **daily
   incremental runs** where aging accuracy matters.
6. **Output:** a short glossary of the engagement's terms (as used *in this data*), the data
   profile table, and recommended filters for the analysis to follow — then route back for the
   actual analysis.

## Why / learn
The PPM→AR integration is a *handoff between two systems of record with different questions*:
PPM knows what work happened and what it's worth (costs, revenue, funding, by project/task/
award); Receivables knows what's been formally claimed and collected (invoices, due dates,
receipts, by customer). The billing status attribute is the conveyor belt between them, and
"unbilled AR" is simply inventory sitting on that belt — which is why it lives in the Project
Billing bridge area rather than in either endpoint. Most sponsored-AR confusion is a category
error across the seam: expecting project detail in AR data (it only crosses if the grouping
rule carries it), reading PPM revenue as a collectible balance (it isn't until AutoInvoice and
acceptance complete), or comparing an aging built on invoice dates with one built on due dates.
Profiling before analysis is the discipline that catches these early: a column map forces every
field to declare which side of the seam it came from, and the as-of date declares how stale the
belt snapshot is. Get the map right and the analyses downstream become arithmetic; get it wrong
and no amount of careful math rescues the answer.

## Common mistakes
- Treating PPM recognized revenue as billable/collectible AR → it's pre-invoice until AutoInvoice + acceptance complete.
- Expecting project/task columns in Receivables extracts → only present if the invoice grouping rule carries them; join to PPM instead.
- One "unbilled" definition across cost-reimbursable and milestone awards → expense-driven vs schedule-driven; segment first.
- Mixing invoice-date and schedule-date aging in one analysis → label the basis; never blend.
- Analyzing an extract without profiling it → unmapped columns and silent filters poison everything downstream.
- Assuming implementation-specific config (grouping rules, DFFs) → ask; only the documented public model is assumed.

## Tailor to your environment
Capture your instance's specifics in `references/your-environment.md` (real award/sponsor data
in `your-environment.private.md`, git-ignored): which subject areas your roles expose, your
standard extract definitions, which project attributes actually reach AR lines, and your
glossary deviations. **Never commit real award, sponsor, or balance data.**

## References
- references/subject-area-map.md — subject areas by question, typical columns, and the integration status flow
- references/your-environment.md — your extracts, attribute visibility, glossary (fill in)
