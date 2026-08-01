# Citation verification — the triple check

Read at stage 6. This is the anti-hallucination core of the skill. In a medical context a fabricated
or misattributed citation can drive a real decision about a real body, so verification is mechanical
and non-negotiable.

## Contents
- [The rule](#the-rule)
- [Why this is necessary](#why-this-is-necessary)
- [Check 1: existence](#check-1-existence)
- [Check 2: metadata accuracy](#check-2-metadata-accuracy)
- [Check 3: claim support](#check-3-claim-support)
- [Running the verifier](#running-the-verifier)
- [Manual fallback](#manual-fallback)
- [Failure handling](#failure-handling)
- [Labeling in the output](#labeling-in-the-output)
- [Verifying someone else's citations](#verifying-someone-elses-citations)

## The rule

**No citation reaches the output until it passes all three checks:**

1. **It exists** — the DOI or PMID resolves to a real record.
2. **Its metadata matches** — title, authors, journal, and year agree with the canonical record.
3. **It supports the claim** — the source actually states what you attached to it, and you can quote
   the sentence.

A citation failing any check is **removed or explicitly labeled unverified** — never quietly softened
with a hedge and left sitting beside verified ones.

Never write a citation from memory. Every reference in the case file must have been resolved during
this session, or be marked unverified.

## Why this is necessary

Language models produce citation-shaped text fluently: plausible author names, a real journal, a
year that fits, a DOI with the right format — for a paper that does not exist. The failure is
invisible precisely because the output looks correct. Three distinct failure modes:

- **Fabrication** — the paper does not exist at all.
- **Misattribution** — the paper exists, but not with those authors, that year, or that title; or the
  DOI belongs to a different paper.
- **Claim drift** — the paper exists and is cited correctly, but does not say what it is cited for.
  This is the most common and the hardest to catch, because everything except the substance checks
  out.

Check 3 exists specifically to catch claim drift, which checks 1 and 2 cannot detect.

## Check 1: existence

Resolve the identifier against an authoritative registry:

- **DOI** → Crossref (`https://api.crossref.org/works/{DOI}`) or `https://doi.org/{DOI}`. A valid DOI
  returns a metadata record; an invented one returns 404.
- **PMID** → PubMed via NCBI E-utilities `esummary.fcgi?db=pubmed&id={PMID}`. A record comes back or
  it does not.
- **No identifier at all** → search the exact title in PubMed/Europe PMC/Scholar. If a paper with
  that title cannot be found in any database, treat it as **non-existent** until proven otherwise.

A DOI that is merely well-formed proves nothing — it must actually resolve.

## Check 2: metadata accuracy

Compare the claimed citation against the canonical record field by field:

| Field | Passes when | Common failure |
|---|---|---|
| Title | Matches (ignoring case/punctuation/subtitle) | DOI belongs to a different paper |
| First author | Surname matches | Plausible-but-wrong author invented |
| Journal | Matches (accounting for abbreviations) | Prestigious journal substituted |
| Year | Matches, or differs only by online-vs-print | Year drifted to fit a narrative |
| Volume/pages | Match when present | Fabricated detail |

Mismatch handling: a **title or first-author mismatch is disqualifying** — the citation is wrong,
even if a real paper exists at that DOI. Cite the canonical record or drop it. Minor journal-
abbreviation or online-first year differences are acceptable; note them.

## Check 3: claim support

The check that requires actually reading:

1. Retrieve the **full text** where possible (`search-strategy.md` lists legal routes); the abstract
   alone is often an overstatement of the paper.
2. Find the specific passage supporting the claim and **quote it verbatim** in your notes, with its
   location (section, or page if paginated).
3. Confirm the claim does not exceed the source:
   - Does the population match (adults vs. children, healthy vs. comorbid)?
   - Does the study design support the verb used? ("caused" needs more than a cross-sectional study.)
   - Are the effect size and direction represented accurately?
   - Are stated limitations reflected, rather than dropped?
4. If only the abstract was available, mark the claim **abstract-only** — a real and disclosable
   limitation.

If no passage in the source states the claim, the citation does not support it. Find a source that
does, or reduce the claim to what the source actually says.

## Running the verifier

`scripts/verify_citation.py` automates checks 1 and 2 against free, key-less APIs (Crossref, NCBI
E-utilities, Europe PMC). **Check 3 always requires a human/agent reading the text** — no script can
do it.

```bash
# Resolve a DOI and print canonical metadata
python scripts/verify_citation.py --doi 10.1056/NEJMoa2034577

# Resolve a PMID
python scripts/verify_citation.py --pmid 33301246

# Verify a claimed citation: flags title/author/year mismatches
python scripts/verify_citation.py --doi 10.1056/NEJMoa2034577 \
    --claim-title "Safety and Efficacy of the ..." \
    --claim-author "Polack" --claim-year 2020

# JSON output for batch work; exits non-zero if any check fails
python scripts/verify_citation.py --doi 10.xxxx/yyyy --json

# Offline logic tests (no network needed)
python scripts/verify_citation.py --self-test
```

It reports: existence, canonical metadata, field-by-field comparison against any claimed values,
inferred country of origin (see `source-provenance.md`), and retraction indicators. It exits non-zero
when a check fails, so it can gate a batch.

**When the network is unavailable** the script says so plainly rather than guessing — never interpret
a network failure as verification. Fall back to the manual process below and mark the citations
unverified.

## Manual fallback

Without the script, verify by hand:

1. Open `https://doi.org/{DOI}` — it should land on the paper's page.
2. Search the exact title in PubMed and Europe PMC.
3. Compare first author, journal, year against what you plan to write.
4. Check the record for a retraction notice or erratum.
5. Retrieve the full text and quote the supporting sentence.

Slower, equally valid. What is not valid is skipping it.

## Failure handling

| Failure | Action |
|---|---|
| DOI/PMID does not resolve | **Remove the citation.** Do not reword it; find a real source or drop the claim |
| Title/author mismatch | Correct to the canonical record, or remove |
| Paper is retracted | Remove as support. May be mentioned only if explicitly labeled retracted |
| Predatory/non-peer-reviewed venue | Downgrade to unverified lead; do not use as support (`evidence-appraisal.md`) |
| Full text unreachable | Keep, marked **abstract-only**; state the limitation |
| Source does not state the claim | Fix the claim to match the source, or find a different source |
| Network unavailable | Mark all affected citations **unverified**; list exactly what was not checked |

Removing a citation often means weakening or dropping the claim it supported. That is the correct
outcome — the alternative is a confident statement resting on nothing.

## Labeling in the output

Every reference in the case file's list carries its verification status:

```
[V] Verified — identifier resolved, metadata matched, claim confirmed against the text
[A] Abstract-only — identifier and metadata verified; claim checked against the abstract only
[U] Unverified — could not be checked (state why: no network, no identifier, paywalled)
[R] Retracted — shown for completeness; does not support any claim
[X] Excluded-source — country of origin outside the allowed set; quarantine appendix only
```

Include a one-line verification summary — e.g. "27 sources cited: 24 verified, 2 abstract-only, 1
unverified (paywalled); 3 excluded-source leads listed separately" — so the reader can see the
integrity of the evidence base at a glance.

## Verifying someone else's citations

A standalone use of this skill: someone hands you a reference list — from a paper, a supplement
marketing page, a forum post, or an AI-generated answer — and wants to know whether it is real.

Run the same three checks on each entry and return a table: identifier, resolves?, metadata match?,
supports the stated claim?, retracted?, venue quality. Report totals plainly. AI-generated medical
reference lists in particular frequently contain fabricated or misattributed entries, so check every
one rather than spot-checking — and say which specific entries failed and how.
