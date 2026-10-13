# Data formats and parsing

What the files actually contain, how to read them without introducing errors, and the four technical
traps that turn a correct lookup into a wrong answer.

**Contents**
- §1 The two platforms, and what each can answer
- §2 Build and strand: the two silent-wrong-answer traps
- §3 No-calls, and why absence is not absence
- §4 Imputation
- §5 Cross-platform concordance
- §6 Running the bundled script

---

## §1 The two platforms, and what each can answer

**These are different kinds of data and the difference is not cosmetic.**

**23andMe — a genotyping array.** A set of probes for chosen sites. The export is tab-delimited with
comment lines beginning `#`, then columns `rsid`, `chromosome`, `position`, `genotype`. Genotype is
two concatenated alleles (`AG`), a single allele for sex-chromosome and mitochondrial calls in males,
and `--` for a no-call. Position is reported on a declared genome build; the comment header is where
that declaration lives.

**Nebula — sequencing.** Nebula has offered more than one product tier, and **what a given account
actually holds varies** — low-pass sequencing with imputation and higher-depth whole-genome
sequencing are very different data with very different reliability for rare variants. **Establish
which you have before interpreting anything**, from the provider's own account records rather than
from the file. A VCF from a low-pass-plus-imputation pipeline looks superficially like a VCF from
30× sequencing, and the second supports conclusions the first does not. *This is a commercial detail
that changes; confirm it rather than inferring it, and if you cannot establish it, say so in the
report and grade accordingly.*

**The size comparison that reframes everything.** A consumer array probes on the order of a
half-million to a million sites. A human genome carries on the order of four to five million
variant sites relative to the reference. So an array interrogates roughly **a fraction of a percent**
of a person's variation — and the sites it chose are overwhelmingly *common* variants, because that
is what arrays are designed for. Anyone who believes their array "read their DNA" is working from a
false premise, and correcting it early makes every later limitation intelligible.

---

## §2 Build and strand: the two silent-wrong-answer traps

Both of these produce a confident wrong answer rather than an error. That is what makes them
dangerous.

### Genome build

Coordinates differ between GRCh37/hg19 and GRCh38. **A position lookup against the wrong build
returns a different variant, silently.**

- **Detect, never assume.** The bundled script reads the declared build from the header and, when
  none is declared, **warns, proceeds on rsID-keyed lookups only, and signals exit 3** — in text
  mode and under `--json` alike. **It does not refuse**, which an earlier version of this sentence
  claimed; what it refuses is any *positional* interpretation, and no positional lookup may be
  attempted on such a file.
- **Prefer rsIDs over positions** when cross-referencing. An rsID is build-independent; a position is
  not. This single habit eliminates most build errors.
- **Never compare positions across files declaring different builds** without liftover. rsID-based
  comparison across builds is safe; positional comparison is not. The script warns when two inputs
  declare different builds.

### Strand orientation

Consumer platforms report alleles relative to one strand; database entries may be reported relative
to the other. For most sites this is resolvable, because the two possible allele pairs differ:
a C/T site reported on the opposite strand appears as G/A, and C/T versus G/A is distinguishable.

**The dangerous class is A/T and C/G sites** — "ambiguous" or "palindromic". Reverse-complementing
the pair `{A,T}` returns `{A,T}`, so **allele identity alone cannot tell you the orientation**, and a
flipped call inverts which allele is the risk allele.

**Two things get conflated here, and this file conflated them in both directions before getting it
right.** Separate them:

- **Unorientability is a property of the SITE.** An A/T or C/G site is its own reverse complement,
  so allele identity alone cannot tell you which strand the file reports.
- **Ambiguity of a CALL is a property of the (site, genotype) pair** — and that is what matters,
  because what gets interpreted is a **dosage**.

Work it at a C/G site where C is the risk allele. A **heterozygous** `CG` call carries one copy of
each allele; flip the strand and the C reads as G and the G as C — still one copy each. **The dosage
is 1 either way, so a heterozygote at a palindromic site is fully usable.** A **homozygous** `CC`
call is 2 copies on one orientation and 0 on the other, and that is the genuinely unresolvable case.

```
 site    call   under a flip   dosage      verdict
 C/G     C/G    G/C            1 either way   CLEAR        <- usable
 C/G     C/C    G/G            2 or 0         AMBIGUOUS    <- the dangerous one
 C/T     C/C    G/G            distinguishable pair         CLEAR
 unknown C/C    ?              ?              UNDETERMINED
```

**So the only unresolvable class is a homozygote at a palindromic site** — and it is invisible to any
check that looks at the genotype without knowing the site's pair, because `CC` could sit at a C/G
site or a C/T one. The bundled script's first implementation returned "not ambiguous" for a
homozygote and passed it silently; its second returned AMBIGUOUS for *every* call at a palindromic
site once the pair was known, which told the reader not to count a heterozygote that was never in
doubt. **Both directions are errors, and only the first is loud** — the second quietly suppresses
real findings.

Practical consequence: **to resolve a homozygote you need the site's allele pair from an external
reference.** Without it, the honest output is that ambiguity could not be ruled out. A heterozygote
needs nothing.

**Resolution, in order of reliability:** use the platform's own documented strand convention for that
array version; check allele frequency against a population reference and see which assignment is
consistent (works only when the frequencies are asymmetric enough to discriminate); or use a
flanking-sequence match. **When orientation cannot be resolved, report the call as unresolved rather
than picking** — and note that this is needed only for the homozygous case.

---

## §3 No-calls, and why absence is not absence

A no-call (`--`, or `./.` in VCF) is a site the assay failed to call. It is not a reference genotype,
and treating it as one manufactures a finding.

**Two distinct things look identical in a naive read, and the skill must separate them:**

1. **Probed and failed** — the site is in the file with a no-call.
2. **Never probed** — the site is absent from the file entirely, because the array was never built
   to ask about it.

Neither is evidence about the person. The second is the more consequential misreading: **a variant's
absence from the file is not evidence of its absence from the person.** The bundled script
distinguishes them, labelling absent catalogue sites explicitly as possibly never probed.

**Report the overall no-call rate before any interpretation.** A high rate across the file is a
quality problem affecting everything downstream; a no-call at a site you were about to interpret
means that finding does not exist.

### A VCF's silence is not a reference call — and this is where fabricated genotypes come from

**An array file and a VCF have different semantics for absence, and treating them alike manufactures
genotypes.** On an array every probed site has a row, so absence means "never probed". A
**variants-only VCF carries variant lines only**, so a site with no row is either homozygous reference
*or* never covered — **the same observation, which is no observation.**

**The case that makes this concrete, and it is the worst one in the skill:** an APOE **e3/e3** person
is reference at *both* defining sites. Their APOE is therefore **entirely invisible in a
variants-only VCF** — and a parser that reads absence as reference reports a confident e3/e3 for
someone whose APOE region was never sequenced. The bundled script's first version did exactly this
from a zero-coverage gVCF block; its self-test now asserts the refusal, and the negative control
confirms the old logic produced `e3/e3`.

Three VCF-specific traps, each of which turns absence into a confident call:

| Trap | What it looks like | The honest reading |
| :--- | :--- | :--- |
| **Variants-only file** | No line at the site | No information. Not a reference genotype |
| **Reference block (gVCF)** | A line with a symbolic ALT (`<NON_REF>`, `<*>`) or an `END=` interval, usually `GT 0/0` | The block asserts *no variant was called across a span*. It asserts nothing about any particular position inside it |
| **Zero depth** | `GT 0/0` (or even `0/1`) with `DP=0` | A genotype emitted with no supporting reads. No information, and emphatically not a reference call |

**So establish which kind of VCF you have before reading a single genotype out of it**, and when the
file is variants-only, record every catalogued site that is missing as *unobserved* rather than as
reference. The script does this and refuses to call APOE from absence; a hand-rolled lookup, or a
spreadsheet import, will not.

---

## §4 Imputation

Imputation infers genotypes at unmeasured sites from measured ones plus a reference panel of known
haplotypes. It is legitimate and widely used — and it produces **statistical inferences, not
measurements**.

**The problem is where its accuracy fails.** Imputation works well for common variants in
well-represented populations, and degrades for rare variants and for ancestries under-represented in
the reference panel. Those are precisely the cases people most want answered: rare variants are the
clinically significant ones, and ancestry under-representation compounds every other portability
problem.

**Consequences the skill must enforce:**
- **Never let an imputed genotype support a clinical finding.** It is at best a prompt for a measured
  confirmatory test.
- **Establish whether a VCF is imputed**, which is a property of the pipeline, not visible in a
  genotype column. Low-pass-plus-imputation products are mostly imputed by construction.
- **Record imputation status per finding** in the ledger. "Imputed, ancestry under-represented in the
  panel" is a materially different grade from "directly measured at 30× depth".

---

## §5 Cross-platform concordance

Two platforms genotyping the same person is a **genuine quality signal** and the single best check
available without ordering a new test.

- **Compare by rsID**, not position (§2).
- **Compare allele sets**, not strings: `AG` and `GA` are the same genotype.
- **A discordant call at a site you were about to interpret is a finding in itself** — it means at
  least one platform is wrong there, you cannot tell which, and the correct output is "unresolved,
  requires confirmation" rather than a coin flip.
- **A low concordance rate overall** points at a sample, pipeline, or identity problem and
  invalidates the whole analysis until explained.
- **Concordance is not accuracy.** Two platforms can agree and both be wrong, particularly if they
  share a design limitation or a reference panel. Agreement raises confidence; it does not establish
  truth, and it does not substitute for clinical confirmation.

### Sample identity comes before concordance, and before any interpretation

A low concordance rate has two very different explanations, and conflating them wastes an audit:
genotyping error, or **the two files are not the same person**. Mislabelled kits, a relative's
export, and a file saved under the wrong name are all realistic.

**Check identity first.** Count sites where the two files give genotypes sharing **no allele** —
one file homozygous for one allele and the other homozygous for the other. For the same individual
this should be essentially zero, bounded only by error rate; for two different people it rises
sharply, and for unrelated people it is large. Restrict the count to autosomal, both-called,
diploid, **non-palindromic** sites, because palindromic sites can appear to disagree purely from
orientation and would manufacture a false identity failure.

**If identity fails, stop.** Report it and interpret nothing — an audit of two people's data merged
as one is worse than no audit. If identity passes but concordance is still poor, you have a quality
problem to characterise rather than an identity problem.

---

## §6 Running the bundled script

```bash
# One file
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-raw-data-audit/scripts/triage_genome.py" genome.txt

# Both platforms — adds the concordance pass
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-raw-data-audit/scripts/triage_genome.py" \
    genome.txt nebula.vcf.gz

# Machine-readable, for building the ledger
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-raw-data-audit/scripts/triage_genome.py" \
    genome.txt nebula.vcf.gz --json

# Offline logic tests, no input files needed
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-raw-data-audit/scripts/triage_genome.py" --self-test
```

**What it reports:** format and declared build per file, total sites, no-call count and rate,
chromosome count, cross-platform concordance with the discordant sites named, genotypes at the
catalogued sites with absent ones labelled, a three-state strand assessment per site
(`AMBIGUOUS` / `CLEAR` / `UNDETERMINED`), and the APOE diplotype including the one ambiguous
combination.

**The refusals are the valuable part.** Each of these was a defect first and is now an assertion in
the self-test:

- **Ploidy is validated before anything is called.** Comparing `set(genotype)` makes
  `set("C") == set("CC")`, so a half-call, a truncated field or a haploid `GT` was read as a
  homozygote — and at APOE that produced a confident **e4/e4 from a single observed allele**. Any
  genotype that is not a two-allele diploid call is now refused with the reason.
- **Concordance excludes non-diploid comparisons instead of scoring them.** The same `set()` collapse
  made `CC` and `C` agree, inflating the audit's own quality gate. Allele order still agrees
  (`AG` == `GA`), which is the property worth keeping.
- **A reference block or a `DP=0` call yields no genotype**, and a variants-only VCF triggers an
  explicit warning that absence is not reference (§3).
- **Non-T/C alleles at either APOE site are refused, not complemented.** Both sites are T/C and the
  complement set A/G is disjoint from it, so a strand flip there is *detectable* — an A or G is a
  parsing or mapping error. (Contrast FTO rs9939609, A/T, where a flip is undetectable in principle.)
- **A diplotype that resolves only by invoking the rare e1 haplotype carries a caution**, because a
  genotyping error at one of the two sites is the likelier explanation than a rare haplotype.
- **The two APOE sites are 138 bp apart in every build** (c.526 − c.388, both in exon 4), so the
  script checks the spacing in the file's own coordinates and warns when a row is mis-mapped. The
  spacing is build-independent; the absolute positions are not, and are never assumed.

**Two format details it does not special-case, and you should know about:** 23andMe codes
insertions and deletions as `DD`/`DI`/`II` rather than as bases, and carries internal
platform-specific marker IDs that are not rsIDs and have no stable external meaning. The script
reads both without crashing, but a conversion pipeline that silently discards them — some public
converters do — loses a whole variant class. If indels matter to a question you are asking, verify
they survived whatever produced your file.

**What it refuses to do:** assign risk, assign pathogenicity, or recommend anything. It dispatches on
file *content* rather than extension, because extensions lie, and it rejects unrecognised input
loudly (exit 2) rather than parsing garbage into plausible-looking findings.

**Exit codes:** `0` parsed · `2` unreadable, empty, or unrecognised format · `3` build undeclared,
so positional interpretation would be unsafe · `5` bad usage.
