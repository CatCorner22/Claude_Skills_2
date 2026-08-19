---
name: ui-and-ux-inspection
description: >-
  Inspects a bespoke web application for usability, cognitive-load, accessibility,
  interaction, workflow, performance, and privacy defects — tracing critical user
  processes backward from successful end states, separating observed evidence from
  inference, and producing reproducible severity- and confidence-rated findings with
  affected routes, remediation, and verification tests (a ui-ux-inspection.md report
  plus machine-readable ui-ux-findings.json). Use when the user asks to inspect or
  audit a web interface; review its UX, UI, forms, navigation, tables, or cognitive
  load; simplify a workflow; analyze screenshots or routes; generate Playwright or
  accessibility tests; compare an implementation with design heuristics; or create a
  remediation backlog. Triggers: inspect the UI, UX audit, usability review,
  accessibility audit, cognitive load, form review, navigation review, simplify a
  workflow, remediation backlog, playwright accessibility tests, heuristic evaluation.
metadata:
  version: "1.2.0"
  source: >-
    Adapted from the user's ui-and-ux-inspection spec (2026-08-04), itself distilled
    from their report 'Eye Tracking, Web-App Usability, and Cognitive Design'; the
    human-factors instruments (Fitts, NASA-TLX) carry [snippet-only] provenance marks
    in references/human-factors-instruments.md.
---

# UI and UX Inspection

## When to use
- Inspecting or auditing an existing web interface — UX, UI, forms, navigation, tables,
  accessibility, or cognitive load.
- Simplifying a workflow; analyzing screenshots or routes; generating Playwright or
  accessibility tests; comparing an implementation with design heuristics; creating a
  remediation backlog.
- Not for: building a new accessible UI or design system from scratch → see
  `continuous-improvement-skills:lean-six-sigma-for-software` (and its
  references/accessible-ui-design-system.md). Syncing UI vocabulary to a reference product → the
  worked method lives in an archived design-language skill for one dense clinical-SaaS product,
  restorable from `archive/skills/`.

## Do it
The full step-by-step procedure is preserved verbatim in references/procedure.md — read it
before a real inspection. The operational shape:

1. **Preflight and authorization.** Read the repo's docs; confirm report-only vs
   write permission; identify commands that are safe to run. Never connect to production,
   submit real transactions, send messages, delete data, or alter accounts unless
   explicitly authorized. Use test fixtures and least-privilege accounts; detect and
   redact secrets from logs and screenshots; record unavailable inputs as scope limits.
2. **Build an interface inventory.** Identify framework, router, design system, form
   library, state management, API client, auth flow, testing tools, analytics hooks.
   Enumerate routes, layouts/navigation, forms, tables, dialogs, menus, notifications,
   loading/empty/error/permission states, destructive actions, onboarding gates. Map
   shared components to consuming routes; flag one-offs that duplicate the design system.
3. **Define critical user outcomes** as observable end states — "the user submits a valid
   reimbursement request and receives a trackable reference," never "the user visits the
   dashboard" or "clicks submit."
4. **Trace each process backward** from its successful end state: list the minimum
   information, authorization, and commitment required and the latest safe point each is
   needed; mark every current step essential / inferable / reusable / deferrable /
   mergeable / removable / risk control; count screens, modals, decisions, required
   fields, repeated entries, waits, confirmations; propose a shorter path that preserves
   security, legal, financial, and accessibility requirements; draw current-vs-proposed
   Mermaid flows. State that step reductions are proposals until measured.
5. **Run the inspection passes** (checklists verbatim in references/procedure.md):
   visual hierarchy and scanability (an attention proxy — never call a static check eye
   tracking), Gestalt grouping, choices and progressive disclosure, affordances and
   signifiers, navigation and mental models, forms (the 20-point field checklist),
   feedback/state/recovery (test slow, failed, duplicate, out-of-order responses),
   tables/filters/search, onboarding and engagement, accessibility (WCAG 2.2 AA default;
   automated checks plus the manual checks — the spec's thirteen, plus the three WCAG 2.2
   additions in the house addendum in references/procedure.md: focus not obscured by sticky
   chrome, a single-pointer alternative to every drag, and consistently placed help; automated
   success does not prove accessibility), responsive and environmental behavior (320–1440 px
   widths, zoom, reduced motion, offline, stale edits), performance (INP/LCP/CLS with p75 budgets;
   Lighthouse is a diagnostic, not the only measure), and privacy. Quantify tap-target
   and pointing findings with Fitts's index of difficulty (computed from DOM geometry —
   report `D`, `W`, and current-vs-proposed ID), and structure the cognitive-load pass
   with the six NASA-TLX subscales so each flag names its driver — both per
   references/human-factors-instruments.md, as design-heuristic proxies: the geometry is
   observed evidence; predicted movement time or workload is inference, capped at
   `medium` confidence.
6. **Write the automated test plan.** Detect the existing package manager and test
   framework first; prefer Playwright, `@axe-core/playwright`, and Lighthouse (CI) when
   compatible. Generate task-level tests, not only page-load tests: keyboard-only
   critical path, values survive server validation failure, one mutation per Save despite
   repeated activation, dialog focus trap and restore, filter persistence, undo of
   destructive actions. Where automated evidence is insufficient, pose focused
   human-validation prompts rather than asserting a conclusion.
7. **Produce the two artifacts.**
   - `ui-ux-inspection.md` — executive summary; scope and limitations; critical findings;
     workflow analysis; accessibility, performance, and privacy results; prioritized
     remediation plan; test plan.
   - `ui-ux-findings.json` — machine-readable findings per the schema in
     references/finding-schema.md: each finding carries id, title, category, severity,
     confidence, status, routes, user_process, affected_users, evidence_type,
     observed_evidence, user_impact, heuristics, standards, reproduction, remediation,
     verification, estimated_effort, dependencies, privacy_notes.
   Map each finding to the smallest effective remedy using
   references/remediation-patterns.md. Optional, only when authorized: test files,
   Lighthouse reports, sanitized screenshots, route inventory, code patches, flow diagrams.

**Ground rules — the spec's ethical spine, in force on every run:**
- Distinguish observed evidence from inference; every finding states which it rests on.
- Never claim that automated inspection proves usability.
- Prohibited assumptions — never infer: citizenship or nativity; disability; age; gender;
  race or ethnicity; literacy; medical status; intent to consent; production
  authorization; permission to retain screenshots or telemetry.
- Eye-tracking mode is optional and disabled by default. Never activate a webcam or eye
  tracker without explicit informed consent, an approved protocol, a stated purpose, a
  data-minimization plan, a retention/deletion schedule, access controls, legal and
  privacy review, and an alternative for people who decline (full protocol in
  references/procedure.md).
- No production personal data in screenshots; redact secrets and identifiers. Flag
  jurisdiction-dependent biometric/privacy questions for qualified review — never give a
  categorical legal conclusion.

## Why / learn
Screen-by-screen review grades surfaces; users experience processes. Tracing backward from
the successful end state exposes what each step actually contributes — the minimum
information, authorization, and commitment the outcome requires — so steps that contribute
nothing become visibly deferrable or removable, while genuine risk controls are kept and
moved to the latest safe point instead of being flattened along with the friction.
Separating observed evidence from inference, and rating every finding for both severity and
confidence, is what turns a report into a workable backlog: engineers can rank by impact,
discount low-confidence items, and re-verify any finding from its reproduction steps — a
finding without evidence and a verification test is just an opinion. And native semantics
beat custom controls because the platform ships keyboard behavior, focus management, state
exposure, and the assistive-technology contract for free; a custom widget must re-earn all
of that and tends to fail silently for exactly the users least able to report it.

## Common mistakes
- Calling a static hierarchy check "eye tracking" → label it an attention or scanability
  proxy; real gaze data requires the consented, off-by-default eye-tracking mode.
- Page-load-only tests → generate task-level tests that complete, break, and recover the
  critical path.
- Treating Lighthouse as the performance verdict → it is a lab diagnostic; prefer
  real-user p75 distributions (INP/LCP/CLS) for production decisions.
- Reporting Fitts/TLX-derived numbers as user data → the ID is measured geometry, but
  movement-time and workload claims are model/rubric inference; label them so and keep
  them out of `observed_evidence`.
- Asserting usability from automated evidence → automation finds defects; pose
  human-validation prompts for what only humans can confirm.
- Collecting biometric, webcam, production-analytics, or personal data without explicit
  authorization → prohibited; record purpose, basis, retention, and opt-out for any
  collection you do find.
- Inferring demographics (nativity, disability, age, gender, race, literacy) from behavior
  or appearance → prohibited; if a study needs them, use an optional direct screener with
  an explicit definition.

## Tailor to your environment
Fill in references/your-environment.md: target routes, critical processes written as
outcomes, test-account policy, browser matrix, performance budgets, and the default
write_permission. Real URLs, credential procedures, or client specifics belong in
references/your-environment.private.md — git-ignored, never committed.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/ui-and-ux-inspection.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/procedure.md — the full inspection procedure, verbatim from the source spec
  (preflight → privacy inspection)
- references/remediation-patterns.md — the ten remediation pattern groups, verbatim
- references/finding-schema.md — canonical JSON schema for ui-ux-findings.json
- references/human-factors-instruments.md — Fitts's law and NASA-TLX as design-heuristic
  instruments for tap-target and cognitive-load findings: the math, administration
  discipline, finding-schema mapping, and honest limits
- references/your-environment.md — fill-in: routes, processes, accounts, browsers, budgets
