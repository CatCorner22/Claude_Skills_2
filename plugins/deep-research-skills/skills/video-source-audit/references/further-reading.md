# Further reading

Books and articles that make you better at this work, grouped by what you are trying to learn.

**Contents**
- §0 The verification standard used here — read this first
- §1 Learn to read a study
- §2 Understand risk numbers (the centerpiece literature)
- §3 How good science goes wrong
- §4 How communication distorts findings
- §5 Appraisal and reporting instruments — two different families
- §6 Contested works: cite the dispute, not just the work
- §7 What was dropped, and why

---

## §0 The verification standard used here — read this first

**Every entry below was checked against retrieved catalogue or index records, never against a search
tool's generated prose.** That distinction is the single most important methodological point in this
file, and it generalises to every citation this skill will ever produce.

A web-search tool returns two things: a list of **retrieved records** (titles and URLs from an
index) and a **model-written summary** beneath them. The summary will confidently state a publisher,
year, volume, page range, and DOI **for items that returned no supporting record at all**. It is
generated text, not retrieval. Reading it as evidence is how a citation list acquires perfectly
formed entries that resolve to nothing.

**The rule: an identifier is verified only if it appears in a returned record** — a PMID in a
pubmed.ncbi.nlm.nih.gov URL, a DOI inside a publisher URL, an OpenLibrary OL-id. If the identifier
appears only in the prose, it is unverified, and unverified means it does not ship.

Two further traps this file guards against:

- **Edition vs work.** Catalogue lookups usually land on an *edition* record, so a 1993 reissue of a
  1954 book resolves with a 1993 date. Where the original year matters it is given as the work's
  year, with the edition noted separately.
- **Fuzzy title matching.** Catalogue search returns confident near-misses — a different book, by a
  different author, with a similar title. Match author *and* title before accepting a record.

Where full text is freely available, that is noted, because a source a reader can actually open is
worth more than a better one behind a paywall.

---

## §1 Learn to read a study

| Work | Author(s) | Year | Identifier | What it is for |
| :--- | :--- | :--- | :--- | :--- |
| *Testing Treatments: better research for better healthcare* (2nd ed.) | Evans, Thornton, Chalmers, Glasziou | 2011 | NCBI Bookshelf **NBK66204** — free full text | The best lay introduction to why fair tests of treatments are necessary. Start here. |
| *Know Your Chances: Understanding Health Statistics* | Woloshin, Schwartz, Welch | 2008 | NCBI Bookshelf **NBK115435** — free full text | The plain-language drill on converting health claims into absolute numbers. Ships risk charts and a number converter. |
| *Bad Science* | Goldacre | 2008 | OpenLibrary **OL24468384M** | How to spot a bad study in the wild. |
| *Bad Pharma* | Goldacre | 2012 | OpenLibrary **OL25682902M** | Publication bias and missing trial data as structural, not accidental. |
| *Ending Medical Reversal* | Prasad, Cifu | 2015 | OpenLibrary **OL27208534M** | Why widely adopted practices get overturned — the base rate for "studies show". |
| *Statistics Done Wrong* | Reinhart | — | OpenLibrary work **OL17612294W** | The specific analytical errors, named, with fixes. |

## §2 Understand risk numbers (the centerpiece literature)

This is the evidence base behind the skill's insistence on absolute-beside-relative.

| Work | Identifier | Why it matters here |
| :--- | :--- | :--- |
| Akl et al., "Using alternative statistical formats for presenting risks and risk reductions" (Cochrane Review CD006776) | **PMID 21412897**, DOI 10.1002/14651858.CD006776.pub2 | The single most on-point citation for this skill: a systematic review of RRR vs ARR vs NNT presentation effects. |
| Covey, "A meta-analysis of the effects of presenting treatment benefits in different formats" | **PMID 17873250** | 31 experiments across 24 articles on format effects. |
| Gigerenzer, Gaissmaier, Kurz-Milcke, Schwartz, Woloshin, "Helping Doctors and Patients Make Sense of Health Statistics" | **PMID 26161749** | The natural-frequencies programme that the plain-language method in the taxonomy rests on. |
| Gigerenzer, Edwards, "Simple tools for understanding risks: from innumeracy to insight" (BMJ 2003) | **PMID 14512488** | Short, practical, and the best single thing to hand someone. |
| Wegwarth et al., "Do physicians understand cancer screening statistics?" | **PMID 22393129** | Evidence that the misunderstanding is not confined to lay audiences. |
| Schwartz, Woloshin, Black, Welch, "The role of numeracy in understanding the benefit of screening mammography" | **PMID 9412301** | The screening/PPV problem in a real population. |
| Zipkin et al., "Evidence-based risk communication: a systematic review" | **PMID 25133362** | What actually works when communicating risk. |
| Akl et al., "Framing of health information messages" (Cochrane) | **PMID 22161408** | Gain vs loss framing. |
| Spiegelhalter, "Risk and Uncertainty Communication" | DOI 10.1146/annurev-statistics-010814-020148 | The statistician's overview. |

**Books:** *Calculated Risks* — Gigerenzer — OpenLibrary **OL7947684M** (published in the UK as
*Reckoning with Risk*, OL work **OL28353266W** — **the same book**; do not list both) ·
*Risk Savvy* — Gigerenzer — **OL26179594M** · *The Art of Statistics* — Spiegelhalter —
**OL27934405M** · *The Norm Chronicles* — Blastland & Spiegelhalter — **OL27167950M** (the MicroMort:
personal risk on one comparable scale) · *Innumeracy* — Paulos — work **OL1960756W** ·
*Naked Statistics* — Wheelan — work **OL19167522W** ·
*Calling Bullshit* — Bergstrom & West — 2020 — ISBN **9780525509189**.

## §3 How good science goes wrong

| Work | Identifier |
| :--- | :--- |
| Greenland, Senn, Rothman, Carlin, Poole, Goodman, Altman, "Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations" (Eur J Epidemiol 2016;31:337–350) | **PMID 27209009**, DOI 10.1007/s10654-016-0149-3 — open access |
| Wasserstein, Lazar, "The ASA Statement on p-Values: Context, Process, and Purpose" (Am Stat 2016;70(2):129–133) | DOI 10.1080/00031305.2016.1154108 |
| Simmons, Nelson, Simonsohn, "False-positive psychology" | **PMID 22006061** |
| Munafò et al., "A manifesto for reproducible science" | DOI 10.1038/s41562-016-0021 |
| Chalmers, Glasziou, "Avoidable waste in the production and reporting of research evidence" (Lancet 2009) | **PMID 19525005** |

The Greenland et al. paper is the most directly useful item in this file: it is an enumerated list
of 25 specific misinterpretations of p-values, intervals, and power, and it doubles as a checklist
for the statistics axis.

## §4 How communication distorts findings

This is the literature that justifies the skill's `UPSTREAM-DISTORTION` flag.

| Work | Identifier | Finding |
| :--- | :--- | :--- |
| Sumner et al., "The association between exaggeration in health related science news and academic press releases" (BMJ 2014) | **PMC4262123**, DOI 10.1136/bmj.g7015 | The keystone: exaggeration in news tracks exaggeration already present in the university press release. |
| Independent replication of the above | **PMC6833989** | The pattern held on a fresh sample. |
| Sumner et al., "Exaggerations and Caveats in Press Releases and Health-Related Science News" | **PMID 27978540** / PMC5158314 | Follow-up. |
| "Causal overstatements reduced in press releases following academic study of health news" | **PMC7236584** | Evidence the problem is tractable. |
| Yavchitz, Boutron, Bafeta et al., "Misrepresentation of Randomized Controlled Trials in Press Releases and News Coverage" (PLoS Med 2012) | **PMC3439420** | Where in the chain distortion enters. |
| Boutron, Ravaud, "Misrepresentation and distortion of research in biomedical literature" (PNAS 2018;115:2613–2619) | **PMID 29531025**, DOI 10.1073/pnas.1710755115 | The canonical treatment of "spin", with a taxonomy this skill's fidelity ladder parallels. |
| Gøtzsche, "Believability of relative risks and odds ratios in abstracts" (BMJ 2006) | **PMID 16854948** | Why an abstract-only audit (tier T1) is weak evidence. |

## §5 Appraisal and reporting instruments — two different families

**These are not interchangeable, and conflating them produces a grade that measures prose hygiene
and calls it validity.**

**Reporting guidelines** ask whether the *write-up* is complete. A well-conducted trial reported
badly scores poorly; a poor trial reported meticulously scores well.

- CONSORT 2010 (parallel-group RCTs) — **PMID 20334633**, DOI 10.1136/bmj.c332
- PRISMA 2020 (systematic reviews) — **PMID 33782057** (BMJ 2021;372:n71)
- STROBE (observational studies) — **PMID 18064739**; PLoS Med version DOI 10.1371/journal.pmed.0040296

**Appraisal and certainty instruments** ask whether the *result* can be believed.

- RoB 2 (risk of bias in RCTs) — **PMID 31462531**
- ROBINS-I (non-randomised intervention studies) — **PMID 27733354**
- AMSTAR 2 (systematic-review conduct) — **PMID 28935701**
- GRADE (certainty in a body of evidence) — **PMID 18436948**

**Caveat when citing any of these:** CONSORT, PRISMA and STROBE were each co-published across
several journals simultaneously, so more than one PMID legitimately is "the" paper. Cite the PMID
*and* the journal version you actually consulted; do not assert a canonical volume and page you
did not see.

**AMSTAR 2 is also the design precedent for this skill's rubric.** Its output is a confidence rating
— high / moderate / low / critically low — driven by which *critical domains* fail, deliberately not
a summed score, precisely because one critical flaw can invalidate a review that scores well
elsewhere. That is the same reasoning behind this skill's cap ladder and its refusal to average the
three axes.

## §6 Contested works: cite the dispute, not just the work

Presenting a disputed source as settled is exactly the failure this skill grades other people for.

- **Ioannidis, "Why most published research findings are false"** (PLoS Med 2005) — **PMID 16060722**.
  The field's most-cited manifesto *and* formally disputed: Goodman & Greenland's critique
  (**PMID 17456002**), Ioannidis's reply (**PMID 17593900**), and a published correction to the
  original noting an error in a table equation (**PMID 36007233**). Cite it with its dispute.
- **Open Science Collaboration, "Estimating the reproducibility of psychological science"**
  (Science 2015) — **PMID 26315443**. The headline "36% replicated" is an estimate under dispute:
  Gilbert et al.'s comment (**PMID 26941311**) and a Bayesian reanalysis (**PMID 26919473**).
- **Ziliak & McCloskey, *The Cult of Statistical Significance*** — rebutted at length by Hoover &
  Siegler, DOI 10.1080/13501780801913298, with the authors' reply DOI 10.1080/13501780801913413.
- **Kahneman, *Thinking, Fast and Slow*** — excellent for the System 1 / System 2 framing, **not**
  as an evidence base: several popularised results failed to replicate, the load-bearing receipt
  being the multi-lab preregistered replication of ego depletion (**PMID 27474142**), which found a
  trivial effect not distinguishable from zero across 23 labs.
- **Huff, *How to Lie with Statistics*** (1954) — not discredited, but historically complicated.
  *Statistical Science* 20(3) (2005) ran a fiftieth-anniversary symposium including Steele,
  "Darrell Huff and Fifty Years of How to Lie with Statistics", DOI 10.1214/088342305000000205.
  Cite the symposium beside the book.

## §7 What was dropped, and why

The drops are as informative as the keeps, because they show the standard being enforced.

- **Nuovo, Melnikow & Chang, on reporting NNT and absolute risk reduction in RCTs (JAMA 2002)** —
  dropped. A domain-restricted PubMed search returned ten unrelated records and no matching PMID,
  while the generated summary confidently supplied a volume and page range. That is precisely the
  fabrication pattern §0 describes: perfectly formed, entirely unsupported. It would have been the
  easiest entry in this file to include and nobody would have questioned it.
- Two further well-known candidate books failed to resolve to a catalogue record matching both
  author and title, and were dropped rather than cited from memory.

If you extend this list, extend the standard with it: **an entry that cannot be resolved to a
retrieved record does not go in, however confident you are that it exists.**
