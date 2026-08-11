# Evals — safety-and-reliability-skills:sortition-review

## 1. Positive trigger (should load the skill)
> "Our expense approvals only get checked when somebody's already suspicious, and
> everyone knows which ones get looked at — the big round numbers. Also the same
> person has reviewed the same approver's work for three years. Design us a spot-check
> by lot that nobody can game and nobody takes as an accusation."

Expected: skill loads; defines the population as an enumerable list (the export/query
written down); sets the universal floor with no exemptions and names the generals test
(the director's lines are in); designs a verifiable lot (pre-committed seed or dice in
the open, with the could-the-operator-have-chosen test applied); draws reviewer pairs
by lot too and bars permanent reviewer-reviewee pairs; proposes the end-of-role
handover review as a universal default so departure carries no stigma; sizes the draw
to human adjudication capacity with the assistant doing the first pass of every drawn
item (drafts findings with quoted evidence; the human owns every judgment); publishes
the rule (population, odds, mechanics) while keeping individual draws quiet until done.

## 2. Near-miss (statistical-inference guard)
> "We pulled a random sample of 40 invoices and found 3 with errors — what does that
> say about the error rate in the full population, and how confident can we be?"

Expected: `data-analytics-bi-skills:statistical-inference` owns reasoning from a
sample to a population — confidence intervals, test choice, assumptions. sortition-
review designs the GOVERNANCE draw (who reviews, what is drawable, why nobody can rig
it), not the inference from its results. If it loads on an inference ask, the seam is
failing.

## 2b. Near-miss (adversarial-testing guard)
> "We want to run an exercise where a red cell plays a corrupt insider trying to
> sneak fraudulent approvals past our controls while the team responds."

Expected: `decision-science-skills:tabletop-wargaming` owns adversarial exercises with
a red cell, injects, and adjudication. sortition-review is selection design — it
builds the standing draw, not the adversarial rehearsal. If it loads on a red-team
ask, tighten the boundary.

## 3. Quality rubric
- **Does**: the population is enumerable with the enumeration itself written down and
  verifiable; the floor statement admits no exemptions, with stratified odds (never
  stratified eligibility) where volume demands; the lot mechanic passes both halves of
  the acceptance test (operator could not steer it; anyone can verify that afterward),
  with the commitment step predating population close; reviewers are drawn by lot from
  a stake-free pool, pairing history tracked, conflict rule stated in advance; the
  handover review triggers on the transition itself within a stated window; draw size
  is bound by human adjudication capacity, not assistant throughput; the rule is
  published, the draws are not.
- **Teaches**: the two controls kept distinct — universality defeats trigger-gaming
  and stigma (no rule to learn, no inference from being picked), interleaved
  randomness defeats capture (corrupting the pool vs. buying one gatekeeper, the
  Venice arithmetic); why exemptions are routing instructions for evasion and why the
  floor is only real if it covers the generals; why the lot's verifiability matters as
  much as its randomness (the ballotino drew blind and in public); why the clean
  record protects the reviewed, not just the reviewer.
- **Stays honest**: euthynai and Venice facts carried with their [snippet-only]
  provenance marks (Oxford Classical Dictionary / *Ath. Pol.* sourcing; the 1268
  protocol's rounds and 529-year run); no claim that sortition guarantees detection —
  it governs selection, not what a finding is; the human-adjudication gate stated as
  absolute (the assistant drafts findings, the human owns judgments — no consequence
  attaches on the assistant's say-so); no invented statistics about fraud rates;
  boundaries respected — sampling theory to statistical-inference, item substance to
  domain skills, adversarial play to tabletop-wargaming, control architecture to
  bowtie-barrier-analysis.
