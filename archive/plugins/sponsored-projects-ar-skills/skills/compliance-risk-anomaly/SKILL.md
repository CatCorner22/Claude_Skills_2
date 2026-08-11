---
name: compliance-risk-anomaly
description: >-
  Identifies compliance risks, exceptions, and anomalies in sponsored/grant receivables data
  across all sponsor types — scanning the public exception patterns (billing exceptions, holds,
  unapplied receipts, at-risk receipts in aging data), the sponsored-specific risks
  (allowability-suspect charges, funding-limit breaches, overdue-beyond-sponsor-terms), and
  statistical anomalies (outlier aging, DSO spikes, unusual adjustment and credit-memo
  volumes), then cross-checking PPM costs against AR billing for alignment. Use for audit-,
  risk-, or exception-focused questions on sponsored AR. Triggers: sponsored AR exceptions,
  grant AR anomalies, billing exceptions scan, risk register receivables, unusual credit memos,
  DSO spike, funding limit breach, overdue beyond terms, AR risk review, exception report
  grants, at-risk receipts.
---

# Sponsored-AR compliance risk and anomaly detection

## When to use
- Audit-, risk-, or exception-focused review of sponsored/grant AR data for **any sponsor
  type** (federal, state, foundation, industry): what's broken, what's weird, what's exposed.
- Building or refreshing a sponsored-AR risk register.
- Not for: the federal-specific rulebook and write-off/questioned-cost treatment → see
  `sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk` (route federal awards
  there after this scan). Item-level allowability verdicts →
  `sponsored-projects-ar-skills:federal-cost-allowability`. Serious anomaly-detection
  modeling → `machine-learning-skills:anomaly-detection`. Enter via the router
  (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Scan the public exception patterns first** — the ones Fusion's own data structures
   surface: **billing exceptions** and Error-status transactions (the stuck pipeline —
   `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon` owns the deep dive), **holds**
   (contract/billing holds aging quietly), **unapplied receipts** (cash on the books, not on
   invoices), and **at-risk receipts** — disputed, in-collections, or flagged items in
   aging/payment-schedule data. Each is a queue: report count, amount, and age, not just
   existence.
2. **Layer the sponsored-specific risks:**
   - **Allowability-suspect charges** — filter billed costs by project/task attributes for
     categories that fail sponsor terms (route items to
     `sponsored-projects-ar-skills:federal-cost-allowability` for verdicts on federal awards).
   - **Funding-limit breaches** — billed or billable amounts approaching/exceeding award
     funding (Projects - Funding concepts): over-funding billing gets rejected or clawed back.
   - **Overdue beyond sponsor terms** — age receivables against *each sponsor's* payment
     terms, not a generic 30 days; a foundation on 60-day terms isn't late at day 45, a
     sponsor at 2× its terms is a relationship or compliance signal whatever the absolute age.
3. **Run the anomaly pass — yesterday's normal is the baseline:**
   - **Outlier aging** — accounts/awards whose aging profile sits far from their segment's
     (z-score or percentile against the sponsor-category distribution).
   - **DSO spikes** — sudden movement vs the trend (distinguish mix shift from behavior
     change; the KPI skill's decomposition applies).
   - **Adjustment and credit-memo volume** — sudden spikes by preparer, project, or sponsor;
     rising churn is the classic early sign of billing-quality or override problems.
   - Keep methods proportional: rules and z-scores here; hand persistent or subtle patterns
     to `machine-learning-skills:anomaly-detection`. `references/anomaly-playbook.md` has the
     thresholds, formulas, and the risk-register format.
4. **Cross-pillar check: PPM costs vs AR billing.** By award, compare cost categories
   incurred (PPM) with what was billed (AR): billed > allowable-cost base suggests unallowable
   or premature billing; billed ≪ costs suggests unbilled leakage (the recon skill); category
   mismatches (billing travel where no travel cost exists) are the audit-grade anomalies.
5. **Assemble the risk register.** One row per finding: risk description, category
   (exception / sponsored-specific / anomaly / cross-pillar), affected awards/sponsors, dollar
   exposure, likelihood, age/trend, owner, and mitigation. Prioritize by exposure ×
   likelihood × documentation weakness — and separate *conditions* (things wrong now) from
   *indicators* (things trending wrong).
6. **Deliver:** risk register + prioritized exceptions (top N with the math shown) +
   mitigation suggestions per finding (process fix, documentation, escalation) — in the
   router's standard structure, dated, with federal items explicitly routed onward to the
   federal risk skill for regulatory treatment.

## Why / learn
Exception scanning and anomaly detection answer two different questions and this skill
deliberately runs both: exceptions are *known-bad states the system already labels* (an Error
transaction, a hold, an unapplied receipt) — finding them is enumeration, and the discipline
is measuring their age and trend rather than tolerating them as furniture. Anomalies are
*deviations from your own baseline* that no rule anticipated — a DSO spike, a credit-memo
surge — and the discipline there is having a baseline at all (segment norms, trend history)
so "unusual" is a computation, not a feeling. The sponsored layer exists because grant AR has
risk vectors commercial AR lacks: awards have funding ceilings (a hard billing boundary),
sponsor-specific terms (making one aging yardstick wrong by construction), and allowability
rules that make *what* you billed as important as *whether* it's paid. The cross-pillar check
is the deepest test because it compares two systems that should agree but are maintained by
different teams — PPM's account of what happened vs AR's account of what was claimed — and
divergence between them is where both honest leakage and real trouble first become visible.
A risk register, finally, turns all of it from a review into a managed artifact: findings
with owners and trends survive; findings in a slide deck evaporate.

## Common mistakes
- Reporting exceptions as counts without age/trend → an old stable queue and a growing one need different responses.
- One aging yardstick for all sponsors → age against each sponsor's terms; "overdue" is contractual, not universal.
- Anomaly detection without segment baselines → everything (or nothing) looks unusual; compute norms per sponsor category first.
- Reading a DSO spike as behavior before checking mix → the KPI skill's decomposition first; mix shifts mimic trouble.
- Ignoring credit-memo/adjustment churn because net AR looks fine → churn is the leading indicator; net hides it.
- Skipping the cross-pillar check → single-system review misses exactly the misalignments audits find.
- Treating federal awards like the rest of the register → route them to the federal risk skill; the rules (write-offs, refunds) differ categorically.
- A risk register without owners → findings without owners are observations; assign or don't bother.

## Tailor to your environment
Record your risk baseline in `references/your-environment.md` (findings and award data in
`your-environment.private.md`, git-ignored): sponsor payment terms by category, your normal
exception-queue levels, anomaly thresholds tuned to your volumes, and the register's owners
and review cadence. **Never commit real findings, sponsor names, or balances.**

## References
- references/anomaly-playbook.md — exception queue formats, anomaly thresholds/formulas, cross-pillar worksheet, risk-register template
- references/your-environment.md — your terms, baselines, thresholds, owners (fill in)
