# Evals — sponsored-projects-ar-skills:compliance-risk-anomaly

## 1. Positive trigger (should load the skill)
> "Do a risk sweep of our sponsored AR — I want to know about exceptions, anything unusual in
> the aging or adjustments, and whether any awards are billing close to their funding limits.
> Mix of federal, foundation, and industry sponsors."

Expected: skill loads; runs the exception queues (errors, holds, unapplied, at-risk) with age
and trend; ages receivables against sponsor-specific terms; anomaly pass with segment
baselines (outlier aging, DSO spike with mix decomposition, credit-memo churn); funding-limit
proximity check; cross-pillar PPM-vs-AR comparison; delivers a prioritized risk register with
owners, routing federal items onward to the federal risk skill.

## 2. Near-miss (should NOT load this skill)
> "Can we write off this uncollectible NIH receivable, and what does that mean for our Single
> Audit?"

Expected: federal-specific treatment —
`sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk`. If this skill loads
instead, sharpen the general-scan vs federal-rulebook split.

## 3. Quality rubric
A good response:
- **Does the task:** all four scan layers run (exceptions, sponsored-specific, anomalies,
  cross-pillar), register assembled with exposure math, owners, and mitigations.
- **Teaches:** exceptions-vs-anomalies as different questions (enumeration vs baseline
  deviation), sponsor-terms-relative aging, and why the cross-pillar check catches what
  single-system review misses.
- **Safe:** baselines before anomaly claims, mix checked before behavior claims, federal items
  routed to the federal skill rather than treated generically, no real sponsor data committed.
