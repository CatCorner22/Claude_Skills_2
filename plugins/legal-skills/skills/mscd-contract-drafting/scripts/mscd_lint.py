#!/usr/bin/env python3
"""Lint contract text against drafting rules drawn from Ken Adams's *A Manual of Style for
Contract Drafting* (MSCD) and suggest an edit for every finding.

Usage:
  mscd_lint.py <contract.docx | contract.txt | contract.md> [--json] [--review]
               [--house-style shall|must] [--max-words N] [--known-terms FILE]
  mscd_lint.py --self-test            # offline fixture tests, no network, no input file

WHAT THIS DOES
  Deterministic pattern checks only. Every finding carries the matched text, a suggested edit,
  the reason, and the section of the document it sits in, so a drafter can work the list
  section by section. It never rewrites the file. The judgment calls -- whether a given
  "shall" really imposes a duty on the sentence's subject, whether a defined term earns its
  keep -- are surfaced with the test to apply, not decided by the tool.

  Severity vocabulary:
    edit  a deterministic replacement the drafter can apply as written
    flag  needs a lawyer's decision: contested among drafters, or inside a rail (below)
    info  a heuristic hit worth a look; verify before acting

  Two rails downgrade an `edit` to a `flag`, because clarity does not override them:
    risk-allocation    indemnity, defence, hold-harmless, limitation of liability, warranty
                       disclaimers, insurance, releases, liquidated damages -- courts construe
                       these strictly and the words can BE the allocation, so the tool proposes
                       alongside and never cuts
    prescribed-wording an all-capitals block, a statutory or UCC reference, a required notice --
                       text a rule requires verbatim

  Rules (id -- what it catches):
    SHALL-POLICY      "shall" with a non-party subject or a policy verb (shall mean / be deemed /
                      survive / be governed by): language of policy wants the present tense
    SHALL-PASSIVE     passive "shall be <participle>" that hides who must act
    SHALL-DISC        "shall be entitled to" / "shall have the right to": discretion dressed as duty
    SHALL-NEG         "shall not be required to": the negative of discretion
    SHALL-OBLIG       "shall be obligated / required to": a duty wearing two hats
    SHALL-RESP        "shall be responsible for <verb>ing": name the duty directly
    SHALL-THROAT      "covenants and agrees to" / "undertakes to" / "agrees to <verb>": throat-clearing
    HOUSE-STYLE       obligation "shall" under --house-style must (consistency within one instrument)
    MAY-NOT           "may not": prohibition, or absence of discretion? Ambiguous
    AND-OR            "and/or"
    DOUBLET           doublets and triplets ("null and void", "any and all", ...)
    REPS              "represents and warrants" (contested: flagged, never cut)
    ARCHAISM          herein / thereof / said (as an adjective) / such (as a pointer) / hereby ...
    LAWYERISM         pursuant to / prior to / in the event that / set forth in / for the avoidance of doubt
    INCLUDING         "including, but not limited to" / "including without limitation"
    EFFORTS           any efforts standard other than "reasonable efforts"
    PROVISO           "provided, however, that" / "provided that"
    NOTWITHSTANDING   "notwithstanding anything to the contrary" and friends
    NUMBERS           words-and-digits duplication ("thirty (30) days"), and mismatches ("ten (12)")
    BOILERPLATE       WHEREAS / NOW, THEREFORE / IN WITNESS WHEREOF / recital of consideration
    DEF-UNUSED        a defined term that is never used
    DEF-SHALLMEAN     "shall mean" in a definition
    DEF-HEREINAFTER   "(hereinafter referred to as the ...)"
    DEF-UNDEFINED     a capitalised term used like a defined term but never defined
    XREF-DANGLING     "Section 9.9" referenced, no such heading
    XREF-VAGUE        "the foregoing" / "as set forth above" / "the date first written above"
    TIME              "within N days of", "from X to Y", "by <date>", "midnight", "biweekly"
    GENDER            he or she / his/her
    SENTENCE          a sentence over --max-words words (default 60)
    CAPS              an all-capitals run: conspicuousness may be load-bearing (flag only)
    PLACEHOLDER       unfilled blanks ([insert ...], [__], TBD)

WHAT THIS DELIBERATELY DOES NOT DO
  It does not decide what a clause should say, does not touch substance, and does not know the
  governing law. Treat every `flag` as a question for the lawyer responsible for the document.

Exit codes: 0 no findings; 1 findings; 2 input unreadable; 5 bad usage.
Stdlib only. Reads .docx via zipfile + xml.etree (accepted-changes view: deletions excluded,
insertions included); .txt/.md as UTF-8 text.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import zipfile

__version__ = "1.0.1"

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


class InputError(Exception):
    pass


# ----------------------------------------------------------------------------- input


def read_docx(path: str) -> list[dict]:
    import xml.etree.ElementTree as ET
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml")
    except (zipfile.BadZipFile, KeyError, OSError) as e:
        raise InputError(f"not a readable .docx: {e}")
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        raise InputError(f"word/document.xml is not well-formed XML: {e}")
    paras: list[dict] = []
    for p in root.iter(W_NS + "p"):
        style = None
        pstyle = p.find(f"{W_NS}pPr/{W_NS}pStyle")
        if pstyle is not None:
            style = pstyle.get(W_NS + "val")
        parts: list[str] = []
        for node in p.iter():
            if node.tag == W_NS + "t":
                parts.append(node.text or "")
            elif node.tag == W_NS + "tab":
                parts.append("\t")
            elif node.tag in (W_NS + "br", W_NS + "cr"):
                parts.append(" ")
        text = re.sub(r"\s+", " ", "".join(parts)).strip()
        if text:
            paras.append({"text": text, "style": style})
    return paras


def paragraphs_from_text(raw: str) -> list[dict]:
    paras: list[dict] = []
    for line in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        t = line.strip()
        if not t:
            continue
        # Re-join hard-wrapped prose: a line that starts lowercase continues the previous
        # paragraph when that paragraph has not ended a sentence.
        if (paras and t[0].islower() and not re.search(r"[.;:!?]$", paras[-1]["text"])
                and not HEAD_NUM_RE.match(t)):
            paras[-1]["text"] += " " + t
        else:
            paras.append({"text": t, "style": None})
    return paras


def read_text(path: str) -> list[dict]:
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as fh:
            return paragraphs_from_text(fh.read())
    except OSError as e:
        raise InputError(str(e))


def read_any(path: str) -> list[dict]:
    if path.lower().endswith(".docx"):
        return read_docx(path)
    return read_text(path)


# ----------------------------------------------------------------------------- sections

HEAD_NUM_RE = re.compile(
    r"^\s*(?:(?:ARTICLE|Article|SECTION|Section|§)\s+)?"
    r"((?:\d+(?:\.\d+)*)|[IVXLC]+)(?![\w%$])\.?\)?\s*[-–—:.]?\s*(.*)$")
ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
SMALL_WORDS = {"of", "and", "for", "the", "to", "or", "in", "on", "by", "a", "an", "&"}


def roman_to_int(s: str) -> int | None:
    if not s or any(ch not in ROMAN for ch in s):
        return None
    total = 0
    for i, ch in enumerate(s):
        v = ROMAN[ch]
        if i + 1 < len(s) and ROMAN[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total


def heading_info(p: dict) -> tuple[str | None, str, bool]:
    """Return (section id or None, caption, is_heading_line)."""
    t = p["text"]
    style = (p.get("style") or "").lower()
    m = HEAD_NUM_RE.match(t)
    if style.startswith("heading") or style == "title":
        if m:
            return m.group(1), m.group(2).strip().rstrip(".:"), True
        return t[:60].rstrip(".:"), "", True
    if m:
        num, rest = m.group(1), m.group(2)
        if num.isalpha():
            num = str(roman_to_int(num) or num)
        if rest == "" or rest[:1].isupper() or rest[:1] in "\"“(":
            cap = re.match(r"^((?:[A-Z][\w'’-]*(?:\s+(?:of|and|for|the|to|or)\s+|\s+)?){1,8}?)[.:]", rest)
            if cap:
                return num, cap.group(1).strip(), True
            words = rest.rstrip(".:").split()
            titleish = (0 < len(words) <= 8 and len(rest) <= 60 and rest.count(".") <= 1
                        and all(w[:1].isupper() or w in SMALL_WORDS for w in words))
            if titleish:
                return num, rest.rstrip(".:"), True
            return num, "", False
    if len(t) <= 80 and len(t.split()) <= 12 and t.upper() == t and re.search(r"[A-Z]{3}", t):
        return t.rstrip(".:"), "", True
    return None, "", False


# ----------------------------------------------------------------------------- rails

RISK_RE = re.compile(
    r"\b(indemnif\w*|hold\s+harmless|defend|defen[cs]e|limitation\s+of\s+liability|"
    r"limit(?:s|ed)?\s+(?:its\s+|their\s+)?liability|liability\s+(?:is|shall\s+be)\s+limited|"
    r"consequential|incidental\s+damages|punitive|exemplary|special\s+damages|disclaim\w*|"
    r"warrant(?:y|ies)|as[\s-]is|merchantability|fitness\s+for\s+a\s+particular\s+purpose|"
    r"insurance|exculpat\w*|release[sd]?|releasing|waive[sd]?|waiver|liquidated\s+damages|"
    r"cap\s+on\s+liability|aggregate\s+liability)\b", re.I)
CAPS_RUN_RE = re.compile(r"(?:\b[A-Z][A-Z'’()-]+[,.;:]?\s+){7,}[A-Z][A-Z'’()-]+")
PRESCRIBED_RE = re.compile(
    r"\bU\.?C\.?C\.?\b|\bUniform\s+Commercial\s+Code\b|\bCiv(?:il)?\.?\s+Code\b|§\s*\d|"
    r"\b\d+\s+U\.?S\.?C\.?\b|\bC\.?F\.?R\.?\b|\bstatut\w+|\brequired\s+by\s+(?:applicable\s+)?law\b|"
    r"\bnotice\s+is\s+hereby\s+given\b|\bWARNING\b|\bNOTICE:")


def rails_for(text: str) -> list[str]:
    rails = []
    if RISK_RE.search(text):
        rails.append("risk-allocation")
    if CAPS_RUN_RE.search(text) or PRESCRIBED_RE.search(text):
        rails.append("prescribed-wording")
    return rails


RAIL_TEXT = {
    "risk-allocation": "risk allocation: courts construe these words strictly and against the "
                       "drafter, and the words can be the allocation -- propose alongside, do "
                       "not cut on this tool's authority",
    "prescribed-wording": "prescribed wording: a rule may require this text verbatim or "
                          "conspicuously -- keep it, and route any change to a lawyer",
}


# ----------------------------------------------------------------------------- vocab

PARTY_WORDS = {
    "party", "parties", "buyer", "seller", "purchaser", "vendor", "supplier", "customer",
    "client", "company", "corporation", "contractor", "subcontractor", "consultant", "employee",
    "employer", "executive", "licensor", "licensee", "lessor", "lessee", "landlord", "tenant",
    "borrower", "lender", "guarantor", "indemnitor", "indemnitee", "provider", "recipient",
    "distributor", "manufacturer", "agent", "principal", "owner", "operator", "franchisor",
    "franchisee", "assignor", "assignee", "grantor", "grantee", "trustee", "beneficiary",
    "investor", "issuer", "holder", "member", "manager", "shareholder", "stockholder",
    "partner", "bank", "insurer", "insured", "carrier", "shipper", "consignee", "sponsor",
    "institution", "university", "hospital", "physician", "patient", "government", "agency",
    "city", "county", "we", "you", "he", "she", "they",
}
NONPARTY_CAPS = {
    "Agreement", "Agreements", "Contract", "Section", "Sections", "Article", "Articles",
    "Exhibit", "Exhibits", "Schedule", "Schedules", "Annex", "Appendix", "Clause", "Term",
    "Effective", "Date", "Dates", "Closing", "Notice", "Notices", "Services", "Service",
    "Products", "Product", "Software", "Confidential", "Information", "Work", "Deliverables",
    "Deliverable", "Fees", "Fee", "Price", "Purchase", "Payment", "Payments", "Interest",
    "Title", "Risk", "Property", "Premises", "Equipment", "Goods", "Business", "Day", "Days",
    "Month", "Year", "Period", "Time", "Amount", "Amounts", "Invoice", "Invoices", "Statement",
    "Report", "Reports", "Order", "Orders", "Plan", "Policy", "License", "Licence", "Warranty",
    "Representation", "Claim", "Claims", "Loss", "Losses", "Damages", "Indemnity", "Insurance",
    "Law", "Laws", "Rules", "Regulations", "Code", "Act", "Court", "Dispute", "Arbitration",
    "Change", "Request", "Specification", "Specifications", "Documentation", "Data",
    "Materials", "Intellectual", "Rights", "Right", "Trademark", "Trademarks", "Patent",
    "Patents", "Copyright", "Copyrights", "Territory", "Quarter", "Milestone", "Milestones",
    "Project", "Site", "Delivery", "Shipment", "Each", "Any", "All", "No", "Nothing", "Neither",
    "None", "Either", "This", "These", "Those", "Such", "The", "A", "An", "If", "Unless",
    "Except", "Subject", "Upon", "After", "Before", "Within", "During", "In", "On", "At", "To",
    "For", "From", "With", "Without", "Where", "When", "Whether", "Provided", "However",
    "Notwithstanding", "Interest", "Rent", "Taxes", "Tax", "Costs", "Cost", "Expenses",
    "Expense", "Obligations", "Obligation", "Liability", "Liabilities", "Security", "Collateral",
    "Loan", "Note", "Shares", "Stock", "Units", "Option", "Options", "Benefits", "Salary",
    "Compensation", "Bonus", "Severance", "Termination", "Expiration", "Renewal", "Extension",
    "Assignment", "Amendment", "Waiver", "Force", "Majeure", "Governing", "Jurisdiction",
    "Venue", "Counterparts", "Headings", "Entire", "Survival", "Severability", "Remedies",
    "Remedy", "Default", "Event", "Events", "Breach", "Cure", "Schedule", "Timeline",
}
SKIP_SUBJECT_TAIL = {"which", "that", "who", "whom", "and", "or", "nor"}

PERFORMANCE_VERBS = (
    r"grants?|assigns?|conveys?|transfers?|releases?|waives?|acknowledges?|agrees?|appoints?|"
    r"accepts?|confirms?|consents?|delegates?|licenses?|sells?|terminates?|authori[sz]es?|"
    r"certifies|declares?|ratifies|irrevocably|unconditionally|and|expressly|also")

# --- shall family ---------------------------------------------------------------
SHALL_POLICY_RE = re.compile(
    r"\bshall\s+(?:not\s+)?(?:"
    r"be\s+(?:deemed|governed|construed|interpreted|binding|effective|conclusive|final|null|"
    r"void|valid|invalid|enforceable|unenforceable|subject|applicable|liable|limited|in\s+(?:full\s+)?"
    r"(?:force|effect)|the\s+(?:sole|exclusive)|due|payable|effective|a\b|an\b|the\b)|"
    r"mean|means|include|includes|constitute|constitutes|apply|applies|survive|survives|"
    r"terminate|terminates|expire|expires|commence|commences|govern|governs|prevail|prevails|"
    r"control|controls|remain|remains|continue|continues|have\s+the\s+meaning|take\s+effect|"
    r"take\s+place|occur|become|becomes|cease|ceases|accrue|accrues|bear\s+interest|"
    r"pass\b|vest\b|automatically)\b", re.I)
SHALL_DISC_RE = re.compile(
    r"\bshall\s+(?:be\s+entitled\s+to|have\s+the\s+(?:right|option|discretion|ability)\s+to|"
    r"be\s+(?:permitted|allowed|free|able)\s+to|be\s+at\s+liberty\s+to|"
    r"have\s+the\s+right,?\s+but\s+not\s+the\s+obligation,?\s+to)\b", re.I)
SHALL_NEG_RE = re.compile(
    r"\bshall\s+(?:not\s+be\s+(?:required|obligated|obliged|bound)\s+to|"
    r"have\s+no\s+(?:obligation|duty)\s+to|be\s+under\s+no\s+obligation\s+to|"
    r"not\s+be\s+entitled\s+to)\b", re.I)
SHALL_OBLIG_RE = re.compile(r"\bshall\s+be\s+(?:obligated|obliged|required|bound)\s+to\b", re.I)
SHALL_RESP_RE = re.compile(r"\bshall\s+be\s+responsible\s+for\s+(\w+ing)\b", re.I)
SHALL_PASSIVE_RE = re.compile(
    r"\bshall\s+(?:not\s+)?be\s+((?:\w+ed|\w+en|made|paid|sent|kept|held|built|put|set|done|"
    r"borne|sold|met|left|taken|shown|known|drawn|withdrawn|written|chosen|given|lost|won|"
    r"spent|brought|bought|sought|caught|taught|told|found|heard|read|led|fed|hit|cut|"
    r"shut|split|spread|let|cast|hung|dealt|meant|felt|kept|slept|bound|wound|ground|"
    r"struck|stuck|sworn|torn|worn|born|begun|sung|sunk|driven|risen|ridden|frozen|stolen|"
    r"broken|spoken|woken|forgotten|gotten|hidden|bitten|beaten|eaten|seen|been|undertaken|"
    r"overtaken|mistaken|forsaken|shaken|fallen|overridden|understood|withheld|upheld))\b"
    r"(?:\s+(?:in|on|at|to|by|from|for|with|within|no|not|prior|before|after|upon|under|"
    r"through|against|during|as|and|or|,|;|\.))?", re.I)
PASSIVE_EXCLUDE = {
    "deemed", "governed", "construed", "interpreted", "entitled", "permitted", "allowed",
    "obligated", "obliged", "required", "bound", "limited", "subject", "been", "liable",
}
BY_AGENT_RE = re.compile(r"\bby\s+(?:the\s+|an?\s+|its\s+|such\s+)?([A-Z][\w'’]*(?:\s+[A-Z][\w'’]*){0,3}|[a-z]+)")
THROAT_RE = re.compile(
    r"\b(?:covenants?\s+and\s+agrees?\s+(?:to|that)|undertakes?\s+to|is\s+obligated\s+to|"
    r"is\s+required\s+to|has\s+an?\s+obligation\s+to|have\s+an?\s+obligation\s+to|"
    r"agrees?\s+that\s+(?:it|he|she|they)\s+(?:shall|will)|agrees?\s+to\s+(?!the\b|a\b|an\b|"
    r"this\b|that\b|these\b|those\b|such\b|all\b|any\b|its\b|his\b|her\b|their\b|our\b|your\b|"
    r"be\b|do\b|so\b|it\b)[a-z]+)\b", re.I)
MAY_NOT_RE = re.compile(r"\bmay\s+not\b", re.I)
MUST_RE = re.compile(r"\bmust\b", re.I)

# --- phrase rules -------------------------------------------------------------------
AND_OR_RE = re.compile(r"\band/or\b", re.I)
DOUBLETS = [
    (r"\bnull\s+and\s+void\b", "void", "edit"),
    (r"\bany\s+and\s+all\b", "all (or any -- pick the one the sentence needs)", "edit"),
    (r"\beach\s+and\s+every\b", "each (or every)", "edit"),
    (r"\bfull\s+and\s+complete\b", "complete", "edit"),
    (r"\bdue\s+and\s+payable\b", "due", "edit"),
    (r"\bterms\s+and\s+conditions\b", "terms", "edit"),
    (r"\bsole\s+and\s+exclusive\b", "sole / exclusive -- they differ; pick the one you mean", "edit"),
    (r"\bfinal\s+and\s+binding\b", "final / binding -- say which effect you mean", "edit"),
    (r"\bfree\s+and\s+clear\b", "free of [liens, claims ...]", "edit"),
    (r"\bmade\s+and\s+entered\s+into\b", "is entered into / is dated", "edit"),
    (r"\bby\s+and\s+(?:between|among)\b", "between / among", "edit"),
    (r"\bcease\s+and\s+desist\b", "stop", "edit"),
    (r"\bfurnish\s+and\s+(?:supply|provide)\b", "provide", "edit"),
    (r"\btrue(?:,\s*correct,?)?\s+and\s+(?:correct|complete|accurate)\b", "accurate", "edit"),
    (r"\bin\s+full\s+force\s+and\s+effect\b", "in effect", "edit"),
    (r"\bpower\s+and\s+authority\b", "authority", "edit"),
    (r"\bover\s+and\s+above\b", "more than / in addition to", "edit"),
    (r"\bsave\s+and\s+except\b", "except", "edit"),
    (r"\bunless\s+and\s+until\b", "until / unless -- they differ; pick one", "edit"),
    (r"\bwhen\s+and\s+if\b|\bif\s+and\s+when\b|\bas\s+and\s+when\b", "if / when -- pick one", "edit"),
    (r"\border\s+and\s+direct\b", "direct", "edit"),
    (r"\bkind\s+and\s+nature\b", "kind", "edit"),
    (r"\balter\s+or\s+change\b|\bchange\s+or\s+alter\b", "change", "edit"),
    (r"\b(?:modify|modified)\s+or\s+amend(?:ed)?\b|\bamend(?:ed)?\s+or\s+modif(?:y|ied)\b", "amend", "edit"),
    (r"\bsuccessors\s+and\s+assigns\b",
     "keep if the successor/assign distinction is intended (a conveyancing term of art); "
     "otherwise 'successors'", "flag"),
    (r"\bright,\s*title,?\s+and\s+interest\b",
     "conveyancing formula -- keep for a transfer of ownership; otherwise 'rights'", "flag"),
    (r"\bindemnif(?:y|ies),?\s+defend,?\s+and\s+hold\s+harmless\b|"
     r"\bindemnif(?:y|ies)\s+and\s+hold\s+harmless\b|"
     r"\bdefend,?\s+indemnif(?:y|ies),?\s+and\s+hold\s+harmless\b|"
     r"\bhold\s+harmless\s+and\s+indemnif(?:y|ies)\b",
     "do not cut 'defend': in many jurisdictions the duty to defend is distinct and broader "
     "than indemnity (triggered by what is alleged, not by what is finally owed). Whether "
     "'hold harmless' adds anything to 'indemnify' is contested. Propose 'indemnify' (plus "
     "'defend' if a defence duty is intended) alongside the original, for a lawyer in the "
     "governing jurisdiction", "flag"),
]
REPS_RE = re.compile(r"\brepresents?\s+and\s+warrants?\b|\brepresentations?\s+and\s+warrant(?:y|ies)\b", re.I)
ARCHAISMS = [
    (r"\bherein(?:after|before|above|below)?\b", "in this agreement (or cite the section)"),
    (r"\bhereof\b", "of this agreement"),
    (r"\bhereto\b", "to this agreement"),
    (r"\bhereunder\b", "under this agreement"),
    (r"\bherewith\b", "with this agreement / enclosed"),
    (r"\bthereof\b", "of it / of that -- name the thing"),
    (r"\btherein\b", "in it -- name the thing"),
    (r"\bthereto\b", "to it"),
    (r"\bthereunder\b", "under it"),
    (r"\btherefor\b", "for it"),
    (r"\bthereby\b", "by that / so"),
    (r"\btherewith\b", "with it"),
    (r"\bwhereof\b", "of which"),
    (r"\bwherein\b", "in which / where"),
    (r"\bwhereby\b", "by which / under which"),
    (r"\baforesaid\b|\baforementioned\b|\babove-?mentioned\b|\babove-?referenced\b", "the / that -- name it"),
    (r"\bwitnesseth\b", "delete"),
    (r"\bforthwith\b", "immediately"),
    (r"\bwhatsoever\b|\bwhosoever\b|\bwheresoever\b", "delete"),
    (r"\bper\s+annum\b", "per year"),
    (r"\bmutatis\s+mutandis\b", "state the changes instead"),
    (r"\binter\s+alia\b", "among other things"),
    (r"\bab\s+initio\b", "from the start"),
    (r"\bipso\s+facto\b", "delete, or state the consequence"),
    (r"\bin\s+lieu\s+of\b", "instead of"),
]
SAID_RE = re.compile(
    r"\bsaid\s+(?=(?:[A-Z]|party|parties|agreement|notice|property|premises|goods|services|"
    r"amount|indemnity|period|date|time|sum|term|equipment|work|product|employee|contractor|"
    r"payment|price|fee|obligation|right|claim|lease|license|licence|loan))")
HEREBY_RE = re.compile(r"\bhereby\b(?!\s+(?:" + PERFORMANCE_VERBS + r")\b)", re.I)
SUCH_RE = re.compile(r"(?<![Aa]ny\s)(?<![Nn]o\s)(?<!each\s)(?<!every\s)(?<!all\s)(?<![Ii]n\s)(?<![Oo]f\s)"
                     r"(?<!for\s)(?<!with\s)(?<!to\s)(?<!at\s)(?<!and\s)(?<!or\s)\bsuch\s+(?!as\b)(\w+)"
                     r"(?!(?:\s+\w+){0,3}\s+as\b)")
LAWYERISMS = [
    (r"\bpursuant\s+to\b", "under", "edit"),
    (r"\bprior\s+to\b", "before", "edit"),
    (r"\bsubsequent\s+to\b", "after", "edit"),
    (r"\bin\s+the\s+event\s+that\b", "if", "edit"),
    (r"\bin\s+the\s+event\s+of\b", "if ... / on ...", "edit"),
    (r"\buntil\s+such\s+time\s+as\b", "until", "edit"),
    (r"\bat\s+such\s+time\s+as\b", "when", "edit"),
    (r"\bin\s+accordance\s+with\b", "under / as required by / in the manner stated in", "info"),
    (r"\bset\s+forth\s+(?:in|on|below|above|herein)\b", "stated in / in", "edit"),
    (r"\bfor\s+the\s+avoidance\s+of\s+doubt\b", "delete; if the clarification is needed, state it as a rule", "edit"),
    (r"\bit\s+is\s+(?:hereby\s+)?(?:understood\s+and\s+)?agreed\s+that\b", "delete the throat-clearing and state the rule", "edit"),
    (r"\bthe\s+parties\s+hereto\b", "the parties", "edit"),
    (r"\bof\s+any\s+kind\s+or\s+nature\b", "delete", "edit"),
    (r"\bas\s+the\s+case\s+may\s+be\b", "delete; restructure so each case is stated", "edit"),
    (r"\bat\s+any\s+time\s+and\s+from\s+time\s+to\s+time\b", "at any time", "edit"),
    (r"\bin\s+connection\s+with\b", "for / about / under -- name the relationship", "info"),
    (r"\bwith\s+respect\s+to\b|\bin\s+respect\s+of\b", "for / about / of", "info"),
    (r"\bon\s+the\s+part\s+of\b", "by", "edit"),
    (r"\bduring\s+the\s+term\s+hereof\b", "during the term", "edit"),
]
INCLUDING_RE = re.compile(
    r"\bincluding,?\s+(?:but\s+not\s+limited\s+to|without\s+limitation)\b|"
    r"\bincludes?,?\s+(?:but\s+(?:is|are)\s+not\s+limited\s+to|without\s+limitation)\b", re.I)
EFFORTS_RE = re.compile(
    r"\b(best|all\s+reasonable|reasonable\s+best|commercially\s+reasonable|good[- ]faith|"
    r"diligent|every|all|utmost|greatest|every\s+reasonable)\s+(efforts?|endeavou?rs)\b", re.I)
PROVISO_RE = re.compile(r"\bprovided,?\s+(?:however|further),?\s+that\b|\bprovided\s+that\b|;\s*provided\b", re.I)
NOTW_RE = re.compile(r"\bnotwithstanding\b", re.I)
BOILERPLATE = [
    (r"^\s*WHEREAS\b|\bWHEREAS,", "recitals: plain sentences under a 'Background' heading, no 'WHEREAS'"),
    (r"\bNOW,?\s+THEREFORE\b", "lead-in: 'The parties therefore agree as follows.'"),
    (r"\bIN\s+WITNESS\s+WHEREOF\b", "concluding clause: 'The parties are signing this agreement on the date stated in the introductory clause.'"),
    (r"\bWITNESSETH\b", "delete"),
    (r"\bKNOW\s+ALL\s+(?:MEN|PERSONS)\s+BY\s+THESE\s+PRESENTS\b", "delete"),
    (r"\bin\s+consideration\s+of\s+the\s+(?:mutual\s+)?(?:covenants|promises|premises|agreements)\b",
     "delete the recital of consideration -- reciting consideration does not create it"),
    (r"\bfor\s+(?:other\s+)?good\s+and\s+valuable\s+consideration\b", "delete the recital of consideration"),
    (r"\bthe\s+(?:receipt\s+and\s+)?sufficiency\s+of\s+which\s+(?:is|are)\s+(?:hereby\s+)?acknowledged\b", "delete"),
    (r"\bintending\s+to\s+be\s+legally\s+bound\b",
     "delete -- unless Pennsylvania law applies, where the phrase has statutory effect "
     "(Uniform Written Obligations Act) [canon attribution]"),
    (r"\bhave\s+(?:caused\s+this\s+agreement\s+to\s+be\s+)?executed\s+this\s+agreement\b|"
     r"\bhave\s+caused\s+this\s+agreement\s+to\s+be\s+executed\b",
     "'The parties are signing this agreement ...'"),
]
BOILERPLATE_RX = [(re.compile(p, re.I), s) for p, s in BOILERPLATE]
PARTIES_HERETO_RE = re.compile(r"\bthe\s+parties\s+hereto\b", re.I)


def _inside(span, claimed) -> bool:
    return any(a <= span[0] and span[1] <= b for a, b in claimed)


def claimed_spans(text: str) -> list[tuple[int, int]]:
    """Spans owned by a more specific rule, so the generic rules do not double-report them."""
    spans = []
    for rx in (DEF_HEREINAFTER_RE, DEF_SHALLMEAN_RE, PARTIES_HERETO_RE):
        spans += [m.span() for m in rx.finditer(text)]
    for rx, _ in BOILERPLATE_RX:
        spans += [m.span() for m in rx.finditer(text)]
    return spans
XREF_VAGUE_RE = re.compile(
    r"\b(?:as\s+)?(?:set\s+forth|described|provided|stated|specified)\s+(?:herein)?(?:above|below)\b|"
    r"\bthe\s+foregoing\b|\bhereinabove\b|\bhereinbelow\b|\bthe\s+date\s+first\s+(?:written|set\s+forth|stated)\s+above\b|"
    r"\bthe\s+date\s+first\s+above\s+written\b", re.I)
GENDER_RE = re.compile(r"\b(?:he\s+or\s+she|she\s+or\s+he|his\s+or\s+her|her\s+or\s+his|him\s+or\s+her|"
                       r"his/her|he/she|him/her|s/he|himself\s+or\s+herself)\b", re.I)
PLACEHOLDER_RE = re.compile(
    r"\[\s*(?:●|•|_+|insert[^\]]*|bracket[^\]]*|tbd|to\s+be\s+(?:determined|confirmed|agreed)|"
    r"name|date|amount|number|address|title)\s*\]|\bTBD\b|(?<![\w\[])_{3,}(?![\w\]])|\[\s*\]", re.I)
DEF_SHALLMEAN_RE = re.compile(r"[\"“][^\"”]{1,80}[\"”]\s+shall\s+(?:mean|include|have\s+the\s+meaning)\b", re.I)
DEF_HEREINAFTER_RE = re.compile(r"\(\s*hereinafter(?:\s+referred\s+to\s+as)?\s+(?:the\s+|an?\s+)?[\"“]", re.I)

# --- numbers ----------------------------------------------------------------------------
_SMALL = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
          "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
          "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
          "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
          "seventy": 70, "eighty": 80, "ninety": 90}
_MULT = {"thousand": 1000, "million": 10 ** 6, "billion": 10 ** 9}
NUM_WORD = r"(?:" + "|".join(list(_SMALL) + ["hundred"] + list(_MULT)) + r")"
UNIT = r"(?:percent|per\s+cent|dollars?|days?|years?|months?|weeks?|hours?|business\s+days?|calendar\s+days?)"
NUM_WORDS_FIRST_RE = re.compile(
    rf"\b({NUM_WORD}(?:[\s-]+(?:{NUM_WORD}|and))*)\s+(?:{UNIT}\s+)?\(\s*(?:US\s*)?\$?\s*(\d[\d,]*(?:\.\d+)?)\s*%?\s*\)", re.I)
NUM_DIGITS_FIRST_RE = re.compile(
    rf"(?:US\s*)?\$?\s*\b(\d[\d,]*(?:\.\d+)?)\s*%?\s*\(\s*({NUM_WORD}(?:[\s-]+(?:{NUM_WORD}|and))*)\s*(?:{UNIT})?\s*\)", re.I)


def words_to_number(s: str) -> int | None:
    total, cur, seen = 0, 0, False
    for tok in re.split(r"[\s-]+", s.lower()):
        if tok in ("and", ""):
            continue
        if tok in _SMALL:
            cur += _SMALL[tok]
            seen = True
        elif tok == "hundred":
            cur = (cur or 1) * 100
            seen = True
        elif tok in _MULT:
            total += (cur or 1) * _MULT[tok]
            cur = 0
            seen = True
        else:
            return None
    return total + cur if seen else None


# --- time ---------------------------------------------------------------------------------
DATE = r"(?:[A-Z][a-z]+\s+\d{1,2},\s+\d{4}|\d{1,2}\s+[A-Z][a-z]+\s+\d{4}|the\s+[A-Z]\w+(?:\s+[A-Z]\w+)*\s+Date)"
TIME_RULES = [
    (re.compile(r"\bwithin\s+(?:\w+\s+)?(?:\(\d+\)\s+)?(?:calendar\s+|business\s+)?days?\s+(?:of|from)\b", re.I),
     "state the direction and the trigger: 'no later than N days after [event]' (or 'before', if that is the meaning)", "edit"),
    (re.compile(rf"\bfrom\s+{DATE}\s+(?:to|until|through)\b"),
     "say whether the endpoints are included: 'from X through Y, inclusive' or 'beginning on X and ending on Y'", "flag"),
    (re.compile(rf"\bbetween\s+{DATE}\s+and\b"),
     "say whether the boundary dates are included", "flag"),
    (re.compile(rf"\bby\s+{DATE}\b"),
     "'no later than' -- 'by' leaves open whether the deadline day itself counts", "info"),
    (re.compile(r"\bmidnight\b", re.I), "which of the day's two midnights? 'midnight at the end of [date]' or 'at the beginning of [date]', with the time zone", "flag"),
    (re.compile(r"\bbi-?(?:weekly|monthly|annual(?:ly)?)\b", re.I),
     "ambiguous (twice per period, or every two periods): state the interval in words", "flag"),
]

# --- definitions / cross-references ------------------------------------------------------------
QUOTED_DEF_RE = re.compile(r"[\"“]([A-Z][A-Za-z0-9'’ -]{0,60}?)[\"”]\s+(?:means|shall\s+mean|has\s+the\s+meaning|includes|refers\s+to)\b")
PAREN_RE = re.compile(r"\(([^()]{1,200})\)")
QUOTED_TERM_RE = re.compile(r"[\"“]([A-Z][A-Za-z0-9'’ -]{0,60}?)[\"”]")
BARE_DEF_RE = re.compile(r"^([A-Z][A-Za-z0-9'’ -]{1,40}?)\s+(?:means|has\s+the\s+meaning)\b")
CAND_TERM_RE = re.compile(r"\b([A-Z][a-z]+(?:\s+(?:of|and|for|the)\s+[A-Z][a-z]+|\s+[A-Z][a-z]+){0,3})\b")
DETERMINERS = r"(?:the|a|an|any|each|all|such|no|every|this|that|these|those|its|their|his|her)"
CAP_DETS = {"The", "A", "An", "Any", "Each", "All", "Such", "No", "This", "That", "These", "Those",
            "Its", "Their", "Every", "Either", "Neither"}
STOP_TERMS = {
    "Section", "Sections", "Article", "Articles", "Exhibit", "Exhibits", "Schedule", "Schedules",
    "Annex", "Appendix", "Clause", "Clauses", "Paragraph", "Chapter", "Part", "Page", "State",
    "States", "United States", "Code", "Act", "Court", "Day", "Days", "Month", "Year",
    "January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
    "Saturday", "Sunday", "Inc", "LLC", "Ltd", "Corp", "Co", "Mr", "Ms", "Mrs", "Dr", "US",
    "USA", "UK", "EU", "A", "An", "The", "This", "That", "These", "Those", "If", "Any", "Each",
    "All", "No", "In", "On", "At", "To", "For", "From", "By", "With", "Without", "Upon", "Of",
    "And", "Or", "Not", "Nor", "But", "Except", "Unless", "Subject", "Provided", "However",
    "Notwithstanding", "Whereas", "Now", "Therefore", "Witnesseth", "Date",
}
XREF_SEP = r"(?:\s*,?\s*(?:and|or|through|to)\s+|\s*[,–-]\s*)"
XREF_SECTION_RE = re.compile(r"\bSections?\s+((?:\d+(?:\.\d+)*)(?:\s*\([a-z0-9]+\))*(?:" + XREF_SEP + r"(?:\d+(?:\.\d+)*)(?:\s*\([a-z0-9]+\))*)*)")
XREF_ARTICLE_RE = re.compile(r"\bArticles?\s+((?:[IVXLC]+|\d+)(?:" + XREF_SEP + r"(?:[IVXLC]+|\d+))*)")


def plural_pattern(term: str) -> str:
    e = re.escape(term)
    alts = [e, e + "s", e + "es"]
    if term.endswith("y"):
        alts.append(re.escape(term[:-1]) + "ies")
    return r"\b(?:" + "|".join(alts) + r")\b"


# ----------------------------------------------------------------------------- engine


def _finding(rule, severity, idx, text, suggest, why, span=None):
    return {"rule": rule, "severity": severity, "para": idx, "text": text, "suggest": suggest,
            "why": why, "pos": span[0] if span else 0}


def _snip(text: str, m, pad: int = 30) -> str:
    a, b = max(0, m.start() - pad), min(len(text), m.end() + pad)
    s = text[a:b]
    return ("…" if a else "") + s + ("…" if b < len(text) else "")


def _subject_before(text: str, idx: int) -> list[str]:
    start = max(text.rfind(c, 0, idx) for c in ".;:(") + 1
    words = text[start:idx].split()
    return words[-8:]


def _looks_like_party(words: list[str]) -> bool:
    for w in words:
        bare = w.strip(",'\"“”()")
        if not bare or bare.endswith(("'s", "’s")):
            continue
        if bare.lower() in PARTY_WORDS:
            return True
        if bare[:1].isupper() and bare not in NONPARTY_CAPS and not bare.isupper():
            return True
    return False


def rule_shall(idx, text, ctx):
    out = []
    hs = ctx["house_style"]
    claimed = ctx.get("claimed", [])
    for m in re.finditer(r"\bshall\b", text, re.I):
        tail = text[m.start():m.start() + 90]
        snip = _snip(text, m, 40)
        ctx["shall_total"] += 1
        if _inside(m.span(), claimed):
            ctx["shall_policy"] += 1       # a definition's "shall mean": DEF-SHALLMEAN owns it
            continue
        d = SHALL_DISC_RE.match(tail)
        if d:
            ctx["shall_disc"] += 1
            out.append(_finding("SHALL-DISC", "edit", idx, snip,
                                "'may' -- language of discretion",
                                "'shall be entitled to' and 'shall have the right to' grant a choice; "
                                "'shall' belongs only to a duty. Test: swap 'shall' for 'has a duty to' "
                                "and the sentence breaks.", m.span()))
            continue
        n = SHALL_NEG_RE.match(tail)
        if n:
            ctx["shall_disc"] += 1
            out.append(_finding("SHALL-NEG", "edit", idx, snip,
                                "'is not required to' (or 'is not entitled to')",
                                "A negated requirement is absence of a duty, which is policy or "
                                "discretion, not an obligation.", m.span()))
            continue
        o = SHALL_OBLIG_RE.match(tail)
        if o:
            ctx["shall_oblig"] += 1
            out.append(_finding("SHALL-OBLIG", "edit", idx, snip,
                                "'shall <verb>' -- drop 'be obligated/required to'",
                                "'shall' already imposes the duty; the extra words only add a second "
                                "way to read it.", m.span()))
            continue
        r = SHALL_RESP_RE.match(tail)
        if r:
            ctx["shall_oblig"] += 1
            out.append(_finding("SHALL-RESP", "info", idx, snip,
                                f"'shall {r.group(1)[:-3]}' -- state the duty with its verb",
                                "'responsible for doing X' is a duty to do X; say so directly, or if "
                                "the point is who bears a cost, say 'shall pay'.", m.span()))
            continue
        p = SHALL_POLICY_RE.match(tail)
        if p:
            ctx["shall_policy"] += 1
            verb = p.group(0)[len(m.group(0)):].strip()
            out.append(_finding("SHALL-POLICY", "edit", idx, snip,
                                f"present tense -- '{_present(verb)}' (language of policy)",
                                "This states a rule of the contract, not a party's duty. Test: 'shall' "
                                "is right only where 'has a duty to' fits; a term does not have a duty "
                                "to survive, an agreement has no duty to be governed.", m.span()))
            continue
        pv = SHALL_PASSIVE_RE.match(tail)
        if pv and pv.group(1).lower() not in PASSIVE_EXCLUDE:
            ctx["shall_passive"] += 1
            after = text[m.end():m.end() + 160]
            ag = BY_AGENT_RE.search(after)
            if ag:
                sug = f"active voice with the actor as subject: '{ag.group(1)} shall …'"
            else:
                sug = "active voice: name who must act -- 'The <party> shall …'"
            out.append(_finding("SHALL-PASSIVE", "edit", idx, snip, sug,
                                "A passive 'shall be done' leaves the duty with nobody; if no party is "
                                "named, it reads as policy and binds no one.", m.span()))
            continue
        subj = _subject_before(text, m.start())
        if subj and subj[-1].lower() in SKIP_SUBJECT_TAIL:
            ctx["shall_oblig"] += 1
            continue
        if subj and not _looks_like_party(subj):
            ctx["shall_policy"] += 1
            out.append(_finding("SHALL-POLICY", "edit", idx, snip,
                                "present tense -- the subject is not a party, so this is a rule "
                                "of the contract, not a duty",
                                "Apply the test: can the subject have a duty? '" + " ".join(subj[-4:]) +
                                " has a duty to …' does not make sense, so 'shall' is misused.", m.span()))
            continue
        ctx["shall_oblig"] += 1
        if hs == "must":
            out.append(_finding("HOUSE-STYLE", "info", idx, snip, "'must' (house style)",
                                "The house style uses 'must' for obligations; mixing 'shall' and 'must' "
                                "in one instrument invites an argument that they mean different things.",
                                m.span()))
    return out


def _present(verb_phrase: str) -> str:
    v = verb_phrase.lower().strip()
    neg = v.startswith("not ")
    if neg:
        v = v[4:]
    table = {
        "be deemed": "is deemed", "be governed": "is governed", "be construed": "is to be construed",
        "be interpreted": "is to be interpreted", "be binding": "binds / is binding",
        "be effective": "is effective", "be conclusive": "is conclusive", "be final": "is final",
        "be null": "is void", "be void": "is void", "be valid": "is valid", "be invalid": "is invalid",
        "be enforceable": "is enforceable", "be unenforceable": "is unenforceable",
        "be subject": "is subject", "be applicable": "applies", "be liable": "is liable",
        "be in full force": "is in effect", "be in force": "is in effect", "be in effect": "is in effect",
        "be due": "is due", "be payable": "is payable", "mean": "means", "include": "includes",
        "constitute": "constitutes", "apply": "applies", "survive": "survives",
        "terminate": "terminates", "expire": "expires", "commence": "begins", "govern": "governs",
        "prevail": "prevails", "control": "controls", "remain": "remains", "continue": "continues",
        "have the meaning": "has the meaning", "take effect": "takes effect", "take place": "takes place",
        "occur": "occurs", "become": "becomes", "cease": "ceases", "accrue": "accrues",
        "bear interest": "bears interest", "pass": "passes", "vest": "vests",
        "automatically": "automatically …", "be a": "is a", "be an": "is an", "be the": "is the",
    }
    for k in sorted(table, key=len, reverse=True):
        if v.startswith(k):
            rest = v[len(k):]
            res = table[k]
            if neg:
                res = res.replace("is ", "is not ", 1) if res.startswith("is ") else "does not " + k
            return res + rest
    if v.startswith("be "):
        return ("is not " if neg else "is ") + v[3:]
    return ("does not " if neg else "") + v


def rule_phrases(idx, text, ctx):
    out = []
    for m in MAY_NOT_RE.finditer(text):
        out.append(_finding("MAY-NOT", "edit", idx, _snip(text, m),
                            "'shall not' for a prohibition; 'is not entitled to' / 'is not required to' "
                            "if the point is absence of discretion",
                            "'may not' can mean a prohibition, the absence of a right, or a mere "
                            "possibility ('might not'), and a court has to pick.", m.span()))
    for m in AND_OR_RE.finditer(text):
        out.append(_finding("AND-OR", "edit", idx, _snip(text, m),
                            "'A or B, or both' / 'one or more of A and B' -- state the combination you mean",
                            "'and/or' has been read as 'and', as 'or', and as both.", m.span()))
    for pat, sug, sev in DOUBLETS:
        for m in re.finditer(pat, text, re.I):
            out.append(_finding("DOUBLET", sev, idx, _snip(text, m), sug,
                                "A doublet invites the argument that each word adds something "
                                "different; say the one thing you mean once.", m.span()))
    for m in REPS_RE.finditer(text):
        out.append(_finding("REPS", "flag", idx, _snip(text, m),
                            "MSCD: 'states' (one verb, one fact asserted). The bar: the doublet may "
                            "preserve distinct remedies. Follow MSCD in fresh drafting; flag, do not "
                            "change, in an instrument under negotiation or in force",
                            "Contested among transactional lawyers, so this is a decision, not an edit.",
                            m.span()))
    claimed = ctx.get("claimed", [])
    for pat, sug in ARCHAISMS:
        for m in re.finditer(pat, text, re.I):
            if _inside(m.span(), claimed):
                continue
            out.append(_finding("ARCHAISM", "edit", idx, _snip(text, m), sug,
                                "Archaisms make the reader translate; modern English says the same "
                                "thing without the detour.", m.span()))
    for m in SAID_RE.finditer(text):
        if _inside(m.span(), claimed):
            continue
        out.append(_finding("ARCHAISM", "edit", idx, _snip(text, m), "the / that",
                            "'said' as an adjective is a pointing word from pleading; 'the' or 'that' "
                            "does the job.", m.span()))
    for m in HEREBY_RE.finditer(text):
        if _inside(m.span(), claimed):
            continue
        out.append(_finding("ARCHAISM", "edit", idx, _snip(text, m),
                            "delete -- keep 'hereby' only in language of performance ('Acme hereby grants')",
                            "'hereby' earns its place only where the sentence performs an act by "
                            "being signed.", m.span()))
    for m in SUCH_RE.finditer(text):
        out.append(_finding("ARCHAISM", "info", idx, _snip(text, m), "'that' / 'the' / 'those'",
                            "'such' as a pointing word is lawyer dialect; 'that' reads naturally. "
                            "Verify: 'such … as' is a different, legitimate use.", m.span()))
    for pat, sug, sev in LAWYERISMS:
        for m in re.finditer(pat, text, re.I):
            out.append(_finding("LAWYERISM", sev, idx, _snip(text, m), sug,
                                "Plain words carry the same meaning with less reader effort.", m.span()))
    for m in INCLUDING_RE.finditer(text):
        out.append(_finding("INCLUDING", "edit", idx, _snip(text, m),
                            "'including' -- and where a restrictive reading would hurt, restructure so "
                            "the general class stands on its own",
                            "The tail is meant to defeat a restrictive reading (ejusdem generis), but "
                            "courts have read 'including' restrictively with and without it, and an "
                            "interpretation provision is no more reliable; omitting the tail once also "
                            "invites the inference that the omission meant something.", m.span()))
    for m in EFFORTS_RE.finditer(text):
        out.append(_finding("EFFORTS", "flag", idx, _snip(text, m),
                            "'reasonable efforts', defined once -- MSCD's position is that one standard "
                            "is enough and the gradations are not reliable",
                            "The bar disagrees about whether 'best' outranks 'commercially reasonable'; "
                            "courts have gone both ways. A lawyer's call, with the definition the fix.",
                            m.span()))
    for m in PROVISO_RE.finditer(text):
        out.append(_finding("PROVISO", "edit", idx, _snip(text, m),
                            "restate as what it is: a condition ('if', 'only if'), an exception "
                            "('except that', 'but'), or a separate sentence",
                            "A proviso can be read as a condition, an exception, or a new rule; "
                            "the word does not say which.", m.span()))
    for m in NOTW_RE.finditer(text):
        out.append(_finding("NOTWITHSTANDING", "flag", idx, _snip(text, m),
                            "state the exception where it applies ('except as provided in Section X', "
                            "'subject to Section Y') and delete the override",
                            "'notwithstanding anything to the contrary' creates a precedence puzzle: "
                            "two provisions each claim to win.", m.span()))
    for rx, sug in BOILERPLATE_RX:
        for m in rx.finditer(text):
            out.append(_finding("BOILERPLATE", "edit", idx, _snip(text, m), sug,
                                "Ritual words signal a contract without doing anything; the plain "
                                "version does the same job.", m.span()))
    for m in XREF_VAGUE_RE.finditer(text):
        out.append(_finding("XREF-VAGUE", "edit", idx, _snip(text, m),
                            "cite the section number (or the introductory clause)",
                            "'above' and 'the foregoing' move when the document is edited; a section "
                            "reference does not.", m.span()))
    for m in GENDER_RE.finditer(text):
        out.append(_finding("GENDER", "info", idx, _snip(text, m),
                            "repeat the defined term, use 'it' for an entity, or use 'they' if the "
                            "house style allows",
                            "Paired pronouns are clutter and still miss cases.", m.span()))
    for m in PLACEHOLDER_RE.finditer(text):
        out.append(_finding("PLACEHOLDER", "flag", idx, _snip(text, m), "fill it in or delete it",
                            "An unfilled blank in a signed document is a dispute.", m.span()))
    for m in DEF_SHALLMEAN_RE.finditer(text):
        out.append(_finding("DEF-SHALLMEAN", "edit", idx, _snip(text, m),
                            "'means' / 'includes' / 'has the meaning'",
                            "A definition is language of policy; 'shall' adds nothing and suggests a duty.",
                            m.span()))
    for m in DEF_HEREINAFTER_RE.finditer(text):
        out.append(_finding("DEF-HEREINAFTER", "edit", idx, _snip(text, m),
                            "(\"Term\") -- or (the \"Term\")",
                            "'hereinafter referred to as' is eight words doing the work of a pair of "
                            "quotation marks.", m.span()))
    for m in THROAT_RE.finditer(text):
        out.append(_finding("SHALL-THROAT", "edit", idx, _snip(text, m),
                            "'shall <verb>' -- the duty, stated once",
                            "'agrees to', 'covenants and agrees', 'undertakes to' restate the fact that "
                            "the contract is an agreement; the obligation is what the verb says.",
                            m.span()))
    if ctx["house_style"] == "shall":
        pass  # MSCD uses 'must' for conditions and non-party requirements; leave it alone.
    for rx, sug, sev in TIME_RULES:
        for m in rx.finditer(text):
            out.append(_finding("TIME", sev, idx, _snip(text, m), sug,
                                "Period and deadline wording is where otherwise careful drafts go "
                                "ambiguous: direction, trigger, and endpoints each need stating.",
                                m.span()))
    return out


def rule_numbers(idx, text, ctx):
    out = []
    for rx, wi, di in ((NUM_WORDS_FIRST_RE, 1, 2), (NUM_DIGITS_FIRST_RE, 2, 1)):
        for m in rx.finditer(text):
            w = words_to_number(m.group(wi))
            try:
                d = float(m.group(di).replace(",", ""))
            except ValueError:
                d = None
            if w is None or d is None:
                continue
            if abs(w - d) > 1e-9:
                out.append(_finding("NUMBERS", "flag", idx, _snip(text, m),
                                    f"the words say {w:,} and the digits say {m.group(di)} -- resolve "
                                    "which controls, then state the number once",
                                    "A words-and-digits mismatch is a live dispute; a loan document with "
                                    "the two disagreeing is the standard cautionary tale.", m.span()))
            else:
                out.append(_finding("NUMBERS", "edit", idx, _snip(text, m),
                                    "state the number once -- digits for amounts, percentages, times of "
                                    "day and most contract numbers; words for small numbers in prose if "
                                    "that is the house style; never both",
                                    "Saying it twice doubles the chance of an inconsistency and adds "
                                    "nothing when the two agree.", m.span()))
    return out


def rule_sentences(idx, text, ctx):
    out = []
    maxw = ctx["max_words"]
    protected = re.sub(r"\b(No|Inc|Ltd|Corp|Co|Mr|Ms|Mrs|Dr|U\.S|e\.g|i\.e|etc|vs|v)\.", r"\1<dot>", text)
    for s in re.split(r"(?<=[.;:!?])\s+(?=[A-Z(\"“])", protected):
        n = len(s.split())
        if n > maxw:
            out.append(_finding("SENTENCE", "info", idx, s[:70].replace("<dot>", ".") + "…",
                                f"{n} words -- split it, or tabulate the enumerated parts as (a), (b), (c)",
                                "Long sentences hide modifiers' scope; enumeration makes each element "
                                "and its scope visible.", (0, 0)))
    if len(text.split()) > 200 and text.count(";") >= 3:
        out.append(_finding("SENTENCE", "info", idx, text[:70] + "…",
                            "tabulate: one enumerated clause per element",
                            "A 200-word paragraph with semicolons is a list wearing a paragraph's "
                            "clothes.", (0, 0)))
    return out


def rule_caps(idx, text, ctx):
    out = []
    for m in CAPS_RUN_RE.finditer(text):
        out.append(_finding("CAPS", "flag", idx, _snip(text, m, 10),
                            "if a rule requires conspicuous text (UCC § 2-316 warranty disclaimers; "
                            "§ 1-201(b)(10) [canon attribution]), keep it conspicuous -- bold or "
                            "contrasting type can satisfy that and reads better than capitals, but do "
                            "not change it on this tool's authority",
                            "Capitals are hard to read and are also the traditional way to meet a "
                            "conspicuousness requirement; which of those is in play is a legal question.",
                            m.span()))
    return out


PARA_RULES = [rule_shall, rule_phrases, rule_numbers, rule_sentences, rule_caps]


def collect_definitions(paras: list[dict], known: set[str]) -> dict:
    """Return {term: [para indexes where it is defined]}."""
    defs: dict[str, list[int]] = {}
    for i, p in enumerate(paras):
        t = p["text"]
        for m in QUOTED_DEF_RE.finditer(t):
            defs.setdefault(m.group(1).strip(), []).append(i)
        for pm in PAREN_RE.finditer(t):
            for qm in QUOTED_TERM_RE.finditer(pm.group(1)):
                defs.setdefault(qm.group(1).strip(), []).append(i)
        bm = BARE_DEF_RE.match(t)
        if bm:
            defs.setdefault(bm.group(1).strip(), []).append(i)
    for k in known:
        defs.setdefault(k, [])
    return defs


def _is_defined(term: str, defs: dict) -> bool:
    if term in defs:
        return True
    for d in defs:
        if re.fullmatch(plural_pattern(d), term):
            return True
        if term in d.split() or (" " in d and term in d):
            return True
    return False


def doc_rules(paras: list[dict], ctx: dict) -> list[dict]:
    out = []
    body = "\n".join(p["text"] for p in paras)
    defs = collect_definitions(paras, ctx["known_terms"])
    ctx["definitions"] = sorted(defs)
    # DEF-UNUSED
    for term, sites in defs.items():
        if term in ctx["known_terms"] and not sites:
            continue
        total = len(re.findall(plural_pattern(term), body))
        if total - len(sites) <= 0:
            out.append(_finding("DEF-UNUSED", "edit", sites[0] if sites else 0, f"\"{term}\"",
                                "delete the definition, or use the term",
                                "A defined term that is never used is a promise the document does not "
                                "keep, and a reader will hunt for the use.", (0, 0)))
    # DEF-UNDEFINED
    counts: dict[str, int] = {}
    det_counts: dict[str, int] = {}
    first_use: dict[str, int] = {}
    for i, p in enumerate(paras):
        if ctx["heading_flags"][i]:
            continue
        t = p["text"]
        for m in CAND_TERM_RE.finditer(t):
            term, start = m.group(1), m.start()
            words = term.split()
            det = False
            if words[0] in CAP_DETS:
                if len(words) == 1:
                    continue
                term = " ".join(words[1:])
                start += len(words[0]) + 1
                det = True
            prefix = t[:start]
            if not det:
                if (start == 0 or re.search(r"[.!?:;]\s*$", prefix)
                        or prefix[-2:].strip() in ("\"", "“", "(", "'")):
                    continue
                det = bool(re.search(DETERMINERS + r"\s+$", prefix, re.I))
            if term in STOP_TERMS or term.split()[0] in STOP_TERMS:
                continue
            counts[term] = counts.get(term, 0) + 1
            first_use.setdefault(term, i)
            if det:
                det_counts[term] = det_counts.get(term, 0) + 1
    for term, n in sorted(counts.items()):
        if n >= 3 and det_counts.get(term, 0) >= 2 and not _is_defined(term, defs):
            if any(term != o and term in o and counts.get(o, 0) >= 2 for o in counts):
                continue
            out.append(_finding("DEF-UNDEFINED", "info", first_use[term], term,
                                f"define it once (\"{term}\" means …) or use lowercase if it is not a "
                                "defined term",
                                f"'{term}' is capitalised and used {n} times like a defined term, but "
                                "no definition was found.", (0, 0)))
    # XREF-DANGLING
    ids = ctx["section_ids"]
    if len(ids) >= 3:
        expanded = set()
        for s in ids:
            parts = s.split(".")
            for k in range(1, len(parts) + 1):
                expanded.add(".".join(parts[:k]))
        for i, p in enumerate(paras):
            t = p["text"]
            refs = []
            for m in XREF_SECTION_RE.finditer(t):
                refs += re.findall(r"\d+(?:\.\d+)*", m.group(1))
            for m in XREF_ARTICLE_RE.finditer(t):
                for r in re.findall(r"[IVXLC]+|\d+", m.group(1)):
                    refs.append(str(roman_to_int(r) or r) if r.isalpha() else r)
            for r in refs:
                if r not in expanded:
                    out.append(_finding("XREF-DANGLING", "flag", i, f"Section {r}",
                                        "point it at the section that exists, or add the section",
                                        "A cross-reference to a section that is not there is a drafting "
                                        "error a court cannot fix for you.", (0, 0)))
    return out


def lint_paragraphs(paras: list[dict], house_style="shall", max_words=60, known_terms=None) -> dict:
    ctx = {"house_style": house_style, "max_words": max_words, "known_terms": set(known_terms or []),
           "shall_total": 0, "shall_oblig": 0, "shall_policy": 0, "shall_disc": 0, "shall_passive": 0,
           "section_ids": [], "heading_flags": [], "sections": []}
    findings: list[dict] = []
    current = {"id": "", "caption": "(front matter)"}
    for i, p in enumerate(paras):
        sid, caption, is_head = heading_info(p)
        if sid is not None:
            current = {"id": sid, "caption": caption}
            ctx["section_ids"].append(sid)
        ctx["heading_flags"].append(is_head)
        ctx["sections"].append(dict(current))
        if is_head and len(p["text"]) <= 100 and not re.search(r"[.;:]\s+\S", p["text"]):
            continue   # a bare heading line gets no prose rules
        rails = rails_for(p["text"])
        ctx["claimed"] = claimed_spans(p["text"])
        for rule in PARA_RULES:
            for f in rule(i, p["text"], ctx):
                if rails and f["severity"] == "edit":
                    f["severity"] = "flag"
                f["rail"] = rails
                findings.append(f)
    for f in doc_rules(paras, ctx):
        f["rail"] = rails_for(paras[f["para"]]["text"]) if paras else []
        findings.append(f)
    for f in findings:
        sec = ctx["sections"][f["para"]] if f["para"] < len(ctx["sections"]) else {"id": "", "caption": ""}
        f["section"] = (sec["id"] + " " + sec["caption"]).strip() or "(front matter)"
    findings.sort(key=lambda f: (f["para"], f["pos"], f["rule"]))
    sev = {"edit": 0, "flag": 0, "info": 0}
    for f in findings:
        sev[f["severity"]] += 1
    return {
        "version": __version__,
        "paragraphs": len(paras),
        "sections": len(ctx["section_ids"]),
        "shall": {"total": ctx["shall_total"], "obligation": ctx["shall_oblig"],
                  "policy": ctx["shall_policy"], "discretion": ctx["shall_disc"],
                  "passive": ctx["shall_passive"]},
        "definitions": ctx["definitions"],
        "counts": sev,
        "findings": findings,
    }


# ----------------------------------------------------------------------------- output


def format_human(rep: dict, path: str) -> str:
    L = [f"MSCD lint {__version__} -- {path}",
         f"  paragraphs: {rep['paragraphs']} | sections: {rep['sections']} | defined terms: {len(rep['definitions'])}",
         f"  shall: {rep['shall']['total']} (obligation-looking {rep['shall']['obligation']}, policy "
         f"{rep['shall']['policy']}, discretion {rep['shall']['discretion']}, passive {rep['shall']['passive']})",
         f"  findings: {rep['counts']['edit']} edits, {rep['counts']['flag']} flags, {rep['counts']['info']} info"]
    if not rep["findings"]:
        L.append("  no findings")
        return "\n".join(L)
    last = None
    for f in rep["findings"]:
        if f["section"] != last:
            L.append(f"\n== {f['section']} ==")
            last = f["section"]
        tag = f["severity"].upper()
        if f.get("rail"):
            tag += " · " + " / ".join(RAIL_TEXT[r].split(":")[0] for r in f["rail"])
        L.append(f"  [{tag}] {f['rule']} (para {f['para'] + 1}): {f['text']}")
        L.append(f"      -> {f['suggest']}")
        L.append(f"      why: {f['why']}")
        if f.get("rail"):
            for r in f["rail"]:
                L.append(f"      rail: {RAIL_TEXT[r]}")
    return "\n".join(L)


def format_review(rep: dict, path: str) -> str:
    """A Smart Brevity cover note: the point first, why it matters, then the decisions."""
    fs = rep["findings"]
    by_rule: dict[str, int] = {}
    for f in fs:
        by_rule[f["rule"]] = by_rule.get(f["rule"], 0) + 1
    top = ", ".join(f"{k} ×{v}" for k, v in sorted(by_rule.items(), key=lambda kv: -kv[1])[:5])
    flags = [f for f in fs if f["severity"] == "flag"]
    edits = rep["counts"]["edit"]
    L = [f"**Redline cover note -- {os.path.basename(path)}**", ""]
    if not fs:
        L.append("**No findings.** The text passes every deterministic check; the judgment calls "
                 "(category of each sentence, defined-term hygiene) still need a read.")
        return "\n".join(L)
    L.append(f"**What changed:** {edits} edits proposed across {rep['sections']} sections "
             f"({top}). Every edit is a wording change, not a change of substance.")
    L.append("")
    L.append(f"**Why it matters:** {rep['shall']['total']} uses of 'shall', of which "
             f"{rep['shall']['policy']} state rules rather than duties and {rep['shall']['passive']} "
             "hide who must act. Each one is a question a court would otherwise answer.")
    if flags:
        L.append("")
        L.append(f"**Needs your call ({len(flags)}) -- flagged, not changed:**")
        for f in flags[:12]:
            L.append(f"- § {f['section']}: {f['rule']} -- {f['text'][:90]}")
        if len(flags) > 12:
            L.append(f"- … and {len(flags) - 12} more in the full report")
    dangling = [f for f in fs if f["rule"] == "XREF-DANGLING"]
    if dangling:
        L.append("")
        L.append("**Cross-references to fix:** " + ", ".join(sorted({f['text'] for f in dangling})))
    L.append("")
    L.append("**Go deeper:** run without --review for the section-by-section list with a suggested "
             "edit and the reason on every line.")
    return "\n".join(L)


# ----------------------------------------------------------------------------- self-test

FIXTURE = """\
MASTER SERVICES AGREEMENT

THIS MASTER SERVICES AGREEMENT (hereinafter referred to as the "Agreement") is made and entered into as of January 1, 2025, by and between Acme Industries, Inc., a Delaware corporation ("Acme"), and Zenith Consulting LLC ("Zenith").

WHEREAS, Acme wishes to obtain certain services; and WHEREAS, Zenith is willing to provide such services;

NOW, THEREFORE, in consideration of the mutual covenants herein contained and for good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties agree as follows:

1. Definitions.
"Deliverable" shall mean any work product described in a Statement of Work.
"Widget" means any product manufactured by Acme.
"Business Day" means a day other than a Saturday, Sunday, or public holiday in New York.

2. Services.
2.1 Zenith shall perform the Services described in each Statement of Work. Zenith covenants and agrees to use its best efforts to meet each milestone, and shall use reasonable efforts to retain key personnel.
2.2 The Services shall be performed by Zenith in accordance with the specifications set forth in the Statement of Work, including, but not limited to, the acceptance criteria.
2.3 Acme shall be entitled to reject any Deliverable within ten (10) Business Days of delivery; provided, however, that Acme shall not be required to give reasons.
2.4 Zenith shall deliver each report no later than 10 Business Days after the end of each month. Acme may reject a report that does not conform to the specifications in Exhibit A.
2.5 Acme hereby grants Zenith a non-exclusive license to use the Acme Marks during the Term.

3. Fees.
3.1 Acme shall pay Zenith a fee of thirty thousand dollars ($30,000) per month for the Services, and/or such other amount as the parties may agree in writing.
3.2 Invoices shall be paid within thirty (30) days of receipt. Any late payment shall bear interest at ten percent (12%) per annum.
3.3 Zenith may not assign this Agreement without Acme's prior written consent.
3.4 Zenith is hereby advised that a deposit of $5,000 (five thousand dollars) is due on signing.

4. Term and Termination.
4.1 This Agreement shall commence on the Effective Date and shall continue for two (2) years unless terminated earlier pursuant to Section 4.2.
4.2 Either party may terminate this Agreement in the event that the other party materially breaches it and fails to cure the breach within thirty (30) days after notice. Notwithstanding anything to the contrary herein, Sections 5, 6, and 9.9 shall survive termination.

5. Indemnification.
Zenith shall indemnify, defend, and hold harmless Acme from and against any and all claims, losses, and damages arising out of or relating to Zenith's breach of this Agreement, said indemnity to apply whether or not such claims are meritorious.

6. Warranties.
EXCEPT AS EXPRESSLY STATED IN THIS AGREEMENT, ZENITH DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Zenith represents and warrants that the Deliverables will conform to the specifications.

7. General.
7.1 This Agreement shall be governed by the laws of the State of New York. He or she who signs for a party confirms that he or she is authorized to do so.
7.2 Any notice must be in writing. The parties hereto agree that the foregoing constitutes the entire agreement and supersedes any and all prior agreements, and that nothing herein shall be deemed to create a partnership. For the avoidance of doubt, time is of the essence. Zenith shall deliver the final report by [insert date].

8. Miscellaneous.
8.1 If any provision of this Agreement is held to be invalid, illegal, or unenforceable in any respect by a court of competent jurisdiction, then such provision will be deemed modified to the minimum extent necessary to make it valid, legal, and enforceable, and the validity, legality, and enforceability of the remaining provisions of this Agreement will not in any way be affected or impaired, and the parties will negotiate in good faith to replace the offending provision with one that approximates its economic effect.
8.2 Zenith's obligations under this Section shall end on termination, and Zenith's liability shall be limited to the fees paid.
8.3 Acme shall not be liable for consequential damages.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.
"""


def _build_docx(path: str, lines: list[str]) -> None:
    """Write a minimal .docx (no python-docx): one w:p per line, Heading1 for numbered captions."""
    from xml.sax.saxutils import escape
    body = []
    for ln in lines:
        style = ""
        if re.match(r"^\d+\.\s+[A-Z]", ln) or ln.isupper() or (len(ln.split()) <= 3 and not ln.endswith(".")):
            style = '<w:pPr><w:pStyle w:val="Heading1"/></w:pPr>'
        body.append(f'<w:p>{style}<w:r><w:t xml:space="preserve">{escape(ln)}</w:t></w:r></w:p>')
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           '<w:body>' + "".join(body) + '</w:body></w:document>')
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
          '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '</Relationships>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", doc)


def self_test() -> int:
    failures: list[str] = []
    total = 0

    def check(name: str, cond: bool) -> None:
        nonlocal total
        total += 1
        if not cond:
            failures.append(name)

    paras = paragraphs_from_text(FIXTURE)
    rep = lint_paragraphs(paras)
    fs = rep["findings"]

    def para_of(needle: str) -> int:
        for i, p in enumerate(paras):
            if needle in p["text"]:
                return i
        return -1

    def hits(rule: str, needle: str | None = None, para: int | None = None):
        return [f for f in fs if f["rule"] == rule
                and (needle is None or needle in f["text"])
                and (para is None or f["para"] == para)]

    check("fixture parsed into paragraphs", rep["paragraphs"] >= 25)
    check("sections detected", rep["sections"] >= 8)
    # boilerplate / preamble
    check("BOILERPLATE: WHEREAS", bool(hits("BOILERPLATE", "WHEREAS")))
    check("BOILERPLATE: NOW, THEREFORE", bool(hits("BOILERPLATE", "NOW, THEREFORE")))
    check("BOILERPLATE: consideration recital", bool(hits("BOILERPLATE", "in consideration of the mutual covenants")))
    check("BOILERPLATE: receipt and sufficiency", bool(hits("BOILERPLATE", "sufficiency of which")))
    check("BOILERPLATE: IN WITNESS WHEREOF", bool(hits("BOILERPLATE", "IN WITNESS WHEREOF")))
    check("DOUBLET: made and entered into", bool(hits("DOUBLET", "made and entered into")))
    check("DOUBLET: by and between", bool(hits("DOUBLET", "by and between")))
    check("DEF-HEREINAFTER fires on the preamble", bool(hits("DEF-HEREINAFTER")))
    check("XREF-VAGUE: date first written above", bool(hits("XREF-VAGUE", "date first written above")))
    # archaisms, with the performance-language control
    check("ARCHAISM: herein", len(hits("ARCHAISM", "herein")) >= 2)
    check("ARCHAISM: 'said indemnity'", bool(hits("ARCHAISM", "said indemnity")))
    check("ARCHAISM: 'hereby advised' (not performance)", bool(hits("ARCHAISM", "hereby advised")))
    check("FP control: 'hereby acknowledged' inside the consideration recital is owned by BOILERPLATE", not hits("ARCHAISM", "hereby acknowledged"))
    check("FP control: 'hereby grants' is NOT flagged", not hits("ARCHAISM", "hereby grants"))
    check("ARCHAISM info: 'such claims' pointer", any(f["severity"] == "info" for f in hits("ARCHAISM", "such claims")))
    check("ARCHAISM: per annum", bool(hits("ARCHAISM", "per annum")))
    check("FP control: 'hereinafter' is owned by DEF-HEREINAFTER, not double-flagged", not hits("ARCHAISM", "hereinafter"))
    check("FP control: WHEREOF inside IN WITNESS WHEREOF is not an ARCHAISM", not hits("ARCHAISM", "WITNESS WHEREOF"))
    check("FP control: 'shall mean' is owned by DEF-SHALLMEAN, not SHALL-POLICY", not hits("SHALL-POLICY", "shall mean"))
    check("SHALL-POLICY: possessive subject ('Zenith's obligations ... shall end')", bool(hits("SHALL-POLICY", "shall end")))
    check("SHALL-POLICY: 'liability shall be limited'", bool(hits("SHALL-POLICY", "liability shall be limited")))
    check("SHALL-POLICY: party subject with a policy verb ('Acme shall not be liable')", bool(hits("SHALL-POLICY", "shall not be liable")))
    check("_present: not apply", _present("not apply") == "does not apply")
    check("_present: be a", _present("be a") == "is a")
    check("_present: not be liable", _present("not be liable") == "is not liable")
    check("_present: be adjusted (generic be)", _present("be adjusted") == "is adjusted")
    # definitions
    check("DEF-SHALLMEAN: Deliverable", bool(hits("DEF-SHALLMEAN", "Deliverable")))
    check("DEF-UNUSED: Widget", bool(hits("DEF-UNUSED", "Widget")))
    check("FP control: Business Day used in the plural is NOT unused", not hits("DEF-UNUSED", "Business Day"))
    check("FP control: Agreement (hereinafter form) is NOT unused", not hits("DEF-UNUSED", "Agreement"))
    und = {f["text"] for f in hits("DEF-UNDEFINED")}
    check("DEF-UNDEFINED: Statement of Work", "Statement of Work" in und)
    check("DEF-UNDEFINED: Services", "Services" in und)
    check("DEF-UNDEFINED is reported at the first use",
          any(f["para"] == para_of("described in a Statement of Work") for f in hits("DEF-UNDEFINED", "Statement of Work")))
    check("FP control: Delaware / New York are NOT reported undefined", not ({"Delaware", "New York", "State"} & und))
    check("FP control: Deliverables (plural of a defined term) is NOT undefined", "Deliverables" not in und)
    # shall family
    check("SHALL-THROAT: covenants and agrees to", bool(hits("SHALL-THROAT", "covenants and agrees")))
    check("EFFORTS: best efforts flagged", any(f["severity"] == "flag" for f in hits("EFFORTS", "best efforts")))
    check("FP control: reasonable efforts NOT flagged", not hits("EFFORTS", "reasonable efforts to retain"))
    pv = hits("SHALL-PASSIVE", "performed by Zenith")
    check("SHALL-PASSIVE: 'shall be performed by Zenith'", bool(pv))
    check("SHALL-PASSIVE names the actor from 'by Zenith'", bool(pv) and "Zenith shall" in pv[0]["suggest"])
    check("SHALL-PASSIVE: 'Invoices shall be paid' (no actor)", bool(hits("SHALL-PASSIVE", "Invoices shall be paid")))
    check("SHALL-DISC: shall be entitled to", bool(hits("SHALL-DISC", "entitled to")))
    check("SHALL-NEG: shall not be required to", bool(hits("SHALL-NEG", "not be required")))
    check("SHALL-POLICY: shall bear interest", bool(hits("SHALL-POLICY", "bear interest")))
    check("SHALL-POLICY: This Agreement shall commence", bool(hits("SHALL-POLICY", "shall commence")))
    check("SHALL-POLICY: shall continue", bool(hits("SHALL-POLICY", "shall continue")))
    check("SHALL-POLICY: shall survive", bool(hits("SHALL-POLICY", "shall survive")))
    check("SHALL-POLICY: shall be governed", bool(hits("SHALL-POLICY", "shall be governed")))
    check("SHALL-POLICY: shall be deemed", bool(hits("SHALL-POLICY", "shall be deemed")))
    check("FP control: 'Zenith shall perform' yields no shall finding",
          not [f for f in fs if f["rule"].startswith("SHALL") and "Zenith shall perform" in f["text"]])
    check("FP control: 'Acme shall pay' yields no shall finding",
          not [f for f in fs if f["rule"].startswith("SHALL") and "Acme shall pay" in f["text"]])
    check("shall stats: total equals the token count",
          rep["shall"]["total"] == len(re.findall(r"\bshall\b", FIXTURE, re.I)))
    # phrases
    check("LAWYERISM: in accordance with (info)", bool(hits("LAWYERISM", "in accordance with")))
    check("LAWYERISM: set forth in", bool(hits("LAWYERISM", "set forth in")))
    check("LAWYERISM: pursuant to", bool(hits("LAWYERISM", "pursuant to")))
    check("LAWYERISM: in the event that", bool(hits("LAWYERISM", "in the event that")))
    check("LAWYERISM: for the avoidance of doubt", bool(hits("LAWYERISM", "avoidance of doubt")))
    check("LAWYERISM: the parties hereto", bool(hits("LAWYERISM", "parties hereto")))
    check("INCLUDING: but not limited to", bool(hits("INCLUDING")))
    check("PROVISO: provided, however, that", bool(hits("PROVISO")))
    check("AND-OR", bool(hits("AND-OR")))
    check("MAY-NOT (and: a short numbered sentence is linted, not skipped as a heading)", bool(hits("MAY-NOT")))
    check("NOTWITHSTANDING", bool(hits("NOTWITHSTANDING")))
    check("REPS flagged (not edit)", any(f["severity"] == "flag" for f in hits("REPS")))
    check("GENDER: he or she", len(hits("GENDER")) >= 1)
    check("PLACEHOLDER: [insert date]", bool(hits("PLACEHOLDER", "insert date")))
    check("XREF-VAGUE: the foregoing", bool(hits("XREF-VAGUE", "the foregoing")))
    # numbers
    nums = hits("NUMBERS")
    check("NUMBERS: 'ten (10)' edit", any("ten (10)" in f["text"] and f["severity"] == "edit" for f in nums))
    check("NUMBERS: 'thirty thousand dollars ($30,000)' edit", any("$30,000" in f["text"] and f["severity"] == "edit" for f in nums))
    check("NUMBERS: 'two (2) years' edit", any("two (2)" in f["text"] and f["severity"] == "edit" for f in nums))
    check("NUMBERS: digits-first '$5,000 (five thousand dollars)' edit", any("five thousand" in f["text"] and f["severity"] == "edit" for f in nums))
    check("NUMBERS mismatch: 'ten percent (12%)' is a flag", any("12%" in f["text"] and f["severity"] == "flag" for f in nums))
    check("words_to_number: thirty thousand", words_to_number("thirty thousand") == 30000)
    check("words_to_number: one hundred twenty-five", words_to_number("one hundred twenty-five") == 125)
    check("words_to_number: two million three hundred thousand", words_to_number("two million three hundred thousand") == 2300000)
    check("words_to_number: nonsense is None", words_to_number("blue") is None)
    # time
    check("TIME: within ten (10) Business Days of", bool(hits("TIME", "Business Days of")))
    check("TIME: within thirty (30) days of receipt", bool(hits("TIME", "days of receipt")))
    check("FP control: 'within thirty (30) days after notice' is NOT a TIME finding", not hits("TIME", "days after notice"))
    # cross-references
    check("XREF-DANGLING: 9.9", bool(hits("XREF-DANGLING", "9.9")))
    check("FP control: Section 4.2 exists", not hits("XREF-DANGLING", "4.2"))
    check("FP control: Sections 5 and 6 exist", not hits("XREF-DANGLING", "Section 5") and not hits("XREF-DANGLING", "Section 6"))
    # rails
    p5 = para_of("indemnify, defend, and hold harmless")
    ind = hits("DOUBLET", "hold harmless", p5)
    check("DOUBLET: indemnify/defend/hold harmless found", bool(ind))
    check("…is a flag with the risk-allocation rail", bool(ind) and ind[0]["severity"] == "flag" and "risk-allocation" in ind[0]["rail"])
    check("…suggestion says do not cut 'defend'", bool(ind) and "defend" in ind[0]["suggest"])
    aa5 = hits("DOUBLET", "any and all", p5)
    check("'any and all' inside the indemnity is downgraded to flag", bool(aa5) and aa5[0]["severity"] == "flag")
    aa7 = hits("DOUBLET", "any and all", para_of("supersedes any and all"))
    check("'any and all' in a plain paragraph stays an edit", bool(aa7) and aa7[0]["severity"] == "edit")
    p6 = para_of("MERCHANTABILITY")
    caps = hits("CAPS", None, p6)
    check("CAPS flag on the disclaimer", bool(caps) and caps[0]["severity"] == "flag")
    check("disclaimer paragraph carries the prescribed-wording rail", bool(caps) and "prescribed-wording" in caps[0]["rail"])
    # clean paragraph and sections
    p24 = para_of("no later than 10 Business Days after")
    check("clean paragraph 2.4 has zero findings", not [f for f in fs if f["para"] == p24])
    check("findings in 2.3 carry section 2.3", all(f["section"].startswith("2.3") for f in fs if f["para"] == para_of("shall be entitled to reject")))
    check("findings in 5 carry the caption", any(f["section"] == "5 Indemnification" for f in fs if f["para"] == p5))
    # sentence length
    check("SENTENCE: the 8.1 wall of words", bool(hits("SENTENCE", None, para_of("competent jurisdiction"))))
    check("no SENTENCE finding on 2.4", not hits("SENTENCE", None, p24))
    # house style
    rep_must = lint_paragraphs(paras, house_style="must")
    check("--house-style must adds HOUSE-STYLE infos on obligation shalls",
          len([f for f in rep_must["findings"] if f["rule"] == "HOUSE-STYLE"]) >= 3)
    check("default style adds none", not hits("HOUSE-STYLE"))
    # known terms suppress DEF-UNDEFINED
    rep_known = lint_paragraphs(paras, known_terms={"Services", "Statement of Work"})
    check("--known-terms suppresses DEF-UNDEFINED", not [f for f in rep_known["findings"] if f["rule"] == "DEF-UNDEFINED" and f["text"] in ("Services", "Statement of Work")])
    rep_known2 = lint_paragraphs(paras, known_terms={"Escrow Agent"})
    check("a known term defined elsewhere and unused here is NOT reported DEF-UNUSED",
          not [f for f in rep_known2["findings"] if f["rule"] == "DEF-UNUSED" and "Escrow Agent" in f["text"]])
    # docx round trip
    with tempfile.TemporaryDirectory() as td:
        dp = os.path.join(td, "fixture.docx")
        _build_docx(dp, [ln for ln in FIXTURE.split("\n") if ln.strip()])
        dparas = read_docx(dp)
        drep = lint_paragraphs(dparas)
        key = lambda r: sorted((f["rule"], f["text"]) for f in r["findings"])
        check("docx: same paragraph count as text", len(dparas) == len(paras))
        check("docx: identical (rule, text) findings", key(drep) == key(rep))
        check("docx: Heading1 style recognised as a section", drep["sections"] >= 8)
        dp2 = os.path.join(td, "styled.docx")
        _build_docx(dp2, ["Background", "Acme wishes to obtain services.", "Payment", "Acme shall pay the fee."])
        check("docx: an unnumbered heading is a section by its style alone", lint_paragraphs(read_docx(dp2))["sections"] == 2)
        tp = os.path.join(td, "fixture.txt")
        with open(tp, "w", encoding="utf-8") as fh:
            fh.write(FIXTURE)
        import io, contextlib

        def quiet(argv):
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                rc = main(argv)
            return rc, out.getvalue(), err.getvalue()

        rc_find, _, _ = quiet([tp])
        check("exit 1 when there are findings", rc_find == 1)
        cp = os.path.join(td, "clean.txt")
        with open(cp, "w", encoding="utf-8") as fh:
            fh.write("1. Delivery.\nZenith shall deliver each report no later than 10 days after month end.\n")
        rc_clean, _, _ = quiet([cp])
        check("exit 0 on clean text", rc_clean == 0)
        rc_missing, _, err_missing = quiet([os.path.join(td, "missing.docx")])
        check("exit 2 on an unreadable path, with the reason on stderr", rc_missing == 2 and "ERROR" in err_missing)
        bad = os.path.join(td, "bad.docx")
        with open(bad, "wb") as fh:
            fh.write(b"not a zip")
        check("exit 2 on a non-zip .docx", quiet([bad])[0] == 2)
        check("exit 5 on no arguments", quiet([])[0] == 5)
        # --json and --review
        _, jtxt, _ = quiet([tp, "--json"])
        j = json.loads(jtxt)
        check("--json is valid JSON with the same finding count", j["counts"] == rep["counts"] and len(j["findings"]) == len(fs))
        _, rv, _ = quiet([tp, "--review"])
        check("--review leads with what changed and why it matters", "What changed" in rv and "Why it matters" in rv)
        check("--review lists the flags", "Needs your call" in rv and "hold harmless" in rv)
        check("--review names the dangling cross-reference", "9.9" in rv)

    print(f"self-test: {total - len(failures)}/{total} checks passed")
    for f in failures:
        print(f"  FAILED: {f}")
    return 0 if not failures else 1


# ----------------------------------------------------------------------------- main


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help=".docx, .txt or .md")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--review", action="store_true", help="Smart Brevity cover note instead of the full list")
    ap.add_argument("--house-style", choices=["shall", "must"], default="shall",
                    help="verb of obligation the instrument uses (MSCD: shall)")
    ap.add_argument("--max-words", type=int, default=60, help="sentence-length threshold (default 60)")
    ap.add_argument("--known-terms", help="file of terms (one per line) to treat as defined elsewhere")
    ap.add_argument("--self-test", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit:
        return 5
    if args.self_test:
        return self_test()
    if not args.file:
        print("provide a file (or --self-test)", file=sys.stderr)
        return 5
    known: set[str] = set()
    if args.known_terms:
        try:
            with open(args.known_terms, encoding="utf-8") as fh:
                known = {ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")}
        except OSError as e:
            print(f"ERROR: cannot read --known-terms: {e}", file=sys.stderr)
            return 2
    try:
        paras = read_any(args.file)
    except InputError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    if not paras:
        print("ERROR: no text found in the file", file=sys.stderr)
        return 2
    rep = lint_paragraphs(paras, args.house_style, args.max_words, known)
    if args.json:
        print(json.dumps({"file": args.file, **rep}, indent=2, ensure_ascii=False))
    elif args.review:
        print(format_review(rep, args.file))
    else:
        print(format_human(rep, args.file))
    return 1 if rep["findings"] else 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
