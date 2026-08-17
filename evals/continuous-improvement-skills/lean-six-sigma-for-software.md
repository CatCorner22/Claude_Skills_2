# Evals — continuous-improvement-skills:lean-six-sigma-for-software

## 1. Positive trigger (should load the skill)
> "We're building a payment-posting module for our practice-management users — they live in
> Curve Hero all day. I want this run with real Lean Six Sigma discipline: define what done
> means up front, get actual front-desk staff designing it with us, make the UI accessible and
> familiar to them, and beat on it hard before we ship."

Expected: skill loads; defines the measurable end state first (charter, CTQs, DMADV since it's
a new build); plans gemba observation + co-design with the actual front-desk doers; runs the
reference-product sync audit of step 3 itself (harvesting the target product's vocabulary
with the verify-in-the-live-product caveat, marking unverified terms — no co-load expected;
the worked dental map is archived); designs to the token-based WCAG 2.2 AA system; sets delivery-metric
control charts; schedules the adversarial gauntlet (property tests on money math, hostile-UX
sweep, STRIDE) and sizes stability/redundancy to an SLO; closes with a control plan and
standardization step.

## 2. Near-miss (should NOT load this skill)
> "Our month-end close process keeps slipping — can you DMAIC it? It's all manual journal
> entries and spreadsheet handoffs, no software build involved."

Expected: a non-software process improvement —
`continuous-improvement-skills:dmaic-problem-solving` handles it. If lean-six-sigma-for-software
loads on generic DMAIC asks with no software delivery component, tighten the description.

## 2b. Near-miss (greedy-token guard)
> "Help me plan a co-design workshop with the front-desk team to improve our patient-intake
> process — PDSA cycles on the paper workflow, no app involved."

Expected: `continuous-improvement-skills:kaizen-and-codesign` owns facilitation of co-design
sessions and the generic PDSA-on-a-process ask. If lean-six-sigma-for-software loads here, its
"co-design"/"Deming"/"PDSA" trigger surface has grown too greedy — the skill's triggers are
deliberately software-qualified ("co-design the UI", "Deming for software delivery").

## 3. Quality rubric
A good response:
- **Does the task:** produces the charter/end-state definition with numbers; a co-design plan
  naming real doers; a terminology map synced to the reference product; UI work grounded in
  the token system with WCAG 2.2 AA gates in CI; delivery metrics control-charted with
  signal-vs-noise discipline; an adversarial pre-release gauntlet; stability patterns sized to
  an explicit SLO; and a control plan that standardizes the gains.
- **Teaches:** explains quality-from-the-system vs inspection (Deming), the TPS mapping it's
  using (jidoka/andon/poka-yoke in pipeline terms), why backward design converts "done" into a
  test, and why tampering with common-cause noise makes things worse.
- **Stays honest:** flags Curve Hero vocabulary as compiled-from-public-sources to be verified
  in the live product; never presents unverified UI terms as fact; keeps metrics aimed at the
  process, not individuals.
