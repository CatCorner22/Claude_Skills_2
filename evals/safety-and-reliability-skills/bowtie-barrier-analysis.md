# Evals — safety-and-reliability-skills:bowtie-barrier-analysis

## 1. Positive trigger (should load the skill)
> "A spoofed CFO email almost got a wire released last quarter. Before the next attempt, map our
> lines of defense: what stands between a fraudulent payment instruction and money leaving, and
> what catches it if it gets through?"

Expected: skill loads; names the hazard ("we move money on instruction") and a single top event
("fraudulent payment instruction accepted as genuine"); generates threat lines by running the HAZOP
guidewords over the payment process (impersonated sender, changed bank details, manipulated file);
places only independent/effective/auditable preventive barriers on each line — rejecting "training"
and "policy" as barriers; builds the right side (recall, KYC/AML chain, insurance, incident
response); attaches escalation factors ("approver on vacation → delegate rubber-stamps") with their
own controls; and assigns every barrier an owner plus an assurance test, keeping the human gate —
people correct the draft, own barriers, and run the tests.

## 2. Near-miss (post-incident guard — should NOT load this skill)
> "A duplicate ACH file posted twice last Tuesday and we paid vendors double. Find out why it
> happened and make sure it never recurs."

Expected: a one-off cause hunt after an incident is
`continuous-improvement-skills:root-cause-analysis`, not a bowtie — the bowtie maps standing
defenses around a hazard, not the causal chain of one event. (Using the finished RCA to add a
missing barrier to an existing bowtie afterward is a legitimate follow-on.)

## 2b. Second near-miss (design-scoring guard — should NOT load this skill)
> "We're redesigning the payment-approval workflow. Score its failure modes — severity, occurrence,
> detection — so we know which ones to engineer out before go-live."

Expected: scoring failure modes of a process design is the FMEA discipline →
`continuous-improvement-skills:fmea` (cross-linked by name from this skill). Also guard the
adversarial-review variant: "poke holes in our treasury transformation plan" is
`continuous-improvement-skills:project-command-center`, not a bowtie.

## 3. Quality rubric
A good response:
- **Does:** one top event per bowtie; threat lines generated systematically from the guideword ×
  parameter matrix, not brainstormed; every barrier passes independent/effective/auditable; both
  sides drawn (preventive and mitigative); escalation factors attached with controls; every barrier
  carries an owner and an assurance test with cadence.
- **Teaches:** why guidewords beat brainstorming (systematic deviation defeats the imagination
  limit); why policy/training are never barriers and where they belong (escalation-factor
  controls); why an untested barrier is scenery — the same doctrine as the library's failover rule.
- **Stays honest:** presents the ICI → Shell/Piper Alpha → CCPS lineage with its [snippet-only]
  provenance; states plainly that financial-services adoption is strong but controlled-measurement
  evidence is thin, offering the method on its structuring merits; keeps the human gate — the model
  drafts the bowtie in minutes, humans correct it, own the barriers, and run the assurance tests.
