---
name: fusion-architect-consult
description: >-
  Consults the fusion-treasury-architect subagent — an elite Oracle Cloud Fusion Financials
  and Treasury architect persona — for expert, configuration-specific answers: exact FSM task
  names and Redwood UI navigation, COA/value-set/CVR design, SLA mapping and journal line
  rules, bank statement parsing (BAI2/CAMT.053/MT940 with segment-level detail),
  reconciliation rule sets and tolerances, AutoInvoice/lockbox/PPR configuration, and
  structured error troubleshooting (root cause → diagnostics → resolution). Use for deep
  Fusion configuration design, integration architecture, or error diagnosis beyond the
  teaching skills. Triggers: fusion configuration, FSM task, redwood navigation, configure
  SLA, CVR design, BAI2 parsing rule, reconciliation rule setup, AutoInvoice grouping rule,
  PPR setup, fusion error troubleshooting, lockbox configuration, fusion architect.
---

# Fusion architect consult

## When to use
- Configuration-specific Oracle Fusion questions: how to *set up* or *change* the system —
  FSM tasks, Redwood navigation, setup parameters, SLA rules, parsing rules, rule sets.
- Diagnosing Fusion errors where the answer needs root-cause analysis against
  configuration, not process coaching.
- Integration architecture across modules (e.g., AR receipt methods ↔ CE reconciliation
  rules; SLA derivations ↔ GL mapping).
- Not for: learning how the modules work and running the processes → this plugin's teaching
  skills (`fusion-gl-and-journals`, `fusion-ap-invoice-to-pay`, `fusion-ar-and-collections`,
  `fusion-cash-management-module`, `fusion-fbdi-data-loading`, `fusion-period-close`).
  OTBI report building → `oracle-otbi-skills`.

## Do it
1. **Frame the question for the architect before delegating.** Gather what it needs to be
   configuration-specific rather than generic: the module and business flow, the release/UI
   generation if known (Redwood vs classic), the error text verbatim (for troubleshooting),
   and any environment documentation already in the project (the plugin skills'
   `references/your-environment.md` files — COA layout, bank formats, rule sets).
2. **Delegate to the `oracle-fusion-finance-skills:fusion-treasury-architect` subagent**
   with that package. The persona answers with: exact FSM task names and navigation paths,
   required parameters, file-format detail at the segment level where banks are involved,
   and upstream/downstream impact notes.
3. **For error diagnosis, require the structured format** the architect enforces:
   1) Root Cause Hypothesis, 2) Diagnostic Steps (SQL or UI), 3) Resolution Steps —
   and relay it whole; the diagnostic steps are the value, not just the fix.
4. **Check the integration-impact section before acting on any answer.** A configuration
   change in one module ripples (receipt method → reconciliation matching; CVR → FBDI loads
   failing; matching tolerance → hold volumes). If the architect's answer doesn't state the
   ripple, ask it to.
5. **Validate configuration advice in a test environment first** — configuration is
   production state, not code: it has no PR review, and some setup steps (flexfield
   structures, ledger options) are one-way. Capture what was changed and why alongside your
   environment documentation.
6. **Route the learning back.** If the consult reveals a repeatable process your team runs
   (not a one-time setup), fold the steps into the relevant teaching skill's
   `your-environment.md` so the knowledge compounds instead of living in one chat.

## Why / learn
The architect persona and the teaching skills split one domain along the *"operate vs
configure"* seam, and the split is deliberate: the teaching skills serve the analyst
running month-end (stable processes, "do + teach" depth), while configuration questions are
combinatorial — release, UI generation, ledger architecture, and existing setup all change
the answer — so they're better served by a persona that interrogates context and answers
with FSM-task precision than by a static document trying to enumerate every path. Shipping
it as a subagent gives it an isolated context window (long configuration transcripts don't
pollute the main conversation) and a tool allowlist that keeps it read-only — an advisor
that can read your environment files but can't touch anything, mirroring the
board-of-advisors design (`board-of-advisors-skills:board-review`). The
test-environment rule exists because Fusion configuration is the rare kind of change with
no undo button and no diff review: the discipline that git provides for code has to be
provided by process — sandbox first, document what changed. And the route-the-learning-back
step is how a consult stops being disposable: answers that describe *your* system belong in
your environment files, where every future skill invocation reads them.

## Common mistakes
- Asking the architect generic accounting questions → that's the teaching skills' job; the architect is for configuration precision.
- Delegating without the error text / module / release context → generic answers; package the context first.
- Applying configuration advice straight to production → sandbox first; some setup is irreversible.
- Ignoring the upstream/downstream impact notes → the ripple is usually where incidents come from; read that section first.
- Accepting a fix without the diagnostic steps → you patched a symptom; the structured format exists to prove the root cause.
- Letting environment-specific answers evaporate → fold them into the relevant skill's `your-environment.md`.

## Tailor to your environment
The architect reads the environment files the teaching skills maintain — keep those current
(COA layout in `fusion-gl-and-journals`, bank formats and rule sets in
`fusion-cash-management-module`, etc.). Record consult-specific context in
`references/your-environment.md` here: your release/update cadence, sandbox refresh
schedule, and who approves configuration changes.

## References
- references/your-environment.md — your release, sandbox process, change approvers (fill in)
