---
name: project-manager-qc
description: >-
  Coordinates work spanning sessions or agents, or a deliverable requiring an independent reviewer. Maintains requirements, amendments, owners, checkpoints, and a complete evidence-based delivery gate. Complements Maximum-Delegation Auditor and Puppet Master; avoids management ceremony on simple single-session work. Triggers: multi-session project, coordinate the subagents, independent QC gate, track work across sessions.
---

# Project Manager and Quality Control

## When to use

- Engage for cross-session/agent coordination or required fresh review. Keep the ledger short; do not create planning documents nobody requested.
- Not for: ordinary single-session efficiency → use `puppet-master`; user handoffs → retain `maximum-delegation-auditor`; blocked routes → use `creative-workaround-genius`.

## Do it

1. **Read the full current request.** Record requirements with source, acceptance check, owner, state, and evidence. Include names, formats/order, units, dates/time zones, exclusions, depth, privacy, and authority. Mark superseded instructions and replacements.
2. **Plan enough to execute.** Map dependencies and assign separate write scopes. Maximum-Delegation Auditor retains feasible authorized work; Puppet Master limits unnecessary context and calls. Use meaningful checkpoints, measured budgets when available, and labeled unknowns. A hard budget needs an essential scope decision, not deleted criteria.
3. **Checkpoint durable state.** Save completed/outstanding criteria, source identities, artifact paths, checks, blockers, next steps, and authority boundaries through supported durable storage. Keep private notes outside public git and caches. Checkpoint at phase/context handoffs. New sessions read current artifacts rather than trust stale summaries.
4. **Sweep every delivery category.** Use an exposed independent reviewer for substantial work or required independent QC. Supply the actual request, artifacts, read-only scope, and safe checks without expected findings. If unavailable, perform a separate self-review and disclose it. Record N/A with a reason where appropriate:
   - Requirements: every criterion with artifact evidence.
   - Numbers: independent recomputation from source and cross-file totals.
   - Claims: citations, completion, tests, saving, and installation statements.
   - Code paths: shipped behavior, filters, joins, deduplication, units, rounding, boundaries.
   - Tests: execute relevant checks and inspect assertions against the shipped path.
   - Files: completeness, durable saving, privacy, and absence of debug debris.
   - Format: exact names, field order, encoding, limits, and rendering where needed.
   - Examples: execute applicable documented commands as written with safe fixtures.
5. **Fix and recheck.** Require evidence of a violated criterion or real risk. Classify findings LOAD (fix before delivery), PUNCH (real but nonblocking), or FUTURE (outside scope), each with a fix and recheck. Resolve LOAD items within authority and retest affected behavior. Never claim a required independent gate passed after self-review. Deliver supported partial work and the exact missing capability if essential. Report outcome, proof, and remaining gaps; save reusable lessons only where authorized.

## Why / learn

Handoffs lose small constraints; a ledger makes them testable. Fresh review reduces shared assumptions. A category sweep avoids stopping after the first loud finding. Additional management pays for coordination and independence, not simply for using several tools.

## Common mistakes

- Reviewing a summary instead of the source request and final files → reopen primary artifacts.
- Calling a second self-review independent → label actual review scope.
- Treating test count as coverage → inspect assertions and execution paths.
- Stopping at the first finding → finish the sweep.

## Tailor to your environment

Use [the environment template](references/your-environment.md) for green checks and checkpoint locations. Resolve from the actual skill root. Keep filled notes outside caches/public git, verify privacy rules, and persist using the host's supported workflow.

## References

- [Environment template](references/your-environment.md): acceptance checks, owners, checkpoints, and review evidence.
