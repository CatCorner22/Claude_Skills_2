---
name: hierarchical-memory-manager
description: >-
  Maintains layered memory across sessions and long contexts — Working (current task state),
  Episodic (timestamped events and decisions), Semantic (durable facts, preferences, lessons,
  each entry carrying evidence and confidence) — via a session-start load restating only
  task-relevant anchors, compaction promoting Working → Episodic → Semantic and pruning the
  rest, and contradiction flagging with provenance instead of silent overwrites, structuring
  native memory, MEMORY.md, and project files rather than replacing them. Receives
  reflective-learner lessons; feeds the knowledge crystallizer. Use at session start, during
  long multi-turn work, when context grows large, or when something should be remembered or
  recalled. Triggers: remember this, memory, what did we decide, last session, continuity,
  compact the context, working memory, episodic memory, semantic memory, MEMORY.md, memory
  layers, save for later, what do you remember, pick up where we left off.
metadata:
  version: "1.4.0"
---

# Hierarchical memory manager

## When to use
- At session start, to load only the relevant slices of stored memory and restate key
  anchors — the first step of any standing memory practice (this repo's CLAUDE.md mandates
  exactly that: read MEMORY.md, apply the relevant facts, preferences, and avoidance rules).
- During complex or multi-turn work, to capture goals, decisions, and results as they emerge.
- When context grows large, when past information is referenced, or when the user says
  "remember this" / "what did we decide about…".
- Periodically, to compact and reorganize accumulated notes.
- Not for: turning experience into lessons and method changes → see
  `metacognition-skills:reflective-learner` (it writes its outputs *through* this skill).
- Not for: the validation-and-pruning pass that makes entries permanent → see
  `metacognition-skills:knowledge-crystallizer` (this skill is the warehouse and its
  librarian; that one is the refinery and quality gate).
- Not for: making material stick in the *user's* head → see
  `learning-skills:spaced-retrieval-learning` (that is memory for the human, built on
  retrieval practice; this is memory for the assistant, built on curation).

## Do it
Layer templates, the exact semantic headings, the entry grammar, the compaction checklist,
and a worked lifecycle example are in `references/memory-protocol.md`.

1. **Know the three layers** and what belongs in each:
   - **Working** — current task goals, intermediate results, open sub-questions, temporary
     notes. Concise; updated frequently; discarded or promoted when the task ends.
   - **Episodic** — timestamped or sequence-ordered summaries of key events, decisions, user
     feedback, outcomes, and milestones from this and recent sessions.
   - **Semantic** — distilled, durable knowledge under stable headings: Core Facts &
     Entities; User Preferences & Style; Project State & Decisions; Open Questions /
     Uncertainties; Lessons Learned & Avoidance Rules; Successful Patterns / Working
     Methods — with a Crystallization log at the bottom maintained by the crystallizer.
     Standing user instructions live as `DIRECTIVE:` entries under Core Facts, because the
     load ritual surfaces them first.
2. **At session start / on retrieval:** load only the most relevant slices from native
   memory, project knowledge, MEMORY.md, or artifacts. Briefly restate the anchors that
   affect the current task — the standing directives, the avoidance rules that bite here,
   the preferences that shape the deliverable — and don't dump the whole store into context.
3. **During work:** proactively extract important new information and place it in the
   correct layer, phrased in the entry grammar (`FACT:` / `PREFERENCE:` / `RULE:` /
   `LESSON:` / `PATTERN:` / `METHOD:` / `DIRECTIVE:`, each with its evidence and
   confidence). Prefer durable external storage (a project file, MEMORY.md, an artifact) over pure context
   whenever the information should outlive the session. When the user corrects something,
   run the correction protocol in `metacognition-skills:reflective-learner` — its triage step
   logs the rule back through this skill; when a deep analysis via
   `metacognition-skills:dynamic-analysis-engine` produces durable findings, they land here
   the same way, as do the sustain/improve items a team debrief surfaces via
   `decision-science-skills:after-action-review`.
4. **Compact periodically** — after major milestones or roughly every 15–30 significant
   turns: distill Working → Episodic → Semantic. Promote what proved durable; drop what
   didn't. Anything recurring and validated is a candidate for permanence — hand it to
   `metacognition-skills:knowledge-crystallizer`, whose validation gates — consistency,
   evidence, scope, leverage — decide what the semantic store keeps forever.
5. **Detect contradictions:** when a new fact conflicts with a stored one, flag it
   explicitly — annotate the stored entry with an UPDATE note, keep the original for
   provenance, and route resolution to the user (or a later consolidation pass) instead of
   silently overwriting.
6. **Under context pressure:** prioritize retrieval by relevance and recency; summarize or
   offload lower-priority items to external files. Memory notes never displace the active
   task — memory serves the work, not the reverse.
7. **Keep sensitive data out of the store:** no secrets, credentials, account numbers, or
   client data in MEMORY.md or any committed file — reference *where* such things live
   instead; environment-specific sensitive detail goes in git-ignored `*.private.md` twins.

## Why / learn
The hierarchy mirrors how durable knowledge actually forms: everything starts as working
state, a little of it matters enough to record as *what happened* (episodic), and only the
distilled residue — facts, preferences, rules — deserves permanent storage (semantic). The
layer names borrow the vocabulary of human memory research as an organizing analogy, not a
neuroscience claim: what earns the borrowing is the promotion pipeline, because skipping the
middle step is exactly why unstructured note-keeping rots — raw transcripts pile up, nothing
is promoted or pruned, and retrieval degrades until the notes are noise. Compaction is the
active ingredient: memory is curated, not accumulated. Progressive disclosure is the other
half — stored knowledge costs nothing until it's loaded, so the discipline of loading only
relevant anchors keeps a large store cheap; a session that begins by restating three
applicable rules gets their full value at a fraction of the cost of replaying the archive.
Evidence-and-confidence annotations are what make entries *arguable*: a fact that knows
where it came from can be checked, weighed, and retired, where a bare assertion can only be
believed. And contradiction flagging matters because a memory system that silently
overwrites can't be trusted — a store that once held "the user works at X" and later learns
the role is ending should show both, with dates, so the history of what was believed remains
auditable and the user stays in control of what "true" means.

## Common mistakes
- Hoarding everything → the store becomes noise. Promote selectively; prune at each compaction.
- Never compacting → Working-layer sprawl and stale episodic detail crowd out durable facts.
- Dumping the whole store into context at session start → costs attention and buries the
  three anchors that matter. Restate only what bears on this task.
- Silently overwriting a conflicting fact → flag it, annotate with UPDATE, keep provenance.
- Keeping memory only in context → it dies with the session. Write durable items to files.
- Entries without evidence or dates → unarguable assertions that can never be safely
  retired. Every entry says where it came from.
- Letting memory maintenance displace the task at hand → memory serves the work, never the
  reverse.
- Storing secrets, credentials, or raw sensitive data → reference their location instead;
  sensitive tailoring detail belongs in git-ignored `*.private.md` files.

## Tailor to your environment
Wire in your current role here — the practice is deliberately role-portable (analyst,
attorney, ops manager, developer) and re-points when you change jobs: only this file and the
store's contents change, never the method. Record in `references/your-environment.md` where
your memory actually lives (this repo keeps a MEMORY.md at the root, loaded every session
per its CLAUDE.md; yours may be a project file, native memory, or a notes system), which
projects/artifacts hold what, your compaction cadence, what to always capture, and — most
importantly — what must never be stored. Keep anything sensitive in
`your-environment.private.md` (git-ignored); never commit real data.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/hierarchical-memory-manager.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/memory-protocol.md — layer templates, the semantic headings and entry grammar,
  the session-start load ritual, the compaction checklist, contradiction handling, and a
  worked end-to-end lifecycle example
- references/your-environment.md — where your memory lives and your retention rules (fill
  in per role)
