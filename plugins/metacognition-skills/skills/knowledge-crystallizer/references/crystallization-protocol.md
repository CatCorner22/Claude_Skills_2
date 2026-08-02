# Crystallization protocol

## Contents
- Validation criteria
- Entry formats (atomic)
- Audit-trail record
- Pruning rules

## Validation criteria
A candidate insight becomes permanent only if it passes all four:

| Check | Question | Fails → |
|---|---|---|
| Consistency | Does it contradict existing semantic memory? | Flag contradiction for resolution |
| Evidence | Observed repeatedly, or user-confirmed? (Once-inferred is weakest) | Hold as candidate |
| Scope | General enough to reuse, specific enough to act on? | Rewrite or split |
| Leverage | Will knowing this change future behavior? | Discard (one-off detail) |

## Entry formats (atomic — one idea each)
```markdown
- FACT: <statement>. (evidence: <source/date>; confidence: high/med)
- PREFERENCE: user prefers <X> when <context>. (confirmed <date>)
- RULE: when <situation>, do <action>. (origin: <reflection/analysis ref>)
- LESSON: <generalizable insight>. (from: <episode>)
- PATTERN: <recurring structure worth reusing>. (seen: <n> times)
- METHOD: current working method for <task> is <approach>. (updated <date>)
```

## Audit-trail record
Append one line per crystallization pass:
```markdown
## Crystallization log
- <date> — Added: <n> entries (<ids/topics>). Merged: <what>. Retired: <what + why>.
  Flagged: <contradictions pending>. Evidence: <links/refs>.
```
Every permanent entry should be traceable to this log; every log line should make the
change reversible (what was there before).

## Pruning rules
- **Merge** entries that say the same thing differently — keep the clearer phrasing.
- **Retire** entries superseded by newer confirmed facts (note the succession in the log).
- **Demote** entries that keep failing to matter — move back to episodic notes rather than
  deleting outright if unsure.
- **Resolve or escalate** any contradiction older than two passes — don't let conflicts age.
- Cadence: light pass at session end; fuller consolidation when the store feels noisy or
  roughly monthly, whichever comes first.
