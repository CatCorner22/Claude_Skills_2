# Memory protocol: layers, entry grammar, load ritual, compaction, worked lifecycle

The method is role-portable: the same store structure serves an analyst's reconciliation
projects, an attorney's matters, an ops manager's vendors and processes, or a developer's
repos. Only the contents change with the job — the layers, grammar, and rituals do not.

## Contents
- Layer templates
- Semantic memory headings (the canonical set)
- The entry grammar (evidence-bearing atoms)
- Session-start load ritual
- Compaction checklist
- Contradiction handling (flag, annotate, keep provenance)
- Worked lifecycle example (one store, three months)
- Sizing and hygiene rules

## Layer templates

### Working memory (volatile — current task only)
```markdown
## Working memory — <task name>
- Goal: <what we're trying to accomplish>
- Status: <where we are>
- Intermediate results: <key numbers/findings so far>
- Open sub-questions: <what's unresolved>
- Temp notes: <anything short-lived>
```

### Episodic memory (sequence-ordered events)
```markdown
## Episodic log
- <YYYY-MM-DD or turn-marker> — <decision/event>: <one-line summary + outcome>
- <YYYY-MM-DD> — User feedback: <what they corrected/preferred>
```

### Semantic memory (durable, under stable headings)
```markdown
# Semantic memory — <collaboration name>
## Core Facts & Entities
## User Preferences & Style
## Project State & Decisions
## Open Questions / Uncertainties
## Lessons Learned & Avoidance Rules
## Successful Patterns / Working Methods
## Crystallization log
```
For entities, a lightweight structured block keeps retrieval precise:
```yaml
entity: <name>
type: <system | account | process | person-role>
facts:
  - <fact 1>
  - <fact 2>
last_verified: <date>
```

## Semantic memory headings (the canonical set)
The six headings plus the log are deliberate, and they are the set this repo's own
MEMORY.md uses in production:
- **Core Facts & Entities** — who/what the collaboration is about; standing directives.
- **User Preferences & Style** — how the user wants work done; confirmed, dated.
- **Project State & Decisions** — the current shape of things; decisions with their dates.
- **Open Questions / Uncertainties** — known unknowns, so no one re-derives or invents them.
- **Lessons Learned & Avoidance Rules** — hard-won "when X, do/never Y" entries with origins.
- **Successful Patterns / Working Methods** — approaches that worked and should be reused.
- **Crystallization log** — one line per consolidation pass, appended by
  `metacognition-skills:knowledge-crystallizer`; the store's audit trail.

Stable headings matter more than clever ones: retrieval is a *scan*, and a scanner that
knows where preferences live finds them in seconds.

## The entry grammar (evidence-bearing atoms)
Every semantic entry is one idea, typed, with its provenance attached:
```markdown
- FACT: <statement>. (evidence: <source/date>; confidence: high/med)
- PREFERENCE: user prefers <X> when <context>. (confirmed <date>)
- RULE: when <situation>, do <action>. (origin: <incident/reflection ref>)
- LESSON: <generalizable insight>. (from: <episode>)
- PATTERN: <recurring structure worth reusing>. (seen: <n> times)
- METHOD: current working method for <task> is <approach>. (updated <date>)
- DIRECTIVE: <standing user instruction>. (user-stated <date>, standing)
```
The parenthetical is not decoration. An entry that knows where it came from can be
re-checked, weighed against a contradicting claim, and retired cleanly; a bare assertion
can only be believed or ignored. This grammar is shared with the crystallizer's validation
gates — capture in this shape and the permanence pass gets cheaper.

## Session-start load ritual
1. Open the semantic store (e.g. MEMORY.md at the repo root — this repo's CLAUDE.md
   mandates reading it at every session start).
2. Scan headings; pull only entries that bear on today's task: applicable DIRECTIVEs and
   RULEs first (they constrain everything), then task-relevant FACTs, PREFERENCEs, METHODs.
3. Restate the loaded anchors in one short block ("Applying: <rule>; <preference>; …") so
   the load is visible and checkable — not silently assumed.
4. Leave the rest unloaded. Progressive disclosure: unread entries cost nothing.
5. If the task contradicts a loaded anchor, say so before proceeding — that is either a
   contradiction to flag or a deliberate exception to record.

## Compaction checklist (run after milestones or ~15–30 significant turns)
1. Read the Working layer: what is finished, what is still live?
2. Promote finished items worth remembering into Episodic (one line each, dated).
3. Scan Episodic for patterns that have recurred 2+ times → candidates for Semantic.
   Candidates go through `metacognition-skills:knowledge-crystallizer` (its four gates:
   consistency, evidence, scope, leverage) rather than straight into permanence.
4. Prune: delete Working notes for dead tasks; collapse old Episodic entries into period
   summaries; retire Semantic entries that are stale or superseded (via the crystallizer,
   so the retirement is logged).
5. Re-check Semantic headings stay clean — one idea per bullet, no duplicates.
6. Note the compaction itself in the Episodic log (what was promoted/pruned).

## Contradiction handling (flag, annotate, keep provenance)
When a new fact conflicts with a stored one:
```markdown
⚠ CONTRADICTION
- Stored: <old fact> (recorded <date/source>)
- New: <new fact> (from <source>)
- Resolution: pending user confirmation | resolved → <which won and why>
```
In-place annotation is the durable form — the stored entry gains an UPDATE note and the
original text stays for provenance:
```markdown
- FACT: <original statement>. (evidence: <source>; confidence: high)
  (UPDATE <date>: <what changed> — contradiction flagged, original kept for provenance.)
```
Silent overwriting is the one unforgivable move: it destroys the audit trail that makes
the store trustworthy. If the user resolves the conflict, update Semantic and log the
resolution in Episodic so the change is traceable.

## Worked lifecycle example (one store, three months)
Genericized from this repository's real MEMORY.md — the store that maintains this library.
Swap the nouns for any role: matters for an attorney, vendors for an ops manager, clients
for an analyst, services for a developer.

**Month 1 — capture.** Sessions record durable items as they surface:
```markdown
- FACT: The user works in <domain role> on <platform>; their environment carries
  <domain>-specific tooling. (evidence: observed in session, <date>; confidence: high)
- PREFERENCE: Deliverables follow the "do + teach" standard — perform the task AND explain
  the reasoning. (user-selected at scoping; confirmed throughout)
```
**Month 2 — an incident becomes a RULE.** A destructive command chained with a
verification step runs before the verification is read; work is briefly lost, then
restored. The reflection (via `metacognition-skills:reflective-learner`) lands here as:
```markdown
- RULE: Never chain an evidence-gathering command with a destructive command in one step —
  verify in one step, act in the next. (origin: <date> incident, recovery documented)
```
Note what makes it durable: cause-level phrasing ("chained commands"), not outcome-level
("lost work"), plus the origin pointer.

**Month 3 — the world changes; the store flags, never rewrites.** The user announces the
role recorded in Month 1 is ending. The store does *not* delete the fact:
```markdown
- FACT: The user works in <domain role> on <platform>… (evidence: …; confidence: high)
  (UPDATE <date>: the user's role is ending — see the standing directive below.
  Contradiction flagged, original kept for provenance.)
- DIRECTIVE: Build nothing new mounted on <old employer>'s workflows; existing skills stay
  as the user's portable professional assets. (user-stated <date>, standing)
```
Every later session's load ritual now surfaces the DIRECTIVE first, and the store's
history still shows what was true before. That is the whole design working at once:
capture → rule-formation → contradiction flagged with provenance → session-start anchors.

## Sizing and hygiene rules
- Working notes live in context or a scratch file; they are never committed.
- Episodic detail has a shelf life — collapse to period summaries once it stops being
  consulted (retention cadence goes in `your-environment.md`).
- The semantic store should stay scannable in one read; when it stops being, that is a
  crystallizer consolidation trigger, not a reason for a second store.
- No secrets, credentials, account numbers, or client data — ever. Reference the location
  of sensitive material instead ("credentials in the team vault"), and keep sensitive
  tailoring detail in git-ignored `*.private.md` twins.
- One store per collaboration. Two stores answering the same question will eventually
  disagree, and then neither is trusted.
