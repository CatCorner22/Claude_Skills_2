---
name: medical-research-detective
description: >-
  Investigates health questions across published medical literature — multi-database searches
  (PubMed, Europe PMC, Cochrane, Google Scholar), connecting dots between seemingly unrelated
  symptoms, drugs, labs, and exposures to surface overlooked common causes, filtering sources by
  country of origin, and triple-checking every citation so nothing is fabricated. Produces a
  graded case file: ranked hypotheses, evidence for and against, questions and tests for a
  clinician, red flags, and gaps. Research only — never diagnosis, dosing, or treatment
  advice. Use for a puzzling symptom cluster, a suspected drug or nutrient interaction, a
  condition that resists explanation, a second-opinion literature review, or verifying a
  medical claim or citation. Triggers: medical research,
  research my symptoms, connect these symptoms, what could link, overlooked cause, deep dive on
  this condition, PubMed, Google Scholar, medical literature, drug interaction research, verify
  this study, check this citation.
metadata:
  version: "1.9.0"
---

# Medical research detective

Investigates the published literature the way a detective works a case: gather every fact, generate
rival hypotheses, hunt the connections nobody made because the findings live in different
specialties, then verify every citation before it reaches you.

**This is research, not medical care.** It produces literature and questions to take to a licensed
clinician. It does not diagnose, does not recommend starting/stopping/changing any treatment, and
does not give doses. See `references/output-format.md` for the standing safety framing.

## When to use
- A cluster of symptoms, labs, or diagnoses that nobody has tied together, or a condition that
  resists explanation — "what could link all of these?"
- Hunting an overlooked common cause: a drug or nutrient interaction, a side effect that mimics a
  new disease, an exposure, a deficiency, a "great imitator" condition.
- A deep literature review on a condition, drug, or test — far past first-page search results.
- Verifying a medical claim, study, or citation someone handed you (including one produced by an AI).
- Not for: general non-medical research → use the built-in `deep-research` skill. Diagnosis, dosing,
  or "what should I take" → that is a clinician's job; this skill reframes the question into research
  plus questions to ask them. An emergency → stop and use the red-flag list in
  `references/output-format.md`, which routes to urgent care.

## Do it
Screen for urgency (stage 0), then work the case in seven stages. Depth is the point: a shallow pass is the failure mode. Do not stop at
the first plausible answer — the whole value is in stage 2 and the disconfirmation pass in stage 5.

0. **Screen for urgency before anything else.** Read the presented findings against the red-flag
   list in `references/output-format.md` *first* — before framing, before hypotheses, before a
   single search. If any red flag is present, **say so as the first thing in the reply, name
   which one, and tell the user to seek care now**; do not lead with a differential, and do not
   make the urgent-care note the eleventh item of a stage-7 report the user may never scroll to.
   Research and urgency are not alternatives — offer to continue the research afterwards, and
   continue it if they want, but the routing comes first. This skill is slow by design and its
   users bring real presentations; a seven-stage investigation is the wrong shape of answer to a
   time-critical one, and being right three thousand words later is not being right.

1. **Frame the case.** Collect what is actually known before searching: the findings (symptoms, labs,
   imaging, diagnoses) with **onset dates and sequence**; every drug, supplement, and dose change
   with *when it started*; relevant history, exposures, diet, family history; what has already been
   ruled out and *how*. Restate it back as a case summary and name the specific question(s) the
   research must answer. Ask the user for missing anchors rather than assuming them — especially
   timing, which is where most dot-connections hide.

2. **Generate rival hypotheses before searching.** Write a differential *first*, so the search tests
   ideas instead of confirming one. Run **all eight** generators in
   `references/dot-connection-method.md`, including the ones that feel unlikely: (1) one unifying
   cause; (2) two coincident common conditions — the standing rival to (1); (3) iatrogenic — a drug,
   supplement, interaction, or prescribing cascade; (4) deficiency or excess; (5) mechanism-chaining
   (X depletes Y → Y is needed for Z → the finding); (6) "great imitators" and commonly-missed
   conditions; (7) temporal/exposure — what changed before onset; (8) the negative-space question —
   what has never actually been tested, which converts directly into a stage-7 recommendation. Then
   apply the base-rate check (a common disease presenting oddly beats a rare one presenting
   typically) and aim for at least 5–8 candidates, the boring ones included. This is the medical
   edition of a domain-general discipline: `decision-science-skills:competing-hypotheses-analysis`
   owns the full hypothesis-matrix method (judge by disconfirmation, never by accumulation), and the
   base-rate check is `math-foundations-skills:probability-fundamentals` applied to disease
   frequency.

3. **Build an explicit search strategy.** For each hypothesis, write the PICO-style question, then
   the query: MeSH terms plus free-text synonyms (drug generic *and* brand, symptom lay term *and*
   clinical term), boolean structure, and date/language limits. Plan the co-occurrence searches that
   do the dot-connecting — searching finding A **AND** finding B together is what surfaces the paper
   nobody in either specialty read. See `references/search-strategy.md`.

4. **Search wide, then chase citations.** Run each query across multiple databases (they index
   different journals): PubMed/MEDLINE, Europe PMC, Cochrane, Google Scholar, ClinicalTrials.gov.
   `${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/search_pubmed.py` runs the PubMed pass and returns structured hits. Then **chain**:
   backward through the reference lists of the best papers, forward through "cited by" to newer work.
   Apply the country-of-origin policy from `references/source-provenance.md` as you go — allowed
   sources support conclusions; excluded-country sources go to the quarantine appendix and never
   support a claim. Country is **not** in search results; it comes from author affiliations, so run
   `verify_citation.py` on the hits you keep and read its provenance line. Keep searching until new
   queries stop returning new papers (saturation), not until you have "enough."

5. **Appraise, then try to kill each hypothesis.** Grade every source by study design, size, and
   quality using `references/evidence-appraisal.md`; check for retraction and predatory venues.
   Then invert: for each surviving hypothesis, actively search for the evidence that would
   **disconfirm** it and report what you find. A hypothesis that survives a real attempt to kill it
   is worth far more than one that merely accumulated supporting hits.

6. **Triple-check every citation.** Before any citation reaches the output it must pass all three
   checks in `references/citation-verification.md`: (a) it **exists** (DOI/PMID resolves),
   (b) its **metadata matches** (title, authors, journal, year), and (c) the source **actually
   states the claim** you attached to it — quote the supporting sentence. Run
   `${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/verify_citation.py` on each DOI/PMID. A citation that fails any check is removed, not
   softened. If verification is impossible (no network, paywalled full text), label the claim
   **unverified** and say exactly what could not be checked.
   - **Read the tool's three-state answers as three states.** Each check returns pass, fail, or
     *unknown*, and unknown is not a quiet pass. `PROVENANCE PARTIAL` / `UNRECOGNIZED` /
     `UNKNOWN` mean an affiliation did not resolve — including one institution inside a
     multi-site string whose other institutions did — so the country question is still open and
     you resolve it from the paper. `RETRACTION STATUS UNVERIFIED` means the Retraction Watch
     feed never answered for that record and the only evidence was publication-type metadata,
     which lags a notice by weeks; check the publisher page before relying on the source. The
     tool is built to fail toward "look at this," so treating an unknown as a pass converts its
     one designed safety margin into the failure it was margin against.

7. **Assemble the case file.** Produce the structure in `references/output-format.md` using
   `assets/case-file-template.md`: plain-language summary first, then hypotheses ranked with
   confidence grades and evidence for *and* against, the dot-connections with their strength, the
   questions and candidate tests to bring to a clinician, red flags, open gaps and what would close
   them, the excluded-sources appendix, and the full verified reference list. Lead with what a
   non-specialist can act on; keep the technical grading beneath it (audience-first structure is
   `writing-skills:explanation-design`'s method — concrete first, curse-of-knowledge stripped).

## Why / learn
The reason ordinary search fails on hard cases is **specialty siloing**: the cardiology literature
describes finding A, the gastroenterology literature describes finding B, and no paper contains both
because no author was looking at both. A search engine matches your words against single documents,
so it can only return what someone already wrote down together. Dot-connection is therefore not a
better query — it is a different *move*: you hypothesize the bridge (a shared mechanism, a drug, a
deficiency, a single upstream cause), then search for the bridge itself, then search the two findings
in the same query to see whether anyone ever noticed. That is why stage 2 comes before stage 3.

**Hypotheses must precede searching** for the same reason a detective names suspects before combing
evidence: search is a confirmation machine. Type in one idea and the literature will happily supply
support for it, because with millions of papers something supports almost anything. Writing rivals
first, then actively trying to *kill* each one, is what converts searching into investigating. The
strength of a conclusion comes from what survived attack, not from how many hits agreed.

**The evidence hierarchy is what keeps a good story honest.** A mechanism that *sounds* compelling —
this drug depletes that nutrient, which explains that symptom — is a lead, not a finding. Case
reports and animal studies generate hypotheses; cohorts and trials test them; systematic reviews
weigh them. Reporting a case-report-grade link with trial-grade confidence is the single most
damaging thing this kind of research does, because it sends someone to their doctor certain about
something that was never established. Hence grading every link and saying plainly which are leads.

**Citation verification is the anti-hallucination guarantee**, and it matters most precisely here.
A fabricated or misattributed citation in a medical context can drive a real decision about a real
body. Language models are fluent at producing citation-shaped text — plausible authors, plausible
journal, plausible year — that resolves to nothing. The only defense is mechanical: resolve the
identifier, compare the metadata, and confirm the source actually says it. Verification is cheap;
being confidently wrong about someone's health is not. The same asymmetry drives the
country-provenance policy: it is a source-integrity control about verifiability and known
data-integrity risk in parts of the literature, not a judgment about any nation's people or
scientists.

## Common mistakes
- Searching before writing a differential → confirmation bias; you find support for whatever you
  typed. Write rival hypotheses first.
- Stopping at the first plausible explanation → the overlooked cause is usually the fifth idea, not
  the first. Push to saturation.
- Treating a mechanism as proof ("X depletes Y, so X caused Z") → mechanisms are leads; label them as
  such until a clinical study supports the link.
- One database only → PubMed, Europe PMC, Cochrane, and Google Scholar index different things; a
  single-source search silently misses whole literatures.
- Ignoring timing → onset sequence is often the decisive clue; a symptom that began three weeks after
  a new prescription is a different case than one that predates it.
- Citing an abstract you did not read past → the abstract frequently overstates the finding. Verify
  the claim against the actual text and quote it.
- Presenting relative risk without absolute risk ("doubles your risk") → meaningless without the base
  rate. Give both.
- Letting an unverifiable citation through with a hedge → remove it or label it unverified; never let
  it sit alongside verified ones.
- Drifting into advice ("you should stop taking…") → stay on the research side; convert every
  actionable impulse into a question or a test to raise with the clinician.

## Tailor to your environment
Record your setup in `references/your-environment.md`: conditions or drugs you research repeatedly,
your preferred databases, whether you have institutional/library full-text access (which changes how
much of stage 6's claim-check can be done), your preferred reading level and output length, and any
standing country/journal preferences beyond the defaults.

**Privacy matters more here than anywhere else in this library.** Personal health information —
yours or anyone else's — belongs in `references/your-environment.private.md`, which is git-ignored,
never in a committed file. Keep only sanitized, structural examples in version control. When a case
involves a real person, work from de-identified facts (ages as ranges, no names, no dates of birth,
no record numbers).

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/medical-research-detective.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/dot-connection-method.md — the detective methodology: hypothesis generators, cross-silo bridging, disconfirmation
- references/search-strategy.md — databases, MeSH/synonyms/PICO, boolean, citation chaining, Google Scholar technique
- references/evidence-appraisal.md — evidence hierarchy, study designs, GRADE-lite grading, statistics literacy, retraction and predatory-venue checks
- references/citation-verification.md — the triple-check protocol and the anti-fabrication rules
- references/source-provenance.md — country-of-origin policy, how provenance is determined, the quarantine tier
- references/output-format.md — case-file structure, confidence grades, red flags, safety framing
- references/your-environment.md — your conditions, databases, access, and preferences (add when supplied)

## Scripts
> Paths use `${CLAUDE_PLUGIN_ROOT}` so they resolve from **any** working directory once the
> plugin is installed. A bare `scripts/…` path only works inside a clone of the marketplace
> repo, which is not where a user runs these.
- `${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/search_pubmed.py` — searches PubMed via the free NCBI E-utilities API; returns structured hits (PMID, DOI, title, first author, journal, year, publication type, retraction flag) as text or JSON, ranked by evidence hierarchy. Country of origin is **not** in PubMed's summary metadata — run `verify_citation.py` on the hits you keep to do the stage-4 affiliation-country pass. `--help` for options; no API key required.
- `${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/verify_citation.py` — resolves a DOI or PMID against Crossref/PubMed/Europe PMC, returns canonical metadata, compares it to a claimed title/author/year, and flags mismatches, excluded-country provenance, and retractions. Provenance and retraction are **three-state** (pass / fail / unverified), because Europe PMC's endpoint is a search rather than a lookup and the Retraction Watch feed does not answer for every record; an "unverified" is a question for you, not a pass. `--self-test` runs the offline logic tests (104 checks).
