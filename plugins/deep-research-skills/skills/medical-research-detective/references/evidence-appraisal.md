# Evidence appraisal

Read at stage 5. How to judge what a source is worth, so a compelling story never outruns its
evidence.

## Contents
- [The evidence hierarchy](#the-evidence-hierarchy)
- [Study designs and what each can prove](#study-designs-and-what-each-can-prove)
- [GRADE-lite: assigning confidence](#grade-lite-assigning-confidence)
- [Reading the statistics](#reading-the-statistics)
- [Quality red flags inside a study](#quality-red-flags-inside-a-study)
- [Venue quality and predatory journals](#venue-quality-and-predatory-journals)
- [Retraction and correction checking](#retraction-and-correction-checking)
- [Conflicts of interest and funding](#conflicts-of-interest-and-funding)
- [Weighing a body of evidence](#weighing-a-body-of-evidence)

## The evidence hierarchy

Strongest to weakest, for questions about whether something *causes* or *treats* something:

1. **Systematic review / meta-analysis** of well-conducted randomized trials
2. **Randomized controlled trial (RCT)** — large, well-designed, pre-registered
3. **Prospective cohort study** — follows people forward over time
4. **Case-control study** — works backward from outcome to exposure
5. **Cross-sectional study** — a snapshot; shows association, cannot establish sequence
6. **Case series / case report** — documents that something happened, in a few people
7. **Mechanistic, in-vitro, or animal study** — shows a pathway is possible in a model
8. **Expert opinion, narrative review, editorial** — useful orientation, not evidence of effect

The hierarchy is a default, not a law. A large, consistent cohort can outweigh a small, flawed RCT,
and for questions about *harms* (rare adverse effects), observational data and case reports are often
the only ethical evidence that exists — a well-documented case series of a drug reaction is
meaningful even though it sits low in the table.

**The rule that matters most here:** a dot-connection resting on levels 6–7 is a **Lead**. It says
"this is possible and someone documented it," not "this is what happened."

## Study designs and what each can prove

| Design | Can establish | Cannot establish | Watch for |
|---|---|---|---|
| RCT | Causation, within its population | Generalization beyond the enrolled group | Narrow inclusion criteria; short follow-up; surrogate endpoints |
| Prospective cohort | Strong association, correct time order | Causation (confounding remains) | Loss to follow-up; unmeasured confounders |
| Case-control | Association, efficiently for rare outcomes | Time order, incidence | Recall bias; how controls were chosen |
| Cross-sectional | Prevalence, correlation | Which came first | Reverse causation |
| Case report/series | That a phenomenon occurs | How often, or that it generalizes | Publication favors the dramatic |
| Mechanistic/animal | Biological plausibility | That it happens in humans at real doses | Doses far above human exposure; species differences |

**Association is not causation** — the standing caution. Strength, consistency across studies,
dose–response, correct temporality, and biological plausibility all raise confidence; none alone
establishes cause.

## GRADE-lite: assigning confidence

Assign every claim in the case file a confidence grade, and state the basis:

| Grade | Criteria |
|---|---|
| **High** | Consistent findings from systematic reviews or multiple good RCTs; large effect; directly applicable |
| **Moderate** | One good RCT, or several consistent large observational studies; minor limitations |
| **Low** | Small, few, or conflicting studies; observational only; indirect population or outcome |
| **Very low** | Case reports, mechanistic reasoning, or expert opinion only |

Downgrade for: inconsistency between studies, small samples/wide confidence intervals, indirectness
(different population, dose, or outcome than the question), and likely publication bias. Upgrade
observational evidence for: a very large effect, a clear dose–response relationship, or when
plausible confounding would have *reduced* the observed effect.

Report the grade next to the claim, not in a footnote — the reader needs to see the strength at the
moment they read the assertion.

## Reading the statistics

Enough numeracy to avoid the standard traps:

- **Absolute vs. relative risk.** "Doubles the risk" is meaningless alone. If risk goes from 1 in
  10,000 to 2 in 10,000, the relative risk increase is 100% (RR = 2.0) and the absolute risk increase is 0.01%. **Always
  give both**, and give the base rate.
- **Confidence intervals.** Width is the message: a 95% CI of 1.8–2.2 is a precise estimate; 1.01–14.5
  is barely distinguishable from noise. A CI for a ratio that **crosses 1.0** is not statistically
  significant, whatever the point estimate looks like.
- **p-values.** p < 0.05 means "unlikely under the null," not "important" or "true." It says nothing
  about effect size, and it is heavily gamed.
- **Effect size and NNT.** Statistically significant ≠ clinically meaningful. Number needed to treat
  (or harm) translates an effect into human terms: NNT 8 is a strong treatment; NNT 400 usually is
  not, whatever the p-value.
- **Multiple comparisons / p-hacking.** Testing many outcomes guarantees some "significant" results
  by chance. Prefer pre-registered primary outcomes; be suspicious when the headline finding is a
  subgroup or a secondary endpoint.
- **Surrogate endpoints.** A drug that improves a lab number has not been shown to improve how
  someone feels, functions, or survives. Say which was measured.
- **Sample size.** A dramatic finding in 12 people is a hypothesis.
- **Publication bias.** Positive results are published far more often than null ones; a literature of
  small positive studies with no null studies is a warning sign. Check trial registries for
  registered-but-unpublished studies.

## Quality red flags inside a study

- No control or comparison group where one was feasible
- Not pre-registered, or reported outcomes differ from the registered ones (outcome switching)
- High dropout, or dropouts excluded from analysis rather than intention-to-treat
- Unblinded assessment of a subjective outcome
- Conclusions in the abstract that the results section does not support
- Composite endpoints where a single mild component drives the whole effect
- Extrapolation from animal doses far beyond human exposure
- Very short follow-up for a chronic condition

## Venue quality and predatory journals

Predatory journals publish for a fee with little or no peer review, and they are indexed by broad
search tools. Signals to check before trusting a source found only in a general web search:

- Is the journal **selected for MEDLINE**, or listed in the **DOAJ**? Absence is a caution flag.
  MEDLINE selection is a real quality screen — a committee reviews the journal against
  published criteria. Being *in PubMed* is not the same thing: PubMed also carries whatever a
  PMC-depositing journal sends, which is how predatory content reaches it. Check the journal in
  the NLM Catalog and look for "Currently indexed for MEDLINE", rather than reading a PubMed
  hit as a quality signal.
- Does the publisher belong to a recognized body (e.g. COPE membership)?
- Is there a real editorial board with identifiable, relevant experts?
- Does the site promise implausibly fast review, or spam solicitations?
- Does the journal name closely mimic a well-known title?

A finding published only in a questionable venue is not evidence; treat it as an unverified lead and
say so. Preprints are a different category: legitimate but **not yet peer-reviewed** — label them as
preprints explicitly and check whether a peer-reviewed version has since appeared.

## Retraction and correction checking

**Always check before citing.** Retracted papers keep circulating and keep getting cited for years,
and in medicine that propagates directly into harm.

Check by: looking for a retraction/expression-of-concern notice on the publisher's page and in the
PubMed record (which flags "Retracted Publication" as a publication type), and searching retraction
databases for the DOI/PMID. `scripts/verify_citation.py` does the machine-checkable part of this on
every lookup: it reads PubMed's publication types, the Crossref `updated-by` annotations (Crossref
carries the Retraction Watch database, refreshed on working days, so a DOI check sees a retraction
even though the retracted record keeps its original title), and any retraction marker anchored at the
start of the title. A clean result is still only as current as those records — a notice issued this
week may not have propagated, so check the publisher page for anything load-bearing.

Also check for **corrections/errata** — a paper can stand while a key number in it does not; the
script reports these separately, as a note rather than a failure. If a retracted paper is nonetheless
historically important to the story, you may mention it *labeled as retracted*, never as support for
a claim.

## Conflicts of interest and funding

Look at who funded the study and what the authors disclose. Industry funding does not invalidate a
study — much good research is industry-funded — but it is associated with more favorable results, so
it is context the reader deserves. Note it when the funder has a direct stake in the outcome, and
give more weight to independently funded replications. The same goes for author conflicts on
guideline documents and reviews.

## Weighing a body of evidence

Individual studies matter less than the pattern across them:

1. **Consistency** — do independent groups, in different populations, find the same thing?
2. **Totality** — is the claim supported by the whole literature, or by the two studies that agree
   with it? Actively look for the studies that disagree.
3. **Recency and supersession** — has a later, larger study overturned an older one? Forward citation
   chaining is how you find out.
4. **Directness** — was the studied population, dose, and outcome actually the one in question?
5. **Coherence** — does the claim fit with what else is known physiologically?

When the evidence genuinely conflicts, say so and characterize the disagreement, rather than picking
the side that fits the hypothesis. "Two large cohorts found X; a 2019 RCT did not replicate it" is a
more useful sentence than a confident conclusion in either direction.
