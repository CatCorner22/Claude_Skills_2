# Memory protocol (layer templates & compaction checklist)

## Contents
- Layer templates
- Semantic memory headings
- Compaction checklist
- Contradiction handling

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
# Semantic memory
## Core Facts & Entities
## User Preferences & Style
## Project State & Decisions
## Open Questions / Uncertainties
## Lessons Learned & Avoidance Rules
## Successful Patterns / Working Methods
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

## Compaction checklist (run after milestones or ~15–30 significant turns)
1. Read the Working layer: what is finished, what is still live?
2. Promote finished items worth remembering into Episodic (one line each, dated).
3. Scan Episodic for patterns that have recurred 2+ times → distill into Semantic
   (a preference, rule, or fact), then trim the episodic detail.
4. Prune: delete Working notes for dead tasks; collapse old Episodic entries into
   period summaries; retire Semantic entries that are stale or superseded.
5. Re-check Semantic headings stay clean — one idea per bullet, no duplicates.
6. Note the compaction itself in the Episodic log (what was promoted/pruned).

## Contradiction handling
When a new fact conflicts with a stored one:
```markdown
⚠ CONTRADICTION
- Stored: <old fact> (recorded <date/source>)
- New: <new fact> (from <source>)
- Resolution: pending user confirmation | resolved → <which won and why>
```
Never silently overwrite. If the user resolves it, update Semantic and log the
resolution in Episodic so the change is auditable.
