# Evals — coding-agent-skills:software-archaeology

## 1. Positive trigger (should load the skill)
> "I inherited this service. Its `conf/` directory has ~300 files in three different
> naming styles, plus a `deprecated/` folder nobody trusts enough to delete. Before we
> migrate, dig into this legacy — which of these are dead?"

Expected: skill loads; bounds the site (the `conf/` tree, grain = file) and the strata
question (removal candidates ahead of a migration); harvests dating evidence with
version-control history and reference direction ranked above filesystem timestamps; emits
a draft Harris matrix as a Mermaid `flowchart TB` (newest era on top, dashed edges marked
unverified) and asks the human to correct it; names the eras from evidence signatures;
classifies every artifact living floor / fill / rubble against the evidence bars, with
insufficient-evidence artifacts defaulting to fill; treats the `deprecated/` label as a
claim, not evidence, and checks whether anything living still reads into that folder;
proposes the scream test for rubble only — reversible disable, window sized to each
artifact's usage rhythm, listener and rollback named — citing the documented ~15%
scream rate `[snippet-only]` as the reason to test even the "obviously dead"; ends with
a site report. Nothing is deleted before it is recorded, and nothing is deleted as the
test itself.

## 2. Near-miss (single-incident guard — should NOT load)
> "The nightly import job crashed at 2am and the queue backed up. Why did this happen?"

Expected: `continuous-improvement-skills:root-cause-analysis` territory — one failure,
one causal chain, containment then 5 Whys. Excavation reconstructs a whole deposit's
history so safe demolition is possible; it does not explain last night's incident.

## 2b. Near-miss (one-fence guard — should NOT load)
> "We're designing a new export feature — the team wants a message queue but I suspect a
> cron job would do. Is this overengineered?"

Expected: `coding-agent-skills:soviet-space-graphite` — a simplicity challenge on a new
build, with its Graphite Test carrying the single-fence Chesterton check. Software
archaeology is the whole-site method for accreted systems with hundreds of fences, not a
design-simplicity pass on something being built now.

## 3. Quality rubric
- **Does**: bounded site and grain; dating by convergence of at least two independent
  evidence lines; a relationship graph (not just a file list) in the house Mermaid
  conventions with uncertain edges dashed; named eras each backed by two evidence lines;
  layer classification meeting the evidence bars; scream test with reversible disable,
  rhythm-sized window, named listener, rollback plan, and archive-before-delete; a filed
  site report.
- **Teaches**: the law of superposition translated to software (override/wrapper/migration
  = later); why usage is the only authority on use (labels, docs, and owners all lie);
  why record-before-remove is Chesterton's fence systematized for whole sites; why the
  documented ~15% scream rate justifies testing even unanimous "it's dead" claims.
- **Stays honest**: provenance marks (`[snippet-only]`) preserved on the Harris/Reinhard/
  Hunt & Thomas/Microsoft claims; no invented percentages beyond the sourced ones;
  insufficient evidence classified FILL, never RUBBLE; the assistant's draft matrix
  presented as a hypothesis for human correction, not as ground truth.
