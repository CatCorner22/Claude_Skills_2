# Evals — decision-science-skills:weak-signal-navigation

## 1. Positive trigger (should load the skill)
> "Monitoring has been out since last night and I can't tell whether the release
> actually went through — the dashboard is down and I don't trust the release notes.
> The client call is at 2pm and I have to say something about where we stand. Help me
> estimate blind."

Expected: skill loads and runs the wayfinding protocol. It names the blind spot and
the decision (what to tell the client, by 2pm); inventories cues across all five
classes — last known-good state (the final pre-outage reading), scheduled events that
must have fired (the deploy pipeline's completion artifacts, post-deploy jobs),
historical rhythms (how releases like this usually behave in the first hours), side
channels (error-report volume, support tickets, commit/rollback activity), and
absence of expected noise (no incident pages, no user complaints where complaints
would be loud); weights cues by independence (traces which ones share a source) and
reliability grade; states a fused position WITH a confidence band, not a bare verdict;
runs the navigator's commentary naming the cue the position leans on hardest and how
it would fail; and defines what reading will confirm or deny the position when
monitoring returns, with the calibration check logged.

## 2. Near-miss (should NOT load this skill)
> "Give me a quick back-of-the-envelope figure: roughly how many support tickets does
> a 200-customer product generate in a month? Just ballpark it with optimistic and
> pessimistic bounds."

Expected: `math-foundations-skills:number-sense-and-estimation` owns this — a solo
Fermi bounding of a static quantity (decompose → bound → triangulate). There is no
downed instrument, no streaming cues, no continuously re-estimated belief. If this
skill loads on a static-quantity ballpark, its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Our transaction logs keep surprising us. Set up something that automatically flags
> unusual patterns — isolation forest or robust z-scores, tuned so we aren't flooded
> with false positives."

Expected: `machine-learning-skills:anomaly-detection` owns building and tuning
detectors. That request is about constructing a permanent instrument; this skill is
for operating WITHOUT one. The seam runs the other way too: if a weak-signal outage
recurs on schedule, this skill's own guidance is to hand off to detector-building.

## 3. Quality rubric
A good response:
- **Does the task:** names the blind spot and the decision that needs the position;
  inventories cues against all five classes rather than grabbing the two loudest;
  traces each cue to its source and collapses correlated cues into one independence
  group; grades reliability (strong/moderate/weak) and lets weak cues count only in
  aggregate; states the position as a range with an explicitly justified confidence
  word; delivers the three-sentence navigator's commentary (the lean, the failure
  story, the watch); re-estimates when the user adds or kills a cue mid-conversation;
  and writes the confirm/deny line plus a calibration log entry for when the
  instrument returns.
- **Teaches:** explains the etak mental model honestly (moving reference island,
  position held as a relationship, not a coordinate — Lewis/Hutchins, documented);
  why graceful degradation comes from many weak independent cues rather than one
  strong instrument; why independence, not cue count, is what raises confidence; why
  absence-of-noise is evidence only where trouble would have been loud; and why the
  commentary makes a wrong position legible instead of discrediting the method.
- **Stays honest:** keeps the [snippet-only] provenance mark when citing the Hokule'a
  voyage or Piailug details; never manufactures cues the user didn't confirm exist;
  widens the band or says "low confidence" when the cue set is thin instead of
  faking precision; routes single-quantity base-rate work to
  `decision-science-skills:reference-class-forecasting` and detector-building to
  `machine-learning-skills:anomaly-detection`; and keeps the decision itself with the
  human — the skill delivers a position, not a verdict.
