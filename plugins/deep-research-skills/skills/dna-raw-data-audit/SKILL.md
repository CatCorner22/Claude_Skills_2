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
  version: "1.2.0"
  source: >-
    Built from an eight-stream research pass with adversarial verification. Citations verified
    against retrieved index records only, never a search tool's generated prose; the APOE
    diplotype algebra and all arithmetic were recomputed by execution. See
    references/variant-catalog.md for the verification standard and what was dropped.
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

2. **Identify what you actually have, and detect the build.** 23andMe exports and Nebula outputs are
   different data with different limits, and a position lookup against the wrong genome build
   silently returns the wrong variant. Detect rather than assume. Formats, build detection, and the
   array-versus-sequencing distinction: `references/data-formats-and-parsing.md` §1–2.

3. **Run the quality pass, and report it before any interpretation.** No-call rate, total sites,
   and — if both files are present — concordance between them. Two platforms genotyping the same
   person is a genuine quality signal, and a discordant call at a site you were about to interpret
   is a finding in itself. The bundled script does this pass; see **Scripts**.

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
   type and both must be stated correctly. For **arrays**, a population-scale study of ~49,908
   people with both chip and sequencing data found chip genotyping performs well for *common*
   variants and collapses in positive predictive value for *very rare* ones — and the dominant
   mechanism is Bayesian, not fixable by better probes: at a rare variant's prevalence, even a
   99.9%-specific assay is wrong about most of the people it flags. For **sequencing**, that
   literature does not transfer; the reason is instead that consumer sequencing is not reported
   under clinical-laboratory conditions, and short reads stay weak for repeat expansions, large
   structural variants and pseudogene-confounded loci. Either way: **no clinically significant
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

12. **Decide actionability honestly, then report.** An intervention must exist, and it must have
    been shown to change the outcome *in carriers specifically*, before a genotype is actionable.
    Most findings fail that test and should say so. Then assemble the six-section report in
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
- **No genotype-based recommendation of a drug, supplement, or peptide.** For peptides in
  particular there is essentially no established gene-interaction evidence, so a genotype supplies
  no basis for recommending one. This rail is what stops the skill becoming a genotype-flavoured
  supplement storefront, which is its most likely failure mode.
- **Confirmation before action** on any clinically significant finding, always stated.
- **A variant of uncertain significance is not a finding to act on.** Report it as uncertain and
  leave it there.
- **Absent from the file ≠ absent from the person.** Never offer a negative result as reassurance
  without saying what was and was not probed.
- **No star-allele call without the data to support it** — no phase, no call; no copy-number
  assay, no CYP2D6 call.
- **Population-based penetrance** for a person tested without a family history. Family-ascertained
  estimates answer a different question. `references/risk-communication.md` §3.
- **Regulatory and sport-prohibition status is named by mechanism, never frozen as fact.** It moves.
  Point at the live source.
- **Relatives did not consent.** A finding can implicate parents, siblings and children. Flag that
  before disclosing, and never volunteer inferred family structure — relatedness, consanguinity, or
  non-paternity — as an aside. If the data implies it, say that such inferences are possible and ask
  whether the person wants them addressed at all.
- **Serious findings get a named handoff, not a paragraph.** If something genuinely urgent surfaces,
  say so first, plainly, with the route to a clinician — do not bury it in section 5 of a long report.

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
suggested. There is also more variation *between* families carrying the same variant than between
positions within a gene, which is itself an argument against quoting any single number as *the*
penetrance.

**Actionability is a higher bar than association, and almost nothing clears it.** A variant can be
genuinely associated with an outcome and still be useless, because the question is not "does this
predict something?" but "does knowing this change what I should do?" That requires an intervention
to exist *and* to have been tested in carriers. Most consumer-genetics content conflates prediction
with actionability, which is how a real association becomes a supplement recommendation that no
study supports. Where the general recommendation does not change based on genotype — which is the
common case — saying so is the correct, useful answer.

**The most over-interpreted variant in consumer genetics is MTHFR**, and getting it right is a good
test of whether a genetics tool is trustworthy. A professional-society practice guideline advised
against routine MTHFR polymorphism testing on the grounds of minimal clinical utility; it was later
amended, and the recommendation against testing stood through the amendment. Multiple other
professional bodies reached the same position. `references/interventions-evidence.md` carries the
resolved citations and what the evidence does and does not support.

## Common mistakes
- Interpreting before running the quality pass → a no-call or a discordant site interpreted as a
  genotype is a fabricated finding.
- Looking up a position without checking the genome build → silently returns a different variant.
- Ignoring strand orientation on A/T and C/G sites → these are the ambiguous class, and a flipped
  call inverts the result. See `references/data-formats-and-parsing.md` §2.
- Reading "not in my file" as "I don't have it" → the array never asked. In a variants-only VCF it is
  worse: absence and homozygous-reference are the same observation, so reading silence as a reference
  call fabricates a genotype — the APOE e3/e3 case is the one that bites.
- Treating one observed allele as a homozygote → comparing genotypes as *sets* makes `C` and `CC`
  identical, which turns a half-call into a confident homozygous call. The bundled script refused
  this only after it had shipped the bug.
- Leading with a polygenic score's AUC → AUC is invariant to prevalence and the person's question is
  not. Lead with the top-decile *absolute* risk and the share of cases outside the flagged group.
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
that genetic and health detail belongs in the git-ignored `.private.md` twin, never in a committed
file.

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
  rate, checks concordance when two files are given, and extracts only the catalogued sites. It
  deliberately does **not** compute risk, assign pathogenicity, or recommend anything: it establishes
  what the data says so the interpretation is done against verified genotypes rather than assumed
  ones. It validates ploidy before calling anything, refuses genotypes from gVCF reference blocks
  and `DP=0` lines, flags a variants-only VCF's absence semantics, checks the build-independent
  138 bp spacing between the two APOE sites, and reports strand state as
  `AMBIGUOUS`/`CLEAR`/`UNDETERMINED`. `--self-test` runs the offline parsing and algebra tests —
  including the APOE ambiguity case and a regression assertion for each of those refusals.
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
