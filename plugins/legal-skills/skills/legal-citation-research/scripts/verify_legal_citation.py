#!/usr/bin/env python3
"""Parse legal citations out of text and verify them against CourtListener -- failing to
UNVERIFIED, never to a false VERIFIED.

Usage:
  verify_legal_citation.py <brief.txt | memo.md | brief.docx> [--json] [--offline] [--endpoint URL]
  verify_legal_citation.py --cite "678 F. Supp. 3d 443" [--cite "..."] [--json]
  verify_legal_citation.py --self-test        # offline tests against a local mock server

Token: set COURTLISTENER_API_TOKEN in the environment, or pass --token-file PATH (first line).
Without a token the script still parses and classifies every citation and reports each one
UNVERIFIED with the manual fallback. The token is never printed and never written anywhere.

WHAT THIS DOES
  1. Parses case citations offline -- volume, reporter, page, pinpoint, court/year parenthetical
     -- using a compact reporter table derived from the Free Law Project's reporters-db
     (BSD-2-Clause), tolerant of spacing and period variants ("F.Supp.3d", "F Supp 2d") and
     the known variant spellings ("Fed. Appx.", "Wn.2d").
  2. Classifies statutes, regulations and rules (U.S.C., C.F.R., Fed. R. ...) and database cites
     (WL, LEXIS), which CourtListener's lookup cannot resolve, and names where to verify them.
  3. With a token and a network, POSTs the text to CourtListener's citation-lookup endpoint and
     maps each result:
        200 -> VERIFIED      a cluster came back: case name, filing date, URL
        404 -> NOT FOUND     well-formed, absent from the corpus: the fabrication signal
        300 -> AMBIGUOUS     several clusters; they are listed
        400 -> UNRECOGNIZED  the reporter string was not recognised
        429 -> UNVERIFIED    rate-limited; retry later
     and anything else -- no token, transport failure, HTTP error, malformed JSON, a 200 with no
     clusters -- is UNVERIFIED. Citations CourtListener finds that the parser missed are listed too,
     and the text is posted even when the local parser finds nothing, so a brief whose citations
     all fall outside the local table still gets CourtListener's own parser.
  4. Prints the manual fallback for every citation that is not VERIFIED.

WHAT THIS DELIBERATELY DOES NOT DO
  It never reads the opinion, so it cannot tell you whether the case holds what the brief says,
  whether it is still good law, or whether the pinpoint is right. VERIFIED means the citation
  resolves to a real decision; that is all. Those further checks are the skill's steps.

Exit codes:
  0  every case citation VERIFIED, or no citation found by either parser after CourtListener
     was consulted
  1  at least one NOT FOUND, AMBIGUOUS or UNRECOGNIZED -- needs attention before filing
  3  at least one UNVERIFIED -- the check could not be completed, including a document scan in
     which no case citation parsed locally and CourtListener was not consulted or did not answer
     (an explicit --cite input is exempt: the user named exactly what to check)
  2  input unreadable
  5  bad usage
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

__version__ = "1.0.3"
ENDPOINT = "https://www.courtlistener.com/api/rest/v4/citation-lookup/"
SITE = "https://www.courtlistener.com"
USER_AGENT = "legal-citation-research/1.0 (citation verification; stdlib urllib)"
TIMEOUT = 40
MAX_TEXT = 60_000        # CourtListener accepts up to 64,000 characters per request
MAX_CITES = 200          # and up to 250 citations per request
TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reporters_compact.json")

FALLBACK = ("manual check: search the citation in quotation marks together with the case name on a "
            "court website, CourtListener, Google Scholar, Westlaw or Lexis. It counts as verified "
            "only when a source returns the case name AND the reporter citation together; generated "
            "prose, a bare URL, or a snippet without both is not verification. Until then it stays "
            "UNVERIFIED and does not go in the filing.")


class InputError(Exception):
    pass


# ----------------------------------------------------------------------------- reporters

def _squash(s: str) -> str:
    return re.sub(r"[\s.]", "", s)


def load_reporters(path: str = TABLE) -> dict:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    editions: dict = data["editions"]
    variations: dict = data["variations"]
    exact: dict[str, str] = {ed: ed for ed in editions}
    for var, canon in variations.items():
        exact.setdefault(var, canon)
    compact: dict[str, str] = {}
    squash: dict[str, str] = {}
    for ed in editions:
        compact.setdefault(ed.replace(" ", ""), ed)
        squash.setdefault(_squash(ed), ed)
    for var, canon in variations.items():
        compact.setdefault(var.replace(" ", ""), canon)
        squash.setdefault(_squash(var), canon)
    keys = sorted(set(editions) | set(variations), key=len, reverse=True)
    parts = []
    for k in keys:
        # Periods optional, and whitespace allowed after each one, so "N. Y. S. 2d", "N.Y.S.2d"
        # and "F Supp 2d" all reach the same edition. Never swallow trailing whitespace: the
        # page number's separator is matched separately.
        alt = r"\s*".join(re.escape(w) for w in k.split(" ")).replace(r"\.", r"\.?\s*")
        while alt.endswith(r"\s*"):
            alt = alt[:-3]
        parts.append(alt)
    alternation = "|".join(parts)
    cite_re = re.compile(
        r"(?<![\w§/.-])(\d{1,4})\s+(" + alternation + r")\s+"
        r"(\d{1,9}(?!\d)(?:-[A-Za-z0-9]+)?|_{2,}|—+|–+|-{2,})"
        r"(?:,\s*(?:at\s+)?(\d+(?:[-–]\d+)?)(?![\d\s,]*[A-Za-z]))?"
        r"(?:\s*\(([^()]*?\b((?:1[6-9]|20)\d{2})\b[^()]*)\))?")
    return {"editions": editions, "exact": exact, "compact": compact, "squash": squash, "re": cite_re}


def canonical(rep: str, tbl: dict) -> str | None:
    r = re.sub(r"\s+", " ", rep.strip())
    return (tbl["exact"].get(r) or tbl["compact"].get(r.replace(" ", ""))
            or tbl["squash"].get(_squash(r)))


DATABASE_TYPES = {"specialty_west", "specialty_lexis"}
STATUTE_RES = [
    ("STATUTE", re.compile(r"\b(\d{1,2})\s+U\.?\s?S\.?\s?C\.?(?:\s*(?:A|S)\.?)?\s*(?:§{1,2}|[Ss]ec(?:tion|\.)?)?\s*(\d+[\w().\-–]*)"),
     "verify the text and its currency at uscode.house.gov (or the official code)"),
    ("REGULATION", re.compile(r"\b(\d{1,2})\s+C\.?\s?F\.?\s?R\.?\s*(?:§{1,2}|[Pp]art|pt\.)?\s*(\d+(?:\.\d+)?[\w().\-–]*)"),
     "verify at ecfr.gov and check the Federal Register for amendments"),
    ("RULE", re.compile(r"\bFed\.\s*R\.\s*(?:Civ|Crim|App|Evid|Bankr)\.\s*P\.\s*\d+(?:\.\d+)?(?:\([a-zA-Z0-9]+\))*"),
     "verify at uscourts.gov/rules-policies (current rules and amendments)"),
]
SHORT_FORM_RE = re.compile(r"\b(?:Id\.|id\.|Ibid\.|supra)\b")


# ----------------------------------------------------------------------------- parsing

def read_docx(path: str) -> str:
    import xml.etree.ElementTree as ET
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    try:
        with zipfile.ZipFile(path) as z:
            root = ET.fromstring(z.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError, OSError, ET.ParseError) as e:
        raise InputError(f"not a readable .docx: {e}")
    paras = []
    for p in root.iter(W + "p"):
        t = "".join((n.text or "") if n.tag == W + "t" else (" " if n.tag in (W + "tab", W + "br") else "")
                    for n in p.iter())
        if t.strip():
            paras.append(t.strip())
    return "\n".join(paras)


def read_any(path: str) -> str:
    if path.lower().endswith(".docx"):
        return read_docx(path)
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as fh:
            return fh.read()
    except OSError as e:
        raise InputError(str(e))


def parse_citations(text: str, tbl: dict) -> list[dict]:
    """Return one entry per distinct citation, in order of first appearance."""
    found: list[dict] = []
    index: dict[str, dict] = {}
    masked = text

    def add(key, entry):
        if key in index:
            index[key]["count"] += 1
        else:
            entry["count"] = 1
            index[key] = entry
            found.append(entry)

    for kind, rx, where in STATUTE_RES:
        for m in rx.finditer(text):
            raw = re.sub(r"\s+", " ", m.group(0)).strip()
            add(f"{kind}:{_squash(raw)}", {"kind": kind, "cite": raw, "where": where, "status": kind})
            masked = masked[:m.start()] + " " * (m.end() - m.start()) + masked[m.end():]
    for m in tbl["re"].finditer(masked):
        vol, rep_raw, page, pin, paren, year = m.groups()
        canon = canonical(rep_raw, tbl)
        if canon is None:
            continue
        ctype = tbl["editions"].get(canon, {}).get("t", "")
        placeholder = not page[0].isdigit()
        norm = f"{vol} {canon} {'___' if placeholder else page}"
        court = None
        if paren:
            court = re.sub(r"\s+", " ", re.sub(r"\b(?:(?:1[6-9]|20)\d{2})\b", "", paren)).strip(" ,")
            court = re.sub(r"\b(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)\.?\s+\d{1,2},?$", "", court).strip(" ,") or None
        entry = {"kind": "database" if ctype in DATABASE_TYPES else ("slip" if placeholder else "case"),
                 "cite": re.sub(r"\s+", " ", m.group(0)).strip(), "volume": vol, "reporter": canon,
                 "reporter_as_written": rep_raw, "page": None if placeholder else page, "pinpoint": pin,
                 "court": court, "year": year, "normalized": norm, "status": None}
        if entry["kind"] == "database":
            entry["where"] = "verify in Westlaw or Lexis; CourtListener's lookup cannot resolve a database cite"
            entry["status"] = "DATABASE"
        elif entry["kind"] == "slip":
            entry["where"] = "no reporter page yet: verify by docket number and date on the court's site"
            entry["status"] = "SLIP"
        add(norm, entry)
    return found


# ----------------------------------------------------------------------------- lookup

class LookupFailure(Exception):
    pass


def read_token(token_file: str | None) -> str | None:
    if token_file:
        try:
            with open(token_file, encoding="utf-8") as fh:
                tok = fh.readline().strip()
        except OSError as e:
            raise LookupFailure(f"cannot read --token-file: {e}")
        return tok or None
    return os.environ.get("COURTLISTENER_API_TOKEN") or None


def post_lookup(text: str, token: str, endpoint: str, timeout: int = TIMEOUT) -> list:
    data = urllib.parse.urlencode({"text": text}).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, method="POST",
                                 headers={"Authorization": f"Token {token}", "User-Agent": USER_AGENT,
                                          "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise LookupFailure("rate-limited (HTTP 429): wait a minute and retry")
        if e.code in (401, 403):
            raise LookupFailure(f"token rejected (HTTP {e.code}): check COURTLISTENER_API_TOKEN")
        raise LookupFailure(f"HTTP {e.code} from CourtListener")
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise LookupFailure(f"network unavailable ({getattr(e, 'reason', e)})")
    try:
        parsed = json.loads(body.decode("utf-8", errors="replace"))
    except ValueError:
        raise LookupFailure("malformed response (not JSON)")
    if not isinstance(parsed, list):
        raise LookupFailure("unexpected response shape (expected a list)")
    return parsed


def _match_result(entries: list[dict], res: dict) -> dict | None:
    norms = {re.sub(r"\s+", " ", n).strip() for n in (res.get("normalized_citations") or []) if isinstance(n, str)}
    raw = re.sub(r"\s+", " ", str(res.get("citation") or "")).strip()
    for e in entries:
        if e["kind"] != "case":
            continue
        if e["normalized"] in norms or (raw and raw == e["cite"]):
            return e
        if raw and _squash(raw) == _squash(f"{e['volume']} {e['reporter']} {e['page']}"):
            return e
    return None


def apply_results(entries: list[dict], results: list) -> list[dict]:
    """Map CourtListener results onto parsed entries; return the extra citations it found."""
    extras = []
    for res in results:
        if not isinstance(res, dict):
            continue
        e = _match_result(entries, res)
        status = res.get("status")
        clusters = res.get("clusters") or []
        verdict, detail = _verdict(status, clusters, res.get("error_message"))
        if e is None:
            # Keep every unmatched result, whatever its status: an UNRECOGNIZED or UNVERIFIED
            # citation that only CourtListener saw is exactly the one the exit code must carry.
            extras.append({"kind": "case", "cite": str(res.get("citation") or "?"), "status": verdict,
                           "detail": detail, "count": 0, "found_by": "courtlistener-only"})
            continue
        if e.get("status") in (None, "UNVERIFIED"):
            e["status"], e["detail"] = verdict, detail
            if verdict == "VERIFIED":
                c = clusters[0]
                e["case_name"] = c.get("case_name")
                e["date_filed"] = c.get("date_filed")
                e["url"] = SITE + c["absolute_url"] if c.get("absolute_url") else None
    for e in entries:
        if e["kind"] == "case" and e.get("status") is None:
            e["status"], e["detail"] = "UNVERIFIED", "CourtListener returned no result for this citation"
    return extras


def _verdict(status, clusters, error_message) -> tuple[str, str]:
    if status == 200:
        if clusters:
            c = clusters[0]
            return "VERIFIED", f"{c.get('case_name') or '(no name)'} ({c.get('date_filed') or 'date ?'})"
        return "UNVERIFIED", "status 200 but no cluster was returned -- treat as unresolved"
    if status == 404:
        return "NOT FOUND", ("no decision at this reporter, volume and page in CourtListener. Before "
                             "calling it fabricated, check that the reporter and years are covered; then "
                             "verify in Westlaw, Lexis or the official reporter. Treat as fabricated until found")
    if status == 300:
        names = "; ".join(f"{c.get('case_name')} ({c.get('date_filed')})" for c in clusters[:5]) or "(unlisted)"
        return "AMBIGUOUS", f"{len(clusters)} candidates: {names} -- add the case name and year to pin it"
    if status == 400:
        return "UNRECOGNIZED", f"reporter not recognised by CourtListener ({error_message or 'no message'}); check the abbreviation"
    if status == 429:
        return "UNVERIFIED", "rate-limited by CourtListener; retry in a minute"
    return "UNVERIFIED", f"unexpected status {status!r} ({error_message or 'no message'})"


def verify(text: str, tbl: dict, token: str | None, endpoint: str = ENDPOINT, offline: bool = False,
           document: bool = True) -> dict:
    """`document` is True for a whole-text scan (a brief, a memo), where the local parser may have
    missed a case citation and the absence of a remote check must not read as clean; it is False
    for explicit `--cite` inputs, where the user named exactly what to check."""
    entries = parse_citations(text, tbl)
    cases = [e for e in entries if e["kind"] == "case"]
    mode = "offline" if offline else ("no-token" if not token else "live")
    extras: list[dict] = []
    failure = None
    if mode == "live" and (cases or text.strip()):
        # Post even when the local parser found nothing: CourtListener runs its own, broader
        # parser, and a text whose citations all fall outside the local regex must not come back
        # as "nothing to verify".
        if len(text) <= MAX_TEXT and len(cases) <= MAX_CITES:
            chunks = [text]
        elif cases:
            chunks = ["\n".join(e["cite"] for e in cases[i:i + MAX_CITES]) for i in range(0, len(cases), MAX_CITES)]
        else:
            chunks = [text[i:i + MAX_TEXT] for i in range(0, len(text), MAX_TEXT)]
        results: list = []
        for n, chunk in enumerate(chunks):
            if n:
                time.sleep(1.0)
            try:
                results += post_lookup(chunk, token, endpoint)
            except LookupFailure as e:
                failure = str(e)
                break
        if failure is None:
            extras = apply_results(entries, results)
    remote_scan = None
    if mode != "live" or failure:
        reason = {"offline": "--offline", "no-token": "no COURTLISTENER_API_TOKEN"}.get(mode, failure)
        for e in cases:
            e["status"], e["detail"] = "UNVERIFIED", f"not checked: {reason}"
        if document and not cases and text.strip():
            # A document scan in which no case citation parsed locally and no remote parser ran:
            # that is "could not verify", not "nothing to verify" -- a brief whose case citations
            # all fall outside the local table looks exactly like this, and it must not exit clean.
            # Explicit --cite inputs skip this: the user named exactly what to check.
            if failure:
                how = f"CourtListener was contacted but the lookup failed: {failure}"
            else:
                how = f"CourtListener was not consulted ({reason})"
            others = [e for e in entries if e["kind"] != "case"]
            tail = ("; the statute, regulation, rule or database citations listed above were "
                    "classified, not verified" if others else "")
            remote_scan = {"status": "UNVERIFIED",
                           "detail": f"no case citation parsed locally and {how}{tail}"}
    counts = {}
    for e in entries + extras:
        counts[e["status"]] = counts.get(e["status"], 0) + 1
    if remote_scan:
        counts["UNVERIFIED"] = counts.get("UNVERIFIED", 0) + 1
    return {"version": __version__, "mode": mode, "endpoint": endpoint if mode == "live" else None,
            "failure": failure, "citations": entries, "courtlistener_only": extras,
            "remote_scan": remote_scan, "counts": counts}


def exit_code(rep: dict) -> int:
    c = rep["counts"]
    if any(c.get(k) for k in ("NOT FOUND", "AMBIGUOUS", "UNRECOGNIZED")):
        return 1
    if c.get("UNVERIFIED"):
        return 3
    return 0


# ----------------------------------------------------------------------------- output

def format_human(rep: dict, source: str) -> str:
    L = [f"Legal citation check {__version__} -- {source}   (CourtListener: {rep['mode']}"
         + (f"; {rep['failure']}" if rep["failure"] else "") + ")"]
    kinds = {}
    for e in rep["citations"]:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    L.append("  parsed: " + ", ".join(f"{v} {k}" for k, v in sorted(kinds.items())) if kinds else "  parsed: no citations found")
    width = 13
    for e in rep["citations"]:
        st = e["status"]
        line = f"  {st:<{width}} {e['cite']}"
        if e.get("count", 1) > 1:
            line += f"  (×{e['count']})"
        if st == "VERIFIED":
            line += f"  -- {e.get('case_name')} ({e.get('date_filed')})  {e.get('url') or ''}"
        elif e.get("detail"):
            line += f"  -- {e['detail']}"
        elif e.get("where"):
            line += f"  -- {e['where']}"
        if e["kind"] == "case" and st != "VERIFIED":
            line += f"\n{'':{width + 3}}{FALLBACK}"
        L.append(line)
    for e in rep["courtlistener_only"]:
        L.append(f"  {e['status']:<{width}} {e['cite']}  -- found by CourtListener only (the parser missed it): {e['detail']}")
        if e["status"] != "VERIFIED":
            L.append(f"{'':{width + 3}}{FALLBACK}")
    if rep.get("remote_scan"):
        L.append(f"  {'UNVERIFIED':<{width}} (the whole text)  -- {rep['remote_scan']['detail']}")
        L.append(f"{'':{width + 3}}{FALLBACK}")
    c = rep["counts"]
    L.append("summary: " + ", ".join(f"{k.lower()} {v}" for k, v in sorted(c.items())) + f"  (exit {exit_code(rep)})")
    return "\n".join(L)


# ----------------------------------------------------------------------------- self-test

FIXTURES = [
    # (text, [(volume, canonical reporter, page)], note)
    ("Commonwealth v. Muniz, 164 A.3d 1189 (Pa. 2017)", [("164", "A.3d", "1189")], "eyecite"),
    ("asdf 22 A. 2d 332 asdf", [("22", "A.2d", "332")], "eyecite: spaced edition"),
    ("171 Wn.2d 1016", [("171", "Wash. 2d", "1016")], "eyecite: variant spelling"),
    ("559 N.W.2d 826", [("559", "N.W.2d", "826")], "eyecite"),
    ("Reece v. State of Washington, 310 F.2d 139 (1962)", [("310", "F.2d", "139")], "eyecite"),
    ("Hurst v. Florida, — U.S. —, 136 S.Ct. 616, 193 L.Ed.2d 504 (2016)",
     [("136", "S. Ct.", "616"), ("193", "L. Ed. 2d", "504")], "eyecite: dash placeholders skipped"),
    ("Houston Cmty. Coll. Sys. v. Wilson, ---- U.S. ----, 142 S. Ct. 1253, 1259, ---- L. Ed. 2d ---- (2022)",
     [("142", "S. Ct.", "1253")], "eyecite: pinpoint"),
    ("Mavrovich v Vanderpool, 427 F Supp 2d 1084 (D Kan 2006)", [("427", "F. Supp. 2d", "1084")], "eyecite: no periods"),
    ("Foo v. Bar,  1 F.Supp. 1 (SC 1967)", [("1", "F. Supp.", "1")], "eyecite: no spaces"),
    ("However, as we explained in Kaiser Foundation, supra, 13 Cal.App.5th at 1146", [], "short form only"),
    ("123 N. Y. S. 2d 456", [("123", "N.Y.S.2d", "456")], "eyecite: spaced out"),
    ("260 F. R. D. 38", [("260", "F.R.D.", "38")], "eyecite"),
    ("8 N. Y. 3d 204", [("8", "N.Y.3d", "204")], "eyecite"),
    ("Rogers v Rogers (63 NY2d 582 [1984])", [("63", "N.Y.2d", "582")], "eyecite: squashed"),
    ("Spano v. People of State of New York, 360 U.S. 315", [("360", "U.S.", "315")], "eyecite"),
    ("Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)", [("678", "F. Supp. 3d", "443")], "the cautionary case"),
    ("Foo v. Bar 1 U.S. 12, 347-348 (4th Cir. 1982)", [("1", "U.S.", "12")], "eyecite: range pinpoint"),
    ("see 42 U.S.C. § 1983 and 29 C.F.R. § 541.600; Fed. R. Civ. P. 11(b)", [], "non-case cites"),
    ("Id. at 12. See supra note 3.", [], "short forms"),
    ("Bob v. Carol, 2015 WL 2375225 (N.D. Ill. May 18, 2015)", [], "database cite is not a case entry"),
]


def _mock_server():
    """A local stand-in for CourtListener's lookup endpoint, driven by substrings in the text."""
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer
    state = {"requests": 0, "auth_seen": []}

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):  # keep the self-test quiet
            pass

        def do_POST(self):
            state["requests"] += 1
            auth = self.headers.get("Authorization", "")
            state["auth_seen"].append(auth)
            n = int(self.headers.get("Content-Length") or 0)
            text = urllib.parse.parse_qs(self.rfile.read(n).decode("utf-8")).get("text", [""])[0]
            if not auth.startswith("Token ") or auth == "Token bad":
                self._send(401, b'{"detail": "Invalid token."}')
                return
            if len(text) > 64_000:
                self._send(400, b'{"detail": "text is too long"}')
                return
            if "RATE" in text:
                self._send(429, b'{"detail": "Request was throttled."}')
                return
            if "BROKEN" in text:
                self._send(200, b"<html>not json</html>")
                return
            out = []
            if "678 F. Supp. 3d 443" in text:
                out.append({"citation": "678 F. Supp. 3d 443", "normalized_citations": ["678 F. Supp. 3d 443"],
                            "start_index": 0, "end_index": 19, "status": 200, "error_message": "",
                            "clusters": [{"id": 1, "case_name": "Mata v. Avianca, Inc.", "date_filed": "2023-06-22",
                                          "absolute_url": "/opinion/1/mata-v-avianca-inc/"}]})
            if "999 F.3d 9999" in text:
                out.append({"citation": "999 F.3d 9999", "normalized_citations": ["999 F.3d 9999"], "status": 404,
                            "error_message": "Citation not found: '999 F.3d 9999'", "clusters": []})
            if "1 U.S. 1" in text:
                out.append({"citation": "1 U.S. 1", "normalized_citations": ["1 U.S. 1"], "status": 300,
                            "error_message": "Multiple citations found for '1 U.S. 1'",
                            "clusters": [{"id": 2, "case_name": "A v. B", "date_filed": "1790-01-01", "absolute_url": "/opinion/2/a/"},
                                         {"id": 3, "case_name": "C v. D", "date_filed": "1791-01-01", "absolute_url": "/opinion/3/c/"}]})
            if "171 Wn.2d 1016" in text:
                out.append({"citation": "171 Wn.2d 1016", "normalized_citations": [], "status": 400,
                            "error_message": "Unable to find reporter", "clusters": []})
            if "12 F.3d 34" in text:
                out.append({"citation": "12 F.3d 34", "normalized_citations": ["12 F.3d 34"], "status": 200,
                            "error_message": "", "clusters": []})
            if "EXTRA404" in text:
                out.append({"citation": "6 Haw. 6", "normalized_citations": ["6 Haw. 6"], "status": 404,
                            "error_message": "Citation not found", "clusters": []})
            if "EXTRA400" in text:
                out.append({"citation": "7 Zzz. 7", "normalized_citations": [], "status": 400,
                            "error_message": "Unable to find reporter", "clusters": []})
            if "EXTRA200" in text:
                out.append({"citation": "8 Haw. 8", "normalized_citations": ["8 Haw. 8"], "status": 200,
                            "error_message": "", "clusters": []})
            if "EXTRA" in text:
                out.append({"citation": "5 Haw. 5", "normalized_citations": ["5 Haw. 5"], "status": 200,
                            "error_message": "", "clusters": [{"id": 4, "case_name": "E v. F", "date_filed": "1850-01-01",
                                                              "absolute_url": "/opinion/4/e/"}]})
            self._send(200, json.dumps(out).encode("utf-8"))

        def _send(self, code, body):
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    srv = HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/lookup/", state


def self_test() -> int:
    import contextlib
    import io
    import tempfile
    failures: list[str] = []
    total = 0

    def check(name, cond):
        nonlocal total
        total += 1
        if not cond:
            failures.append(name)

    tbl = load_reporters()
    check("reporter table loads with editions and variations", len(tbl["editions"]) > 1000 and len(tbl["exact"]) > len(tbl["editions"]))
    check("canonical: exact edition wins over a variation ('B.R.' is the Bankruptcy Reporter)", canonical("B.R.", tbl) == "B.R.")
    check("canonical: variation maps ('Fed. Appx.' -> \"F. App'x\")", canonical("Fed. Appx.", tbl) == "F. App'x")
    check("canonical: compact spacing ('F.Supp.3d')", canonical("F.Supp.3d", tbl) == "F. Supp. 3d")
    check("canonical: squashed ('FSupp2d')", canonical("F Supp 2d", tbl) == "F. Supp. 2d")
    check("canonical: unknown is None", canonical("Zzz. Rptr.", tbl) is None)
    for text, expected, note in FIXTURES:
        got = [(e["volume"], e["reporter"], e["page"]) for e in parse_citations(text, tbl) if e["kind"] == "case"]
        check(f"parse [{note}]: {text[:50]!r} -> {expected}", got == expected)
    ents = parse_citations("Mata v. Avianca, Inc., 678 F. Supp. 3d 443, 448-49 (S.D.N.Y. 2023)", tbl)
    check("parse: pinpoint, court and year captured",
          ents and ents[0]["pinpoint"] == "448-49" and ents[0]["court"] == "S.D.N.Y." and ents[0]["year"] == "2023")
    ents = parse_citations("see 42 U.S.C. § 1983; 29 C.F.R. § 541.600; Fed. R. Civ. P. 11(b); 2015 WL 2375225; 1 U.S. ___", tbl)
    kinds = {e["kind"]: e for e in ents}
    check("STATUTE classified with a verification route", "STATUTE" in kinds and "uscode" in kinds["STATUTE"]["where"])
    check("REGULATION classified", "REGULATION" in kinds and "ecfr" in kinds["REGULATION"]["where"])
    check("RULE classified", "RULE" in kinds)
    check("database cite classified, not sent as a case", "database" in kinds and kinds["database"]["status"] == "DATABASE")
    check("slip placeholder page classified", "slip" in kinds and kinds["slip"]["page"] is None)
    check("statute digits are not re-parsed as a case ('42 U.S.C.' is not '42 U.S.')",
          not [e for e in ents if e["kind"] == "case"])
    wl = [e for e in parse_citations("Bob v. Carol, 2015 WL 2375225 (N.D. Ill. May 18, 2015)", tbl) if e["kind"] == "database"]
    check("a database identifier keeps all its digits ('2015 WL 2375225', not '237522')",
          wl and wl[0]["cite"].startswith("2015 WL 2375225") and wl[0]["page"] == "2375225")
    check("a page of more than nine digits is not truncated into a false citation",
          not parse_citations("see 1 U.S. 1234567890 for nothing", tbl))
    dup = parse_citations("678 F. Supp. 3d 443 ... again 678 F. Supp. 3d 443 ... and 678 F.Supp.3d 443", tbl)
    check("duplicates collapse to one entry with a count", len(dup) == 1 and dup[0]["count"] == 3)

    # --- live path against the mock -------------------------------------------------------
    srv, url, state = _mock_server()
    try:
        text = ("Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023); Fake v. Case, 999 F.3d 9999 (2d Cir. 2021); "
                "1 U.S. 1; 171 Wn.2d 1016; 12 F.3d 34; 7 F.3d 7; 42 U.S.C. § 1983; 28 U.S.C. 1331")
        rep = verify(text, tbl, "secret-token-abc", url)
        by = {e["normalized"]: e for e in rep["citations"] if e["kind"] == "case"}
        check("live: mode is live", rep["mode"] == "live" and state["requests"] == 1)
        check("live: 200 -> VERIFIED with case name and URL",
              by["678 F. Supp. 3d 443"]["status"] == "VERIFIED" and by["678 F. Supp. 3d 443"]["case_name"] == "Mata v. Avianca, Inc."
              and by["678 F. Supp. 3d 443"]["url"].startswith(SITE))
        check("live: 404 -> NOT FOUND (the fabricated citation)", by["999 F.3d 9999"]["status"] == "NOT FOUND")
        check("live: 300 -> AMBIGUOUS with candidates listed", by["1 U.S. 1"]["status"] == "AMBIGUOUS" and "A v. B" in by["1 U.S. 1"]["detail"])
        check("live: 400 -> UNRECOGNIZED", by["171 Wash. 2d 1016"]["status"] == "UNRECOGNIZED")
        check("live: 200 with no clusters -> UNVERIFIED, never VERIFIED", by["12 F.3d 34"]["status"] == "UNVERIFIED")
        check("live: statute stays STATUTE", [e for e in rep["citations"] if e["kind"] == "STATUTE"][0]["status"] == "STATUTE")
        check("live: a citation CourtListener never answered is UNVERIFIED, not silently dropped",
              by["7 F.3d 7"]["status"] == "UNVERIFIED" and "no result" in by["7 F.3d 7"]["detail"])
        check("statute without a section sign is still a statute", len([e for e in rep["citations"] if e["kind"] == "STATUTE"]) == 2)
        check("live: exit 1 when a NOT FOUND is present", exit_code(rep) == 1)
        check("live: the token is sent as 'Token <value>'", state["auth_seen"][-1] == "Token secret-token-abc")
        out = format_human(rep, "memo")
        check("human output never contains the token", "secret-token-abc" not in out and "secret-token-abc" not in json.dumps(rep))
        check("human output carries the fallback on every non-verified case", out.count("manual check:") == 5)

        rep2 = verify("Good v. Case, 678 F. Supp. 3d 443 (S.D.N.Y. 2023).", tbl, "secret-token-abc", url)
        check("live: all verified -> exit 0", exit_code(rep2) == 0 and rep2["counts"] == {"VERIFIED": 1})

        rep3 = verify("RATE 678 F. Supp. 3d 443", tbl, "secret-token-abc", url)
        check("live: 429 -> UNVERIFIED with the rate-limit reason, exit 3",
              rep3["citations"][0]["status"] == "UNVERIFIED" and "rate-limited" in rep3["failure"] and exit_code(rep3) == 3)
        rep4 = verify("BROKEN 678 F. Supp. 3d 443", tbl, "secret-token-abc", url)
        check("live: malformed JSON -> UNVERIFIED", rep4["citations"][0]["status"] == "UNVERIFIED" and "malformed" in rep4["failure"])
        rep5 = verify("678 F. Supp. 3d 443", tbl, "bad", url)
        check("live: rejected token -> UNVERIFIED naming the token problem",
              rep5["citations"][0]["status"] == "UNVERIFIED" and "token rejected" in rep5["failure"])
        before = state["requests"]
        rep6 = verify("678 F. Supp. 3d 443", tbl, None, url)
        check("no token: UNVERIFIED and no request is made",
              rep6["mode"] == "no-token" and rep6["citations"][0]["status"] == "UNVERIFIED" and state["requests"] == before)
        rep7 = verify("678 F. Supp. 3d 443", tbl, "secret-token-abc", url, offline=True)
        check("--offline: UNVERIFIED and no request is made", rep7["mode"] == "offline" and state["requests"] == before)
        rep8 = verify("EXTRA 678 F. Supp. 3d 443", tbl, "secret-token-abc", url)
        check("a citation CourtListener finds that the parser missed is reported as courtlistener-only",
              rep8["courtlistener_only"] and rep8["courtlistener_only"][0]["cite"] == "5 Haw. 5")
        rep11 = verify("Plain prose with no reporter citation the local table knows. EXTRA", tbl, "secret-token-abc", url)
        check("live mode still posts when the local parser finds no cases, and reports the API-only result",
              rep11["mode"] == "live" and rep11["courtlistener_only"] and rep11["courtlistener_only"][0]["cite"] == "5 Haw. 5"
              and rep11["counts"].get("VERIFIED") == 1)
        rep12 = verify("More prose, nothing parsed locally. EXTRA404", tbl, "secret-token-abc", url)
        check("an API-only NOT FOUND counts toward the exit code", rep12["counts"].get("NOT FOUND") == 1 and exit_code(rep12) == 1)
        before2 = state["requests"]
        blank = verify("   ", tbl, "secret-token-abc", url)
        check("blank text makes no request and exits 0", state["requests"] == before2 and exit_code(blank) == 0)
        rep13 = verify("RATE prose with nothing the local parser knows", tbl, "secret-token-abc", url)
        check("remote-only scan failure -> UNVERIFIED and exit 3, never a false clean",
              bool(rep13["remote_scan"]) and rep13["counts"].get("UNVERIFIED") == 1 and exit_code(rep13) == 3)
        rep14 = verify("prose EXTRA400", tbl, "secret-token-abc", url)
        check("an API-only UNRECOGNIZED result is kept and drives exit 1",
              rep14["counts"].get("UNRECOGNIZED") == 1 and exit_code(rep14) == 1)
        rep15 = verify("prose EXTRA200", tbl, "secret-token-abc", url)
        check("an API-only 200 with no cluster is kept as UNVERIFIED and drives exit 3",
              rep15["counts"].get("UNVERIFIED") == 1 and exit_code(rep15) == 3 and "manual check:" in format_human(rep15, "x"))
        rep16 = verify("prose with no citations and no token", tbl, None, url)
        check("no token + nothing parsed locally -> UNVERIFIED (not consulted), exit 3, said in the output",
              exit_code(rep16) == 3 and "not consulted" in format_human(rep16, "x"))
        check("a failed live request says 'contacted', never 'not consulted'",
              "contacted" in rep13["remote_scan"]["detail"] and "not consulted" not in rep13["remote_scan"]["detail"])
        rep18 = verify("see 42 U.S.C. § 1983 and nothing else", tbl, None, url, document=True)
        check("document scan, statute only, no token -> sentinel says the statute was classified, not verified; exit 3",
              exit_code(rep18) == 3 and "classified, not verified" in rep18["remote_scan"]["detail"]
              and "no case citation" in rep18["remote_scan"]["detail"])
        rep19 = verify("42 U.S.C. § 1983", tbl, None, url, document=False)
        check("explicit --cite of a statute, offline/no token -> no sentinel, exit 0", rep19["remote_scan"] is None and exit_code(rep19) == 0)
        rep17 = verify("prose with no citations, consulted", tbl, "secret-token-abc", url)
        check("nothing found by either parser after CourtListener answered -> exit 0", exit_code(rep17) == 0)
        big = ("x" * 70_000) + " 678 F. Supp. 3d 443 and 999 F.3d 9999"
        rep9 = verify(big, tbl, "secret-token-abc", url)
        check("oversize text is sent as citation strings, and still resolves",
              rep9["counts"].get("VERIFIED") == 1 and rep9["counts"].get("NOT FOUND") == 1)
        # a filing-shaped docx round trip
        with tempfile.TemporaryDirectory() as td:
            dp = os.path.join(td, "brief.docx")
            doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
                   '<w:p><w:r><w:t>See Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023).</w:t></w:r></w:p>'
                   '</w:body></w:document>')
            with zipfile.ZipFile(dp, "w") as z:
                z.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
                z.writestr("word/document.xml", doc)
            def run(argv):
                o, e_ = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e_):
                    rc = main(argv)
                return rc, o.getvalue(), e_.getvalue()

            tok = _write(td, "tok", "secret-token-abc\n")
            rc, out, _ = run([dp, "--endpoint", url, "--token-file", tok])
            check("docx input: parsed and verified end to end, exit 0", rc == 0 and "VERIFIED" in out)
            check("human output on the docx path never contains the token", "secret-token-abc" not in out)
            rc, out, _ = run([dp, "--endpoint", url, "--token-file", tok, "--json"])
            j = json.loads(out)
            check("--json output parses and omits the token", j["mode"] == "live" and "secret-token-abc" not in out)
            rc_bad, _, err = run([os.path.join(td, "missing.docx"), "--offline"])
            check("unreadable input -> exit 2 with the reason on stderr", rc_bad == 2 and "ERROR" in err)
            rc_cite, out, _ = run(["--cite", "999 F.3d 9999", "--endpoint", url, "--token-file", tok])
            check("--cite path: fabricated citation -> exit 1 and NOT FOUND printed", rc_cite == 1 and "NOT FOUND" in out)
            rc_none, _, _ = run([])
            check("no arguments -> exit 5", rc_none == 5)
            rc_st, out_st, _ = run(["--cite", "42 U.S.C. § 1983", "--offline"])
            check("--cite of a statute with --offline exits 0 and does not claim nothing was parsed",
                  rc_st == 0 and "STATUTE" in out_st and "no case citation" not in out_st)
            rc_tf, _, err = run(["--cite", "1 U.S. 1", "--token-file", os.path.join(td, "nope")])
            check("missing --token-file -> exit 2", rc_tf == 2 and "token-file" in err)
    finally:
        srv.shutdown()
    # transport failure: a port with nothing listening
    dead = "http://127.0.0.1:9/lookup/"
    rep10 = verify("678 F. Supp. 3d 443", tbl, "secret-token-abc", dead, )
    check("transport failure -> UNVERIFIED, exit 3", rep10["citations"][0]["status"] == "UNVERIFIED" and exit_code(rep10) == 3)

    print(f"self-test: {total - len(failures)}/{total} checks passed")
    for f in failures:
        print(f"  FAILED: {f}")
    return 0 if not failures else 1


def _write(d, name, content):
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)
    return p


# ----------------------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="text, markdown or .docx to scan")
    ap.add_argument("--cite", action="append", help="verify this citation (repeatable)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--offline", action="store_true", help="parse and classify only; no network")
    ap.add_argument("--endpoint", default=ENDPOINT, help=argparse.SUPPRESS)
    ap.add_argument("--token-file", help="file whose first line is the CourtListener API token")
    ap.add_argument("--self-test", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit:
        return 5
    if args.self_test:
        return self_test()
    if not args.file and not args.cite:
        print("provide a file or --cite (or --self-test)", file=sys.stderr)
        return 5
    try:
        tbl = load_reporters()
    except (OSError, ValueError, KeyError) as e:
        print(f"ERROR: reporter table unreadable ({e}); it ships beside this script as reporters_compact.json", file=sys.stderr)
        return 2
    if args.file:
        try:
            text = read_any(args.file)
        except InputError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        source = args.file
    else:
        text = "\n".join(args.cite)
        source = "--cite"
    try:
        token = None if args.offline else read_token(args.token_file)
    except LookupFailure as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    rep = verify(text, tbl, token, args.endpoint, offline=args.offline, document=bool(args.file))
    if args.json:
        print(json.dumps({"source": source, **rep}, indent=2, ensure_ascii=False))
    else:
        print(format_human(rep, source))
    return exit_code(rep)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
