# Acquisition and source tracing

How to get the transcript, how to find what the video cited, how to resolve it, and — the part
that matters most — how each of these fails and what to do instead of guessing.

**Contents**
- §1 Reachability preflight and the three outcomes
- §2 Where sources hide in a video
- §3 The resolver ladder
- §4 Reading the source: depth tiers
- §5 Detecting a source that does not exist
- §6 Failure modes, and what the audit says when they fire

---

## §1 Reachability preflight and the three outcomes

Run this **before** promising an audit. The single most damaging thing this skill can do is produce
a confident grade for a video it never read.

```bash
# Metadata only — cheap, and answers "can I reach this at all?"
yt-dlp --skip-download --dump-json "<url>" > meta.json

# Transcript. Prefer human captions; fall back to auto-captions.
yt-dlp --skip-download --write-subs --write-auto-subs \
       --sub-langs "en.*" --sub-format vtt --convert-subs srt -o "vid" "<url>"

# Description text (where the source links live)
python3 -c "import json;print(json.load(open('meta.json'))['description'])"
```

The bundled script wraps all three and normalizes the result:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/video-source-audit/scripts/fetch_transcript.py" "<url>"
```

**Three outcomes, never to be conflated:**

| Outcome | How you know | What the audit does |
| :--- | :--- | :--- |
| Reachable, captions exist | transcript file written, non-empty | proceed |
| Reachable, no captions | metadata fetched, subtitle list empty | say so; offer to work from a pasted transcript; do not infer content from the title |
| Not reachable | fetch errors — network policy, geo-block, private, removed, age-gated | **stop.** Report which error. Emit `NOT-GRADED`. |

The third row is the one that requires discipline. In a restricted network, a blocked fetch and a
genuinely dead link return *indistinguishable* failures. The audit must therefore report the
**mechanism** it observed, not the conclusion it would like to draw:

- `CONNECT tunnel failed, response 403` / an explicit egress-blocked error → *this environment*
  cannot reach the host. Says nothing about whether the video or source exists.
- HTTP 404 from a host you did reach → the resource is absent.
- `Video unavailable` / `Private video` from yt-dlp → reached the platform, the video is gone.

Writing "the source does not exist" when what happened was "I could not reach the network" is the
worst error this skill can make, because it converts a tooling limitation into an accusation.

### Auto-caption de-duplication (do not skip this)

YouTube's auto-caption VTT uses a **rolling two-line window**: each cue repeats the tail of the
previous cue so the on-screen text scrolls. Fed to a model raw, the same sentence appears three or
four times. Measured across real auto-caption files, the rolling format runs on the order of **15-20x** the
token cost of the same content de-duplicated — the exact multiple depends on whether the
comparison is against plain or timecoded text, so treat the order of magnitude as the finding. Collapse it before doing anything else — the bundled
script does this, and `--convert-subs srt` alone does **not**.

De-duplicated, transcript size is a non-problem: a 60-minute talk is on the order of 15,000 tokens
with timecodes, and a 3-hour podcast well under 50,000. **Do not build a chunking strategy you do
not need.** The real context pressure in this skill comes from the *sources*, which are numerous
and long, not from the transcript, which is one document.

---

## §2 Where sources hide in a video

Check all seven. Most audits that miss a source missed it in one of the last four.

1. **Description links** — the primary location. Present in full in the metadata JSON's description
   field; it is not truncated there the way it is in a collapsed web view.
2. **Pinned comment** — creators routinely post corrections and source lists here, and a correction
   the creator issued themselves is directly relevant to the comprehensiveness grade.
3. **Spoken references** — "a 2019 Lancet paper by Smith", "the Framingham data". These have no
   link and must be resolved from the words alone (§3).
4. **Chapter titles** — often name the study or concept.
5. **Linked companion article** — a newsletter, blog post, or Substack carrying the real citation
   list. Follow it; it frequently contains everything the description omitted.
6. **On-screen citations** — text or a screenshot of a paper shown in frame. **These are invisible
   to a transcript-based audit.** This is a hard limit of the method, not an oversight, and it must
   be disclosed: say that on-screen sources may exist and were not captured, and note the effect on
   the comprehensiveness grade. If the user can screenshot them, ask.
7. **Shortened links** — expand before resolving, and report the destination, since a shortener
   hides where a "source" actually points (sometimes at a store page, not a study).

---

## §3 The resolver ladder

Work top to bottom; stop when you have a durable identifier plus canonical metadata.

| Source shape | Resolver | Read from the response |
| :--- | :--- | :--- |
| DOI | Crossref `api.crossref.org/works/{doi}` | `message.title`, `author`, `container-title`, `issued` |
| DOI not in Crossref | DataCite `api.datacite.org/dois/{doi}` | Zenodo/OSF/figshare/Dryad live here, **not** in Crossref |
| Any DOI or title | OpenAlex `api.openalex.org/works/doi:{doi}` | also gives open-access status and cited-by count |
| Biomedical | PubMed E-utilities `esearch` → `esummary` → `efetch` | PMID, publication type, retraction flag |
| Biomedical full text | Europe PMC REST | often full text where PubMed gives only the abstract |
| Preprint | arXiv API | note preprint status explicitly in the ledger |
| Open-access copy | Unpaywall `api.unpaywall.org/v2/{doi}?email=` | requires an email parameter |
| Book | OpenLibrary; Google Books | resolve to a **work**, then note the edition separately |

**Operational notes that save real time:**

- **Identify yourself, but check how each service wants it — they differ, and one changed.**
  Crossref runs a "polite pool" keyed on an email in the query (`?mailto=`) or User-Agent, and
  service is more consistent inside it. Unpaywall *requires* an email parameter. **OpenAlex now
  authenticates with an API key** (`?api_key=`) — the mailto polite pool it previously operated is
  deprecated, so mailto-only code silently gets the unauthenticated budget. Verify each service's
  current requirement rather than assuming they are alike; this is exactly the kind of detail that
  moves.
- **Distinguish 404 from 429.** A 404 means the identifier is wrong or the record is elsewhere; a
  429 means back off and retry. Treating a rate-limit as a nonexistent source is a false accusation.
- **A resolved edition is not a first-publication year.** Catalogue lookups usually land on an
  *edition* record. A 1993 reissue of a 1954 book will resolve with a 1993 date. Report the work's
  original year and the edition separately, or report neither.
- **Verify the citation mechanically** rather than by eye:
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/medical-research-detective/scripts/verify_citation.py" --doi <doi> --claim-title "..." --claim-author "..." --claim-year <year>`
  It resolves the identifier, compares claimed metadata to canonical, and flags retractions.
- **When only a search tool is available**, treat the returned link records as evidence and the
  generated prose summary as *not* evidence. Search summaries state confident publishers, years,
  volumes, and DOIs for items that produced no supporting record. `references/further-reading.md`
  documents this failure and the standard used against it.

### Resolving a spoken reference with no link

"A 2019 Lancet paper by Smith showing X" → search the claim's substance plus the named constraints
(`X AND Smith AND 2019`), restricted to the journal where one is named. Then confirm the candidate
actually contains the claim before accepting it. If several papers fit and none is decisive, the
claim is `SOURCE-AMBIGUOUS`: the video cited too vaguely to be checked, which is itself a
comprehensiveness finding (checklist item 1) rather than an accuracy failure.

---

## §4 Reading the source: depth tiers

Record which tier each claim was audited at. The report must state this, because the tiers do not
support the same conclusions.

| Tier | What was read | What it supports |
| :--- | :--- | :--- |
| **T3 Full** | methods, results tables, limitations | any fidelity code, including reversal and cherry-picking |
| **T2 Partial** | abstract + results table or figure | most codes; weak on cherry-picking and on scope |
| **T1 Abstract only** | abstract | existence and rough direction only |
| **T0 Not read** | metadata only, or unreachable | **nothing.** Mark `SOURCE-NOT-READ`, exclude from the denominator |

Abstracts systematically overstate their own papers — spin is a documented and measured feature of
abstract writing. An audit conducted at T1 that reports a confident fidelity verdict has inherited
the abstract's spin and laundered it into a grade. Never let T1 evidence produce a reversal finding.

---

## §5 Detecting a source that does not exist

Three distinct states hide behind "I could not find it", and they grade differently:

1. **Fabricated** — the identifier resolves to nothing *from a host you successfully reached*, or
   resolves to a real paper whose metadata does not match the claim at all. This is the only one
   that may trigger the fabrication cap.
2. **Unreachable** — the resolver could not be contacted. Not evidence of anything. `SOURCE-NOT-READ`.
3. **Ambiguous** — the reference is too vague to identify uniquely (§3). A citation-quality finding.

Before recording a fabrication, confirm you reached the resolver at all: fetch a known-good
identifier through the same path in the same session. If that also fails, you are in state 2 and
have no fabrication finding to make.

---

## §6 Failure modes, and what the audit says when they fire

| Failure | What the audit reports |
| :--- | :--- |
| Video unreachable | `NOT-GRADED`, with the observed error. No grades of any kind. |
| No captions and no pasted transcript | `NOT-GRADED`. Offer the paste path. |
| Video is not about sources at all (vlog, opinion, entertainment) | Say so and stop. There is nothing to audit; this is not a failing grade, it is the wrong instrument. |
| Sources are on screen only | Proceed, disclose the gap, and cap comprehensiveness confidence. |
| All sources paywalled at abstract | Proceed at T1, and say plainly that no reversal or cherry-picking finding can be supported. |
| The "source" is another video | Follow one hop to *its* sources. If the chain never reaches primary literature, that is the finding. |
| Non-English video | Audit only if the transcript is reliable; translation error is indistinguishable from misrepresentation, so say which language and how the transcript was obtained. |
| Fewer than five checkable claims | `INCOMPLETE` on the rate-based axes — but a proven cap still fires (see the grading rubric's precedence rule). |
