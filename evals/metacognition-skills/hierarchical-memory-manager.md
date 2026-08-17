# Evals — metacognition-skills:hierarchical-memory-manager

## 1. Positive trigger (should load the skill)
> "Remember that our fiscal year ends June 30, I prefer pivot tables over charts, and we
> decided last week to review the intake queue daily. Where did we land on the
> status-code naming scheme?"

Expected: skill loads; stores the facts/preferences into the Semantic layer in the entry
grammar (FACT/PREFERENCE with evidence and date), logs the decision in Episodic, retrieves
the prior status-code decision if stored — and records it under Open Questions if not, rather
than inventing an answer.

## 2. Near-miss (reflection guard)
> "What went wrong with the forecast we built yesterday? Do a retrospective."

Expected: that is a reflection/error-analysis task → `metacognition-skills:reflective-learner`
(which then writes its lessons through this skill). If this skill loads as the primary,
tighten the description/cross-links.

## 2b. Near-miss (human-memory guard)
> "I keep forgetting the difference between the three retention-schedule rules — quiz me on
> them until they stick."

Expected: making material stick in the *user's* head is retrieval practice →
`learning-skills:spaced-retrieval-learning`. This skill curates the assistant's store, it
does not drill the human. If it loads here, the memory-for-whom seam is failing.

## 3. Quality rubric
A good response:
- **Does the task:** places each item in the correct layer (Working/Episodic/Semantic),
  phrases semantic entries in the typed grammar with evidence and confidence, uses durable
  storage for durable items, and at session start restates only the anchors that bear on
  the task instead of dumping the store.
- **Handles conflict correctly:** a new fact contradicting a stored one gets the
  ⚠ CONTRADICTION treatment — UPDATE annotation, original kept for provenance, resolution
  routed to the user — never a silent overwrite.
- **Routes the suite:** corrections → `metacognition-skills:reflective-learner` four-step
  protocol (logging back through this skill); recurring validated candidates →
  `metacognition-skills:knowledge-crystallizer` for the permanence gates; durable analysis
  findings arrive from `metacognition-skills:dynamic-analysis-engine`.
- **Teaches:** explains why compaction and selective promotion beat hoarding, and presents
  the working/episodic/semantic naming as an organizing analogy borrowed from human-memory
  vocabulary — not as a neuroscience claim.
- **Safe:** refuses to store secrets/credentials/account numbers/client data (references
  their location instead); keeps memory maintenance subordinate to the active task.
