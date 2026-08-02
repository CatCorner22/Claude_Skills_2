---
name: hierarchical-memory-manager
description: >-
  Maintains multi-layered, actively curated memory across sessions and long contexts —
  Working (current task state), Episodic (timestamped events and decisions), and Semantic
  (durable facts, preferences, lessons) — with periodic compaction, contradiction detection,
  and progressive disclosure, structuring native memory, MEMORY.md, and project files rather
  than replacing them. Use at session start, during long multi-turn work, when context grows
  large, when past information is referenced, or when asked to remember something. Triggers:
  remember this, memory, what did we decide, last session, continuity, compact the context,
  working memory, episodic memory, semantic memory, MEMORY.md, memory layers, save for later.
---

# Hierarchical memory manager

## When to use
- At session start, to load only the relevant slices of stored memory and restate key anchors.
- During complex or multi-turn work, to capture goals, decisions, and results as they emerge.
- When context grows large, when past information is referenced, or when the user says
  "remember this" / "what did we decide about…".
- Periodically, to compact and reorganize accumulated notes.
- Not for: turning experience into lessons and method changes → see
  `metacognition-skills:reflective-learner` (it writes its outputs *through* this skill).

## Do it
1. **Know the three layers** and what belongs in each:
   - **Working** — current task goals, intermediate results, open sub-questions, temporary
     notes. Concise; updated frequently; discarded or promoted when the task ends.
   - **Episodic** — timestamped or sequence-ordered summaries of key events, decisions, user
     feedback, outcomes, and milestones from this and recent sessions.
   - **Semantic** — distilled, durable knowledge under stable headings: Core Facts & Entities;
     User Preferences & Style; Project State & Decisions; Open Questions / Uncertainties;
     Lessons Learned & Avoidance Rules; Successful Patterns / Working Methods.
2. **At session start / on retrieval:** load only the most relevant slices from native memory,
   project knowledge, MEMORY.md, or artifacts. Briefly restate the anchors that affect the
   current task — don't dump the whole store into context.
3. **During work:** proactively extract important new information and place it in the correct
   layer using structured Markdown (headers + bullets, or lightweight YAML/JSON blocks for
   entities). Prefer durable external storage (a project file, MEMORY.md, an artifact) over
   pure context whenever the information should outlive the session.
4. **Compact periodically** — after major milestones or roughly every 15–30 significant turns:
   distill Working → Episodic → Semantic. Promote what proved durable; drop what didn't.
5. **Detect contradictions:** when a new fact conflicts with a stored one, flag it explicitly
   for user resolution (or a later consolidation pass) instead of silently overwriting.
6. **Under context pressure:** prioritize retrieval by relevance and recency; summarize or
   offload lower-priority items to external files. Never let memory notes displace the active
   task — memory serves the work, not the reverse.
7. Layer templates and the compaction checklist live in `references/memory-protocol.md`.

## Why / learn
The hierarchy mirrors how durable knowledge actually forms: everything starts as working state,
a little of it matters enough to record as *what happened* (episodic), and only the distilled
residue — facts, preferences, rules — deserves permanent storage (semantic). Skipping the middle
step is why unstructured note-keeping rots: raw transcripts pile up, nothing is promoted or
pruned, and retrieval degrades until the notes are noise. Compaction is the active ingredient —
memory is curated, not accumulated. Progressive disclosure is the other half: stored knowledge
costs nothing until it's loaded, so the discipline of loading only relevant slices keeps a large
memory cheap. And contradiction detection matters because a memory system that silently
overwrites can't be trusted; surfacing conflicts keeps the store auditable and the user in
control of what "true" means.

## Common mistakes
- Hoarding everything → the store becomes noise. Promote selectively; prune at each compaction.
- Never compacting → Working-layer sprawl and stale episodic detail crowd out durable facts.
- Silently overwriting a conflicting fact → flag contradictions for resolution instead.
- Keeping memory only in context → it dies with the session. Write durable items to files.
- Letting memory maintenance displace the task at hand → memory serves the work, never the reverse.
- Storing secrets, credentials, or raw sensitive data → never memorize these; reference their
  location instead.

## Tailor to your environment
Record where your memory actually lives in `references/your-environment.md`: the path to your
MEMORY.md or project memory files, which projects/artifacts hold what, your preferred compaction
cadence, and — importantly — what must never be stored (account numbers, client data,
credentials). Keep anything sensitive in `your-environment.private.md` (git-ignored); never
commit real data.

## References
- references/memory-protocol.md — layer templates, semantic headings, and the compaction checklist
- references/your-environment.md — where your memory lives and your retention rules (add when supplied)
