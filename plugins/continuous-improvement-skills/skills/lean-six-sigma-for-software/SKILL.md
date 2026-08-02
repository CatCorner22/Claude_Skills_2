---
name: lean-six-sigma-for-software
description: >-
  Runs software projects as Lean Six Sigma operations — Deming's standardize-and-measure
  discipline (PDSA, variation, quality built in), Toyota Production System practice (jidoka,
  andon, poka-yoke, standard work) translated to code and pipelines, DMAIC/DMADV with
  begin-with-the-end-in-mind backward design, co-design with real users, and hybrid project
  management — then builds to a full-stack standard: UI vocabulary and patterns synced to a
  reference product (Curve Hero design language included), beautiful WCAG 2.2 AA accessible
  design, stability and redundancy engineering, and adversarial testing before release. Use
  when building or improving software with lean/six sigma rigor, or making an app feel native
  to Curve Hero users. Triggers: lean six sigma software, DMAIC software, Toyota production
  system, Deming, PDSA, standardize and measure, begin with the end in mind, curve hero,
  adversarial testing, accessible UI, WCAG, stability redundancy, co-design.
---

# Lean Six Sigma for software

## When to use
- Building a new application or feature with end-to-end rigor: defined end state, co-designed
  UI, measured delivery, adversarially tested, controlled after release.
- Improving an existing software process (slow releases, defect leakage, abandoned features)
  with DMAIC instead of vibes.
- Making a product's UI feel native to users of a reference product — vocabulary, fields, and
  patterns synced (Curve Hero support built in: `references/curve-hero-design-language.md`).
- Installing engineering standards: accessibility, stability/redundancy, full-stack quality
  gates, adversarial test gauntlets.
- Not for: facilitating the improvement workshop itself →
  `continuous-improvement-skills:kaizen-and-codesign`; generic DMAIC on non-software processes
  → `continuous-improvement-skills:dmaic-problem-solving`; pure code-level minimalism →
  `full-stack-dev-skills:lean-code-principles`; deep single-layer builds → the
  `full-stack-dev-skills` skill for that layer.

## Do it
1. **Begin with the end in mind — define the end state first.** Write the destination as
   verifiable statements before any design: who uses it, the outcome it must produce, and the
   measurable definition of "working" (CTQs, SLOs, task-success rate, WCAG 2.2 AA
   conformance). Charter it on one page: quantified problem/opportunity, scope and
   out-of-scope, sponsor, timebox, top risks. Choose the method: improving something that
   exists → DMAIC; designing something new → DMADV. Both in
   `references/dmaic-codesign-and-pm.md`.
2. **Go to the gemba and co-design with the real users.** Watch the actual doers work in the
   current tool before mocking anything; harvest their vocabulary — their words become your
   labels. Design with them (paper mocks they mark up, rapid prototype PDSA loops), verify by
   watching task completion, and keep them as the standing panel after ship. Method in
   `references/dmaic-codesign-and-pm.md` §5.
3. **Sync the UI to the reference product.** When the software must feel native to users of an
   existing product, run the sync audit: inventory that product's modules, screen names, field
   labels, statuses, and phrases; build a terminology map (their term → your screen); mirror
   interaction patterns users already know; and keep one term per concept everywhere. The
   Curve Hero design language — modules like the Sidekick and Scheduler, its field and
   workflow vocabulary, and its cloud practice-management patterns — is pre-mapped in
   `references/curve-hero-design-language.md` with provenance caveats.
4. **Design beautiful, accessible, dense-but-calm UI from tokens.** Build on the design system
   in `references/accessible-ui-design-system.md`: token-driven color/type/spacing, WCAG 2.2
   AA engineered in (contrast, focus, keyboard, target size, redundant-entry elimination),
   card-on-canvas density for all-day professional use, and forms that never lose work.
   Accessibility checks run as blocking CI gates — jidoka, not audit theater.
5. **Build to standard work.** The full-stack standard in
   `references/full-stack-standards.md`: strict types end to end (poka-yoke), contract-first
   APIs, constraint-enforcing database, golden-path templates, 12-factor config, observability
   wired from day one. Deviations get an ADR — that's kaizen input. Depth per layer:
   `full-stack-dev-skills:*`.
6. **Measure the process while you build.** Instrument the value stream (lead time, deploy
   frequency, change failure rate, defect escape rate) and control-chart it; distinguish
   special-cause signals from common-cause noise before reacting (Deming's two mistakes —
   `references/deming-and-tps.md` §4). Every improvement is a PDSA cycle with a stated
   prediction. Metrics judge the process, never the people.
7. **Run the adversarial gauntlet before release.** Property-based tests on the algorithmic
   core, fuzz every parser and API surface, mutation-test the critical module, inject faults
   at every external seam, STRIDE the design, and sweep the UI with hostile input (O'Brien,
   Feb 29, the 2 GB "CSV"). Full playbook and pre-release checklist in
   `references/adversarial-testing.md`.
8. **Engineer stability and redundancy to the SLO.** Timeouts, retries with jitter, idempotency
   keys, circuit breakers, queues as shock absorbers; layered redundancy from tested backups
   up to multi-AZ as the error budget justifies — and no further (excess redundancy is muda);
   deploy ≠ release (flags, canaries, rehearsed rollback); degrade honestly. Patterns in
   `references/stability-and-redundancy.md`. Verify the claims with fault injection — an
   untested failover is scenery.
9. **Standardize, control, and hand the gains a guardian.** Update the golden path and
   standard work with what the project learned; automate the new checks in CI; leave a control
   plan (chart, owner, response rule) on both the delivery metrics and the runtime SLOs; run
   the retrospective as kaizen and schedule the 30/60-day follow-up. Improvement without
   control is a temporary donation to entropy.

## Why / learn
Deming's core insight makes this one discipline rather than two: **quality comes from the
system, not from inspection or heroics** — so you improve outcomes by standardizing the method,
measuring its variation, and changing the system when the data says so. Software is unusually
lucky here: its "machines" (CI, types, linters, flags) can enforce standards automatically
(jidoka), its production line can be observed in real time (telemetry is the gemba), and its
experiments are cheap (a canary is a PDSA cycle with a rollback). TPS supplies the mechanics —
stop-the-line on defects, small batches, WIP limits, mistake-proofing — and each maps one-to-one
onto modern delivery practice, which is no accident: DevOps is lean manufacturing rediscovered.
Backward design ("begin with the end in mind" — Covey's phrase; DMADV's Define phase in
practice) is what keeps the build honest: a defined, measurable end state converts scope
debates into muda detection and converts "done" from a feeling into a test. Co-design and
UI-vocabulary sync are the same principle applied to interfaces: the people who do the work
hold the knowledge, so their words and workflows are the spec — an app that speaks the user's
language (the language their current tool taught them) has near-zero translation cost, and
translation cost is cognitive waste paid on every click, all day. Accessibility rides the same
logic — WCAG conformance engineered in as tokens, gates, and primitives costs a fraction of
retrofit and produces the calm, legible, keyboard-fast UI that expert users call "beautiful."
Adversarial testing is Deming's "cease dependence on inspection" taken seriously: you can't
inspect quality in at the end, but you *can* attack your own system early enough that the
attack is construction. And stability engineering is the Swiss-cheese model in code — layered,
imperfect, independent defenses, sized by an error budget so reliability spending stops where
the promise is kept. The through-line: standardize so you can measure, measure so you can
improve, improve so the standard rises — forever.

## Common mistakes
- Starting from a solution ("rewrite it in X") instead of a defined end state → DMADV's
  Define phase exists to prevent exactly this; write the acceptance test first.
- Reacting to every metric blip or incident with process changes → tampering (Deming's
  funnel); check the control chart before "fixing" noise.
- Co-design with managers as proxies for users → you inherit a proxy's guesses; recruit the
  actual doers.
- Syncing UI vocabulary in some screens but not others → one term per concept, everywhere;
  a half-synced app is more confusing than an unsynced one.
- Treating accessibility as a pre-launch audit → retrofit costs 5–10×; tokens, primitives,
  and CI gates from day one.
- Skipping the adversarial pass because "tests are green" → green tests prove intended
  behavior on expected input; adversaries don't send expected input.
- Redundancy as gold-plating (multi-region for an internal tool) → size reliability to the
  SLO; beyond it is muda.
- Shipping the improvement without a control plan → the gain evaporates; standardize,
  automate the check, assign the chart an owner.
- Measuring people instead of the process → red beads; gamed metrics and hidden problems.

## Tailor to your environment
Fill `references/your-environment.md` with your reference product (Curve Hero or another),
your value-stream baseline and where its control charts live, your stack and golden path,
your co-design panel, your SLOs and redundancy tier, and your adversarial cadence. Keep
anything sensitive in `your-environment.private.md` (git-ignored); never commit real client
or patient data.

## References
- references/deming-and-tps.md — Deming's system (SoPK, PDSA, variation, the points that matter) and the TPS→software translation table
- references/dmaic-codesign-and-pm.md — DMAIC/DMADV for software, CTQs and delivery metrics, co-design method, hybrid PM artifacts
- references/curve-hero-design-language.md — Curve Hero's modules, vocabulary, and patterns; the UI sync-audit method for any reference product
- references/accessible-ui-design-system.md — tokens, WCAG 2.2 AA engineering, density, forms, components, testing checklist
- references/full-stack-standards.md — the advanced-but-well-accepted stack as standard work, with Definition of Done
- references/adversarial-testing.md — property-based, fuzzing, mutation, chaos, STRIDE, hostile-UX sweep, the gauntlet checklist
- references/stability-and-redundancy.md — SLOs/error budgets, seam patterns, data integrity, redundancy layers, release safety
- references/your-environment.md — your reference product, baselines, stack, panel, SLOs (fill in)
