# Crystallization protocol: gates, formats, audit trail, pruning, worked pass

The refinery between noticing and knowing. Raw material arrives from the memory manager's
Working/Episodic layers, reflection cycles, analyses, and debriefs; what leaves is a small
number of validated, atomic, evidence-bearing entries — plus one audit line proving the
pass happened. Role-portable throughout: the same gates serve an analyst's close lessons,
an attorney's matter patterns, an ops manager's vendor rules, or a developer's incident
rules.

## Contents
- Harvest sources
- Validation gates
- Entry formats (atomic)
- Integration rules
- Audit-trail record
- Pruning rules
- Contradiction handling and escalation
- Worked example: one crystallization pass end to end
- Cadence

## Harvest sources
A candidate is anything that might matter beyond today. Sweep, in order:
1. The Working layer of `metacognition-skills:hierarchical-memory-manager` — decisions and
   findings from the task just finished.
2. The Episodic log — anything that has now appeared 2+ times is auto-nominated.
3. Reflection outputs from `metacognition-skills:reflective-learner` — its "actionable
   updates" section is pre-shaped for this pass.
4. Analysis conclusions from `metacognition-skills:dynamic-analysis-engine` — durable
   findings, not intermediate numbers.
5. Team-debrief outputs — an after-action review's sustain/improve list
   (`decision-science-skills:after-action-review`) is prime input: "sustain" items become
   PATTERNs, "improve" items become RULEs or METHOD updates.

## Validation gates
A candidate becomes permanent only if it passes all four:

| Gate | Question | Fails → |
|---|---|---|
| Consistency | Does it contradict existing semantic memory? | Flag contradiction for resolution (see below) |
| Evidence | Observed repeatedly, or user-confirmed? (Once-inferred is weakest) | Hold as candidate |
| Scope | General enough to reuse, specific enough to act on? | Rewrite or split |
| Leverage | Will knowing this change future behavior? | Discard (one-off detail) |

Gate order matters: consistency first, because a contradiction changes how every other
gate is read — strong evidence *for* a candidate that contradicts a stored fact is exactly
the situation that must reach the user, not be averaged away.

## Entry formats (atomic — one idea each)
```markdown
- FACT: <statement>. (evidence: <source/date>; confidence: high/med)
- PREFERENCE: user prefers <X> when <context>. (confirmed <date>)
- RULE: when <situation>, do <action>. (origin: <reflection/analysis/incident ref>)
- LESSON: <generalizable insight>. (from: <episode>)
- PATTERN: <recurring structure worth reusing>. (seen: <n> times)
- METHOD: current working method for <task> is <approach>. (updated <date>)
- DIRECTIVE: <standing user instruction>. (user-stated <date>, standing)
```
Distillation rules:
- **One idea per entry.** "User likes X and the close runs on WD3" is two entries.
- **Cause level, not outcome level.** "Assumed last period's layout without checking"
  transfers; "the report was late" doesn't.
- **Actionable phrasing.** A RULE reads as when-then; a PATTERN names when to reuse it.
- **Provenance attached.** The parenthetical is what lets a future pass re-weigh or retire
  the entry; an entry without it can only be believed or ignored.

## Integration rules
- Entries land in the correct stable heading of the semantic store via
  `metacognition-skills:hierarchical-memory-manager`: Core Facts & Entities; User
  Preferences & Style; Project State & Decisions; Open Questions / Uncertainties; Lessons
  Learned & Avoidance Rules; Successful Patterns / Working Methods.
- **Structural changes are proposals, not writes.** An insight that warrants editing a
  skill, project instructions, or standing methods goes to the user with the evidence; on
  sign-off, skill edits follow `coding-agent-skills:writing-agent-skills`.
- Sensitive material never crystallizes: no secrets, credentials, account numbers, or
  client data — record *where* such things live instead.

## Audit-trail record
Append one line per crystallization pass to the Crystallization log at the bottom of the
semantic store:
```markdown
## Crystallization log
- <date> — Added: <n> entries (<topics>). Merged: <what>. Retired: <what + why>.
  Flagged: <contradictions pending>. Evidence: <links/refs>.
```
Every permanent entry should be traceable to a log line; every log line should make the
change reversible (what was there before). One line is the deliberate size: cheap enough
that the pass actually runs at every milestone, rich enough to audit. This repository's own
MEMORY.md carries a month of these entries, and their drift from one line to twenty is
itself the failure mode the rule guards against — when a pass needs a paragraph, the pass
was too big, not the log too small.

## Pruning rules
- **Merge** entries that say the same thing differently — keep the clearer phrasing, note
  the merge in the log.
- **Retire** entries superseded by newer confirmed facts (note the succession in the log;
  keep the retired text reachable through it).
- **Demote** entries that keep failing to matter — back to episodic notes rather than
  deletion if unsure.
- **Resolve or escalate** any contradiction older than two passes — conflicts must not age.
- Prefer a smaller, cleaner store: every stale entry costs a little retrieval quality on
  every future load.

## Contradiction handling and escalation
When a validated candidate contradicts a stored entry, the stored entry is annotated —
never rewritten:
```markdown
- FACT: <original statement>. (evidence: <source>; confidence: high)
  (UPDATE <date>: <new information> — contradiction flagged, original kept for provenance.)
```
The pass's log line records the flag ("Flagged: 1 contradiction (<topic>), handled per
protocol"). Resolution routes: user confirms → the winning fact is recorded with the
resolution noted; user unavailable → the flag stands, and both readings stay visible to
every future session-start load.

## Worked example: one crystallization pass end to end
Genericized from a real pass over this repository's MEMORY.md — the store that maintains
this library. Three candidates arrive at session end:

**Candidate A** — from a reflection after an incident: a verification command was chained
with a destructive command in one step, and the destructive step ran before the evidence
was read; work was briefly lost, then recovered.
- Consistency: no conflict. Evidence: one incident, but user-confirmed and costly. Scope:
  rewritten from "don't force-push" (too narrow) to the cause level. Leverage: high —
  changes every future risky operation.
- **Distilled:** `RULE: never chain an evidence-gathering command with a destructive
  command in one step — verify in one step, act in the next. (origin: <date> incident)`
- **Integrated:** Lessons Learned & Avoidance Rules.

**Candidate B** — from working notes: the exact wording of a one-off status update the
user liked.
- Leverage gate fails: the wording belongs to one artifact that will not exist again, so
  knowing it changes nothing about future work.
- **Discarded** (noted as episodic detail only). If the phrasing recurs, the episodic log
  auto-nominates it.

**Candidate C** — the user announces their role (recorded three weeks earlier as a high-
confidence FACT) is ending, and issues a standing instruction about future work.
- Consistency gate fires: contradiction with the stored employment fact.
- **Handled:** the original FACT gains an UPDATE annotation (original kept for
  provenance); a new `DIRECTIVE:` entry records the standing instruction; nothing is
  deleted.

**Log line appended:**
```markdown
- <date> — Added: 2 entries (chained-command rule; standing directive). Merged: none.
  Retired: none. Flagged: 1 contradiction (role fact), handled per protocol.
  Evidence: session history through <ref>.
```
Every future session now loads the DIRECTIVE first, the RULE guards every risky command,
the trivia never entered the store, and the store's history still shows what was believed
before. That is the full pipeline — harvest, four gates, atomic distillation, guarded
integration, prune-by-discard, one-line audit — on real material.

## Cadence
- Light pass at session end; a pass at every milestone (the standing cadence a memory
  practice mandates — this repo's CLAUDE.md names milestones and session end explicitly).
- Fuller consolidation when the store feels noisy or roughly monthly, whichever first.
- If passes keep getting skipped, shrink the pass, not the cadence — the one-line log
  exists precisely so the habit survives busy periods.
