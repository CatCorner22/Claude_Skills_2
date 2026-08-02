---
name: knowledge-crystallizer
description: >-
  Extracts, validates, and integrates durable insights from analysis, reflection, and experience
  into structured semantic memory and evolving working methods — harvesting candidate insights,
  checking them against existing knowledge for consistency and evidence strength, distilling them
  into atomic well-scoped entries, integrating with an audit trail, and pruning redundant or
  stale items. Use after significant analysis or reflection cycles, when a pattern recurs across
  interactions, at session end, or when consolidating lessons into permanent knowledge or skill
  updates. Triggers: crystallize, consolidate knowledge, distill lessons, save what we learned,
  make this permanent, update working methods, clean up the knowledge base, merge duplicate
  notes, retire stale facts, capability map.
---

# Knowledge crystallizer

## When to use
- After a significant analysis (`dynamic-analysis-engine`) or reflection (`reflective-learner`)
  cycle has produced insights worth keeping.
- When the same pattern, preference, or fix has recurred across 2+ interactions.
- At session end, or whenever the knowledge base needs consolidation and pruning.
- Not for: the moment-to-moment capture and layering of notes → see
  `metacognition-skills:hierarchical-memory-manager`; this skill is the *refinery* that turns
  its raw material into permanent, validated knowledge.

## Do it
1. **Harvest.** Collect candidate insights from recent Working/Episodic memory, reflection
   outputs, and analysis findings. A candidate is anything that might matter beyond today.
2. **Validate each candidate** before it becomes permanent:
   - Consistent with existing semantic memory? If not, flag the contradiction — don't overwrite.
   - Evidence strength: observed once, or repeatedly? Inferred, or confirmed by the user?
   - Right scope: general enough to reuse, specific enough to act on?
   - Items failing validation wait as candidates or go to the user for confirmation.
3. **Distill** validated items into atomic, well-scoped entries — one idea per entry, phrased
   actionably: a fact, a preference, a lesson, a rule, a pattern, or an updated method.
4. **Integrate.** Write entries into the correct semantic-memory sections via
   `metacognition-skills:hierarchical-memory-manager`. Where an insight warrants a *structural*
   change — updating a skill, project instructions, or standing working methods — propose it
   and get user sign-off for anything significant (skill edits go through
   `coding-agent-skills:writing-agent-skills`).
5. **Prune & consolidate.** Merge redundant entries, retire stale or superseded ones, resolve
   flagged conflicts. A smaller, cleaner store retrieves better than a larger, noisier one.
6. **Keep the audit trail.** Record what was crystallized, from what evidence, and what was
   pruned — so the knowledge base stays inspectable and every change is reversible.
7. Validation criteria and the crystallization record format are in
   `references/crystallization-protocol.md`.

## Why / learn
Insights are perishable: an observation that lives only in one session's context is gone by the
next, and one that gets dumped unvalidated into permanent notes is worse — it pollutes the store
with one-off trivia and unverified guesses that later retrieval treats as truth. Crystallization
is the quality gate between *noticing* and *knowing*. The validate step is what makes the
knowledge base trustworthy (every permanent entry earned its place with evidence); the distill
step is what makes it usable (atomic entries can be retrieved and applied singly, where a
paragraph of mixed observations cannot); and the prune step is what keeps it efficient (semantic
memory competes for attention — every stale entry costs a little retrieval quality forever).
The audit trail turns the whole thing from a black box into a system the user can inspect,
question, and roll back — which is exactly what makes permanent memory safe to build.

## Common mistakes
- Crystallizing everything → one-off details fossilize into noise. High-leverage, generalizable
  items only.
- Skipping validation → a single misheard preference becomes permanent "truth."
- Compound entries ("user likes X and also the close runs on WD3 and…") → split into atoms.
- Silent structural changes → skill or instruction updates without sign-off erode trust.
- Never pruning → the store grows write-only until retrieval degrades.
- No audit trail → knowledge can't be traced to evidence, so it can't be safely corrected.

## Tailor to your environment
Record in `references/your-environment.md` your crystallization preferences: what counts as
significant enough for permanent storage, which changes always need your confirmation, where the
audit trail lives, and your pruning cadence. Keep anything sensitive in
`your-environment.private.md` (git-ignored); never commit real data.

## References
- references/crystallization-protocol.md — validation criteria, entry formats, and the audit-trail record
- references/your-environment.md — your thresholds, confirmations, and cadence (add when supplied)
