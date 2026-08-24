# Your value stream (sanitized template)

Wire in your current role here. The method is domain-neutral by design — it maps an
analyst's request stream, an attorney's intake-to-filing pipeline, an ops manager's
order-to-delivery flow, or a developer's commit-to-deploy path equally well, and it moves
with you to the next job. Keep this committed file **structural**: stream kinds, metric
sources, and cadences. Real vendor/customer names, account numbers, or internal system
detail belong in `your-environment.private.md` — that suffix is git-ignored and never
committed.

- **Value stream / product family in scope:** <e.g. standard requests of one type; one recurring pipeline>
- **Boundaries:** starts when <trigger>; ends when <done condition>.
- **SIPOC (high level):**
  - Suppliers → <who feeds the process>
  - Inputs → <what they feed in>
  - Process (5–7 steps) → <receive → … → deliver>
  - Outputs → <what comes out>
  - Customers → <who receives it>
- **Data-box sources:** where you pull CT, wait time, and %C&A <e.g. system timestamps,
  ticketing tool, approval-workflow logs, manual timing during the walk>.
- **Volume / takt:** <items per day/week; available work time ÷ demand = takt, if you level to it>
- **Baseline metrics (current state):** lead time <…>; process time <…>; flow efficiency <…%>; worst-%C&A step <…>.
- **Targets (future state):** lead time <…>; CT <…>; %C&A <…>.
- **Known waits / bottlenecks:** <e.g. approvals above a threshold queue for days; a nightly batch cutoff; one reviewer>
- **Owner / cadence for re-mapping:** <who owns the map; how often you re-walk and re-measure it>
