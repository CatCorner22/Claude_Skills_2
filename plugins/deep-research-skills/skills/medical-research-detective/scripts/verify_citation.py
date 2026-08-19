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
import unicodedata
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
# hint, used only where no country name appears — because cities are not unique
# across countries and a bare substring match on them is wrong in both
# directions: "Moscow, ID 83844, USA" (University of Idaho) is not Russian, and
# "Busan" contains the letters "usa". Matching is therefore word-bounded; a
# country name beats a city *within the same institution segment* (see
# infer_provenance, which splits on institution boundaries so a second country
# is not silently swallowed); and a city sitting in a US postal address is
# recognized as American wherever the country name falls (see _is_us_locality).
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
    ("taiwan", ["taiwan", "republic of china", "r.o.c"], ["taipei"]),
]

# "Taiwan, Republic of China" is the standard Taiwanese affiliation, and the bare
# substring "china" inside it flagged Academia Sinica papers as excluded-country --
# a false positive that quietly removes legitimate research from a review. Taiwan is
# resolved first and, when it is present, a china hit that rests ONLY on the
# "republic of china" wording is dropped. A mainland signal in the same string
# (an explicit "china" elsewhere, or a mainland city) still stands on its own.
_TAIWAN_ROC_RE = re.compile(r"\b(?:taiwan|r\.?o\.?c\.?)\b", re.I)

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

# Crossref carries the Retraction Watch database (acquired 2023, refreshed on
# working days) as `updated-by` entries on the work record itself, so a DOI
# lookup already downloads the authoritative answer — it just has to be read.
# This matters because Crossref keeps the *original* title on a retracted paper:
# there is no "RETRACTED:" prefix to catch, and Crossref's `type` stays
# "journal-article", so without this the script reported a retracted paper as
# clean. Only the retraction family blocks; corrections and errata are reported
# separately in verify(), since a correction does not invalidate a paper.
RETRACTION_UPDATE_TYPES = {
    "retraction", "partial_retraction", "withdrawal", "removal",
    "expression_of_concern",
}
CORRECTION_UPDATE_TYPES = {
    "correction", "corrigendum", "erratum", "addendum", "clarification",
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
# Letters that NFKD does not decompose into base + combining mark.
_FOLD_MAP = str.maketrans({"ß": "ss", "ø": "o", "æ": "ae", "œ": "oe",
                           "ł": "l", "đ": "d", "ð": "d", "þ": "th"})


def fold_accents(s: str) -> str:
    """'Müller' -> 'Muller', 'étude' -> 'etude'.

    Claimed citations are routinely typed without diacritics while the canonical
    record keeps them. Without folding, the non-ASCII letters were simply deleted
    ('étude' -> 'tude'), so a correctly-cited German or French paper could fail a
    check whose failure is *disqualifying*.
    """
    if not s:
        return ""
    s = s.lower().translate(_FOLD_MAP)
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))


def normalize_title(s: str) -> str:
    """Lowercase, fold accents, strip punctuation, collapse whitespace."""
    if not s:
        return ""
    s = re.sub(r"[^a-z0-9\s]", " ", fold_accents(s))
    s = re.sub(r"\s+", " ", s).strip()
    return s


def compact_title(s: str) -> str:
    """All non-alphanumerics removed. Makes 'B 12'=='B12', which survives even
    the word-boundary rules below."""
    return re.sub(r"[^a-z0-9]", "", fold_accents(s))


def dehyphenate_title(s: str) -> str:
    """Punctuation deleted rather than spaced out, so 'B-12' -> 'b12' while the
    word boundaries survive: 'vitamin b12 deficiency'."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", "", fold_accents(s))).strip()


def _prefix_or_equal(a: str, b: str) -> bool:
    """Prefix comparison that stops at a word boundary.

    A bare startswith() made 'Vitamin B1' match 'Vitamin B12 deficiency' — B1 and
    B12 are different vitamins with different syndromes, and a title mismatch is
    *disqualifying*, so a false PASS here lets a wrong citation through the one
    gate meant to catch it.
    """
    return bool(a) and bool(b) and (a == b or a.startswith(b + " ") or b.startswith(a + " "))


def titles_match(a: str, b: str, threshold: float = 0.85) -> bool:
    """Token-overlap comparison, tolerant of subtitles, punctuation, accents, and
    the hyphenation differences common in medical titles."""
    na, nb = normalize_title(a), normalize_title(b)
    if not na or not nb:
        return False
    if _prefix_or_equal(na, nb):
        return True
    # Hyphenation-insensitive comparison (B-12 vs B12, COVID-19 vs COVID19).
    if _prefix_or_equal(dehyphenate_title(a), dehyphenate_title(b)):
        return True
    ca, cb = compact_title(a), compact_title(b)
    if ca and cb and ca == cb:
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
    renderings of one name. The key is accent-folded, so 'Müller' and 'Muller' —
    the same author in two registries — compare equal.
    """
    if not author:
        return ""
    a = author.strip()
    if "," in a:
        return fold_accents(a.split(",")[0].strip())
    parts = [p for p in re.split(r"\s+", a) if p]
    if not parts:
        return ""

    # 'Smith J' / 'van der Berg JA' -> trailing initials; surname is everything before them
    if len(parts) > 1 and _is_initials(parts[-1]):
        return fold_accents(" ".join(parts[:-1]))

    # 'J. Smith' / 'J A Smith' -> leading initials; surname is everything after them
    lead = 0
    while lead < len(parts) - 1 and _is_initials(parts[lead]):
        lead += 1
    if lead:
        return fold_accents(" ".join(parts[lead:]))

    # 'van der Berg' -> absorb the nobiliary/compound particles before the final token
    i = len(parts) - 1
    while i > 0 and parts[i - 1].lower().strip(".") in NAME_PARTICLES:
        i -= 1
    return fold_accents(" ".join(parts[i:]))


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

# Words that mark a segment as naming an *institution* rather than a department,
# a role, or the tail of a name split across an " and ". Used to decide whether an
# unresolved segment is a real second institution worth reporting. "department",
# "division", "unit" are deliberately absent: they head sub-units of the
# institution named later in the same string.
_INSTITUTION_WORDS = (
    "university", "universite", "universidad", "universita", "universitat",
    "hospital", "hopital", "hospitalier", "institute", "institut", "college",
    "school", "center", "centre", "clinic", "klinik", "academy", "academia",
    "laboratory", "laboratoire", "foundation", "polytechnic", "faculty",
)


def _hit(hints, low: str) -> bool:
    """Word-bounded substring test on an accent-folded string.

    Bare `in` would match 'usa' inside 'Busan'. Folding both sides is what lets
    "Universitätsspital Zürich" and "Ōsaka" resolve at all — unfolded, the accented
    rendering an author actually uses matched nothing and the paper came back
    PROVENANCE UNRECOGNIZED.
    """
    return any(re.search(r"\b" + re.escape(fold_accents(h)) + r"\b", low) for h in hints)


_US_STATE_CODES = {
    "al", "ak", "az", "ar", "ca", "co", "ct", "de", "dc", "fl", "ga", "hi", "id",
    "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms", "mo",
    "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa",
    "pr", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy",
}

# The tail of a US postal address as it follows the city: an optional second
# locality, then the two-letter state code and an optional ZIP —
# "Moscow, ID 83844", "St. Petersburg and Tampa, FL". Deliberately short: it
# will not step over an institution name, so "Beijing and Harvard Medical
# School, Boston, MA" leaves Beijing alone.
# The state code must follow the city IMMEDIATELY — only punctuation and whitespace
# between them. An earlier version allowed an intervening one- or two-word locality,
# which made "Zhongshan Hospital, Shanghai, and Cleveland Clinic, OH, USA" read
# Shanghai as an American town and report the paper as clean US provenance. That is
# the failure this module's header calls the worst possible one, so the guard is
# deliberately narrow: it suppresses only the adjacent "Moscow, ID 83844" shape.
_US_TAIL_RE = re.compile(r"[\s,]*([a-z]{2})\b[\s,]*(\d{5})?")
# What may follow the state code (and optional ZIP) for the tail to read as a US address.
# Anchored, because "does 'usa' appear anywhere in this line?" is not a test of adjacency:
# in "Institute of X, Beijing, Co-affiliated with Yale, New Haven, CT 06510, USA" the token
# after "Beijing" is "Co" (Colorado) and "USA" is 50 characters away at the end of the line.
_US_COUNTRY_TAIL_RE = re.compile(r"[\s,.]*(?:usa|u\.?s\.?a|united states)\b")


def _is_us_locality(low: str, city: str) -> bool:
    """True when `city` reads as an American town rather than its foreign namesake.

    A US state code immediately after the city settles it, and covers the whole
    family: Moscow ID, St. Petersburg FL, Vienna VA, Berlin NH.

    **This guard fails safe, and the adjacency is what makes that true.** It suppresses a
    city hit only when the city is immediately followed by a state code AND that code is
    immediately followed by a ZIP or by the country name — never on the strength of "USA"
    appearing somewhere else in the string, and never when the string independently names
    an excluded country. The cost is accepted in the right direction: an unusual tail the
    pattern does not recognise leaves the excluded country reported for a human to wave
    off, because a false flag costs a reviewer seconds while a false clear silently defeats
    the provenance policy the caller is relying on.
    """
    # Backstop: an explicit excluded-country NAME anywhere outranks any locality guess.
    for _country, names, _cities in _COUNTRY_HINTS:
        if _country in EXCLUDED_COUNTRIES and _hit(names, low):
            return False
    for m in re.finditer(r"\b" + re.escape(city) + r"\b", low):
        tail = _US_TAIL_RE.match(low, m.end())
        if not tail or tail.group(1) not in _US_STATE_CODES:
            continue
        # A ZIP immediately after the state code settles it. Otherwise the country marker
        # must sit immediately after the state code — NOT merely somewhere in the string.
        #
        # The earlier `or _hit(["usa"], low)` form was a hole wide enough to drive the whole
        # provenance policy through: any two-letter English word that happens to be a state
        # code, followed anywhere later by "USA", suppressed the city. Verified leaks —
        #   "Institute of X, Beijing, Co-affiliated with Yale, New Haven, CT 06510, USA"
        #     -> "Co" reads as Colorado, "USA" sits at the end of the line -> ['usa'] only
        #   "Tianjin Medical University, Tianjin, In collaboration with NIH, Bethesda, MD ..."
        #     -> "In" reads as Indiana                                     -> ['usa'] only
        # Both suppressed the excluded-country city BEFORE the carry-through in
        # infer_provenance could see it, so the paper verified clean. Adjacency closes it:
        # "Co-affiliated" is followed by neither a ZIP nor a country name.
        if tail.group(2):
            return True
        if _US_COUNTRY_TAIL_RE.match(low, tail.end()):
            return True
    return False


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
    found, unrecognized, unresolved_segments = [], [], []
    for aff in affiliations or []:
        low = fold_accents(aff or "")
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
            city_hits = [
                c for c, _, cities in _COUNTRY_HINTS
                if any(_hit([city], seg) and not _is_us_locality(low, city)
                       for city in cities)]
            seg_hits = named or city_hits
            # A country NAME normally outranks a city guess within one institution.
            # The exception is an excluded country: segmentation cannot split a
            # comma-only string like "Beijing Anzhen Hospital, Beijing, Cleveland
            # Clinic, OH, USA", so "usa" would otherwise discard the Beijing hit and
            # the paper would verify clean — the failure this module exists to
            # prevent. An excluded-country city hint is therefore always carried
            # through for a human to confirm, never silently outranked.
            for c in city_hits:
                if c in EXCLUDED_COUNTRIES and c not in seg_hits:
                    seg_hits = seg_hits + [c]
            # Taiwan/ROC disambiguation, applied after the excluded-country backstop so
            # it can only remove a hit that rests solely on the "Republic of China" form.
            if "china" in seg_hits and _TAIWAN_ROC_RE.search(seg):
                mainland = _hit(["chinese", "p.r.c", "prc"], seg) or any(
                    _hit([city], seg)
                    for _c, _n, cities in _COUNTRY_HINTS if _c == "china"
                    for city in cities)
                bare_china = re.search(r"(?<!republic of )\bchina\b", seg)
                if not mainland and not bare_china:
                    seg_hits = [c for c in seg_hits if c != "china"]
            hits.extend(seg_hits)
            # An affiliation string routinely lists several institutions. Until
            # this check existed, `unrecognized` was decided for the WHOLE string:
            # if any one segment resolved, the string counted as resolved and every
            # unresolvable institution inside it vanished. That produced a clean
            # `provenance_allowed: True` on
            #   "Xiangya Hospital, Central South University, Changsha, Hunan;
            #    and Massachusetts General Hospital, Boston, MA, USA"
            # — the excluded-country lead affiliation silently dropped because the
            # US co-author's segment resolved. That is the exact failure the
            # segmentation above was introduced to prevent, arriving one level up.
            #
            # A segment counts as an unresolved institution only when it names an
            # institution AND carries a comma (so it has locality structure of its
            # own). "Massachusetts General Hospital" split off an " and " has no
            # comma and is treated as a continuation, not a second site.
            if not seg_hits and "," in seg and any(w in seg for w in _INSTITUTION_WORDS):
                frag = seg.strip(" ,.;")
                if frag and frag not in unresolved_segments:
                    unresolved_segments.append(frag)
        if not hits:
            unrecognized.append(aff)
        for c in hits:
            if c not in found:
                found.append(c)
    # Unresolved institutions inside an otherwise-resolved string are reported
    # through the same channel as a wholly unresolved affiliation: the caller's
    # PROVENANCE PARTIAL branch, which asks a human to read the paper's
    # affiliations rather than issuing a pass.
    for frag in unresolved_segments:
        if frag not in unrecognized:
            unrecognized.append(frag)
    return {"countries": found, "unrecognized": unrecognized}


def infer_countries(affiliations) -> list[str]:
    """Country keys only — see infer_provenance() for the unrecognized bucket."""
    return infer_provenance(affiliations)["countries"]


def excluded_countries_in(countries) -> list[str]:
    return [c for c in (countries or []) if c in EXCLUDED_COUNTRIES]


def normalize_update(update: dict) -> dict:
    """One Crossref `updated-by` entry, reduced to what the checks need.

    Shape per Crossref: {"updated": {...}, "DOI": ..., "type": "retraction",
    "label": "Retraction", "source": "retraction-watch"|"publisher"}. `type` is
    read first and `label` used as a fallback, so a vocabulary change surfaces
    rather than disappearing.
    """
    kind = str(update.get("type") or update.get("label") or "").strip().lower()
    kind = re.sub(r"[\s\-]+", "_", kind)
    return {"type": kind, "doi": update.get("DOI"),
            "source": update.get("source") or "crossref"}


def update_kinds(record: dict, vocabulary) -> list[str]:
    """The update types on a record that fall in `vocabulary` (see the two sets above)."""
    out = []
    for u in (record.get("updates") or []):
        kind = str((u or {}).get("type") or "")
        if kind in vocabulary and kind not in out:
            out.append(kind)
    return out


def detect_retraction(record: dict) -> list[str]:
    """Look for retraction/EoC signals in Crossref's update records (authoritative),
    publication types (authoritative), and the title (anchored).

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

    for kind in update_kinds(record, RETRACTION_UPDATE_TYPES):
        signal = f"crossref/retraction-watch: {kind}"
        if signal not in signals:
            signals.append(signal)

    return signals


# ======================================================================
# Registry adapters — normalize each API into one record shape
# ======================================================================
def _record(**kw):
    base = dict(source=None, doi=None, pmid=None, title=None, authors=[],
                first_author=None, journal=None, year=None, publication_types=[],
                affiliations=[], updates=[], url=None)
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
    updates = [normalize_update(u) for u in (m.get("updated-by") or [])
               if isinstance(u, dict)]
    return _record(source="crossref", doi=m.get("DOI"), title=title, authors=authors,
                   updates=updates,
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


def fetch_europepmc(query: str, mailto=None, fetch=http_get_json,
                    expect_doi=None, expect_pmid=None):
    """Europe PMC fallback; also the best free source of affiliation strings.

    `expect_doi` / `expect_pmid` are REQUIRED whenever the query names an
    identifier. This endpoint is a **search**, not a lookup: it returns the
    best-scoring hit for the query string, and DOIs carry characters the query
    language treats as syntax (slashes, parentheses, colons, hyphens), so a
    `DOI:...` query can return a *different* paper rather than nothing at all.
    Accepting that hit unchecked makes a fabricated identifier come back as
    `exists: True` with a real paper's title and authors attached — inverting the
    single verdict this tool exists to deliver. When the returned record does not
    carry the identifier that was asked for, that is a miss, not a match.
    """
    data = fetch(EUROPEPMC, {"query": query, "format": "json", "pageSize": "1",
                             "resultType": "core"})
    if not data:
        return None
    results = (data.get("resultList") or {}).get("result") or []
    if not results:
        return None
    r = results[0]
    if expect_doi and str(r.get("doi") or "").strip().lower() != str(expect_doi).strip().lower():
        return None
    if expect_pmid and str(r.get("pmid") or "").strip() != str(expect_pmid).strip():
        return None
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
    crossref_answered = False
    try:
        if doi:
            record = fetch_crossref(doi, mailto=mailto, fetch=fetch)
            crossref_answered = record is not None
            if record is None:
                record = fetch_europepmc(f"DOI:{doi}", mailto=mailto, fetch=fetch,
                                         expect_doi=doi)
        elif pmid:
            record = fetch_pubmed(pmid, mailto=mailto, fetch=fetch)
            if record is None:
                record = fetch_europepmc(f"EXT_ID:{pmid}", mailto=mailto, fetch=fetch,
                                         expect_pmid=pmid)
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
            if record.get("doi"):
                q, exp = f"DOI:{record['doi']}", {"expect_doi": record["doi"]}
            else:
                q, exp = f"EXT_ID:{record['pmid']}", {"expect_pmid": record["pmid"]}
            extra = fetch_europepmc(q, mailto=mailto, fetch=fetch, **exp)
            if extra and extra["affiliations"]:
                record["affiliations"] = extra["affiliations"]
                if not record.get("publication_types"):
                    record["publication_types"] = extra["publication_types"]
        except VerificationError:
            pass  # enrichment is best-effort

    # A PMID lookup sees PubMed's publication types, which lag a retraction notice
    # by weeks. Crossref's Retraction Watch annotations do not, so pick them up
    # whenever the record carries a DOI and the lookup did not come from Crossref.
    #
    # `authoritative_retraction_source` records whether the Retraction Watch feed
    # actually answered. Without it, "no signal found" and "nothing was consulted"
    # both printed as `not_retracted: True` — a clean bill of health issued by a
    # check that never ran. That happens on two ordinary paths: a DOI Crossref
    # 404s (so the lookup falls through to Europe PMC and the Crossref top-up
    # below 404s again on the same DOI), and a PMID with no DOI at all, where the
    # only evidence is the PubMed publication types this comment already says lag
    # by weeks.
    authoritative_retraction_source = record["source"] == "crossref"
    if record["source"] != "crossref" and record.get("doi") and not record.get("updates"):
        # Saved round-trip only: Crossref already declined this exact DOI, so the
        # retry would 404 again. Skipping it changes latency, not the verdict —
        # `authoritative_retraction_source` stays False either way.
        if not (doi and not crossref_answered
                and str(record["doi"]).strip().lower() == str(doi).strip().lower()):
            try:
                cr = fetch_crossref(record["doi"], mailto=mailto, fetch=fetch)
                if cr is not None:
                    authoritative_retraction_source = True
                    if cr.get("updates"):
                        record["updates"] = cr["updates"]
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
            f"table (e.g. {unrecognized[0][:70]!r}). This is not a verdict either way: it may "
            f"be an unlisted country, or a listed one named only by a city or in a script the "
            f"table does not carry. Resolve it from the paper, then apply source-provenance.md")
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
    elif authoritative_retraction_source:
        out["checks"]["not_retracted"] = True
    else:
        # No signal, but the Retraction Watch feed never answered for this record.
        # Reported as unknown (like the provenance states above), not as a pass:
        # silence from a source that was never asked is not evidence of anything.
        out["checks"]["not_retracted"] = None
        out["flags"].append(
            "RETRACTION STATUS UNVERIFIED — Crossref/Retraction Watch did not answer for "
            "this record, so the only evidence is publication-type metadata, which lags a "
            "retraction notice by weeks. Check the publisher page and Retraction Watch "
            "before relying on this source")

    # A correction is not a retraction: the paper stands, but a number in it may
    # not (evidence-appraisal.md). Reported, never a check failure.
    corrections = update_kinds(record, CORRECTION_UPDATE_TYPES)
    if corrections:
        out["flags"].append(
            f"CORRECTION ON RECORD ({', '.join(corrections)}) — the paper stands, but read "
            f"the notice before quoting a number from it")

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
    _nr = res["checks"].get("not_retracted")
    _nr_word = {True: "clean", False: "FLAGGED"}.get(_nr, "UNVERIFIED (source did not answer)")
    L.append(f"  [-] Retraction check.. {_nr_word}")
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
    # Regression: the prefix comparison ignored word boundaries, so a claimed
    # "Vitamin B1" paper validated against a B12 paper — different vitamin,
    # different syndrome, and a title check is what is supposed to catch that.
    check("B1 does not match B12", not titles_match(
        "Vitamin B1", "Vitamin B12 deficiency"))
    check("mid-word prefix rejected", not titles_match(
        "Cardio", "Cardiology in practice: a review"))
    # Regression: accents were deleted rather than folded ('etude' -> 'tude'), so a
    # correctly-cited French or German paper failed a disqualifying check.
    check("accents fold, not vanish", titles_match(
        "Effets de la metformine — étude", "Effets de la metformine - etude"))
    check("umlaut title matches ascii rendering", titles_match(
        "Über die Wirkung von Metformin", "Uber die Wirkung von Metformin"))
    check("spaced B 12 still matches B12", titles_match(
        "Vitamin B 12 deficiency", "Vitamin B12 deficiency"))

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
    # Regression: accented surnames are the same person in two registries.
    check("surname accent-folded", surname_of("Müller-Lissner S") == "muller-lissner")
    check("accented author matches ascii rendering",
          authors_match("Muller-Lissner", "Müller-Lissner S"))

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
    # Regression: " and " is an institution boundary, so the country name could land
    # in a different segment from the city and Moscow, Idaho was reported as Russian
    # provenance — a hard FAIL on a University of Idaho paper. A US state code (with a
    # ZIP, or in an affiliation that also names the USA) settles it.
    check("Moscow, ID is Idaho",
          infer_countries(["University of Idaho, Moscow, ID, USA"]) == ["usa"])
    check("St. Petersburg, FL is Florida",
          infer_countries(
              ["All Children's Hospital, St. Petersburg, FL, USA"]) == ["usa"])
    # Deliberate, documented trade-off. When the namesake city is NOT adjacent to the
    # state code -- "Moscow and Boise, ID, USA" -- the guard no longer clears it, so the
    # tool reports usa AND russia and asks a human. That is a false flag, and it is the
    # price of never producing a false CLEAR: the adjacency rule was widened once to
    # swallow this case and the widening let "Shanghai, and Cleveland Clinic, OH, USA"
    # verify as clean US provenance. Costing a reviewer ten seconds beats silently
    # passing an excluded-country paper, which is the failure this module exists to stop.
    check("non-adjacent US namesake over-flags rather than clearing",
          sorted(infer_countries(
              ["University of Idaho, Moscow and Boise, ID, USA"])) == ["russia", "usa"])
    # Regression pins for the suppression bug (comma-only strings never segment).
    check("Shanghai + US clinic is not clean US provenance",
          "china" in infer_countries(
              ["Zhongshan Hospital, Shanghai, and Cleveland Clinic, OH, USA"]))
    check("Beijing + US clinic, comma-only, is not clean US provenance",
          "china" in infer_countries(
              ["Beijing Anzhen Hospital, Beijing, Cleveland Clinic, OH, USA"]))
    check("Moscow + US hospital is not clean US provenance",
          "russia" in infer_countries(
              ["Dept of Medicine, Moscow, and Mount Sinai, NY, USA"]))
    check("state code plus ZIP settles it without 'USA'",
          infer_provenance(["University of Idaho, Moscow, ID 83844"])["countries"] == [])
    # ...and the guard must not swallow a real excluded-country institution that
    # merely shares a string with a US address.
    check("US-locality guard leaves Beijing alone",
          sorted(infer_countries(
              ["Beijing Anzhen Hospital, Beijing and Harvard Medical School, "
               "Boston, MA, USA"])) == ["china", "usa"])
    check("Russian St. Petersburg still resolves",
          infer_countries(["St. Petersburg State University, 199034 St. Petersburg"])
          == ["russia"])
    # Taiwan/ROC: "Taiwan, Republic of China" is the standard Taiwanese affiliation and
    # must not be excluded as mainland China -- a false positive here silently removes
    # legitimate research from a review.
    check("Taiwan ROC is Taiwan, not China",
          infer_countries(["Academia Sinica, Taipei, Taiwan, Republic of China"]) == ["taiwan"])
    check("plain Taiwan is Taiwan",
          infer_countries(["National Taiwan University Hospital, Taipei, Taiwan"]) == ["taiwan"])
    check("mainland China still resolves",
          infer_countries(["Chinese Academy of Sciences, Beijing, China"]) == ["china"])
    check("New South Wales is not the UK",
          infer_countries(["University of New South Wales, Kensington NSW 2052"]) == [])
    check("qualified Wales still resolves to uk",
          infer_countries(["Cardiff University, Wales, UK"]) == ["uk"])
    # Regression: accented city and country names matched nothing, so a Swiss or
    # Japanese affiliation written the way its authors write it read as unrecognized.
    check("accented city resolves",
          infer_countries(["Universitätsspital Zürich, Zürich"]) == ["switzerland"])
    check("macron city resolves", infer_countries(["Ōsaka University, Ōsaka"]) == ["japan"])
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
    # Regression: Crossref carries the Retraction Watch annotations, and it keeps the
    # ORIGINAL title on a retracted paper — no "RETRACTED:" prefix, type still
    # "journal-article" — so a DOI check reported a retracted paper as clean until
    # `updated-by` was read.
    check("crossref updated-by retraction caught", detect_retraction(
        {"title": "An ordinary-looking title", "publication_types": ["journal-article"],
         "updates": [normalize_update({"DOI": "10.1/r", "type": "retraction",
                                       "label": "Retraction",
                                       "source": "retraction-watch"})]}))
    check("expression of concern via label fallback", detect_retraction(
        {"title": "A study", "publication_types": [],
         "updates": [normalize_update({"label": "Expression of concern"})]}))
    check("a correction is not a retraction", not detect_retraction(
        {"title": "A study", "publication_types": ["journal-article"],
         "updates": [normalize_update({"type": "correction", "label": "Correction"})]}))
    check("update kinds are sorted into their vocabularies",
          update_kinds({"updates": [normalize_update({"type": "erratum"})]},
                       CORRECTION_UPDATE_TYPES) == ["erratum"])

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

    def stub_retracted(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1000/r", "title": ["Ileal-lymphoid-nodular hyperplasia"],
            "container-title": ["J"], "issued": {"date-parts": [[1998]]},
            "type": "journal-article",
            "updated-by": [{"DOI": "10.1000/notice", "type": "retraction",
                            "label": "Retraction", "source": "retraction-watch"}],
            "author": [{"family": "Wakefield", "given": "A",
                        "affiliation": [{"name": "Royal Free Hospital, London, UK"}]}]}}

    res_r = verify(doi="10.1000/r", fetch=stub_retracted)
    check("e2e crossref retraction flagged",
          any("RETRACTION INDICATOR" in f for f in res_r["flags"]))
    check("e2e crossref retraction fails", res_r["passed"] is False)

    def stub_corrected(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1000/c", "title": ["A cohort study"], "container-title": ["J"],
            "issued": {"date-parts": [[2019]]}, "type": "journal-article",
            "updated-by": [{"DOI": "10.1000/erratum", "type": "correction",
                            "label": "Correction", "source": "publisher"}],
            "author": [{"family": "Smith", "given": "J",
                        "affiliation": [{"name": "NIH, Bethesda, MD, USA"}]}]}}

    res_c = verify(doi="10.1000/c", fetch=stub_corrected)
    check("e2e correction reported", any("CORRECTION ON RECORD" in f for f in res_c["flags"]))
    check("e2e correction is not a failure", res_c["passed"] is True)

    # A PMID lookup must also see the Crossref retraction annotation: PubMed's
    # "Retracted Publication" type lags the notice by weeks.
    def stub_pmid_retracted(url, params=None, mailto=None):
        if url.startswith(CROSSREF):
            return {"message": {"DOI": "10.1/x", "title": ["A study"],
                                "type": "journal-article",
                                "updated-by": [{"DOI": "10.1/n", "type": "retraction",
                                                "label": "Retraction"}]}}
        if url == EUTILS:
            return {"result": {"33301246": {
                "title": "A study", "pubdate": "2020 Dec",
                "fulljournalname": "J", "pubtype": ["Journal Article"],
                "authors": [{"name": "Smith J"}],
                "articleids": [{"idtype": "doi", "value": "10.1/x"}]}}}
        return None  # Europe PMC enrichment finds nothing

    res_pm = verify(pmid="33301246", fetch=stub_pmid_retracted)
    check("e2e pmid picks up crossref retraction",
          any("RETRACTION INDICATOR" in f for f in res_pm["flags"]))

    def stub_net_down(url, params=None, mailto=None):
        raise VerificationError("network unavailable (blocked) — cannot verify")

    res_net = verify(doi="10.1000/x", fetch=stub_net_down)
    check("e2e network error reported", bool(res_net["errors"]))
    check("e2e network error not a pass", res_net["passed"] is False)

    # --- Regression: an unresolvable institution inside an otherwise-resolved
    # affiliation string used to disappear, because `unrecognized` was decided for
    # the whole string. A Chinese lead affiliation co-authored with a US site
    # therefore verified CLEAN — the failure this module exists to prevent.
    prov_mixed = infer_provenance([
        "Xiangya Hospital, Central South University, Changsha, Hunan; "
        "and Massachusetts General Hospital, Boston, MA, USA"])
    check("mixed-site: unresolved institution is reported",
          len(prov_mixed["unrecognized"]) == 1)
    check("mixed-site: resolved country still found",
          prov_mixed["countries"] == ["usa"])
    prov_ru = infer_provenance([
        "Department of Neurology, Sechenov University, Ulyanovsk; "
        "and Mayo Clinic, Rochester, MN, USA"])
    check("mixed-site: unlisted Russian city segment reported",
          len(prov_ru["unrecognized"]) == 1)
    # ...without inventing a second site out of an institution name split on "and".
    check("no false unresolved from 'and' inside one institution name",
          infer_provenance(
              ["Massachusetts General Hospital and Harvard Medical School, "
               "Boston, MA, USA"])["unrecognized"] == [])
    check("no false unresolved from Brigham and Women's",
          infer_provenance(
              ["Brigham and Women's Hospital, Boston, MA, USA"])["unrecognized"] == [])
    check("no false unresolved from a plain department prefix",
          infer_provenance(
              ["Department of Medicine, Mayo Clinic, Rochester, MN, USA"]
          )["unrecognized"] == [])
    # --- Regression: `_is_us_locality` accepted any two-letter English word that happens to
    # be a state code, as long as "USA" appeared ANYWHERE later in the string. Real-shaped
    # affiliations leaked through and verified clean.
    for aff, must in (
        ("Institute of X, Beijing, Co-affiliated with Yale, New Haven, CT 06510, USA", "china"),
        ("Tianjin Medical University, Tianjin, In collaboration with NIH, "
         "Bethesda, MD 20892, USA", "china"),
        ("Wuhan Institute, Wuhan, Or partnered with OHSU, Portland, OR 97239, USA", "china"),
    ):
        check(f"non-adjacent 'usa' no longer suppresses {must} ({aff[:18]}...)",
              must in infer_provenance([aff])["countries"])
    # ...and the shapes the guard exists for are still suppressed.
    for aff in ("Moscow, ID 83844, USA", "University of Idaho, Moscow, ID, USA",
                "St. Petersburg, FL 33701, USA"):
        c = infer_provenance([aff])["countries"]
        check(f"US namesake still resolved: {aff[:24]}",
              "russia" not in c and "usa" in c)

    # The existing excluded-country pins must survive the change.
    check("excluded-country city still carried through a comma-only string",
          set(infer_provenance(
              ["Zhongshan Hospital, Shanghai, and Cleveland Clinic, OH, USA"]
          )["countries"]) == {"china", "usa"})

    def stub_mixed(url, params=None, mailto=None):
        return {"message": {
            "DOI": "10.1000/m", "title": ["A study"], "container-title": ["J"],
            "issued": {"date-parts": [[2022]]}, "type": "journal-article",
            "author": [{"family": "Li", "given": "X", "affiliation": [{"name":
                "Xiangya Hospital, Central South University, Changsha, Hunan; "
                "and Massachusetts General Hospital, Boston, MA, USA"}]}]}}

    res_m = verify(doi="10.1000/m", fetch=stub_mixed)
    check("e2e mixed-site is not a clean provenance pass",
          res_m["checks"]["provenance_allowed"] is None)
    check("e2e mixed-site flags PARTIAL",
          any("PROVENANCE PARTIAL" in f for f in res_m["flags"]))

    # --- Regression: Europe PMC's endpoint is a SEARCH. Returning its top hit
    # without checking the identifier made a fabricated DOI resolve to a real paper.
    def stub_epmc_wrong_paper(url, params=None, mailto=None):
        if url.startswith(CROSSREF):
            return None                      # Crossref 404s the fabricated DOI
        return {"resultList": {"result": [{
            "doi": "10.1016/j.real-different-paper", "pmid": "12345678",
            "title": "An entirely different real paper", "pubYear": "2019",
            "authorList": {"author": [{"fullName": "Real Author"}]},
            "journalInfo": {"journal": {"title": "J"}}}]}}

    res_w = verify(doi="10.9999/fabricated", fetch=stub_epmc_wrong_paper)
    check("europepmc: mismatched DOI is not accepted as the record",
          res_w["exists"] is False)
    check("europepmc: mismatched DOI still flagged as unresolved",
          any("DOES NOT RESOLVE" in f for f in res_w["flags"]))

    def stub_epmc_right_paper(url, params=None, mailto=None):
        if url.startswith(CROSSREF):
            return None
        return {"resultList": {"result": [{
            "doi": "10.9999/only-in-epmc", "pmid": "999",
            "title": "A paper Crossref does not carry", "pubYear": "2019",
            "authorList": {"author": [{"fullName": "Some Author"}]},
            "journalInfo": {"journal": {"title": "J"}},
            "affiliation": "Mayo Clinic, Rochester, MN, USA"}]}}

    res_e = verify(doi="10.9999/only-in-epmc", fetch=stub_epmc_right_paper)
    check("europepmc: matching DOI is accepted", res_e["exists"] is True)

    # --- Regression: "no retraction signal" and "nothing was consulted" both
    # printed as a clean retraction check. On the Europe PMC fallback path the
    # Retraction Watch feed never answered, so the verdict must be unknown.
    check("retraction status is UNVERIFIED when Crossref never answered",
          res_e["checks"]["not_retracted"] is None)
    check("unverified retraction is flagged",
          any("RETRACTION STATUS UNVERIFIED" in f for f in res_e["flags"]))
    check("unverified retraction does not fail the citation", res_e["passed"] is True)
    check("crossref path still reports a real clean check",
          res["checks"]["not_retracted"] is True)
    check("formatter renders the unverified state",
          "UNVERIFIED" in format_human(res_e))

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
