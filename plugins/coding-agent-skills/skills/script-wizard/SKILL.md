---
name: script-wizard
description: >-
  Plans, drafts, and audits substantial technical deliverables — scripts and modules,
  automation, AI system designs, documentation, specifications, and project plans — through
  a disciplined Frame → Diagnose → Design → Build → Audit → Refine workflow that front-loads
  thinking, scales to the task's consequence, and ends with an adversarial defect hunt
  before anything is presented. Use when asked to build, write, fix, review, scope, or
  improve any script, tool, document, or technical artifact of real substance — even when
  phrased casually ("write me a script", "draft this doc", "clean this up") — or to break a
  project into phases, audit a deliverable for defects, or stress-test a technical decision.
  Triggers: write a script, build a tool, draft a document, technical spec, project plan,
  review this code, clean this up, audit this, scope this project, break into phases,
  stress test, improve this process, script wizard.
metadata:
  version: "1.0"
  author: User-drafted workflow spec; adapted to house standard
---

# Script wizard

## When to use
- Building, fixing, reviewing, or improving any technical artifact of real substance: a
  script or module, an automation, a system design, a document someone will rely on, a
  plan with real dependencies — including casually-phrased requests.
- Breaking a project into phases, auditing a finished deliverable, or stress-testing a
  decision before committing to it.
- Not for: production-grade Python where the 2026 toolchain persona should drive → see
  `full-stack-dev-skills:elite-python-engineer` (this skill owns the *process*; that one
  owns Python *standards* — they compose). Authoring Agent Skills →
  `coding-agent-skills:writing-agent-skills`. A multi-agent adversarial review →
  `board-of-advisors-skills:board-review` (Phase 5 here is the lightweight solo version).

## Do it
1. **Scale the workflow to the task — by consequence, not length.** Run all six phases for
   substantial deliverables (multi-file tools, system designs, documents people rely on,
   plans with dependencies). Compress hard for small ones: for a ten-line utility, Phases
   1–3 collapse into one sentence ("Reads the CSV, dedupes on email, writes a new file;
   assumes UTF-8 and a header row") and you go straight to building. A short script that
   touches production data or feeds a financial report gets the full treatment; a long
   document nobody acts on does not. The one compression that rarely pays is skipping the
   audit — small artifacts have edge cases too.
2. **Frame.** Establish what "done" means before touching the artifact: the **objective**
   as an outcome, not a task ("reconcile the bank feed" beats "write a Python script");
   **users and stakeholders** (who runs it, consumes it, approves it); **constraints**
   (environment, dependencies, data access, deadlines, formats); **success criteria**
   that are checkable. State assumptions out loud — unstated assumptions are the raw
   material of rework.
3. **Diagnose.** Find what will break before building: ambiguities that admit two readings;
   hidden assumptions about data shape, volume, encoding, availability; dependencies you
   don't control and what happens when they fail; edge cases (empty input, malformed rows,
   duplicates, nulls, unexpected scale); failure modes in the surrounding process, not
   just the artifact. Separate symptoms from root causes — if a script must clear
   duplicates weekly, something upstream is creating them; say so, then build what was
   asked.
4. **Design.** Propose structure before producing in full — code: modules, interfaces,
   data flow, error-handling strategy; documents: an outline stating each section's
   purpose; projects: workstreams, sequence, dependencies, decision points. Show the
   design when a wrong structure would be expensive to unwind.
5. **Build** on the designed structure. Keep it internally consistent: one term per
   concept, parallel structure for parallel elements, names that reveal intent. Record why
   non-obvious choices were made. Apply the standards reference that fits the deliverable
   (table in References).
6. **Audit — adversarially, before presenting.** Building and critiquing use different
   attention; this phase catches what the building mindset cannot. Work through
   `references/audit-checklist.md`; at minimum ask what breaks, what could be misread,
   which dependency is fragile, and what a skeptical expert attacks first.
7. **Refine.** Fix what the audit found, tighten the language, cut what isn't earning its
   place, strengthen thin sections — then present.
8. **Present in the response architecture** (unless asked otherwise): direct answer first →
   key assumptions → approach (when the method matters) → the artifact → risks and open
   issues → next decisions for the user.
9. **Handle ambiguity without silent guessing.** Name what's missing; infer only where the
   inference is low-risk and say you inferred it; put strategic choices (architecture,
   scope, real tradeoffs) to the user; proceed on a flagged, justified default when waiting
   would stall the work. When several paths are valid, recommend one and name the tradeoff.

## Why / learn
The most common failure in technical work is not incompetence — it is producing a competent
artifact that answers the wrong question, or one that runs on the happy path and breaks on
everything else. Both come from drafting before thinking, which is why the workflow
front-loads Frame and Diagnose: ten minutes of framing almost always costs less than a
rewrite. The Audit phase exists for a different cognitive reason — building and critiquing
use different attention, so the defects your building mindset created are largely invisible
to it; switching deliberately into adversarial review is what surfaces them. Leading with
the answer matters because burying a recommendation under preamble transfers your work to
the reader; and recommending one path (with the tradeoff named) rather than presenting a
survey matters because options without a recommendation push the decision back onto the
user, which is the opposite of help. Finally, calibration is a deliverable property:
presenting an untested artifact as verified is the hardest defect for a user to detect, so
say plainly what was tested, what was inferred, and what remains unknown.

## Common mistakes
- Drafting before framing → a polished answer to the wrong question. Frame first, briefly.
- Skipping the audit because the artifact is small → small artifacts still have edge cases.
- Running six ceremonial phases on a trivial request → buries the answer; scale by consequence.
- Presenting options without a recommendation → returns the work to the user. Recommend and
  name the tradeoff.
- Guessing silently on an underspecified request → name the gap, flag the default you chose.
- Claiming "tested/verified" for work that wasn't → say exactly what was and wasn't exercised.
- Fixing the symptom while ignoring the root cause you spotted → build what was asked AND
  say what's upstream.

## Tailor to your environment
Record your recurring deliverable types and their standards in
`references/your-environment.md`: the scripts you build most (e.g. reconciliation tooling,
Oracle data pulls), house documentation formats, review/approval gates, and the systems
artifacts must integrate with. Keep anything sensitive in `your-environment.private.md`
(git-ignored); never commit real data.

## References
- references/audit-checklist.md — the Phase 5 adversarial review, in full (use on every audit)
- references/python-and-code.md — standards for scripts, tools, automation, AI systems
- references/writing-and-drafting.md — standards for documentation, prose, specifications, and contract language (incl. MSCD drafting discipline and the four ambiguity types)
- references/process-and-stakeholders.md — standards for process improvement and project scoping
- references/your-environment.md — your deliverable types, formats, and gates (add when supplied)
