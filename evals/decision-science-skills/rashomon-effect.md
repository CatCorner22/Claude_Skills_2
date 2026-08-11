# Evals — decision-science-skills:rashomon-effect

## 1. Positive trigger (should load the skill)
> "Three engineers wrote up Friday's outage and the write-ups contradict each other —
> everyone remembers it differently: one says the system was degrading before the
> deploy, one swears the canary proved the deploy clean, one blames a connection leak.
> Reconcile the statements."

Expected: loads the reconciliation protocol; takes (or asks for) each account whole and
separately before comparing, with contamination history noted (when written, what each
author had already heard); splits every account into observations / interpretations /
stakes with vantage attached; maps who could actually see what from where; states the
invariant core first; classifies each divergence (perspective / memory / stake / genuine
contradiction) and adjudicates only the genuine ones against logs and timestamps — never
by confidence or seniority; produces a reconciled account with confidence marks
([CORROBORATED]/[SINGLE-VANTAGE]/[INFERRED]/[FORK]) and files any unresolved fork at full
strength with the evidence that would close it.

## 2. Near-miss (rival-causes guard)
> "We've got three plausible causes for the outage — bad deploy, connection-pool
> exhaustion, upstream DNS. Build the matrix and tell me which explanation fits the
> evidence."

Expected: `decision-science-skills:competing-hypotheses-analysis` owns weighing rival
explanations against one body of evidence. This skill reconciles contradictory
testimonies into that body of evidence; if rashomon-effect loads on a pure
which-cause-fits ask with no contradictory accounts in play, the seam is failing.

## 2b. Near-miss (team-debrief guard)
> "The release is done — run us through the after-action: what was supposed to happen,
> what actually happened, what do we sustain and improve next time?"

Expected: `decision-science-skills:after-action-review` owns the four-question team
debrief. rashomon-effect is the tool the AAR reaches for only when its
what-actually-happened step hits hardened contradictions; it should not load on a
routine debrief ask.

## 3. Quality rubric
- **Does**: separate whole-account intake with cognitive-interview moves (report
  everything, context reinstatement, changed-order retelling) and contamination history
  recorded; three-layer split per account with vantage; vantage map; invariant core
  stated before divergences; every divergence classified with the named type; memory
  artifacts tied to a named mechanism (misinformation effect, leading question, delay);
  adjudication only of genuine contradictions, only against physical evidence or
  invariants; reconciled account with per-claim confidence marks; unresolved forks filed
  at full strength with closing evidence named.
- **Teaches**: Heider's scholarly meaning of the effect (good-faith divergence from
  observer circumstances, not lying); Loftus misinformation effect and the verb-choice
  study as the reason intake precedes comparison; the confidence-vs-accuracy relationship
  with the Wixted & Wells initial-confidence nuance stated with its conditions; Denzin
  triangulation as why independent convergence is warrant; why three witnesses who
  compared notes are one source.
- **Stays honest**: good faith remains the default hypothesis and bad faith is a
  conclusion earned with evidence; no dissenting detail silently dropped — the smooth
  single story is flagged as the failure mode; the film attribution stated correctly
  ("In a Grove" plot, "Rashōmon" title) and the "there is no truth" misreading corrected;
  provenance marks kept on the memory-science claims; adjudication never by confidence,
  seniority, or majority.
