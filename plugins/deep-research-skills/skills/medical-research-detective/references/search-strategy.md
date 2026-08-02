# Search strategy

Read at stages 3–4. How to search wide enough and deep enough that "extensive" is literally true.

## Contents
- [The databases and what each is for](#the-databases-and-what-each-is-for)
- [Building a query](#building-a-query)
- [MeSH and synonym expansion](#mesh-and-synonym-expansion)
- [Co-occurrence searches (the dot-connectors)](#co-occurrence-searches-the-dot-connectors)
- [Citation chaining](#citation-chaining)
- [Google Scholar technique](#google-scholar-technique)
- [Finding full text legally](#finding-full-text-legally)
- [When to stop: saturation](#when-to-stop-saturation)
- [Logging the search](#logging-the-search)

## The databases and what each is for

No single database is sufficient — they index different journals, and a one-database search silently
misses whole literatures.

| Database | Best for | Notes |
|---|---|---|
| **PubMed / MEDLINE** | Core biomedical literature | Free; MeSH indexing; the default first pass. `scripts/search_pubmed.py` automates it via NCBI E-utilities |
| **Europe PMC** | Biomedical + preprints + full text | Free; searches full text, not just abstracts — catches findings buried in a paper's body |
| **Cochrane Library** | Systematic reviews, trial quality | The top of the evidence hierarchy; check here early for any well-studied question |
| **Google Scholar** | Breadth, grey literature, forward citations | Indexes beyond MEDLINE; the "Cited by" feature is the best forward-chaining tool |
| **ClinicalTrials.gov / WHO ICTRP** | Ongoing and unpublished trials | Reveals what is being studied now, and detects publication bias (registered trials never published) |
| **Drug label sources** | Approved adverse effects and interactions | Regulator-published labeling in the relevant country; authoritative for known effects |

Search at minimum PubMed + Europe PMC + Google Scholar for any real case; add Cochrane whenever a
question is well-studied enough to have reviews, and ClinicalTrials.gov whenever the question is
about a treatment.

## Building a query

Frame each hypothesis as a **PICO-style** question first — it forces the query to be specific:

- **P**opulation: who (age band, sex, condition, e.g. "adults with type 2 diabetes")
- **I**ntervention/**E**xposure: the drug, deficiency, or exposure being tested
- **C**omparison: versus what (placebo, another drug, no exposure) — often absent, that is fine
- **O**utcome: the finding you are trying to explain

Then translate to boolean, with concept blocks OR'd internally and AND'ed together:

```
(concept A term1 OR term2 OR term3) AND (concept B term1 OR term2) AND (limits)
```

Practical rules:
- **Start broad, then narrow.** A too-specific first query returns nothing and tells you nothing.
  Widen until you get hits, then add constraints.
- **Search each concept alone first** to learn the vocabulary the literature actually uses, then
  combine.
- Use **filters** deliberately (publication type, species, date), and note that filtering to humans
  too early can hide the mechanistic work that generates hypotheses.
- Record queries verbatim so the search is reproducible (see [Logging](#logging-the-search)).

## MeSH and synonym expansion

The single most common reason a search misses a paper is vocabulary mismatch. For every concept,
expand along four axes before searching:

1. **MeSH / controlled vocabulary** — the indexed subject heading, which catches papers regardless of
   the words the authors chose. Look the term up rather than guessing it.
2. **Generic and brand drug names** — the literature uses generic; patients and some case reports use
   brand. Search both, plus the drug *class*.
3. **Lay and clinical terms** — "numbness and tingling" vs. "paresthesia"; "heartburn" vs. "gastro-
   esophageal reflux"; "dizziness" vs. "vertigo"/"presyncope" (which are clinically different — pick
   deliberately).
4. **Spelling and morphology** — British vs. American spellings, singular/plural, hyphenation, and
   truncation (`neuropath*` catches neuropathy/neuropathic/neuropathies).

Include historical or superseded names for conditions and drugs; older literature uses them, and old
literature is where forgotten connections live.

## Co-occurrence searches (the dot-connectors)

This is the step that does the actual detective work. For every pair in the finding matrix
(`dot-connection-method.md`), run the pair directly:

```
("finding A" OR synonymA) AND ("finding B" OR synonymB)
```

Read the results by *type*, because each type means something different:
- **A review or cohort linking them** → potentially an Established/Supported connection.
- **Only case reports** → a Lead. Real, documented, but not established.
- **Nothing at all** → either genuinely unrelated, or a true cross-silo gap. Distinguish by trying
  the bridge search (shared drug / nutrient / mechanism / upstream condition) from the method file.
  Finding nothing is informative and should be reported, not silently dropped.

Also run, for each drug: `"<drug>" AND "<finding>"`, `"<drug>" AND (deficiency OR depletion)`, and
`"<drug A>" AND "<drug B>" AND interaction`.

## Citation chaining

One good paper is a map to a whole literature. Chase both directions, always:

- **Backward** — mine its reference list for the foundational work it rests on. Fast way to reach the
  primary sources behind a claim.
- **Forward** — find everything that has cited it since ("Cited by" in Google Scholar, "Cited by" in
  Europe PMC). This is how you discover that a 2015 finding was overturned in 2021, or that someone
  later tested exactly your hypothesis.

Prioritize chaining from: the most recent systematic review (its references are a curated map), and
any paper that is unusually on-point. Chain at least two levels deep on the best sources — the
single highest-yield habit in literature research, and the one that most distinguishes deep research
from a first-page search.

## Google Scholar technique

Scholar's breadth is its value; its lack of controlled vocabulary is its weakness. Use it for what it
is good at:

- **Forward citations** — "Cited by N" is the best free forward-chaining tool available.
- **Phrase search** with quotes for exact clinical phrases; `-term` to exclude a dominating topic.
- **Field limits**: `intitle:` to force a concept into the title when results are noisy;
  `author:"Last F"` to follow a researcher who works the niche.
- **Date-restrict** to catch recent work, then run the same query unrestricted to catch the classics.
- **Related articles** on a strong hit to find its neighborhood.
- Watch for the same paper appearing many times (preprint + journal + repository) — count it once.
- Scholar indexes predatory and non-peer-reviewed venues too, so apply
  `evidence-appraisal.md`'s venue checks to anything you find only there.

## Finding full text legally

Claim-checking (stage 6c) needs the actual text, not the abstract. In order:

1. **Open-access versions** — PubMed Central, Europe PMC, the journal's own open archive, the DOAJ.
2. **Preprint servers** — for the author's manuscript version of an otherwise-paywalled paper.
3. **Author copies** — many authors post accepted manuscripts on institutional repositories.
4. **Institutional or public library access** — if the user has it (record in `your-environment.md`);
   many public and university libraries provide journal access to members.
5. **Interlibrary loan / requesting from the author** — slow but legitimate.

Never use pirated full-text sources. When full text genuinely cannot be reached, say so and mark the
claim's support level as abstract-only — an abstract regularly overstates what the paper shows.

## When to stop: saturation

Stop when **new queries stop returning new relevant papers** — not when you have "enough" or when the
first plausible answer appears. Concretely, you have reached saturation when:

- The last several distinct queries returned only papers you had already seen.
- Backward and forward chaining from the best sources produces no new on-point work.
- Each hypothesis has been searched both for support **and** for disconfirmation.
- The pair-matrix has been run to completion, including the pairs that returned nothing.

If you stop before saturation (time, access limits), say so explicitly in the case file's gaps
section and name which searches remain unrun. A stated limit is fine; an unstated one is misleading.

## Logging the search

Keep a search log and deliver it with the case file. It makes the work reproducible and shows the
depth honestly:

| Query | Database | Filters | Hits | Kept | Why |
|---|---|---|---|---|---|
| `("drug X" ) AND (deficiency OR depletion)` | PubMed | humans, 10y | 47 | 6 | 2 cohorts, 4 reviews on the depletion link |
| `"finding A" AND "finding B"` | Europe PMC | full text | 3 | 0 | all unrelated context; genuine gap |

The "kept 0" rows matter as much as the others — they are the evidence that a connection was looked
for and not found.
