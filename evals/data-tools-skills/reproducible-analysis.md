# Evals — data-tools-skills:reproducible-analysis

## 1. Positive trigger (should load the skill)
> "Our quarterly capacity study came out different when a colleague reran it last week
> — the headline number moved and nobody changed anything on purpose. Can someone
> rerun this and get the same numbers? Make it reproducible."

Expected: skill loads; defines reproduce vs replicate (Claerbout usage) at the top of
the deliverable; hunts the classic drift sources — seedless randomness, unpinned tool
versions, hand-edited raw or derived files, pasted numbers, an undocumented manual
step; climbs the ladder: environment pinned and seeds recorded in the output, a
one-command rerun with any unscriptable step written down, raw → cleaned → derived
lineage with raw never edited in place (folder mechanics deferred to
`data-tools-skills:data-file-hygiene`), literate analysis so the headline number is
generated not pasted; closes with the verification ritual — fresh-clone rerun plus a
second person independently re-deriving the headline number, both logged — citing the
second-keeper pattern from `safety-and-reliability-skills:split-tally-evidence`.
Python-environment mechanics routed to `coding-agent-skills:python-for-analysts`, not
re-taught.

## 2. Near-miss (code-correctness guard — should NOT load)
> "Set up testing for our FastAPI app — what should we cover at unit vs API vs
> end-to-end level, and how do we stop the suite being so brittle?"

Expected: `full-stack-dev-skills:testing-strategy` territory — proving code behaves as
intended, test levels, fixtures, e2e selection. No analysis, no headline number, no
rerun-by-a-stranger question. Tests catch broken behavior; this skill catches an
analysis that cannot be rebuilt — different failure, different discipline.

## 2b. Near-miss (file-craft guard — should NOT load)
> "Help me pick a file naming convention and folder structure for the monthly
> extracts, and tell me what's safe to commit versus what needs sanitizing first."

Expected: `data-tools-skills:data-file-hygiene` territory — naming, foldering,
raw/processed separation as file craft, and sanitization before sharing. No
same-numbers-twice claim is being made or audited. Reproducible-analysis *mandates*
the separation but does not own the naming and sanitization mechanics.

## 3. Quality rubric
- **Does**: states the reproduce/replicate definitions before anything else; pins
  environment and seeds (recorded in the output, not a side note, and not only for
  Python); produces a one-command rerun with numbered manual steps for the genuinely
  unscriptable; enforces one-directional lineage with the regenerate invariant
  (delete downstream of raw, rebuild identically); makes every headline number
  generated in place; applies FAIR at working level; runs and logs both verification
  checks — fresh clone and second-keeper re-derivation; examples span analyst,
  attorney, ops, and developer cases, not one domain.
- **Teaches**: why definitions come first (the ACM's seven backwards years); why every
  manual click is an invisible parameter; why raw is never edited (audit trail + the
  regenerate invariant die together); why the author's own rerun is not verification
  (blind spots rerun too — hence the second keeper); the crisis literature as the why,
  the ladder as the how.
- **Stays honest**: Ioannidis presented as a model, not a measurement (Goodman &
  Greenland critique named), with the mechanisms taught as the solid core; OSC-2015
  reported with both numbers (97% vs 36%, ~half effect sizes), the Gilbert et al.
  dispute acknowledged, and "36% replicated" never flipped into "64% false";
  [snippet-only] provenance marks preserved on Claerbout/ACM/Plesser, Knuth,
  Wilkinson, Sandve, and the crisis claims; no invented statistics; Gage R&R
  "reproducibility" flagged as a different technical sense, not conflated.
