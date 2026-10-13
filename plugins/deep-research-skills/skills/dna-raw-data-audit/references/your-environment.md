# Your environment — DNA raw-data audit

Fill this in before the first analysis. Several of these answers change the result, and one of them
should be decided *before* anything is read rather than after.

**Keep the filled-in copy at `.claude/skills-env/dna-raw-data-audit.private.md` in your own project, and put
genetic and health detail in the git-ignored `.private.md` twin.** This file ships as a template
inside the installed plugin, where a `/plugin marketplace update` can overwrite it.

---

## Before anything else: what do you not want to know?

**Decide this first.** Some findings cannot be unlearned, some implicate relatives, and some have no
action attached at all — the combination of "serious", "unactionable" and "irreversible" is real and
APOE is the common example.

- Findings you want **excluded** from any report: _____
- Do you want **carrier status** reported? (It is information about your parents and siblings too.) _____
- Do you want findings with **no available action** reported? _____
- Do you want **relatedness inferences** — consanguinity, unexpected family structure, non-paternity
  — addressed at all? Default is **no**, and the skill will not volunteer them. _____
- Is there anyone else who should be part of the conversation before a heritable finding is
  disclosed? _____

The audit honours these. Section 6 of the report will note that something was withheld at your
request, without naming it.

---

## Your files

| | |
| :--- | :--- |
| 23andMe file path | _____ |
| 23andMe chip version, if known | _____ (v3/v4/v5 differ in which sites they probe) |
| Nebula file path | _____ |
| **Nebula product tier** | _____ **(low-pass + imputation, or 30×+ WGS — this materially changes what the data supports; confirm from your account, not from the file)** |
| Any other raw data | _____ (Ancestry, MyHeritage, FTDNA, a clinical report) |
| Where the files live | _____ (keep them **outside** any repository or shared drive) |

**Test, do not assume, that the file is ignored.** `git check-ignore -v <file>` must print a
matching rule. Two traps proven by execution while this skill was being reviewed: the tailoring file
must carry the **`.private.md`** suffix to be ignored (the plain `.md` form is not), and **the file
your provider hands you is a `.zip`** — so an archive pattern is needed as well as the
extension patterns. Neither protection exists in your repository unless you put it there.

**Confirm before proceeding:** the files are not in a git repository, not in a synced cloud folder
shared with anyone, and have not been uploaded to a third-party interpretation service.

---

## Ancestry

This is not demographic box-ticking — it decides whether published estimates transfer to you
(`risk-communication.md` §4).

- Genetic ancestry as far as you know it: _____
- Admixed? Approximate proportions if known: _____
- Any founder population in your background? _____ (changes which variants are worth probing and
  which frequency references apply)

If this is unknown, say so — the audit will report estimates with the portability caveat unresolved
rather than silently assuming the cohorts the literature used.

---

## Family history

Changes how penetrance should be read (`risk-communication.md` §3): with a family history,
family-informed estimates become the right ones; without, population-based estimates are.

- Conditions in first-degree relatives, with ages at diagnosis: _____
- Conditions in second-degree relatives: _____
- Any known genetic diagnosis in the family, with the variant if known: _____
- Any relative who has had clinical genetic testing: _____ (their result may be far more informative
  than your raw data)
- Consanguinity known in the family: _____

---

## Medications and supplements

Makes the pharmacogenomic pass concrete rather than theoretical.

- Current prescription medications: _____
- Drug classes you expect to encounter (planned surgery, a condition in the family, an ongoing
  treatment decision): _____
- Current supplements, with doses: _____
- Any peptides or research compounds currently used: _____ (recorded so interactions can be
  considered; the audit will not recommend or dose any of them)
- Known drug allergies or prior adverse reactions: _____ (a past reaction is stronger evidence than
  any genotype)

---

## Access to confirmatory testing

Determines how much of the audit can reach an actionable conclusion rather than stopping at
"needs confirming".

- Do you have a clinician who will order confirmatory genetic testing? _____
- Access to a clinical genetics service or genetic counsellor? _____
- Can you get routine phenotype bloodwork (ferritin, lipids, 25-OH-D, B12, HbA1c)? _____
  — often **more decisive than the genotype**; see the measure-don't-infer pattern in
  `interventions-evidence.md` §4
- Insurance or employment considerations that make you cautious about having findings in a medical
  record? _____ (a real consideration, and it affects sequencing, not just disclosure)

---

## Network reachability — what this environment can actually verify

**Fill this in before the literature pass, because it decides whether the pass is possible.** The
skill's design defers effect sizes to a live literature search (`variant-catalog.md` §0), and that
instruction is unexecutable where the network blocks the sources. Where it is unexecutable, **a
search tool's prose will happily supply a confident invented number** — so the reachability answer
is a safety control, not an infrastructure note.

Test rather than assume, then record:

- Can you reach a literature index directly (PubMed / PMC / Europe PMC / Crossref)? _____
- Can a page be fetched, or only searched? _____ — search results give *identifiers* inside returned
  URLs; the *numbers* usually live only in generated prose, and those are not the same evidence
- Regulatory sources — a medicines regulator's site, an anti-doping list? _____ *(in the environment
  this skill was built in, both were blocked, which is why `interventions-evidence.md` names
  mechanisms and sends you to the live list instead of quoting it)*
- Your provider's own account pages, for establishing which product tier produced your file? _____

**If the indexes are unreachable:** report it in the report's own research section, take numbers only
from the anchored, provenance-graded figures in `variant-catalog.md` §0, quote them as ranges with
their grade, and **state that the live pass could not be performed** rather than producing figures
that look as though it had.

---

## Output preferences

- Report length: _____ (executive summary only / full six-section report / clinician page only)
- Who else will read it: _____
- Do you want the clinician question list as a separate standalone page? _____
- Technical depth: _____ (plain language throughout / include the grades and rsIDs)

---

## Standing notes

Anything the audit should assume without re-asking — a condition you already know you have, a
finding you have already had confirmed clinically, an interpretation you have already been given and
want checked rather than repeated.

_____

---

## Privacy posture

**A genome is the most sensitive data this library handles.** It identifies you permanently, it
cannot be rotated like a password, and it is partly information about people who never consented.

- **Never commit a genome file.** The marketplace repository this skill ships from ignores the common
  genomic extensions (VCF, gVCF, BCF, BAM/CRAM, FASTQ, PLINK), the provider download archives, and a
  `genomes/` directory — **and none of that travels with the installed plugin.** In *your*
  repository, assume nothing is ignored until `git check-ignore -v <file>` prints a rule.
- **Health and genetic detail belongs in the `.private.md` twin**, which is git-ignored — never in
  this committed template.
- **Do not paste raw data into third-party interpretation services.** Their error rates are
  documented ([PMID 29997392](https://pubmed.ncbi.nlm.nih.gov/29997392/)) and the data-handling terms
  are frequently worse than the interpretation.
- **De-identify when discussing a relative's result**: ages as ranges, no names, no dates of birth.
- **The file is small and feels harmless.** It is not. Treat it like a credential that cannot be
  changed, because that is what it is.
