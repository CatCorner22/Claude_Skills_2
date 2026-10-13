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

- **Detect, never assume.** The bundled script reads the declared build from the header and
  **refuses to proceed** (exit 3) when none is declared, because the alternative is guessing.
- **Prefer rsIDs over positions** when cross-referencing. An rsID is build-independent; a position is
  not. This single habit eliminates most build errors.
- **Never compare positions across files declaring different builds** without liftover. rsID-based
  comparison across builds is safe; positional comparison is not. The script warns when two inputs
  declare different builds.

### Strand orientation

Consumer platforms report alleles relative to one strand; database entries may be reported relative
to the other. For most sites this is resolvable, because the two possible allele pairs differ:
a C/T site reported on the opposite strand appears as G/A, and C/T versus G/A is distinguishable.

**The dangerous class is A/T and C/G sites** — "ambiguous" or "palindromic". An A/T site reported on
the other strand is *still* an A/T site, so **allele identity alone cannot tell you the orientation**,
and a flipped call inverts which allele is the risk allele.

Worked: a site whose risk allele is `A`. The file reports `AT` — heterozygous either way, so no
problem. But where the file reports a homozygote, `AA` on the reported strand is `TT` on the other,
which is the opposite genotype. Interpreting it without resolving orientation is a coin flip
presented as a result.

**Resolution, in order of reliability:** use the platform's own documented strand convention for that
array version; check allele frequency against a population reference and see which assignment is
consistent (works only when the frequencies are asymmetric enough to discriminate); or use a
flanking-sequence match. **When orientation cannot be resolved, report the site as unresolved rather
than picking.** The bundled script flags every A/T and C/G genotype it extracts for exactly this
reason.

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
catalogued sites with absent ones labelled, strand-ambiguity flags, and the APOE diplotype including
the one ambiguous combination.

**What it refuses to do:** assign risk, assign pathogenicity, or recommend anything. It dispatches on
file *content* rather than extension, because extensions lie, and it rejects unrecognised input
loudly (exit 2) rather than parsing garbage into plausible-looking findings.

**Exit codes:** `0` parsed · `2` unreadable, empty, or unrecognised format · `3` build undeclared,
so positional interpretation would be unsafe · `5` bad usage.
