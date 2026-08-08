# Evals — continuous-improvement-skills:qfd-house-of-quality

## 1. Positive trigger (should load the skill)
> "We just finished the co-design interviews for the dental app — I have a pile of patient and
> front-desk needs with rough priorities. Build me a house of quality that translates them into
> measurable engineering characteristics so we can decide what to build first."

Expected: skill loads; organizes the needs into a short weighted WHAT hierarchy in the
customers' own words (weights marked as drafts pending ratification by the actual patients and
staff); writes measurable HOWs (unit, direction, owner); fills the 9/3/1 relationship matrix and
audits empty rows/columns; builds the roof and names each negative correlation's resolution;
computes importance scores as column sums of weight × relationship; benchmarks and sets a target
per HOW; presents the target row as the CTQ set for the downstream build and notes the cascade
(HOWs become the next house's WHATs).

## 2. Near-miss (should NOT load this skill)
> "Help me plan and facilitate the co-design workshop with patients and front-desk staff so we
> can gather their needs for the app in the first place."

Expected: running the session that *gathers* the needs is
`continuous-improvement-skills:kaizen-and-codesign` — it produces this skill's input. If
qfd-house-of-quality loads on facilitation/workshop asks, its trigger surface has crossed the
upstream seam.

## 2b. Near-miss (downstream seam / bare-token guard)
> "We already have our CTQs signed off. Now run the build with real lean six sigma discipline —
> control charts on delivery, adversarial testing before release, the works."

Expected: consuming ratified CTQs to run the build is
`continuous-improvement-skills:lean-six-sigma-for-software`. This skill may name voice-of-
customer and CTQ as the endpoints it bridges, but it must not fire on bare "VOC"/"CTQ" mentions
— those tokens belong to kaizen-and-codesign and lean-six-sigma-for-software respectively. If
qfd-house-of-quality loads here, its description has grown greedy on the endpoint vocabulary.

## 3. Quality rubric
A good response:
- **Does the task:** produces a complete house — weighted WHAT hierarchy, measurable HOWs,
  9/3/1 matrix with the empty-row/empty-column audit, roof with named tradeoff resolutions,
  computed importance scores, benchmarks, and a target row usable as CTQs — plus the cascade
  plan for the top-scoring HOWs.
- **Teaches:** explains the substitution failure QFD prevents (customer voice silently replaced
  hop by hop), why the 9/3/1 spread keeps strong relationships dominant, what empty rows and
  columns mean, and why the roof surfaces tradeoffs while they're still cheap.
- **Stays honest:** marks LLM-drafted weights and cells as proposals for human correction —
  weightings are ratified by actual customers/users, never presented as customer voice on the
  LLM's say-so; keeps the Toyota development-cost evidence attributed as snippet-level HBR
  reporting rather than a verified fact; invents no customer needs not grounded in the notes.
