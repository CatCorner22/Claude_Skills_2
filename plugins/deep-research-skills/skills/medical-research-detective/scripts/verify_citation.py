#!/usr/bin/env python3
"""Verify a medical citation against authoritative registries.

Implements checks 1 (existence) and 2 (metadata accuracy) of the triple-check
protocol in references/citation-verification.md. Check 3 (claim support) always
requires reading the source and cannot be automated.

Also reports inferred country of origin for the source-provenance policy
(references/source-provenance.md) and flags retraction indicators.

Usage:
  verify_citation.py --doi 10.1056/NEJMoa2034577
  verify_citation.py --pmid 33301246
  verify_citation.py --doi 10.xxxx/yyy --claim-title "..." --claim-author "Smith" --claim-year 2020
  verify_citation.py --doi 10.xxxx/yyy --json
  verify_citation.py --self-test          # offline logic tests, no network

Exit codes: 0 = all requested checks passed, 1 = a check failed, 2 = usage/network error.

Stdlib only. Uses free, key-less public APIs: Crossref, NCBI E-utilities, Europe PMC.
Be polite to these services: they are free and shared. Provide a contact e-mail via
--mailto (Crossref gives faster service to identified callers) and avoid hammering
them in tight loops.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

CROSSREF = "https://api.crossref.org/works/"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
USER_AGENT = "medical-research-detective/1.0 (citation verification; stdlib urllib)"
TIMEOUT = 20

# --- Country policy (see references/source-provenance.md) ------------------
EXCLUDED_COUNTRIES = {"china", "russia"}

# Affiliation strings are matched against two tiers of signal.
#
# A *country name* is unambiguous and settles the question. A *city* is a weaker
# hint used only when the string names no country at all — because cities are
# not unique across countries and a bare substring match on them is wrong in
# both directions: "Moscow, ID 83844, USA" (University of Idaho) is not Russian,
# and "Busan" contains the letters "usa". Matching is therefore word-bounded,
# and country names win over cities within the same affiliation string.
#
# Matching is deliberately conservative: it flags for human confirmation rather
# than deciding. Affiliation metadata is frequently missing or partial, and this
# table covers only common countries — see infer_provenance().
_COUNTRY_HINTS = [
    # (country, country-name signals, city signals)
    ("china", ["china", "chinese", "p.r.c", "prc"],
     ["beijing", "shanghai", "guangzhou", "shenzhen", "wuhan", "chengdu",
      "tianjin", "nanjing", "hangzhou"]),
    ("russia", ["russia", "russian", "russian federation"],
     ["moscow", "st. petersburg", "saint petersburg", "novosibirsk",
      "yekaterinburg"]),
    ("usa", ["usa", "u.s.a", "united states"],
     ["boston", "new york", "bethesda", "baltimore"]),
    # "wales" is deliberately absent as a bare hint: it fires inside "New South Wales"
    # (Australia) and resolved that to uk with no caveat. Qualified forms only.
    ("uk", ["united kingdom", "great britain", "england", "scotland", "cymru",
           "wales, uk", "cardiff", "swansea", "uk", "u.k"],
     ["london", "oxford", "manchester", "edinburgh"]),
    ("canada", ["canada"], ["toronto", "montreal", "vancouver", "ottawa"]),
    ("germany", ["germany", "deutschland"],
     ["berlin", "munich", "münchen", "heidelberg", "hamburg", "frankfurt"]),
    ("japan", ["japan"], ["tokyo", "osaka", "kyoto", "nagoya", "sapporo"]),
    ("south africa", ["south africa"],
     ["cape town", "johannesburg", "pretoria", "durban"]),
    ("australia", ["australia"], ["sydney", "melbourne", "brisbane", "perth"]),
    ("netherlands", ["netherlands"],
     ["amsterdam", "rotterdam", "utrecht", "leiden"]),
    ("france", ["france"], ["paris", "lyon", "marseille", "toulouse"]),
    ("sweden", ["sweden"], ["stockholm", "gothenburg", "uppsala", "karolinska"]),
    ("denmark", ["denmark"], ["copenhagen", "aarhus"]),
    ("norway", ["norway"], ["oslo", "bergen"]),
    ("finland", ["finland"], ["helsinki"]),
    ("italy", ["italy", "italia"], ["rome", "milan", "bologna"]),
    ("spain", ["spain"], ["madrid", "barcelona"]),
    ("switzerland", ["switzerland"], ["zurich", "geneva", "basel", "bern"]),
    ("israel", ["israel"], ["tel aviv", "jerusalem", "haifa"]),
    ("south korea", ["south korea", "republic of korea"], ["seoul"]),
    ("singapore", ["singapore"], []),
    ("ireland", ["ireland"], ["dublin"]),
    ("new zealand", ["new zealand"], ["auckland", "wellington"]),
    ("belgium", ["belgium"], ["brussels", "leuven", "ghent"]),
    ("austria", ["austria"], ["vienna", "wien"]),
    ("poland", ["poland"], ["warsaw", "krakow"]),
    ("taiwan", ["taiwan"], ["taipei"]),
]

RETRACTION_MARKERS = [
    "retracted", "retraction", "withdrawn",
    "expression of concern", "editorial expression of concern",
]

# Nobiliary and compound-surname particles. These belong to the surname, so
# "van der Berg J" and "van der Berg" must resolve to the same key.
NAME_PARTICLES = {
    "van", "von", "de", "del", "della", "der", "den", "des", "du", "da", "das",
    "dos", "la", "le", "di", "do", "ter", "ten", "af", "av", "bin", "ibn", "al",
    "abu", "mac", "mc", "st", "san", "santa",
}

# Publication types are authoritative: PubMed assigns these deliberately.
RETRACTION_PUBTYPES = {
    "retracted publication",
    "retraction of publication",
    "expression of concern",
    "editorial expression of concern",
}

# Titles are NOT authoritative, so the marker must be anchored at the start and
# followed by the punctuation a real notice uses ("RETRACTED: <original title>",
# "Retraction of: <original>", "WITHDRAWN: ..."). A bare substring search flags
# ordinary papers -- "Retraction of consent in emergency research", "Patients
# withdrawn from therapy", "Expression of concern among caregivers" were all
# reported as retracted before this was anchored, and the caller turns any signal
# into "do not use as support", i.e. it makes the researcher discard good evidence.
_TITLE_RETRACTION_RE = re.compile(
    r"^\s*\[?\s*"
    r"(editorial expression of concern|expression of concern|retracted|retraction|withdrawn)"
    r"\b\s*(?:article)?\s*(?:of)?\s*[:\-–—]",
    re.I,
)


class VerificationError(Exception):
    pass


# ======================================================================
# Network layer — isolated so all logic below is testable offline.
# ======================================================================
def http_get_json(url: str, params: dict | None = None, mailto: str | None = None):
    """GET a URL and parse JSON. Raises VerificationError with a plain message."""
    if params:
        if mailto:
            params = dict(params, mailto=mailto)
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # genuine "does not exist"
        raise VerificationError(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}")
    except urllib.error.URLError as e:
        raise VerificationError(
            f"network unavailable ({e.reason}) — cannot verify; "
            f"mark citations UNVERIFIED rather than assuming they are valid")
    except json.JSONDecodeError:
        raise VerificationError("response was not valid JSON")


# ======================================================================
# Pure logic — unit-tested by --self-test
# ======================================================================
def normalize_title(s: str) -> str:
    """Lowercase, strip punctuation and articles, collapse whitespace."""
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def compact_title(s: str) -> str:
    """All non-alphanumerics removed. Makes 'B-12'=='B12' and
    'double-blind'=='double blind', which are pervasive in medical titles."""
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def titles_match(a: str, b: str, threshold: float = 0.85) -> bool:
    """Token-overlap comparison, tolerant of subtitles, punctuation, and the
    hyphenation differences common in medical titles."""
    na, nb = normalize_title(a), normalize_title(b)
    if not na or not nb:
        return False
    if na == nb or na.startswith(nb) or nb.startswith(na):
        return True
    # Hyphenation-insensitive comparison (B-12 vs B12, COVID-19 vs COVID19).
    ca, cb = compact_title(a), compact_title(b)
    if ca and cb and (ca == cb or ca.startswith(cb) or cb.startswith(ca)):
        return True
    ta, tb = set(na.split()), set(nb.split())
    if not ta or not tb:
        return False
    overlap = len(ta & tb) / min(len(ta), len(tb))
    return overlap >= threshold


def _is_initials(tok: str) -> bool:
    """True for 'J', 'J.', 'JA', 'J.A.' — an initials token, not a name."""
    t = tok.replace(".", "")
    return 0 < len(t) <= 3 and t.isalpha() and t.isupper()


def surname_of(author: str) -> str:
    """Best-effort surname from 'Smith J', 'J. Smith', 'Smith, John A.', 'van der Berg J'.

    Multi-particle surnames are kept whole. The previous version returned parts[0]
    whenever the last token was initials, so 'van der Berg J' -> 'van' while the same
    person written 'van der Berg' -> 'berg', and authors_match then failed on two
    renderings of one name.
    """
    if not author:
        return ""
    a = author.strip()
    if "," in a:
        return a.split(",")[0].strip().lower()
    parts = [p for p in re.split(r"\s+", a) if p]
    if not parts:
        return ""

    # 'Smith J' / 'van der Berg JA' -> trailing initials; surname is everything before them
    if len(parts) > 1 and _is_initials(parts[-1]):
        return " ".join(parts[:-1]).lower()

    # 'J. Smith' / 'J A Smith' -> leading initials; surname is everything after them
    lead = 0
    while lead < len(parts) - 1 and _is_initials(parts[lead]):
        lead += 1
    if lead:
        return " ".join(parts[lead:]).lower()

    # 'van der Berg' -> absorb the nobiliary/compound particles before the final token
    i = len(parts) - 1
    while i > 0 and parts[i - 1].lower().strip(".") in NAME_PARTICLES:
        i -= 1
    return " ".join(parts[i:]).lower()


def authors_match(claimed: str, actual_first_author: str) -> bool:
    return bool(claimed) and surname_of(claimed) == surname_of(actual_first_author)


def years_match(claimed, actual) -> bool:
    """Allow a 1-year gap: online-first vs print issue is a real, benign case."""
    try:
        return abs(int(str(claimed).strip()) - int(str(actual).strip())) <= 1
    except (TypeError, ValueError):
        return False


# Institution boundaries inside one affiliation string: semicolons, " and ",
# and PubMed's numbered-superscript separators.
_SEGMENTS = re.compile(r";|/|\band\b|(?<=\D)\d\s*[.)]\s")


def _hit(hints, low: str) -> bool:
    """Word-bounded substring test. Bare `in` would match 'usa' inside 'Busan'."""
    return any(re.search(r"\b" + re.escape(h) + r"\b", low) for h in hints)


def infer_provenance(affiliations) -> dict:
    """Resolve affiliation strings to countries.

    Returns {"countries": [...], "unrecognized": [...]} where `unrecognized`
    holds the affiliation strings that matched no country in the table — a
    state that must not be confused with "no affiliation data at all", because
    an unlisted country (source-provenance.md judges those case by case) still
    has to be looked at by a human.

    Within one affiliation string a country name beats a city, so
    "Moscow, ID 83844, USA" resolves to usa, not russia.
    """
    found, unrecognized = [], []
    for aff in affiliations or []:
        low = (aff or "").lower()
        if not low.strip():
            continue
        hits = []
        # Resolve name-beats-city WITHIN each institution, not across the whole
        # string. One affiliation line often lists two institutions in different
        # countries ("Beijing ... ; and Harvard ... USA"); applying the rule to the
        # whole line let a single recognized country NAME discard every city hit,
        # silently suppressing the other country. For an excluded country that is
        # the worst possible failure: a clean PASS on a paper needing quarantine.
        for seg in _SEGMENTS.split(low):
            if not seg.strip():
                continue
            named = [c for c, names, _ in _COUNTRY_HINTS if _hit(names, seg)]
            seg_hits = named or [c for c, _, cities in _COUNTRY_HINTS if _hit(cities, seg)]
            hits.extend(seg_hits)
        if not hits:
            unrecognized.append(aff)
        for c in hits:
            if c not in found:
                found.append(c)
    return {"countries": found, "unrecognized": unrecognized}


def infer_countries(affiliations) -> list[str]:
    """Country keys only — see infer_provenance() for the unrecognized bucket."""
    return infer_provenance(affiliations)["countries"]


def excluded_countries_in(countries) -> list[str]:
    return [c for c in (countries or []) if c in EXCLUDED_COUNTRIES]


def detect_retraction(record: dict) -> list[str]:
    """Look for retraction/EoC signals in publication types (authoritative) and title (anchored).

    Publication types are matched exactly against the set PubMed actually assigns.
    Titles are matched only when the marker is the *leading* token and is followed by
    notice punctuation, because an unanchored substring search reports ordinary
    papers as retracted -- and the caller treats any signal as "do not use as support".
    """
    signals: list[str] = []

    for t in (record.get("publication_types") or []):
        low = str(t).strip().lower()
        if low in RETRACTION_PUBTYPES and low not in signals:
            signals.append(low)

    m = _TITLE_RETRACTION_RE.match(str(record.get("title") or ""))
    if m:
        marker = m.group(1).lower()
        if marker not in signals:
            signals.append(marker)

    return signals


# ======================================================================
# Registry adapters — normalize each API into one record shape
# ======================================================================
def _record(**kw):
    base = dict(source=None, doi=None, pmid=None, title=None, authors=[],
                first_author=None, journal=None, year=None, publication_types=[],
                affiliations=[], url=None)
    base.update(kw)
    return base


def fetch_crossref(doi: str, mailto=None, fetch=http_get_json):
    data = fetch(CROSSREF + urllib.parse.quote(doi), mailto=mailto)
    if not data:
        return None
    m = data.get("message", {})
    authors = []
    affs = []
    for a in m.get("author", []) or []:
        name = " ".join(x for x in [a.get("family"), a.get("given")] if x)
        if name:
            authors.append(name)
        for aff in a.get("affiliation", []) or []:
            if aff.get("name"):
                affs.append(aff["name"])
    date = (m.get("issued", {}).get("date-parts") or [[None]])[0]
    title = (m.get("title") or [None])[0]
    return _record(source="crossref", doi=m.get("DOI"), title=title, authors=authors,
                   first_author=authors[0] if authors else None,
                   journal=(m.get("container-title") or [None])[0],
                   year=date[0] if date else None,
                   publication_types=[m.get("type")] if m.get("type") else [],
                   affiliations=affs, url=m.get("URL"))


def fetch_pubmed(pmid: str, mailto=None, fetch=http_get_json):
    data = fetch(EUTILS, {"db": "pubmed", "id": str(pmid), "retmode": "json"})
    if not data:
        return None
    result = (data.get("result") or {}).get(str(pmid))
    if not result or "error" in result:
        return None
    authors = [a.get("name") for a in result.get("authors", []) if a.get("name")]
    doi = None
    for aid in result.get("articleids", []) or []:
        if aid.get("idtype") == "doi":
            doi = aid.get("value")
    year = None
    pubdate = result.get("pubdate") or ""
    m = re.match(r"(\d{4})", pubdate)
    if m:
        year = int(m.group(1))
    return _record(source="pubmed", pmid=str(pmid), doi=doi, title=result.get("title"),
                   authors=authors, first_author=authors[0] if authors else None,
                   journal=result.get("fulljournalname") or result.get("source"),
                   year=year, publication_types=result.get("pubtype", []) or [],
                   affiliations=[],
                   url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")


def fetch_europepmc(query: str, mailto=None, fetch=http_get_json):
    """Europe PMC fallback; also the best free source of affiliation strings."""
    data = fetch(EUROPEPMC, {"query": query, "format": "json", "pageSize": "1",
                             "resultType": "core"})
    if not data:
        return None
    results = (data.get("resultList") or {}).get("result") or []
    if not results:
        return None
    r = results[0]
    affs = []
    if r.get("affiliation"):
        affs.append(r["affiliation"])
    for a in ((r.get("authorList") or {}).get("author") or []):
        for aff in (a.get("authorAffiliationDetailsList") or {}).get(
                "authorAffiliation", []) or []:
            if aff.get("affiliation"):
                affs.append(aff["affiliation"])
    authors = []
    for a in ((r.get("authorList") or {}).get("author") or []):
        if a.get("fullName"):
            authors.append(a["fullName"])
    return _record(source="europepmc", doi=r.get("doi"), pmid=r.get("pmid"),
                   title=r.get("title"), authors=authors,
                   first_author=authors[0] if authors else (r.get("authorString") or "").split(",")[0],
                   journal=(r.get("journalInfo") or {}).get("journal", {}).get("title"),
                   year=int(r["pubYear"]) if str(r.get("pubYear", "")).isdigit() else None,
                   publication_types=r.get("pubTypeList", {}).get("pubType", []) or [],
                   affiliations=affs)


# ======================================================================
# Verification orchestration
# ======================================================================
def verify(doi=None, pmid=None, claim_title=None, claim_author=None, claim_year=None,
           mailto=None, fetch=http_get_json):
    """Run checks 1 and 2. Returns a result dict; never raises for a 'not found'."""
    out = {
        "query": {"doi": doi, "pmid": pmid},
        "exists": False, "record": None, "checks": {}, "flags": [],
        "passed": False, "errors": [],
    }

    record = None
    try:
        if doi:
            record = fetch_crossref(doi, mailto=mailto, fetch=fetch)
            if record is None:
                record = fetch_europepmc(f"DOI:{doi}", mailto=mailto, fetch=fetch)
        elif pmid:
            record = fetch_pubmed(pmid, mailto=mailto, fetch=fetch)
            if record is None:
                record = fetch_europepmc(f"EXT_ID:{pmid}", mailto=mailto, fetch=fetch)
    except VerificationError as e:
        out["errors"].append(str(e))
        return out

    if record is None:
        out["checks"]["existence"] = False
        out["flags"].append(
            "IDENTIFIER DOES NOT RESOLVE — treat as fabricated/incorrect and REMOVE the citation")
        return out

    # Enrich affiliations from Europe PMC when the primary source lacks them.
    if not record["affiliations"] and (record.get("doi") or record.get("pmid")):
        try:
            q = f"DOI:{record['doi']}" if record.get("doi") else f"EXT_ID:{record['pmid']}"
            extra = fetch_europepmc(q, mailto=mailto, fetch=fetch)
            if extra and extra["affiliations"]:
                record["affiliations"] = extra["affiliations"]
                if not record.get("publication_types"):
                    record["publication_types"] = extra["publication_types"]
        except VerificationError:
            pass  # enrichment is best-effort

    out["exists"] = True
    out["checks"]["existence"] = True
    out["record"] = record

    # --- Check 2: metadata accuracy vs. claimed values
    if claim_title:
        ok = titles_match(claim_title, record["title"] or "")
        out["checks"]["title_match"] = ok
        if not ok:
            out["flags"].append(
                f"TITLE MISMATCH — claimed {claim_title!r}, actual {record['title']!r}. "
                f"Disqualifying: cite the canonical record or remove")
    if claim_author:
        ok = authors_match(claim_author, record["first_author"] or "")
        out["checks"]["author_match"] = ok
        if not ok:
            out["flags"].append(
                f"AUTHOR MISMATCH — claimed first author {claim_author!r}, "
                f"actual {record['first_author']!r}. Disqualifying")
    if claim_year:
        ok = years_match(claim_year, record["year"])
        out["checks"]["year_match"] = ok
        if not ok:
            out["flags"].append(
                f"YEAR MISMATCH — claimed {claim_year}, actual {record['year']}")

    # --- Provenance
    prov = infer_provenance(record["affiliations"])
    countries, unrecognized = prov["countries"], prov["unrecognized"]
    record["inferred_countries"] = countries
    record["unrecognized_affiliations"] = unrecognized
    excluded = excluded_countries_in(countries)
    if excluded:
        out["flags"].append(
            f"EXCLUDED-COUNTRY PROVENANCE ({', '.join(excluded)}) — per the country policy this "
            f"source cannot support a conclusion; quarantine appendix only")
        out["checks"]["provenance_allowed"] = False
    elif countries and not unrecognized:
        out["checks"]["provenance_allowed"] = True
    elif countries and unrecognized:
        # Some affiliations resolved, some did not. Reporting only the resolved
        # ones would hide a possibly-decisive lead affiliation.
        out["checks"]["provenance_allowed"] = None
        out["flags"].append(
            f"PROVENANCE PARTIAL — resolved {', '.join(countries)}, but {len(unrecognized)} "
            f"affiliation(s) matched no country in the table (e.g. {unrecognized[0][:70]!r}). "
            f"Read the paper's corresponding-author affiliation before relying on this")
    elif unrecognized:
        out["checks"]["provenance_allowed"] = None
        out["flags"].append(
            f"PROVENANCE UNRECOGNIZED — affiliation data exists but names no country in the "
            f"table (e.g. {unrecognized[0][:70]!r}). Unlisted countries are judged on the merits "
            f"(source-provenance.md), not assumed excluded — resolve it yourself")
    else:
        out["checks"]["provenance_allowed"] = None
        out["flags"].append(
            "PROVENANCE UNKNOWN — no affiliation metadata available; confirm country "
            "from the paper itself before relying on this source")

    # --- Retraction
    signals = detect_retraction(record)
    if signals:
        out["checks"]["not_retracted"] = False
        out["flags"].append(
            f"RETRACTION INDICATOR ({', '.join(signals)}) — do not use as support; "
            f"verify on the publisher page")
    else:
        out["checks"]["not_retracted"] = True

    hard = [v for k, v in out["checks"].items() if v is False]
    out["passed"] = not hard
    out["reminder"] = ("Checks 1-2 only. Check 3 (does the source actually state your claim?) "
                       "requires reading the text — quote the supporting sentence.")
    return out


def format_human(res: dict) -> str:
    L = []
    q = res["query"]
    L.append(f"Citation check: {'DOI ' + q['doi'] if q['doi'] else 'PMID ' + str(q['pmid'])}")
    L.append("=" * 68)
    if res["errors"]:
        for e in res["errors"]:
            L.append(f"  ERROR: {e}")
        return "\n".join(L)
    if not res["exists"]:
        L.append("  [1] Existence......... FAIL — identifier does not resolve")
        for f in res["flags"]:
            L.append(f"  !! {f}")
        return "\n".join(L)

    r = res["record"]
    L.append("  [1] Existence......... PASS")
    L.append(f"      Title   : {r['title']}")
    L.append(f"      Authors : {', '.join(r['authors'][:4])}{' et al.' if len(r['authors']) > 4 else ''}")
    L.append(f"      Journal : {r['journal']}  ({r['year']})")
    L.append(f"      DOI/PMID: {r.get('doi') or '-'} / {r.get('pmid') or '-'}")
    L.append(f"      Source  : {r['source']}")
    for key, label in (("title_match", "Title match"), ("author_match", "Author match"),
                       ("year_match", "Year match")):
        if key in res["checks"]:
            L.append(f"  [2] {label:<16} {'PASS' if res['checks'][key] else 'FAIL'}")
    countries = r.get("inferred_countries") or []
    unknown_affs = r.get("unrecognized_affiliations") or []
    country_line = ", ".join(countries) if countries else "unresolved"
    if unknown_affs:
        country_line += f" (+{len(unknown_affs)} affiliation(s) not matched)"
    elif not countries:
        country_line = "unknown (no affiliation data)"
    L.append(f"      Country : {country_line}")
    L.append(f"  [-] Retraction check.. {'clean' if res['checks'].get('not_retracted') else 'FLAGGED'}")
    if res["flags"]:
        L.append("")
        for f in res["flags"]:
            L.append(f"  !! {f}")
    L.append("")
    L.append(f"  RESULT: {'PASS (checks 1-2)' if res['passed'] else 'FAIL — see flags'}")
    L.append(f"  NOTE: {res['reminder']}")
    return "\n".join(L)


# ======================================================================
# Offline self-test — proves the logic without network access
# ======================================================================
def self_test() -> int:
    failures, ran = [], []

    def check(name, cond):
        ran.append(name)
        if not cond:
            failures.append(name)

    # Title matching
    check("title exact", titles_match("Vitamin B12 deficiency", "Vitamin B12 deficiency"))
    check("title punctuation", titles_match("Vitamin B-12 deficiency!", "Vitamin B12 deficiency"))
    check("title subtitle", titles_match(
        "Metformin and B12: a cohort study", "Metformin and B12"))
    check("title different", not titles_match(
        "Metformin and vitamin B12 deficiency", "Aspirin for primary prevention of stroke"))

    # Author surname extraction
    check("surname 'Polack F'", surname_of("Polack F") == "polack")
    check("surname 'F. Polack'", surname_of("F. Polack") == "polack")
    check("surname 'Polack, Fernando'", surname_of("Polack, Fernando") == "polack")
    check("authors match", authors_match("Polack", "Polack FP"))
    check("authors mismatch", not authors_match("Smith", "Polack FP"))
    # Regression: multi-particle surnames must survive both citation styles.
    # 'van der Berg J' previously returned 'van' while 'van der Berg' returned
    # 'berg', so one person written two ways failed authors_match.
    check("surname 'van der Berg J'", surname_of("van der Berg J") == "van der berg")
    check("surname 'van der Berg'", surname_of("van der Berg") == "van der berg")
    check("particle surname matches across styles",
          authors_match("van der Berg", "van der Berg J"))
    check("compound surname kept whole", surname_of("Garcia Lopez M") == "garcia lopez")
    check("surname 'de la Cruz A'", surname_of("de la Cruz A") == "de la cruz")

    # Year tolerance
    check("year exact", years_match(2020, 2020))
    check("year online-first", years_match(2020, 2021))
    check("year wrong", not years_match(2015, 2020))
    check("year garbage", not years_match("n/a", 2020))

    # Country inference + exclusion
    check("infer china", "china" in infer_countries(["Dept of Cardiology, Peking Union, Beijing, China"]))
    check("infer usa", "usa" in infer_countries(["Harvard Medical School, Boston, MA, USA"]))
    check("infer germany", "germany" in infer_countries(["Charité, Berlin, Germany"]))
    check("excluded detects china", excluded_countries_in(["china", "usa"]) == ["china"])
    check("excluded detects russia", excluded_countries_in(["russia"]) == ["russia"])
    check("excluded clean", excluded_countries_in(["usa", "japan"]) == [])
    check("no affiliation -> empty", infer_countries([]) == [])
    # Regressions: a bare substring match on a city is wrong in both directions.
    check("Moscow, Idaho is not Russia",
          infer_countries(["University of Idaho, Moscow, ID 83844, USA"]) == ["usa"])
    check("Busan does not contain USA",
          infer_countries(["Pusan National University, Busan, Republic of Korea"])
          == ["south korea"])
    # Regression (2026-08-18): the name-beats-city rule was applied to the whole
    # affiliation string, so one recognized country NAME discarded every city hit.
    # A dual-institution line silently suppressed the excluded country and the
    # citation passed clean — the worst failure this control can have.
    check("two institutions, one excluded, both reported",
          sorted(infer_countries(
              ["Beijing Anzhen Hospital, Beijing 100029; and Harvard Medical "
               "School, Boston, MA, USA"])) == ["china", "usa"])
    check("slash-separated institutions both reported",
          sorted(infer_countries(
              ["Beijing Hospital, China / Harvard, Boston, USA"])) == ["china", "usa"])
    # Regression: a bare "wales" hint fired inside "New South Wales" (Australia)
    # and resolved it to uk with no caveat. Unrecognised is the honest answer.
    check("New South Wales is not the UK",
          infer_countries(["University of New South Wales, Kensington NSW 2052"]) == [])
    check("qualified Wales still resolves to uk",
          infer_countries(["Cardiff University, Wales, UK"]) == ["uk"])
    check("Cambridge UK vs Cambridge MA",
          infer_countries(["MRC Unit, Cambridge, UK"]) == ["uk"]
          and infer_countries(["MIT, Cambridge, MA, USA"]) == ["usa"])
    # An unlisted country is not "no data" — it must surface for human judgment.
    prov = infer_provenance(["Fundacion INFANT, Buenos Aires, Argentina"])
    check("unlisted country is unrecognized, not empty-silent",
          prov["countries"] == [] and len(prov["unrecognized"]) == 1)
    prov2 = infer_provenance(["Fundacion INFANT, Buenos Aires, Argentina",
                              "SUNY Upstate, Syracuse, NY, USA"])
    check("mixed known/unknown reports both",
          prov2["countries"] == ["usa"] and len(prov2["unrecognized"]) == 1)

    # Retraction detection
    check("retraction in title", detect_retraction(
        {"title": "RETRACTED: Ileal-lymphoid-nodular hyperplasia", "publication_types": []}))
    check("retraction in pubtype", detect_retraction(
        {"title": "A study", "publication_types": ["Retracted Publication"]}))
    check("eoc detected", detect_retraction(
        {"title": "Expression of Concern: A study", "publication_types": []}))
    check("clean paper", not detect_retraction(
        {"title": "A normal study", "publication_types": ["Journal Article"]}))
    # Regression: title markers must be ANCHORED. An unanchored substring search
    # flagged all three of these ordinary papers as retracted, and the caller turns
    # any signal into "do not use as support" — i.e. it discarded valid evidence.
    check("no false retraction: 'Retraction of consent...'", not detect_retraction(
        {"title": "Retraction of consent in emergency research: an ethical analysis",
         "publication_types": ["Journal Article"]}))
    check("no false retraction: 'Patients withdrawn from therapy'", not detect_retraction(
        {"title": "Patients withdrawn from therapy: a cohort study",
         "publication_types": ["Journal Article"]}))
    check("no false retraction: 'Expression of concern among caregivers'",
          not detect_retraction(
              {"title": "Expression of concern among caregivers: a qualitative study",
               "publication_types": ["Journal Article"]}))
    check("real notice 'Retraction of: X'", detect_retraction(
        {"title": "Retraction of: Original Title Here", "publication_types": []}))
    check("real notice 'WITHDRAWN: X'", detect_retraction(
        {"title": "WITHDRAWN: Duplicate submission", "publication_types": []}))
    check("pubtype 'Expression of Concern'", detect_retraction(
        {"title": "A study", "publication_types": ["Expression of Concern"]}))

    # End-to-end with a stubbed fetcher (no network)
    def stub_ok(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1056/TEST", "title": ["Metformin and vitamin B12 deficiency"],
            "container-title": ["Test Journal"], "issued": {"date-parts": [[2020]]},
            "type": "journal-article",
            "author": [{"family": "Polack", "given": "F",
                        "affiliation": [{"name": "Harvard Medical School, Boston, MA, USA"}]}],
        }}

    res = verify(doi="10.1056/TEST", claim_title="Metformin and vitamin B12 deficiency",
                 claim_author="Polack", claim_year=2020, fetch=stub_ok)
    check("e2e exists", res["exists"])
    check("e2e passed", res["passed"])
    check("e2e country usa", "usa" in res["record"]["inferred_countries"])

    res_bad = verify(doi="10.1056/TEST", claim_title="A completely different paper title",
                     claim_author="Nobody", fetch=stub_ok)
    check("e2e title mismatch fails", res_bad["passed"] is False)
    check("e2e flags mismatch", any("TITLE MISMATCH" in f for f in res_bad["flags"]))

    def stub_404(url, params=None, mailto=None):
        return None

    res_404 = verify(doi="10.9999/fabricated", fetch=stub_404)
    check("e2e nonexistent", res_404["exists"] is False)
    check("e2e nonexistent flagged", any("DOES NOT RESOLVE" in f for f in res_404["flags"]))

    def stub_excluded(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1000/x", "title": ["A study"], "container-title": ["J"],
            "issued": {"date-parts": [[2021]]}, "type": "journal-article",
            "author": [{"family": "Wang", "given": "L",
                        "affiliation": [{"name": "Peking University, Beijing, China"}]}]}}

    res_x = verify(doi="10.1000/x", fetch=stub_excluded)
    check("e2e excluded flagged", any("EXCLUDED-COUNTRY" in f for f in res_x["flags"]))
    check("e2e excluded fails", res_x["passed"] is False)

    def stub_partial(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1000/p", "title": ["A trial"], "container-title": ["J"],
            "issued": {"date-parts": [[2021]]}, "type": "journal-article",
            "author": [{"family": "Ruiz", "given": "M",
                        "affiliation": [{"name": "Hospital Italiano, Buenos Aires, Argentina"},
                                        {"name": "NIH, Bethesda, MD, USA"}]}]}}

    res_p = verify(doi="10.1000/p", fetch=stub_partial)
    check("e2e partial provenance flagged",
          any("PROVENANCE PARTIAL" in f for f in res_p["flags"]))
    check("e2e partial provenance not asserted allowed",
          res_p["checks"]["provenance_allowed"] is None)

    def stub_net_down(url, params=None, mailto=None):
        raise VerificationError("network unavailable (blocked) — cannot verify")

    res_net = verify(doi="10.1000/x", fetch=stub_net_down)
    check("e2e network error reported", bool(res_net["errors"]))
    check("e2e network error not a pass", res_net["passed"] is False)

    total = len(ran)
    print(f"self-test: {total - len(failures)}/{total} checks passed")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        return 1
    print("all offline logic checks passed")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Verify a citation's existence, metadata, provenance, and retraction status.",
        epilog="Check 3 (does the source state your claim?) requires reading the text.")
    ap.add_argument("--doi")
    ap.add_argument("--pmid")
    ap.add_argument("--claim-title", help="title as cited, to compare against canonical")
    ap.add_argument("--claim-author", help="first author as cited")
    ap.add_argument("--claim-year", help="year as cited")
    ap.add_argument("--mailto", help="your e-mail; Crossref prioritizes identified callers")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--self-test", action="store_true", help="run offline logic tests and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.doi and not args.pmid:
        ap.error("provide --doi or --pmid (or --self-test)")

    res = verify(doi=args.doi, pmid=args.pmid, claim_title=args.claim_title,
                 claim_author=args.claim_author, claim_year=args.claim_year,
                 mailto=args.mailto)
    print(json.dumps(res, indent=2) if args.json else format_human(res))
    if res["errors"]:
        return 2
    return 0 if res["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
