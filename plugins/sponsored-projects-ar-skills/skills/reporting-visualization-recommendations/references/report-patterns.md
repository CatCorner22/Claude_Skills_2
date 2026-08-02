# Sponsored-AR report patterns (reference)

Durable OTBI-style specs. Build mechanics: `oracle-otbi-skills:otbi-report-building`;
scheduling/delivery: `oracle-otbi-skills:otbi-report-scheduling-sharing`.

## Contents
- The five standing reports
- Visual-choice guide
- Recommendation format

## The five standing reports
**1. AR Aging by Project/Sponsor**
- Area: Receivables - Payment Schedules Real Time
- Columns: sponsor (customer), project/contract (if grouping rule exposes; else join offline),
  transaction number/date, due date, balance due, CASE aging bucket
- Prompts: as-of date, sponsor category, BU; label aging basis in the title
- Cadence: weekly to collections, monthly to leadership

**2. Project Invoices Prior to Acceptance**
- Area: Projects - Invoices Real Time
- Columns: contract, project, invoice number, PPM status, generation date, days since
  generation, amount
- Filter: status not yet accepted in AR — this is the generate-to-accept gap
- Cadence: daily during close; weekly otherwise

**3. Unbilled Pipeline by Status**
- Area: Project Billing - Bill Transactions Real Time
- Columns: billing status (Ready to Bill / In Progress / Error), contract, project, amount,
  transaction date, age
- Views: status × sponsor matrix + aged Ready-to-Bill detail
- Cadence: daily incremental run recommended for accuracy

**4. Exception / Error Queue**
- Area: bill transactions filtered to Error + billing-exception patterns
- Columns: reason, contract, amount, age, fix owner (mapped from reason)
- Cadence: daily to the owning teams; trend of queue size + oldest age to management

**5. Award Close-out Exposure**
- Areas: Projects - Funding (end dates) + unbilled pipeline + open AR
- Columns: award/contract, end date, days remaining, unbilled amount, open billed AR,
  total exposure
- Filter: awards ending within 90/120 days
- Cadence: monthly; this is the "money that expires" report

## Visual-choice guide
| Question | Visual |
|---|---|
| Composition of AR by bucket/sponsor | Stacked bar (one bar per segment) |
| Trend of a metric | Line, 12–24 points, YoY overlay where seasonal |
| Ranking (worst sponsors/projects) | Sorted horizontal bar, top N + "other" |
| Flow unbilled → billed → collected | Waterfall |
| Two-metric tension (burn vs billing) | Dual line or scatter by contract |
Describe visuals in words precise enough to build: data, mark type, axes, series, sort, and
the one takeaway the chart must show.

## Recommendation format
| Recommendation | Owner | First step | When | Evidence (table/figure) | Expected effect |
|---|---|---|---|---|---|
Rank collection actions by amount × age × sponsor-risk; rank process actions by queue size ×
age trend. Cap the list at what the owners can actually do before the next report.
