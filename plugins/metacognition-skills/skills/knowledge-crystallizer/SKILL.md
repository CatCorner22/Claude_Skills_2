---
name: knowledge-crystallizer
description: >-
  Extracts durable insights from analysis, reflection, and experience into semantic memory
  and evolving working methods — harvests candidates from working and episodic notes,
  validates them against four gates (consistency, evidence strength, scope, leverage),
  distills survivors into atomic FACT/PREFERENCE/RULE/LESSON/PATTERN/METHOD entries,
  integrates through the memory manager with user sign-off for structural changes, prunes
  redundant or stale entries, and appends one audit line to the crystallization log so
  every change stays traceable and reversible. Use after significant analysis or reflection
  cycles, when a pattern recurs, at session end or milestones, or when consolidating
  lessons into permanent knowledge or skill updates. Triggers: crystallize, consolidate
  knowledge, distill lessons, save what we learned, make this permanent, update working
  methods, clean up the knowledge base, merge duplicate notes, retire stale facts,
  capability map, crystallization pass.
metadata:
  version: "1.2.0"
---

# Knowledge crystallizer

## When to use
- After a significant analysis (`metacognition-skills:dynamic-analysis-engine`) or
  reflection (`metacognition-skills:reflective-learner`) cycle has produced insights worth
  keeping.
- When the same pattern, preference, or fix has recurred across 2+ interactions.
- At milestones and session end — the standing cadence a memory practice mandates (this
  repo's CLAUDE.md schedules exactly this pass: harvest → validate → distill → integrate →
  prune → append one log line).
- Whenever the knowledge base has grown noisy and needs consolidation and pruning.
- Not for: the moment-to-moment capture and layering of notes → see
  `metacognition-skills:hierarchical-memory-manager`; this skill is the *refinery* that
  turns its raw material into permanent, validated knowledge.
- Not for: running the team debrief that surfaces the lessons → see
  `decision-science-skills:after-action-review` (its sustain/improve items are prime
  harvest input for this pass).
- Not for: getting a crystallized rule into the *user's* unaided recall → see
  `learning-skills:spaced-retrieval-learning` (permanence in the store is this skill;
  permanence in a human head is retrieval practice).

## Do it
Validation criteria, entry formats, the audit-trail record, pruning rules, and a worked
crystallization pass are in `references/crystallization-protocol.md`.

1. **Harvest.** Collect candidate insights from recent Working/Episodic memory, reflection
   outputs from `metacognition-skills:reflective-learner`, analysis findings from
   `metacognition-skills:dynamic-analysis-engine`, and any after-action review's
   sustain/improve list. A candidate is anything that might matter beyond today.
2. **Validate each candidate against the four gates** before it becomes permanent:
   - **Consistency** — does it contradict existing semantic memory? If so, flag the
     contradiction with provenance; don't overwrite.
   - **Evidence** — observed once, or repeatedly? Inferred, or confirmed by the user?
   - **Scope** — general enough to reuse, specific enough to act on?
   - **Leverage** — will knowing this actually change future behavior?
   A failed gate routes by which gate it was: a contradiction goes to the user, thin
   evidence waits for another sighting, a badly scoped item is rewritten or split, and a
   low-leverage one is dropped.
3. **Distill** validated items into atomic, well-scoped entries — one idea per entry,
   phrased actionably in the shared grammar: `FACT:` / `PREFERENCE:` / `RULE:` / `LESSON:` /
   `PATTERN:` / `METHOD:` / `DIRECTIVE:`, each carrying evidence and confidence.
   Cause-level phrasing generalizes; outcome-level phrasing doesn't.
4. **Integrate.** Write entries into the correct semantic-memory sections via
   `metacognition-skills:hierarchical-memory-manager` (its stable headings are the
   destination; its contradiction protocol is the guard). Where an insight warrants a
   *structural* change — updating a skill, project instructions, or standing working
   methods — propose it and get user sign-off before changing anything significant (skill
   edits go through `coding-agent-skills:writing-agent-skills`).
5. **Prune & consolidate.** Merge redundant entries, retire stale or superseded ones,
   resolve or escalate flagged conflicts. A smaller, cleaner store retrieves better than a
   larger, noisier one.
6. **Append one line to the Crystallization log** — what was added, merged, retired, and
   flagged, with evidence pointers. One line per pass keeps the audit trail cheap enough to
   maintain and rich enough to make every change traceable and reversible. A pass without
   its log line didn't happen, as far as the store's history is concerned.

## Why / learn
Insights are perishable: an observation that lives only in one session's context is gone by
the next, and one that gets dumped unvalidated into permanent notes is worse — it pollutes
the store with one-off trivia and unverified guesses that later retrieval treats as truth.
Crystallization is the quality gate between *noticing* and *knowing*. The validate step is
what makes the knowledge base trustworthy: every permanent entry earned its place through
the four gates, so a reader can weigh any entry by its evidence instead of taking the
store's word. The distill step is what makes it usable — atomic entries can be retrieved
and applied singly, where a paragraph of mixed observations cannot, and cause-level
phrasing ("chained commands ran before verification") transfers to new situations where
outcome-level phrasing ("we lost work once") never does. The prune step is what keeps it
efficient: semantic memory competes for attention, and every stale entry costs a little
retrieval quality forever. And the one-line audit log is what makes permanent memory *safe*
to build — it turns the store from a black box into a system the user can inspect,
question, and roll back. The economy of the log matters as much as its existence: a pass
cheap enough to run at every milestone actually gets run, which is why the cadence survives
in practice — and this library's own store carries a month of log entries whose drift from
one line to twenty is itself the failure mode the rule guards against.

## Common mistakes
- Crystallizing everything → one-off details fossilize into noise. High-leverage,
  generalizable items only.
- Skipping validation → a single misheard preference becomes permanent "truth."
- Compound entries ("user likes X and also the close runs on WD3 and…") → split into atoms.
- Outcome-level lessons ("the report was late") → rewrite at cause level ("assumed last
  period's layout without checking") so the lesson transfers.
- Silent structural changes → skill or instruction updates without sign-off erode trust.
- Never pruning → the store grows write-only until retrieval degrades.
- Running the pass but skipping the log line → changes become untraceable; the audit trail
  is part of the pass, not an optional extra.
- Resolving a contradiction by deleting the losing entry → annotate and retire with
  provenance instead; the history of what was believed is part of the knowledge.

## Tailor to your environment
Wire in your current role here — the pipeline is role-portable (analyst, attorney, ops
manager, developer) and re-points when you change jobs. Record in
`references/your-environment.md`: what counts as significant enough for permanent storage
in your work, which changes always need your confirmation, where the audit trail lives
(this repo: the Crystallization log at the bottom of MEMORY.md), and your pruning cadence.
Keep anything sensitive in `your-environment.private.md` (git-ignored); never crystallize
secrets, credentials, account numbers, or client data — reference where they live instead.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/knowledge-crystallizer.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/crystallization-protocol.md — the four validation gates, entry formats, the
  audit-trail record, pruning rules, and a worked crystallization pass end to end
- references/your-environment.md — your thresholds, confirmations, audit-trail home, and
  cadence (fill in per role)
