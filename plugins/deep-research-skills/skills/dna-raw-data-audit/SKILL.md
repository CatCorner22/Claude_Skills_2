---
name: dna-raw-data-audit
description: >-
  Audits a personal genome against the published literature — reads 23andMe and Nebula raw data,
  resolves which alleles the files actually support, grades each finding by evidence strength and
  array reliability, and reports risk in absolute terms beside relative. Covers pharmacogenomics,
  carrier status, supplements, medicines, peptides and lifestyle factors, and says plainly when a
  genotype changes nothing. Use for interpreting a DNA raw data file, checking what a gene variant
  actually means, or preparing a genetics question for a clinician. Research only — never diagnosis
  or dosing. Triggers: 23andme, nebula, my dna, raw genetic data, digital dna agent, my genome,
  genetic risk, apoe, mthfr, pharmacogenomic, carrier status, polygenic risk score.
metadata:
  version: "1.5.0"
  source: >-
    Built from an eight-stream research pass, then re-audited by a perspective-diverse adversarial
    pass that found defects in the shipped version and is the reason several claims here are
    narrower than they were. Citations are verified against retrieved index records, never a
    search tool's generated prose, and a claim attaches only to a record whose title was returned
    — a bare URL proves an identifier exists, not what it is. All arithmetic was recomputed by
    execution. See references/variant-catalog.md §0 for the standard, the anchored-figure
    carve-out, and every citation withdrawn on re-check.
---

# Digital DNA Agent — DNA raw-data audit

Takes a personal genome file, works out what it can and cannot actually establish, cross-references
the alleles that matter against the literature, and reports each finding with its evidence strength,
its absolute effect size, and what — if anything — a person should do differently.

**The discipline this skill exists to enforce.** Consumer genomics is dense with confident
interpretation that the underlying data does not support. The most common correct answer to "what
does this variant mean for me?" is *nothing you should act on*, and a skill that cannot say that
clearly is worse than no skill. So every finding here carries three separate things: what the data
supports, how strong the evidence is, and whether any action follows. Those are different
questions, and collapsing them is how genetic reports become horoscopes.

## When to use
- You have a 23andMe and/or Nebula raw data file and want to know what is genuinely in it.
- You have been told you carry some variant — APOE4, MTHFR, Factor V Leiden, a BRCA variant — and
  want the real effect size rather than a headline.
- You are preparing a genetics question for a clinician and want the findings organised so the
  appointment is useful.
- You want to know whether a medication, supplement, or lifestyle change is indicated by your
  genotype — including when the honest answer is that it is not.
- You want to know what your data *cannot* tell you, which for consumer arrays is most of it.
- Not for: a clinical symptom cluster or suspected drug interaction with no genome involved →
  `deep-research-skills:medical-research-detective`. Auditing a video's or article's genetics
  claims → `deep-research-skills:video-source-audit`. Training and nutrition protocols for a
  healthy person → `coding-agent-skills:fitness-nutrition-science`. A statistics question with no
  genome attached → `data-analytics-bi-skills:statistical-inference`.
- **Not a diagnostic service, and not a prescriber.** It produces research and questions, never a
  diagnosis, never a dose.

## Do it

Work the stages in order. Several can fail, and failing them honestly is the point.

1. **Set up privately, before reading anything.** A genome is the most identifying data a person
   has, it implicates biological relatives who did not consent, and it cannot be rotated like a
   password. Keep the file out of any repository, any shared drive, and any paste into a third-party
   service. **Do not assume any repository ignores these files — yours almost certainly does not.**
   The marketplace repository this skill ships from ignores the common genomic extensions, the
   download archives (`.zip`, `.tar.gz`) and a `genomes/` directory, but **that protection does not
   travel with the installed plugin.** Before a genome file goes anywhere near version control, run
   `git check-ignore -v <file>` and get a hit; if you do not, add the patterns first.
   `references/your-environment.md` carries the full posture.

   **And take a stance on where the report goes, because the deliverable's whole point — "take this
   to a clinician" — is the act that creates a medical record.** `your-environment.md` collects the
   insurance and employment concern and nothing consumed it. State plainly: a conversation with a
   clinician about a genetic finding can enter a medical record, the rules on what follows from that
   vary by jurisdiction and by insurance line, and **that is a reason to decide deliberately rather
   than a reason not to go** — the alternative is acting on unconfirmed consumer data alone. Where
   the person is unsure, a genetic counsellor is the right first conversation precisely because it
   can be had before anything is confirmed.

   **Also ask what has already been done.** The pipeline starts from the file and so assumes nobody
   has acted yet, which is often false: a methylfolate stack already being taken, a food group
   already avoided, a drug already stopped. Each changes the job from interpretation to
   **correction**, and a correction delivered without acknowledging what the person already did
   lands as a rebuke. `references/interventions-evidence.md` §4 works the methylfolate case.

2. **Identify what you actually have, and detect the build.** 23andMe exports and Nebula outputs are
   different data with different limits, and a position lookup against the wrong genome build
   silently returns the wrong variant. Detect rather than assume. Formats, build detection, and the
   array-versus-sequencing distinction: `references/data-formats-and-parsing.md` §1–2.

3. **Run the quality pass, and report it before any interpretation — starting with a blocking
   question: are these two files the same person?** A low concordance rate has two very different
   explanations, and conflating them wastes an audit: genotyping error, or **two different people**.
   Mislabelled kits, a relative's export and a file saved under the wrong name are all realistic.
   The test is **opposite homozygotes** — sites where the two files share no allele at all —
   restricted to autosomal, both-called, diploid, non-palindromic sites, because a palindromic site
   can appear to disagree purely from orientation. **If identity fails, stop and report that: an
   audit of two people's data merged as one is worse than no audit.** The bundled script implements
   this gate and refuses to judge it on too few overlapping sites.

   Then the rest of the pass: no-call rate, total sites, and concordance. Two platforms genotyping
   the same person is a genuine quality signal, and a discordant call at a site you were about to
   interpret is a finding in itself — the script reports such a site as discordant and takes **no**
   genotype from it. See **Scripts**. `references/data-formats-and-parsing.md` §5.

4. **Internalise what the file cannot answer, and say it up front.** An array probes a chosen subset
   of sites: a variant's absence from the file is *not* evidence of its absence from the person, and
   a negative consumer result is weak reassurance. Imputed genotypes are statistical inferences, not
   measurements, and imputation degrades precisely for the rare variants people most want checked.
   **A VCF adds its own version of this, and it is worse:** in a variants-only file a missing site is
   homozygous-reference *or* never covered, indistinguishably — so an APOE e3/e3 person, who is
   reference at both defining sites, is invisible in such a file. Never read a VCF's silence as a
   reference call, and never take a genotype from a gVCF reference block or a `DP=0` line.
   `references/data-formats-and-parsing.md` §3–4.

5. **Triage down to what could matter.** Hundreds of thousands of genotypes reduce to a handful that
   could change a decision. Work the funnel in `references/variant-triage.md`: start from the curated
   catalogue of variants with established effect sizes rather than scanning everything, because an
   unfiltered scan generates false positives faster than it generates findings.

6. **Grade every finding on two axes, not one.** *Evidence strength* (what the literature
   establishes) and *array reliability* (whether this platform calls this site dependably) are
   independent, and a finding can be strong on one and worthless on the other. A pathogenic variant
   called unreliably is not a finding; it is a prompt for a confirmatory test.
   `references/variant-triage.md` §2–3.

7. **Apply the confirmation rule to anything clinically significant.** The reason differs by data
   type and both must be stated correctly. For **arrays**, a population-scale study of **roughly fifty thousand**
   people with both chip and sequencing data found chip genotyping performs well for *common*
   variants and collapses in positive predictive value for *very rare* ones — and the dominant
   mechanism is Bayesian, not fixable by better probes: at a rare variant's prevalence, even a
   99.9%-specific assay is wrong about most of the people it flags. For **high-depth sequencing**, the chip-specific
   clustering literature does not transfer — **but the prevalence arithmetic above does, to any
   imperfect assay.** What is additionally true of sequencing: it is not reported under
   clinical-laboratory conditions, and short reads stay weak for repeat expansions, large
   structural variants and pseudogene-confounded loci. **And a low-pass-plus-imputation product is
   not high-depth sequencing** — its rare-variant calls inherit the array argument in full. Either way: **no clinically significant
   finding from consumer data supports action until a clinical-grade laboratory confirms it.** Say
   it every time — not as a disclaimer, as the finding. `references/variant-triage.md` §4.

8. **Do pharmacogenomics properly, which means refusing most of it.** This is where consumer data
   comes closest to being decision-relevant and also where it fails in ways users do not expect.
   Star alleles are diplotypes: calling them generally needs *phase* — which variants sit on the
   same chromosome copy — and for some genes *copy number*. An unphased genotype list supplies
   neither. CYP2D6 is the canonical refusal: deletions, duplications and CYP2D6/CYP2D7 hybrids put
   it beyond array data — **and beyond a plain VCF from whole-genome sequencing too, because the
   limitation is the representation rather than the depth.** The route is a purpose-built caller run
   against the alignment, or a clinical panel with a copy-number assay. Grade callability on three
   axes, not two: phase, structure, **and allele frequency** — a rare variant on a single probe is a
   hypothesis however cleanly it was called. Work the callable-versus-not split in `references/pharmacogenomics.md`,
   and route anything real to a clinical PGx panel ordered by the prescriber.

9. **Convert every risk number into absolute terms before reporting it.** A relative figure without
   its baseline is unreportable here. Give the baseline absolute risk, the person's absolute risk,
   the difference in natural frequencies, *and* the relative figure, with its uncertainty.
   Age-condition it where the literature allows. `references/risk-communication.md`.

10. **Establish ancestry before quoting any population estimate.** Polygenic scores and many risk
    estimates were derived in predominantly European-ancestry cohorts and lose accuracy applied
    elsewhere. This is not a footnote — it determines whether a number means anything for this
    person. `references/risk-communication.md` §4.

11. **Search the current literature for every finding that survives.** The catalogue gives you the
    established baseline; the literature search tells you what has changed, what failed to
    replicate, and whether a newer and larger estimate supersedes the one you were about to quote.
    Resolve every citation against a retrieved record — a search tool's generated prose will state
    confident identifiers for papers that returned no result.

    **When the channel cannot return a number, say so instead of producing one.** This is the stage
    where fabrication is most likely: the instruction asks for a figure, and in environments where
    scholarly resolvers and direct fetches are blocked, a search tool's prose will supply a
    confident invention. The fallback is the three anchored, provenance-graded figures in
    `references/variant-catalog.md` §0 — quoted as ranges, with their grade and design stated — not
    a number you cannot source. **An unsourceable figure is reported as unavailable.**

12. **Decide actionability honestly, then report.** An intervention must exist with evidence at
    **T1 or T2 — or at T3 where the intervention is avoidance of a documented hazard and a
    randomised trial is unobtainable or unethical** — and it must have been shown to change the
    outcome *in carriers specifically*. **State which case you are in.** Most findings fail this
    test and should say so; the avoidance cases are the ones that pass (HFE and iron, G6PD and
    oxidant triggers including high-dose or intravenous vitamin C, ALDH2 and alcohol).
    `references/interventions-evidence.md` §2. Then assemble the six-section report in
    `references/report-template.md`.

**Deliverable contract — six sections, every time, including when the audit cannot proceed.**
1. **Executive summary** — plain language, no notation. What the files are, what was found, what to
   do, and what this cannot tell you. Readable by someone who reads nothing else.
2. **Hyper-thorough analysis** — the quality pass, the full finding ledger (variant, genotype,
   source file, array reliability, evidence tier, effect size, action), and what could not be checked.
3. **Assessment and reasoning** — per finding: the evidence grade, the array-reliability grade, the
   confirmation requirement, and the reasoning. No composite "genetic score".
4. **Statistics breakdown** — absolute beside relative for every number, natural frequencies, the
   arithmetic shown, and the ancestry caveat applied.
5. **Additional research findings** — the current-literature pass: what supersedes or contradicts
   the catalogue, with resolved identifiers and the search disclosed.
6. **Conclusion** — the verdict, the clinician-ready question list, and linked references for both
   the catalogue entries and the independent research.

## Hard rails

These are not hedges. Each exists because violating it causes a specific harm.

- **No doses. Ever.** Not for a drug, not for a supplement, not for a peptide. Dosing is a
  prescriber's act informed by the whole person.
- **No genotype-based recommendation of a drug, supplement, or peptide.** The rail rests on
  **non-actionability, not on absence of evidence** — "no peptide has gene-interaction evidence"
  is false, and a rail resting on a false premise breaks on one counterexample. The accurate form:
  **the peptides this market sells have no genotype indication**, and the peptides that *are*
  genotype-selected are prescription drugs for rare monogenic disease a consumer array cannot
  diagnose. This rail is what stops the skill becoming a genotype-flavoured supplement storefront,
  which is its most likely failure mode. `references/interventions-evidence.md` §2 has the
  counterexample and why it strengthens the rule.
- **Never advise stopping, starting or changing a prescribed medication** — including one the data
  appears to flag, and especially then. Abrupt discontinuation carries its own risk, and the
  prescriber holds context the genome does not. This is the condition under which consumer
  pharmacogenetic reporting is permitted to exist at all, not a house style. All three reference
  files carried this; the file guaranteed to load did not. `references/pharmacogenomics.md` §5,
  `references/report-template.md` §7.
- **Confirmation before action** on any clinically significant finding, always stated.
- **A variant of uncertain significance is not a finding to act on.** Report it as uncertain and
  leave it there.
- **No clinical finding rests on an imputed call.** A low-pass-plus-imputation product is not
  high-depth sequencing: its rare-variant calls are statistical inferences, and they inherit the
  array false-positive argument in full. Establish the product tier from the provider before
  applying either reading. `references/data-formats-and-parsing.md` §4.
- **A negative is never clearance**, and "absent from the file ≠ absent from the person" is only
  half of it. A site **never probed** yields *no* information — not weak reassurance. A site probed
  and called reference is bounded by what was probed, and bounded again by ancestry. State the
  probed set, give the post-negative carrier probability using **ancestry-specific clinical
  sensitivity**, report the **negative likelihood ratio** rather than NPV for anything rare, and
  never let a negative stand as clearance for a condition the person has a family history of.
  `references/risk-communication.md` §5. *(The earlier wording — "never offer reassurance without
  saying what was probed" — licensed the harm: list the probed set, then reassure.)*
- **No star-allele call the data cannot support — which is not the same as "no phase, no call".**
  Where no defined haplotype carries both observed variants in cis, the diplotype *is* determined:
  report it (CYP2C19 heterozygous at `*2` and `*17` is the worked case). Where two or more defined
  diplotypes are consistent, enumerate them, say whether the ambiguity is **nomenclatural or
  clinical**, and name the assay that settles it (TPMT `*3B`/`*3C`). Where the call needs copy
  number or structure — CYP2D6 — do not call. **State any cis assumption rather than leaving it
  silent.** `references/pharmacogenomics.md` §1. *(The absolute form banned everything, since no
  consumer file is phased — and that reference file says in terms that a skill which always reports
  ambiguity is as wrong as one that never does.)*
- **Population-based penetrance** for a person tested without a family history. Family-ascertained
  estimates answer a different question. `references/risk-communication.md` §3.
- **Regulatory and sport-prohibition status is named by mechanism, never frozen as fact.** It moves.
  Point at the live source.
- **Relatives did not consent.** A finding can implicate parents, siblings and children. Flag that
  before disclosing, and never volunteer inferred family structure — relatedness, consanguinity, or
  non-paternity — as an aside. If the data implies it, say that such inferences are possible and ask
  whether the person wants them addressed at all. **And when asked directly** — "compare my file
  with my brother's" — **do not run it.** The arithmetic is simple and sits in
  `references/data-formats-and-parsing.md` §5 for the *identity* check, which is a different
  question asked for a different purpose. A relatedness answer can disclose something irreversible
  about people who are not in the conversation, including one who did not ask; the response is to
  say that plainly and route the question to a genetic counsellor who can handle what it may
  return.
- **Serious findings get a named handoff, not a paragraph — and "serious" needs defining, because
  this is the file an agent always loads.** A finding is urgent when **the exposure is live or
  scheduled**: a drug the person is currently taking or about to start, a booked operation or
  anaesthetic, a first chemotherapy dose — or a reliably-called, high-penetrance, actionable
  variant. Then: say it in the first sentence; name the confirmation step and the clinician; do
  **not** advise stopping or changing a medication; state the unconfirmed-consumer-data uncertainty
  in the same breath; and flag the relatives implication. `references/report-template.md` §7.
- **Establish whose genome this is before reading it.** If the data subject is not the person
  asking, say what changes: they have not consented to this analysis, and findings about them are
  not the requester's to receive. **For a minor's file, do not report predictive adult-onset
  findings** — that decision belongs to the person when they can make it. Route to a clinical
  genetics service. *(A relative's export is a realistic input;
  `references/data-formats-and-parsing.md` §5 treats it as one.)*
- **An exclusion request — "do not tell me about X" — is honoured in full for findings with no
  action attached.** It is overridden only for a reliably-called, actionable, **time-critical**
  finding, and then the report says that an excluded-category finding exists and needs a
  conversation, names the clinician route, and **does not detail it.** Ask before reading the file,
  not after.

## Why / learn

**The data is weaker than the output format implies.** A genotyping array is a set of probes for
chosen sites, not a reading of a genome. It reports what it was built to ask about, which is
overwhelmingly common variation, and its performance on a rare variant is poor for a reason worth
understanding: cluster separation in a genotyping assay depends on having many samples of each
genotype class, and a rare variant supplies almost none. That is why a clinical laboratory
re-tests before anyone acts, and why the honest reading of an alarming raw-data hit is "this needs
confirming", not "I have this".

**Relative risk is where genetic reporting goes wrong, and it goes wrong in a specific way.**
Genotype effects are usually published against a population baseline the reader does not know,
often as odds ratios from case-control designs rather than risks, and frequently without
age-conditioning. So "three times the risk" arrives with three separate pieces of missing context.
Tripling a 0.5% lifetime risk and tripling a 12% one are different conversations, and only one of
them should change behaviour. The library's general treatment of this lives in
`deep-research-skills:video-source-audit`; what is genetics-specific is penetrance, ascertainment,
and age-conditioning, which this skill owns.

**Penetrance is the genetics word for absolute risk, and how a carrier was found changes it.**
Estimates drawn from families selected *because* they had many affected members describe those
families. Someone who finds the same variant incidentally, with no family history, is a different
case — and the honest literature shows the older family-based figures running well above
population-based ones, with newer and larger estimates overlapping more than the early contrast
suggested. **Two disciplines follow:** quote the **age horizon** with every penetrance figure, because
comparing a to-70 estimate against a to-80 one manufactures a gap; and quote a **range**, because
large series have put absolute cumulative risks at the lower end of the published spread with wide
intervals. *(An earlier version of this section also claimed that variation between families carrying
the same variant exceeds variation between positions within a gene. The record cited for it does not
visibly support it, so the claim is withdrawn rather than rehedged — see `risk-communication.md` §3.)*

**Actionability is a higher bar than association, and almost nothing clears it.** A variant can be
genuinely associated with an outcome and still be useless, because the question is not "does this
predict something?" but "does knowing this change what I should do?" That requires an intervention
to exist *and* to have been tested in carriers. Most consumer-genetics content conflates prediction
with actionability, which is how a real association becomes a supplement recommendation that no
study supports. Where the general recommendation does not change based on genotype — which is the
common case — saying so is the correct, useful answer.

**The most over-interpreted variant in consumer genetics is MTHFR**, and getting it right is a good
test of whether a genetics tool is trustworthy. A professional society advised
against routine MTHFR polymorphism testing on the grounds of minimal clinical utility, and the
recommendation stood through a later addendum — which also reclassified the document from an
evidence-based practice guideline to a clinical practice resource, so quote it as that. The position is echoed elsewhere in the literature —
though by a commentary rather than by a second society, which is a distinction this skill got wrong
once and now states carefully. `references/interventions-evidence.md` carries the
resolved citations and what the evidence does and does not support.

## Common mistakes
- Interpreting before running the quality pass → a no-call or a discordant site interpreted as a
  genotype is a fabricated finding.
- Looking up a position without checking the genome build → silently returns a different variant.
- Treating every call at an A/T or C/G site as unusable → the unresolvable case is a **homozygote**
  there (2 copies on one orientation, 0 on the other). A **heterozygote** carries one copy of each
  allele either way, so its dosage is 1 and the call is usable; discarding it is the opposite error
  and suppresses real findings. `references/data-formats-and-parsing.md` §2.
- Reading "not in my file" as "I don't have it" → the array never asked. In a variants-only VCF it is
  worse: absence and homozygous-reference are the same observation, so reading silence as a reference
  call fabricates a genotype — the APOE e3/e3 case is the one that bites.
- Treating one observed allele as a homozygote → comparing genotypes as *sets* makes `C` and `CC`
  identical, which turns a half-call into a confident homozygous call. The bundled script refused
  this only after it had shipped the bug.
- Leading with a polygenic score's AUC → AUC says nothing about how many cases are in the study
  sample, so it cannot be read as this person's risk. Lead with the top-decile *absolute* risk and the share of cases outside the flagged group.
- Calling an APOE diplotype from one SNP → it needs both rs429358 and rs7412, and one specific
  combination is formally ambiguous. The catalogue states which.
- Quoting a star allele from unphased genotypes → not supported; say so instead.
- Quoting a polygenic score without establishing ancestry → the number may not transfer.
- Quoting family-based penetrance to someone with no family history → overstates their risk.
- Treating a GWAS hit as personal information → a per-allele odds ratio near 1 tells an individual
  almost nothing.
- Letting an interesting association become a recommendation → association is not actionability.
- Producing findings because a report format expects findings → "nothing here changes what you
  should do" is a legitimate and common result.

## Tailor to your environment
Record in `references/your-environment.md`: which files you hold and their platform and version;
your genetic ancestry as far as you know it, because it determines which published estimates
transfer; known family history, which changes how penetrance should be read; current medications and
supplements, so the pharmacogenomic pass is relevant rather than theoretical; whether you have
access to clinical-grade confirmatory testing; and which findings you do *not* want surfaced.

**That last one is not optional.** Some findings cannot be unlearned, some implicate relatives, and
some have no action attached. Decide what you want to know before the analysis, not after.

**Keep your filled-in copy outside the plugin, and keep the genome outside it entirely.** This file
ships as a *template* inside the installed plugin, where a `/plugin marketplace update` can
overwrite it. Copy it to `.claude/skills-env/dna-raw-data-audit.private.md` in your own project — and note
that **the `.private.md` suffix is what keeps it out of git — the plain `.md` form is NOT
ignored**, so confirm with `git check-ignore -v` before writing anything into it.

## References
- references/data-formats-and-parsing.md — 23andMe and Nebula formats, build detection, strand
  orientation, no-calls, imputation, array-vs-sequencing coverage, cross-platform concordance
- references/variant-triage.md — the triage funnel, ACMG/AMP tiers and ClinVar review status, the
  two grading axes, the false-positive problem and the confirmation rule, penetrance and ascertainment
- references/pharmacogenomics.md — CPIC and PharmGKB evidence levels, star-allele diplotypes, what
  array data can and cannot call, the gene-drug pairs worth raising with a prescriber
- references/variant-catalog.md — the tiered variant catalogue: effect sizes in absolute terms,
  array reliability, action or no action, with resolved identifiers and the verification standard
- references/risk-communication.md — genetics-specific absolute-vs-relative risk, penetrance
  communication, age-conditioning, ancestry portability, and the reporting template
- references/interventions-evidence.md — grading any intervention: regulatory status and evidence
  tier for medicines, supplements and peptides; the MTHFR corrective; the no-genotype-basis rail
- references/report-template.md — the six-section deliverable and how it degrades honestly
- references/your-environment.md — your files, ancestry, family history, medications, and what you
  do not want to know (fill in)

## Scripts
> Paths use `${CLAUDE_PLUGIN_ROOT}` so they resolve from **any** working directory once the plugin
> is installed. A bare `scripts/…` path only works inside a clone of the marketplace repo, which is
> not where a user runs these.
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-raw-data-audit/scripts/triage_genome.py" <file> [<file2>]` —
  parses 23andMe-format and VCF input, detects the genome build, reports total sites and no-call
  rate, checks concordance when two files are given, and extracts the sites in **its own
  catalogue — a named subset of `references/variant-catalog.md`, not the whole funnel.**
  RYR1/CACNA1S, MT-RNR1 m.1555A>G, the HLA alleles and the BRCA founder variants are **not** in it
  and must be looked up by hand (stage 5 says the same). It
  deliberately does **not** compute risk, assign pathogenicity, or recommend anything: it establishes
  what the data says so the interpretation is done against verified genotypes rather than assumed
  ones. It validates ploidy before calling anything, refuses genotypes from gVCF reference blocks
  and `DP=0` lines, flags a variants-only VCF's absence semantics, checks the build-independent
  138 bp spacing between the two APOE sites, and reports strand state as
  `AMBIGUOUS`/`CLEAR`/`UNDETERMINED`. `--self-test` runs the offline parsing and algebra tests —
  including the APOE ambiguity case and a regression assertion for each of those refusals.
  **It runs on a whole-genome file**: a retained VCF record costs 537 bytes (measured, linear), so
  a 4–6M-record call set would be 2–3 GB held whole; the parse retains only the keys anything
  downstream reads and discloses the restriction, which puts a 5M-record VCF beside a 640k-site
  array at 574 MiB. **Check the `ID` column before reading any finding list from a VCF.** A
  provider file with `ID` as `.` matches an rsID-keyed catalogue zero times, and that failure
  presents as a person who carries nothing — so *nothing keyable* is a **blocking** condition
  (exit 3, named in a `BLOCKING` section), alongside an undeclared build and a sample-identity
  failure. Each means the audit did not happen, not that it came back clean. The fix is dbSNP
  annotation; the fallback is keying by position from an array file's own rows, which the script
  will do only within one declared build, only for SNV-shaped records, and never from a
  coordinate asserted from memory. Identity and concordance compare exactly two files — hand it
  three and it says that neither ran rather than printing a report that looks complete.
- **Test reachability before relying on the citation verifier.** Where the scholarly resolvers are
  blocked — the normal case in this environment — it returns `ERROR: network unavailable` and
  verifies nothing. The operative standard is then `references/variant-catalog.md` §0: an
  identifier counts as verified only when it appears inside a returned URL **and** the record's
  title was returned beside it. Report unverifiable identifiers as unverified, and say in report
  §5 that the live pass could not be performed.
- Citation checking reuses this plugin's existing verifier under the same plugin root:
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/verify_citation.py" --doi <doi>`
  **Use it for existence and metadata checks only.** That script hard-codes a
  country-of-origin exclusion policy (`EXCLUDED_COUNTRIES`) belonging to
  `deep-research-skills:medical-research-detective`, where it is a deliberate data-integrity control
  for that skill's use case. **This skill does not adopt it**, as an explicit decision rather than by
  inheritance: genomics research is produced at scale in the excluded jurisdictions, so applying the
  filter here would silently bias the evidence base of the very literature the skill depends on. Read
  the verifier's resolution and retraction output; **ignore its provenance line.** This skill's
  anti-fabrication standard is whether an identifier resolves to a retrieved record, not where the
  authors work.
