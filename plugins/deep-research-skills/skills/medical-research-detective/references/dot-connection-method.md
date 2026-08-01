# The dot-connection method

Read at stage 2 (hypothesis generation) and stage 5 (disconfirmation). This is the intellectual core
of the skill — the part that separates investigation from search.

## Contents
- [Why dots go unconnected](#why-dots-go-unconnected)
- [The eight hypothesis generators](#the-eight-hypothesis-generators)
- [Building the finding matrix](#building-the-finding-matrix)
- [Bridge searching](#bridge-searching)
- [Base rates: horses before zebras](#base-rates-horses-before-zebras)
- [Disconfirmation: try to kill it](#disconfirmation-try-to-kill-it)
- [Grading a connection](#grading-a-connection)
- [Worked example](#worked-example)

## Why dots go unconnected

Three structural reasons, and each one implies a counter-move.

**Specialty siloing.** Finding A is described in the rheumatology literature; finding B in the
ophthalmology literature. No single paper contains both, because no author was looking at both. A
keyword search can only return documents that already contain your words together, so it structurally
cannot surface a link nobody wrote down. *Counter-move:* hypothesize the bridge, then search for the
bridge, then search A AND B together to see whether anyone ever noticed.

**Attribution closure.** Once a finding has an accepted explanation, investigation stops. A symptom
attributed to a known chronic condition gets filed under it forever, even when its timing does not
fit. *Counter-move:* re-open each finding and ask "what else causes this?" independent of the
existing label — especially where the timing is off.

**Single-agent thinking.** Clinicians and papers usually evaluate one drug, one exposure, one disease
at a time. Interaction effects — two drugs that are fine alone, a drug plus a deficiency, a condition
plus an exposure — fall between the papers. *Counter-move:* enumerate pairs and triples explicitly
(see the finding matrix below).

## The eight hypothesis generators

Run **every** generator deliberately at stage 2, even the ones that feel unlikely. Each is a distinct
way a set of findings can be related. Write down what each produces before you search anything.

1. **Single unifying cause.** Is there one condition that produces all or most of the findings? This
   is the classic detective move (parsimony). Search: the findings' co-occurrence, "syndrome,"
   "multisystem," "presenting features of."

2. **Two coincident conditions.** Sometimes there is no unifying cause and insisting on one is the
   error — especially with age or multiple risk factors, where having two common problems is more
   likely than one rare problem explaining everything. Always keep this on the list as the rival to
   generator 1.

3. **Iatrogenic / drug-caused.** Could a drug, supplement, or procedure be producing the findings?
   Include: direct adverse effects; **drug–drug interactions** (especially shared metabolic pathways
   such as CYP450 inhibition/induction); **drug–nutrient depletions**; withdrawal/rebound effects;
   and *prescribing cascades*, where a side effect is mistaken for a new disease and treated with
   another drug. Anchor on timing: what started, stopped, or changed dose before onset?

4. **Deficiency or excess.** Nutrients, electrolytes, hormones, and trace minerals — deficiency states
   are famously multisystem and famously missed, and they can be caused by diet, malabsorption,
   surgery, or drugs (which chains back to generator 3).

5. **Mechanism-chaining.** Build an explicit causal chain of two or three steps: X inhibits/depletes
   Y → Y is required for Z → loss of Z produces the finding. Chains are how you connect things that
   share no literature. They are also the most seductive form of reasoning here: a chain is a
   **lead**, never a conclusion, until a clinical study supports the endpoints (see
   `evidence-appraisal.md`).

6. **The great imitators and commonly-missed conditions.** Some conditions are notorious for
   presenting as something else across many specialties — endocrine, autoimmune, infectious,
   nutritional, toxic/environmental, and sleep-related causes are recurring offenders. Explicitly ask
   "which conditions are known to mimic this picture?" and search that phrasing directly; review
   articles on differential diagnosis and "diagnostic pitfalls" are written exactly for this.

7. **Temporal / exposure-driven.** What changed before onset — a move, a job, a home repair, water
   source, new pet, travel, season, a diet change, a new device? Environmental and occupational
   exposures are systematically under-asked in clinical encounters.

8. **The negative-space question.** What has *not* been tested or ruled out? Absence of a test is not
   absence of a disease. List which hypotheses have genuinely been excluded and by what evidence —
   often the gap is the answer, and it converts directly into a stage-7 recommendation.

## Building the finding matrix

Enumerating pairs is what makes cross-silo links visible. Lay findings on both axes and ask, for each
cell, "is there any literature linking these two directly?"

|  | Finding A | Finding B | Finding C |
|---|---|---|---|
| **Finding A** | — | search "A AND B" | search "A AND C" |
| **Finding B** |  | — | search "B AND C" |
| **Finding C** |  |  | — |

Then extend the same logic to drug × finding and exposure × finding. With five findings this is ten
pair-searches — tedious, and exactly the work that ordinary searching skips. Also run the triples
when a pair looks promising, since a specific three-finding combination often names a syndrome.

## Bridge searching

When two findings have no direct co-occurrence literature, look for a **shared node** — something
that connects to each of them separately:

- **Shared mechanism/pathway:** search "A" + pathway terms, then "B" + the same pathway terms.
- **Shared anatomy or system:** a single nerve, vessel, or organ that could produce both.
- **Shared drug:** any drug reported to cause A *and* reported to cause B.
- **Shared nutrient/electrolyte:** a deficiency reported in both.
- **Shared upstream condition:** a disease that lists both among its features.

If a shared node exists, you have a candidate bridge — a hypothesis to test, not an answer.

## Base rates: horses before zebras

Parsimony must be disciplined by prevalence, or the method degenerates into rare-disease pattern
matching. Two rules:

- **A common condition presenting atypically is more likely than a rare condition presenting
  typically.** Rank a candidate by (how common it is) × (how well it fits), not by fit alone.
- **Prefer explanations that are common, testable, and reversible.** A cheap blood test that could
  confirm a common deficiency outranks an exotic syndrome as a next step, even if the exotic syndrome
  fits marginally better — it costs little to rule out and is actionable if positive.

State prevalence context whenever you name a rare candidate, so the reader can weigh it properly.

## Disconfirmation: try to kill it

For each surviving hypothesis at stage 5, run this pass explicitly and report the results:

1. **What would we expect to see if this were true that we do not see?** Missing expected features
   are strong evidence against.
2. **What finding does this hypothesis fail to explain?** Note the residual; a hypothesis explaining
   3 of 5 findings should be labeled as such, not sold as complete.
3. **Does the timing actually work?** Check onset sequence and known latency. A cause that started
   after the effect is dead on arrival.
4. **Search for the contrary evidence deliberately.** Query for null results, failed replications,
   "no association," and any systematic review that examined the link. Report what you find even when
   it undercuts an attractive story.
5. **Is there a simpler explanation?** Re-test against generator 2 (two common conditions).

A hypothesis that survives this pass gets a materially higher confidence grade — and you should say
*why* it survived.

## Grading a connection

Label every dot-connection with its strength, using the evidence behind it (details in
`evidence-appraisal.md`):

| Grade | Means | Typical basis |
|---|---|---|
| **Established** | Well-supported in the literature | Systematic reviews / multiple consistent trials or large cohorts |
| **Supported** | Real signal, some consistency | One good trial or several consistent observational studies |
| **Emerging** | Preliminary, plausible, under-studied | Small or conflicting studies; large observational only |
| **Lead** | Hypothesis worth checking, not established | Case reports/series, mechanistic or animal data, plausibility only |
| **Speculative** | Reasoning-only, no direct evidence found | Chain built from separate literatures with no study on the link |

Never present a **Lead** or **Speculative** connection in language that implies causation. Say "no
study has tested this link directly; the reasoning is X, and the way to check it is Y."

## Worked example

*(Illustrative of method only — not a clinical claim.)*

**Findings:** fatigue (18 months), new numbness/tingling in both feet (4 months), mild anemia on
recent labs, long-standing reflux treated for years, metformin for type 2 diabetes.

**Generator 1 (unifying):** is there one condition producing fatigue + neuropathy + anemia? Yes —
several nutritional and endocrine candidates do exactly that.

**Generator 3 (iatrogenic) + 4 (deficiency) + 5 (chaining):** two long-term medications here are
independently associated with malabsorption of a nutrient whose deficiency classically produces that
exact triad. Chain: long-term acid suppression and metformin → reduced absorption of that nutrient →
deficiency → fatigue, peripheral neuropathy, and macrocytic anemia together.

**Cross-silo bridge:** the reflux is filed under gastroenterology, the neuropathy under neurology,
the anemia under primary care, the diabetes under endocrinology. Four silos; the connecting node is a
single nutrient. No one clinician's problem list makes it visible.

**Generator 2 (rival):** diabetes itself commonly causes peripheral neuropathy, and anemia has many
causes — so "diabetic neuropathy + unrelated anemia" is a serious competing explanation that must be
carried forward, not dismissed because the unifying story is prettier.

**Base-rate check:** both the deficiency and diabetic neuropathy are common. This is a horse, not a
zebra — which is a point in the hypothesis's favor and makes it worth checking early.

**Disconfirmation:** does the timing fit the medication history? Does the anemia's red-cell size match
the proposed deficiency or contradict it? Is there a documented normal level of that nutrient on
recent labs — and was it measured with a test sensitive enough to be trusted? Any of these could kill
it.

**Next step it produces:** not "take a supplement" — but "the literature links these medications to
this deficiency, which produces this triad; ask the clinician whether testing that nutrient (and the
related confirmatory marker) is warranted, and whether the anemia's indices fit."
