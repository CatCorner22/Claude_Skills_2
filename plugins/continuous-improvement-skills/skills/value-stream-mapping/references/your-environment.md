# Your value stream (sanitized template)

Fill this in with your real process. If any value is sensitive (real vendor/customer names, account
numbers, internal system details), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Value stream / product family in scope:** <e.g. supplier invoices on standard terms; the monthly close>
- **Boundaries:** starts when <trigger>; ends when <done condition>.
- **SIPOC (high level):**
  - Suppliers → <who feeds the process>
  - Inputs → <what they feed in>
  - Process (5–7 steps) → <receive → … → deliver>
  - Outputs → <what comes out>
  - Customers → <who receives it>
- **Data-box sources:** where you pull CT, wait time, and %C&A <e.g. ERP posting timestamps,
  ticketing tool, approval-workflow logs, manual timing during a gemba walk>.
- **Volume / takt:** <items per day/week; available work time ÷ demand = takt, if you level to it>
- **Baseline metrics (current state):** lead time <…>; process time <…>; PCE <…%>; worst-%C&A step <…>.
- **Targets (future state):** lead time <…>; CT <…>; %C&A <…>.
- **Known waits / bottlenecks:** <e.g. approvals > $10k queue for 2 days; nightly batch cutoff>
- **Owner / cadence for re-mapping:** <who owns the map; how often you refresh it>
