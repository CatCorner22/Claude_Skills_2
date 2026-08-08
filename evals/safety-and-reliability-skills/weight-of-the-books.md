# Evals — safety-and-reliability-skills:weight-of-the-books

## 1. Positive trigger (should load the skill)
> "We're designing the new statement-archive service. It looked fine in the demo with a
> week of test data. Before we commit the schema — will it hold at real volumes? Run the
> weight of the books."

Expected: skill loads; builds the payload inventory (daily lines, retention horizon —
the archive carries every year kept, not a day's feed; the backfile conversion as a
special lot); demands measured numbers from real feed history, not estimates; traces
each load to a bearer with stated capacity and flags any un-owned load as the defect;
applies written factors with exhaustion dates; flags the partition/schema key as a
one-way door earning the largest margin; requires a loaded-test plan (largest real file
replay, quarter-end soak) and labels anything untestable an accepted unknown; delivers
the one-page signed Load Manifest with re-review triggers.

## 2. Near-miss (failure-imagination guard)
> "We're about to commit to the go-live plan for the archive service — assume it failed
> a year from now and tell me everything that could have sunk it."

Expected: `decision-science-skills:pre-mortem` owns broad prospective failure
imagination. Weight-of-the-books quantifies one failure class (payload omission) with an
artifact; if it loads on a general assume-it-failed ask, the seam is failing.

## 2b. Near-miss (post-failure math guard)
> "The archive service has failed four times since go-live — here are the failure
> timestamps; what's the MTBF and should we schedule replacements?"

Expected: `safety-and-reliability-skills:reliability-engineering` owns math on observed
failures (Weibull, MTBF). Weight-of-the-books is the before-commitment review; after
failures exist, the reliability skill takes over.

## 3. Quality rubric
- **Does**: complete payload inventory (the zero-load test for completeness); four
  numbers per load with sources; every load path named with capacity; written factors
  with exhaustion dates; loaded-test plan covering design/peak/special-lot; the signed
  one-page manifest.
- **Teaches**: category omission (the payload felt obvious, so it was never designed
  for); peak-not-average; the tail cracks the slab; empty-building epistemics (a green
  suite on sample data validates the shell); retrofit economics and one-way doors.
- **Stays honest**: measures what can be measured instead of estimating; accepted
  unknowns stated plainly rather than claimed as passes; the commissioning legend held
  as assumed-true-as-given with the lesson standing either way; margins priced, not
  gold-plated everywhere.
