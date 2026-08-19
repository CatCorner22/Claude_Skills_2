#!/usr/bin/env python3
"""Search PubMed/MEDLINE via the free NCBI E-utilities API.

Runs the PubMed pass of stage 4 (references/search-strategy.md) and returns
structured hits so the search is reproducible and loggable rather than ad hoc.

Usage:
  # Single query
  search_pubmed.py "metformin AND vitamin B12 deficiency"

  # Co-occurrence search: the dot-connector. Every pair is searched. A term is
  # quoted as a phrase unless it already carries query syntax (an OR block,
  # truncation, a field tag), which is passed through as written.
  search_pubmed.py --pairs "peripheral neuropathy" "metformin OR glucophage" "anemia"

  # Filters and output
  search_pubmed.py "query" --max 50 --years 10 --humans --type "Review"
  search_pubmed.py "query" --json
  search_pubmed.py --self-test        # offline logic tests, no network

Notes:
  - Stdlib only; no API key required. NCBI asks callers to identify themselves
    and to keep request rates modest — pass --email, and do not run tight loops.
  - Results are a starting point: apply references/evidence-appraisal.md for
    quality and references/source-provenance.md for country of origin, and
    verify anything you cite with verify_citation.py.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
TOOL = "medical-research-detective"
USER_AGENT = "medical-research-detective/1.0 (literature search; stdlib urllib)"
TIMEOUT = 25

# Publication types worth surfacing prominently: they sit high in the evidence
# hierarchy (references/evidence-appraisal.md).
HIGH_VALUE_TYPES = {
    "meta-analysis": "META-ANALYSIS",
    "systematic review": "SYSTEMATIC REVIEW",
    "randomized controlled trial": "RCT",
    "review": "review",
    "case reports": "case report",
    "retracted publication": "!! RETRACTED",
}


class SearchError(Exception):
    pass


def http_get_json(url: str, params: dict, email: str | None = None):
    params = dict(params, tool=TOOL, retmode="json")
    if email:
        params["email"] = email
    full = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(full, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        raise SearchError(f"HTTP {e.code} from NCBI E-utilities")
    except urllib.error.URLError as e:
        raise SearchError(
            f"network unavailable ({e.reason}) — PubMed could not be searched. "
            f"Report the gap; do not present an unrun search as complete")
    except json.JSONDecodeError:
        raise SearchError("E-utilities returned invalid JSON")


# ======================================================================
# Pure logic — covered by --self-test
# ======================================================================
def build_query(term: str, years: int | None = None, humans: bool = False,
                pubtype: str | None = None, language: str | None = None) -> str:
    """Compose an E-utilities query string from a term plus filters."""
    q = term.strip()
    if not q:
        raise SearchError("empty query")
    if humans:
        q += ' AND humans[MeSH Terms]'
    if pubtype:
        q += f' AND "{pubtype}"[Publication Type]'
    if language:
        q += f' AND {language}[Language]'
    if years:
        q += f' AND ("last {years} years"[PDat])'
    return q


# Quotes, parentheses, field tags, truncation, or an uppercase boolean operator
# mean the caller has already written a query block.
_SEARCH_SYNTAX_RE = re.compile(r'["()\[\]*]|\b(?:AND|OR|NOT)\b')


def as_query_block(term: str) -> str:
    """Wrap one term as a query block for a pair search.

    A plain phrase is quoted, so PubMed searches it as a phrase. A term that already
    carries search syntax is passed through untouched, because quoting it changes
    what it means: '("proton pump inhibitor OR PPI")' searches for that whole string
    as a literal phrase, and '"neuropath*"' is a phrase search with the truncation
    switched off — and OR-expanded, truncated concept blocks are exactly what
    search-strategy.md tells you to build.
    """
    t = term.strip()
    return f"({t})" if _SEARCH_SYNTAX_RE.search(t) else f'("{t}")'


def pair_queries(terms: list[str]) -> list[tuple[str, str, str]]:
    """Every unordered pair, as (a, b, query) — the finding-matrix searches."""
    out = []
    for a, b in itertools.combinations([t for t in terms if t.strip()], 2):
        out.append((a, b, f"{as_query_block(a)} AND {as_query_block(b)}"))
    return out


def classify_types(pubtypes) -> list[str]:
    """Map raw publication types to the labels that matter for appraisal."""
    labels = []
    for t in pubtypes or []:
        key = str(t).strip().lower()
        if key in HIGH_VALUE_TYPES:
            label = HIGH_VALUE_TYPES[key]
            if label not in labels:
                labels.append(label)
    return labels


# Publishers mark a retracted article by prefixing the title in caps
# ("RETRACTED:", "WITHDRAWN:") or appending "[Retracted in: ...]". The
# "Retracted Publication" pubtype is the primary signal but lags by weeks to
# months, so the title is checked too — a retracted paper ranked as a clean
# review is the single worst thing this script could hand back.
# Caps-sensitive on the prefix so "Retraction and reproducibility ..." (a
# legitimate methods paper) is not demoted; case-insensitive inside brackets.
RETRACTED_TITLE_RE = re.compile(r"^(RETRACTED|WITHDRAWN)\b|(?i:\[retracted in\b)", re.M)


def title_marks_retraction(title: str) -> bool:
    return bool(RETRACTED_TITLE_RE.search(title or ""))


def parse_year(pubdate: str):
    m = re.match(r"\s*(\d{4})", pubdate or "")
    return int(m.group(1)) if m else None


def summarize_hit(pmid: str, rec: dict) -> dict:
    authors = [a.get("name") for a in (rec.get("authors") or []) if a.get("name")]
    doi = None
    for aid in rec.get("articleids", []) or []:
        if aid.get("idtype") == "doi":
            doi = aid.get("value")
    types = classify_types(rec.get("pubtype", []))
    title = (rec.get("title") or "").rstrip(".")
    if title_marks_retraction(title) and "!! RETRACTED" not in types:
        types.append("!! RETRACTED")
    return {
        "pmid": str(pmid),
        "doi": doi,
        "title": title,
        "first_author": authors[0] if authors else None,
        "authors_n": len(authors),
        "journal": rec.get("fulljournalname") or rec.get("source"),
        "year": parse_year(rec.get("pubdate", "")),
        "types": types,
        "retracted": any("RETRACTED" in t for t in types),
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def rank_hits(hits: list[dict]) -> list[dict]:
    """Evidence-hierarchy first, then recency — so the strongest work is read first."""
    priority = {"META-ANALYSIS": 0, "SYSTEMATIC REVIEW": 1, "RCT": 2,
                "review": 3, "case report": 5}

    def key(h):
        if h["retracted"]:
            return (9, 0)
        best = min([priority.get(t, 4) for t in h["types"]], default=4)
        return (best, -(h["year"] or 0))

    return sorted(hits, key=key)


# ======================================================================
# Search orchestration
# ======================================================================
def search(query: str, retmax: int = 25, email=None, fetch=http_get_json) -> dict:
    res = fetch(ESEARCH, {"db": "pubmed", "term": query, "retmax": str(retmax),
                          "sort": "relevance"}, email=email)
    esr = (res or {}).get("esearchresult", {})
    # E-utilities reports an unexecutable query with HTTP 200 and zero results, putting the
    # reason in ERROR / errorlist / warninglist. Without reading those, a typo'd field tag or
    # an unmatched quoted phrase is indistinguishable from "the literature is silent on this"
    # -- the worst possible confusion for a tool whose job is to find what exists.
    #
    # Not every entry in those blocks means the query failed. NCBI puts a term that
    # simply is not in the index into `errorlist.phrasesnotfound`, and it puts
    # "No items found." into `warninglist.outputmessages` on ORDINARY empty searches.
    # Treating those as hard problems made the tool print "PubMed could not run the
    # query as written" on a perfectly good search -- and, worse, suppressed the
    # "NO HITS - a genuine gap is itself a finding" note on exactly the searches where
    # the gap was real. So the blocks are classified, not copied wholesale:
    #   hard  -> the query did not run as written: ERROR, and a field tag that does
    #            not exist (`fieldsnotfound`). Suppresses the gap note.
    #   note  -> the query ran; these terms matched nothing. Reported, because it often
    #            explains the gap, but it does NOT suppress the gap note.
    #   drop  -> pure status chatter ("No items found.") and empty lists.
    HARD_FIELDS = {"fieldsnotfound"}
    DROP_MESSAGES = {"no items found."}
    problems, notes = [], []
    if esr.get("ERROR"):
        problems.append(str(esr["ERROR"]))
    for key, label in (("errorlist", "error"), ("warninglist", "warning")):
        block = esr.get(key) or {}
        if not isinstance(block, dict):
            continue
        for field, vals in block.items():
            if not vals:
                continue
            vals = vals if isinstance(vals, list) else [vals]
            vals = [v for v in vals if str(v).strip().lower() not in DROP_MESSAGES]
            if not vals:
                continue
            line = f"{label}: {field}={', '.join(map(str, vals))}"
            (problems if field in HARD_FIELDS else notes).append(line)
    ids = esr.get("idlist", []) or []
    total = int(esr.get("count", 0) or 0)
    if not ids:
        return {"query": query, "total": total, "hits": [],
                "problems": problems, "notes": notes}
    summ = fetch(ESUMMARY, {"db": "pubmed", "id": ",".join(ids)}, email=email)
    result = (summ or {}).get("result", {})
    hits = []
    for pid in result.get("uids", []) or []:
        rec = result.get(pid)
        # E-utilities answers an unsummarizable UID with a stub carrying an "error"
        # key. Without this it became a hit with a blank title and no year, sitting
        # in the ranked list as though it were a paper.
        if not isinstance(rec, dict) or rec.get("error"):
            continue
        hits.append(summarize_hit(pid, rec))
    return {"query": query, "total": total, "hits": rank_hits(hits),
            "problems": problems, "notes": notes}


def format_human(res: dict, show_gap_note=True) -> str:
    L = [f"QUERY: {res['query']}",
         f"  {res['total']} total match(es) in PubMed; showing {len(res['hits'])}"]
    # Surface query problems FIRST: a zero-hit result caused by a typo'd field tag reads
    # exactly like a genuine gap, and acting on a fake gap is a research error.
    for prob in res.get("problems") or []:
        L.append(f"  !! QUERY PROBLEM — {prob}")
    if res.get("problems"):
        L.append("  PubMed could not run the query as written; fix it before concluding anything.")
    for note in res.get("notes") or []:
        L.append(f"  (note) {note}")
    if res.get("notes"):
        L.append("  The query ran; the terms above matched nothing in the index — which may be "
                 "the reason for a thin result, not a fault in the query.")
    if not res["hits"]:
        if show_gap_note and not res.get("problems"):
            L.append("  NO HITS — a genuine gap is itself a finding. Record it in the search log,")
            L.append("  then try the bridge search (shared drug / nutrient / mechanism).")
        return "\n".join(L)
    for h in res["hits"]:
        tags = f"  [{', '.join(h['types'])}]" if h["types"] else ""
        L.append("")
        L.append(f"  {h['title']}{tags}")
        author = f"{h['first_author']} et al." if h["authors_n"] > 1 else (h["first_author"] or "?")
        L.append(f"    {author}  |  {h['journal']}  |  {h['year']}")
        L.append(f"    PMID {h['pmid']}" + (f"  DOI {h['doi']}" if h["doi"] else ""))
        if h["retracted"]:
            L.append("    !! RETRACTED — do not use as support for any claim")
    return "\n".join(L)


def self_test() -> int:
    failures, ran = [], []

    def check(name, cond):
        ran.append(name)
        if not cond:
            failures.append(name)

    # Query building
    check("plain query", build_query("metformin") == "metformin")
    check("humans filter", "humans[MeSH Terms]" in build_query("x", humans=True))
    check("years filter", '"last 10 years"[PDat]' in build_query("x", years=10))
    check("pubtype filter", '"Review"[Publication Type]' in build_query("x", pubtype="Review"))
    try:
        build_query("   ")
        check("empty query rejected", False)
    except SearchError:
        check("empty query rejected", True)

    # Pair generation — the dot-connector
    pairs = pair_queries(["a", "b", "c"])
    check("3 terms -> 3 pairs", len(pairs) == 3)
    check("pair query shape", pairs[0][2] == '("a") AND ("b")')
    check("blank terms skipped", len(pair_queries(["a", "", "b"])) == 1)
    # Regression: every term was quoted unconditionally, which silently broke the
    # concept blocks search-strategy.md prescribes — an OR block became a literal
    # phrase, truncation stopped truncating, and an already-quoted term doubled up.
    check("OR block passed through",
          pair_queries(["proton pump inhibitor OR PPI", "B12"])[0][2]
          == '(proton pump inhibitor OR PPI) AND ("B12")')
    check("already-quoted term not double-quoted",
          pair_queries(['"peripheral neuropathy"', "metformin"])[0][2]
          == '("peripheral neuropathy") AND ("metformin")')
    check("truncation survives", as_query_block("neuropath*") == "(neuropath*)")
    check("field tag survives", as_query_block("metformin[tiab]") == "(metformin[tiab])")

    # Type classification
    check("classify RCT", "RCT" in classify_types(["Randomized Controlled Trial"]))
    check("classify meta", "META-ANALYSIS" in classify_types(["Meta-Analysis"]))
    check("classify retracted", any("RETRACTED" in t for t in classify_types(["Retracted Publication"])))
    check("classify unknown ignored", classify_types(["Letter"]) == [])

    # Retraction marked in the title only — the pubtype lags behind the notice.
    check("title-marked retraction caught", title_marks_retraction(
        "RETRACTED: Ileal-lymphoid-nodular hyperplasia"))
    check("withdrawn caught", title_marks_retraction("WITHDRAWN: An early trial"))
    check("bracketed retraction caught", title_marks_retraction(
        "A trial of X [Retracted in: N Engl J Med. 2021]"))
    check("ordinary title about retraction not flagged", not title_marks_retraction(
        "Retraction and reproducibility in clinical research"))
    h = summarize_hit("9500320", {"title": "RETRACTED: A study.", "pubdate": "1998 Feb",
                                  "fulljournalname": "Lancet", "pubtype": ["Journal Article"],
                                  "authors": [{"name": "Wakefield AJ"}], "articleids": []})
    check("title-only retraction reaches the hit", h["retracted"] is True)

    # Year parsing
    check("year parse", parse_year("2020 Dec 31") == 2020)
    check("year parse none", parse_year("") is None)

    # Ranking: meta-analysis first, retracted last
    hits = [
        {"types": ["case report"], "year": 2023, "retracted": False},
        {"types": ["META-ANALYSIS"], "year": 2015, "retracted": False},
        {"types": ["!! RETRACTED"], "year": 2024, "retracted": True},
        {"types": ["RCT"], "year": 2020, "retracted": False},
    ]
    ranked = rank_hits(hits)
    check("meta ranked first", ranked[0]["types"] == ["META-ANALYSIS"])
    check("rct second", ranked[1]["types"] == ["RCT"])
    check("retracted ranked last", ranked[-1]["retracted"] is True)

    # End-to-end with a stubbed fetcher
    def stub(url, params, email=None):
        if url == ESEARCH:
            return {"esearchresult": {"count": "2", "idlist": ["111", "222"]}}
        return {"result": {
            "uids": ["111", "222"],
            "111": {"title": "A meta-analysis of X.", "pubdate": "2019 Jan",
                    "fulljournalname": "J Test", "pubtype": ["Meta-Analysis"],
                    "authors": [{"name": "Smith J"}, {"name": "Doe A"}],
                    "articleids": [{"idtype": "doi", "value": "10.1/x"}]},
            "222": {"title": "A case report.", "pubdate": "2021 Mar",
                    "fulljournalname": "J Case", "pubtype": ["Case Reports"],
                    "authors": [{"name": "Roe B"}], "articleids": []}}}

    res = search("test", fetch=stub)
    check("e2e total", res["total"] == 2)
    check("e2e hits", len(res["hits"]) == 2)
    check("e2e ranked meta first", res["hits"][0]["pmid"] == "111")
    check("e2e doi captured", res["hits"][0]["doi"] == "10.1/x")
    check("e2e title cleaned", res["hits"][0]["title"] == "A meta-analysis of X")
    check("e2e year", res["hits"][0]["year"] == 2019)

    # Regression: an unsummarizable UID comes back as an error stub, and was ranked
    # as though it were a paper with a blank title.
    def stub_error_record(url, params, email=None):
        if url == ESEARCH:
            return {"esearchresult": {"count": "2", "idlist": ["111", "999"]}}
        return {"result": {
            "uids": ["111", "999"],
            "111": {"title": "A real paper.", "pubdate": "2020", "fulljournalname": "J",
                    "pubtype": ["Journal Article"], "authors": [{"name": "Smith J"}],
                    "articleids": []},
            "999": {"uid": "999", "error": "cannot get document summary"}}}

    res_err = search("x", fetch=stub_error_record)
    check("error stub skipped", [h["pmid"] for h in res_err["hits"]] == ["111"])

    # Regression: an unexecutable query returns HTTP 200 with zero hits and the reason in
    # ERROR/errorlist/warninglist. Reported as a plain "no hits" it reads as a genuine gap.
    # A genuinely unexecutable query: the field tag does not exist.
    def stub_bad_query(url, params, email=None):
        return {"esearchresult": {"count": "0", "idlist": [],
                                  "errorlist": {"fieldsnotfound": ["[nonsense]"]}}}
    res_bad = search("bad", fetch=stub_bad_query)
    check("query problems captured", len(res_bad.get("problems") or []) == 1)
    check("query problems named", any("fieldsnotfound" in p for p in res_bad["problems"]))
    rendered = format_human(res_bad)
    check("query problems rendered", "QUERY PROBLEM" in rendered)
    check("fake gap not reported as a gap", "NO HITS" not in rendered)

    # Regression, the other direction: NCBI returns `phrasesnotfound` for any term not in
    # the index and `outputmessages: ["No items found."]` on ordinary empty searches. Read
    # wholesale, those printed "PubMed could not run the query as written" on a perfectly
    # good search AND suppressed the genuine-gap note — silencing the finding on exactly
    # the searches where the gap was real.
    def stub_benign_empty(url, params, email=None):
        return {"esearchresult": {
            "count": "0", "idlist": [],
            "errorlist": {"phrasesnotfound": ["rare-compound-x"], "fieldsnotfound": []},
            "warninglist": {"phrasesignored": [], "quotedphrasesnotfound": [],
                            "outputmessages": ["No items found."]}}}
    res_benign = search("rare-compound-x", fetch=stub_benign_empty)
    check("benign empty search raises no hard problem", res_benign["problems"] == [])
    check("term-not-in-index kept as an informational note",
          any("phrasesnotfound" in n for n in res_benign["notes"]))
    check("'No items found.' is dropped entirely",
          not any("No items found" in n for n in res_benign["notes"]))
    check("empty sub-lists produce nothing", len(res_benign["notes"]) == 1)
    rendered_benign = format_human(res_benign)
    check("genuine gap note survives a benign warning", "NO HITS" in rendered_benign)
    check("benign empty search is not called unexecutable",
          "could not run the query" not in rendered_benign)
    check("the note is still shown to the user", "(note)" in rendered_benign)

    def stub_empty(url, params, email=None):
        return {"esearchresult": {"count": "0", "idlist": []}}

    res0 = search("nothing", fetch=stub_empty)
    check("e2e empty handled", res0["hits"] == [] and res0["total"] == 0)
    check("e2e empty note", "NO HITS" in format_human(res0))

    def stub_down(url, params, email=None):
        raise SearchError("network unavailable (blocked) — PubMed could not be searched")

    try:
        search("x", fetch=stub_down)
        check("network error propagates", False)
    except SearchError:
        check("network error propagates", True)

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
        description="Search PubMed via NCBI E-utilities; returns ranked, structured hits.")
    ap.add_argument("query", nargs="?", help="search query")
    ap.add_argument("--pairs", nargs="+", metavar="TERM",
                    help="search every pair of these terms (the dot-connector)")
    ap.add_argument("--max", type=int, default=25, help="max results per query (default 25)")
    ap.add_argument("--years", type=int, help="limit to the last N years")
    ap.add_argument("--humans", action="store_true", help="limit to human studies")
    ap.add_argument("--type", dest="pubtype", help='e.g. "Review", "Randomized Controlled Trial"')
    ap.add_argument("--language", help="e.g. english")
    ap.add_argument("--email", help="your e-mail; NCBI asks callers to identify themselves")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--self-test", action="store_true", help="run offline logic tests and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.query and not args.pairs:
        ap.error("provide a query or --pairs")

    jobs = []
    if args.query:
        jobs.append(("query", build_query(args.query, args.years, args.humans,
                                          args.pubtype, args.language)))
    if args.pairs:
        for a, b, q in pair_queries(args.pairs):
            jobs.append((f"pair: {a} + {b}",
                         build_query(q, args.years, args.humans, args.pubtype, args.language)))

    results = []
    try:
        for label, q in jobs:
            res = search(q, retmax=args.max, email=args.email)
            res["label"] = label
            results.append(res)
    except SearchError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for res in results:
            print(f"\n### {res['label']}")
            print(format_human(res))
        print("\nNext: appraise quality (evidence-appraisal.md), check country of origin "
              "(source-provenance.md), and verify anything you cite (verify_citation.py).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
