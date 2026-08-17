"""Local simulators for Oracle Fusion CM Advanced Criteria and Parse Rules.

Module 3 (advanced criteria) and Module 4 (parse rules) both let a user try a
rule against a sample string *locally* — the whole point of the app per the PRD:
"Simulating Advanced Criteria SQL and Parsing Regex locally avoids running
failed AutoRecon jobs in the Oracle SaaS environment."

The Python here is the reference implementation and is unit-tested against the
real baseline rules. The browser app mirrors this exact logic in JavaScript so
the sandbox works with no server; keeping one source of truth in Python lets us
prove the behavior against production data.

Two deliberate fidelity choices:
- String comparisons are CASE-SENSITIVE, matching Oracle's data comparison
  behavior ('BANK OF AMERICA, N.A.' will not match 'bank of america').
- Parse-rule literal characters are treated as delimiters/anchors and are NOT
  copied into the target field; only the captured groups populate
  RECON_REFERENCE. That mirrors how Oracle CM parse masks build the target.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


# ======================================================================
# Module 3 — Advanced Criteria SQL simulator
# ======================================================================
# Grammar (precedence low -> high): OR, AND, NOT, comparison, || concat.
# Operands are s.FIELD / t.FIELD references and single-quoted string literals.
# Comparisons supported: LIKE, NOT LIKE, =, <>, !=, IN (...). This is exactly
# the vocabulary the baseline Matching Rules file uses.

_KEYWORDS = {"AND", "OR", "NOT", "LIKE", "IN"}
_TOKEN_RE = re.compile(
    r"""
      (?P<ws>\s+)
    | (?P<str>'(?:[^']|'')*')          # single-quoted, '' escapes a quote
    | (?P<concat>\|\|)
    | (?P<op><>|!=|=)
    | (?P<punct>[(),])
    | (?P<ident>[A-Za-z_][A-Za-z0-9_.]*)
    """,
    re.VERBOSE,
)


class CriteriaError(Exception):
    pass


@dataclass
class _Tok:
    kind: str
    val: str


def _tokenize(s: str):
    toks, i = [], 0
    while i < len(s):
        m = _TOKEN_RE.match(s, i)
        if not m:
            raise CriteriaError(f"unexpected character {s[i]!r} at position {i}")
        i = m.end()
        kind = m.lastgroup
        if kind == "ws":
            continue
        val = m.group()
        if kind == "ident" and val.upper() in _KEYWORDS:
            toks.append(_Tok(val.upper(), val.upper()))
        else:
            toks.append(_Tok(kind, val))
    toks.append(_Tok("eof", ""))
    return toks


# AST node kinds are plain tuples: ("or", a, b), ("and", a, b), ("not", a),
# ("like", l, r, negated), ("cmp", op, l, r), ("in", l, [r...]), ("truthy", l)
# operands: ("field", name), ("str", value), ("concat", [parts])

class _Parser:
    def __init__(self, toks):
        self.toks = toks
        self.p = 0

    def peek(self):
        return self.toks[self.p]

    def next(self):
        t = self.toks[self.p]
        self.p += 1
        return t

    def expect(self, kind):
        t = self.next()
        if t.kind != kind:
            raise CriteriaError(f"expected {kind}, found {t.val or t.kind!r}")
        return t

    def parse(self):
        node = self.parse_or()
        if self.peek().kind != "eof":
            raise CriteriaError(f"unexpected trailing input near {self.peek().val!r}")
        return node

    def parse_or(self):
        left = self.parse_and()
        while self.peek().kind == "OR":
            self.next()
            left = ("or", left, self.parse_and())
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.peek().kind == "AND":
            self.next()
            left = ("and", left, self.parse_not())
        return left

    def parse_not(self):
        if self.peek().kind == "NOT":
            self.next()
            return ("not", self.parse_not())
        return self.parse_factor()

    def parse_factor(self):
        if self.peek().kind == "punct" and self.peek().val == "(":
            self.next()
            node = self.parse_or()
            t = self.next()
            if not (t.kind == "punct" and t.val == ")"):
                raise CriteriaError("unbalanced parenthesis: expected ')'")
            return node
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_operand()
        t = self.peek()
        if t.kind == "LIKE":
            self.next()
            return ("like", left, self.parse_operand(), False)
        if t.kind == "NOT":
            self.next()
            self.expect("LIKE")
            return ("like", left, self.parse_operand(), True)
        if t.kind == "op":
            self.next()
            return ("cmp", t.val, left, self.parse_operand())
        if t.kind == "IN":
            self.next()
            if not (self.peek().kind == "punct" and self.peek().val == "("):
                raise CriteriaError("expected '(' after IN")
            self.next()
            items = [self.parse_operand()]
            while self.peek().kind == "punct" and self.peek().val == ",":
                self.next()
                items.append(self.parse_operand())
            t2 = self.next()
            if not (t2.kind == "punct" and t2.val == ")"):
                raise CriteriaError("unbalanced parenthesis in IN list")
            return ("in", left, items)
        return ("truthy", left)

    def parse_operand(self):
        parts = [self.parse_atom()]
        while self.peek().kind == "concat":
            self.next()
            parts.append(self.parse_atom())
        if len(parts) == 1:
            return parts[0]
        return ("concat", parts)

    def parse_atom(self):
        t = self.next()
        if t.kind == "str":
            return ("str", _unquote(t.val))
        if t.kind == "ident":
            return ("field", t.val)
        if t.kind == "punct" and t.val == "(":
            inner = self.parse_operand()
            t2 = self.next()
            if not (t2.kind == "punct" and t2.val == ")"):
                raise CriteriaError("unbalanced parenthesis in operand")
            return inner
        raise CriteriaError(f"expected a field or string, found {t.val or t.kind!r}")


def _unquote(s: str) -> str:
    return s[1:-1].replace("''", "'")


def _like_to_regex(pattern: str) -> re.Pattern:
    out = ["^"]
    for ch in pattern:
        if ch == "%":
            out.append(".*")
        elif ch == "_":
            out.append(".")
        else:
            out.append(re.escape(ch))
    out.append("$")
    return re.compile("".join(out), re.DOTALL)  # case-sensitive, on purpose


def _fields_in(node, acc):
    tag = node[0]
    if tag == "field":
        acc.add(node[1])
    elif tag == "str":
        pass
    elif tag == "concat":
        for part in node[1]:
            _fields_in(part, acc)
    elif tag in ("or", "and"):
        _fields_in(node[1], acc)
        _fields_in(node[2], acc)
    elif tag == "not":
        _fields_in(node[1], acc)
    elif tag == "like":
        _fields_in(node[1], acc)
        _fields_in(node[2], acc)
    elif tag == "cmp":
        _fields_in(node[2], acc)
        _fields_in(node[3], acc)
    elif tag == "in":
        _fields_in(node[1], acc)
        for it in node[2]:
            _fields_in(it, acc)
    elif tag == "truthy":
        _fields_in(node[1], acc)


def _eval_operand(node, values):
    tag = node[0]
    if tag == "field":
        return str(values.get(node[1], ""))
    if tag == "str":
        return node[1]
    if tag == "concat":
        return "".join(_eval_operand(p, values) for p in node[1])
    raise CriteriaError(f"not an operand: {tag}")


def _eval(node, values):
    tag = node[0]
    if tag == "or":
        return _eval(node[1], values) or _eval(node[2], values)
    if tag == "and":
        return _eval(node[1], values) and _eval(node[2], values)
    if tag == "not":
        return not _eval(node[1], values)
    if tag == "like":
        left = _eval_operand(node[1], values)
        pat = _eval_operand(node[2], values)
        m = bool(_like_to_regex(pat).match(left))
        return (not m) if node[3] else m
    if tag == "cmp":
        op, left, right = node[1], _eval_operand(node[2], values), _eval_operand(node[3], values)
        if op == "=":
            return left == right
        return left != right  # <> or !=
    if tag == "in":
        left = _eval_operand(node[1], values)
        return any(left == _eval_operand(it, values) for it in node[2])
    if tag == "truthy":
        return bool(_eval_operand(node[1], values))
    raise CriteriaError(f"cannot evaluate node {tag}")


def parse_criteria(expression: str):
    """Parse an advanced-criteria expression; raise CriteriaError on bad syntax."""
    return _Parser(_tokenize(expression)).parse()


def fields_referenced(expression: str) -> list[str]:
    acc: set[str] = set()
    _fields_in(parse_criteria(expression), acc)
    return sorted(acc)


def simulate_criteria(expression: str, values: dict) -> dict:
    """Evaluate an advanced-criteria expression against sample field values.

    Returns {result, fields, error}. `values` maps field names (e.g.
    's.ADDENDA_TXT', 't.CPARTY_NAME') to sample strings.
    """
    try:
        ast = parse_criteria(expression)
    except CriteriaError as e:
        return {"result": None, "fields": [], "error": str(e)}
    acc: set[str] = set()
    _fields_in(ast, acc)
    try:
        result = _eval(ast, values)
    except CriteriaError as e:
        return {"result": None, "fields": sorted(acc), "error": str(e)}
    return {"result": bool(result), "fields": sorted(acc), "error": None}


# ======================================================================
# Module 4 — Bank string Parse Rule engine
# ======================================================================
# Supported parse-mask tokens, drawn from the baseline Parse Rules file:
#   (X~)      capture every character to the next literal (or end of field)
#   (a-b)     capture characters at absolute positions a..b (1-based, inclusive)
#   (N)/(NN)  capture exactly that many NUMERIC characters from the cursor
#   (A)/(AA)  capture exactly that many ALPHABETIC characters
#   (X)/(XX)  capture exactly that many ANY characters
# Literal text between tokens is an anchor/delimiter: it must be present and is
# consumed, but is NOT copied into the target. Only captured groups populate the
# RECON_REFERENCE target. A cascade of leading-zero masks (0000000000(N),
# 000000000(NN), ...) is how the baseline strips leading zeros: exactly one
# ladder rule matches a given fixed-width value.

_PAREN_RE = re.compile(r"\(([^)]*)\)")
_POS_RE = re.compile(r"^(\d+)-(\d+)$")
_CLASS_RE = re.compile(r"^[NAX]+$")


@dataclass
class _Seg:
    kind: str            # 'lit' | 'all' | 'pos' | 'class' | 'unknown'
    text: str = ""       # literal text, or raw token
    a: int = 0
    b: int = 0
    cls: str = ""        # for 'class': the per-position class letters


def _lex_rule(rule: str) -> list[_Seg]:
    segs: list[_Seg] = []
    pos = 0
    for m in _PAREN_RE.finditer(rule):
        if m.start() > pos:
            segs.append(_Seg("lit", rule[pos:m.start()]))
        inner = m.group(1).strip()
        if inner == "X~":
            segs.append(_Seg("all", "(X~)"))
        elif _POS_RE.match(inner):
            g = _POS_RE.match(inner)
            segs.append(_Seg("pos", f"({inner})", a=int(g.group(1)), b=int(g.group(2))))
        elif _CLASS_RE.match(inner):
            segs.append(_Seg("class", f"({inner})", cls=inner))
        else:
            segs.append(_Seg("unknown", f"({inner})"))
        pos = m.end()
    if pos < len(rule):
        segs.append(_Seg("lit", rule[pos:]))
    return segs


_CLASS_TEST = {
    "N": str.isdigit,
    "A": str.isalpha,
    "X": lambda c: True,
}


def simulate_parse_rule(rule: str, source: str) -> dict:
    """Apply an Oracle CM parse mask to a source string.

    Returns {output, matched, steps, error}. `output` is what would populate the
    target field (RECON_REFERENCE); `steps` is a human-readable trace.
    """
    if not rule.strip():
        return {"output": "", "matched": False, "steps": [], "error": "empty parse rule"}
    segs = _lex_rule(rule)
    if any(s.kind == "unknown" for s in segs):
        bad = ", ".join(s.text for s in segs if s.kind == "unknown")
        return {"output": "", "matched": False, "steps": [],
                "error": f"unsupported parse token(s): {bad}"}

    out_parts: list[str] = []
    steps: list[str] = []
    cur = 0
    n = len(source)

    for idx, seg in enumerate(segs):
        nxt = segs[idx + 1] if idx + 1 < len(segs) else None
        if seg.kind == "lit":
            if nxt and nxt.kind == "all":
                # literal is a PREFIX delimiter for the following capture-all
                found = source.find(seg.text, cur)
                if found < 0:
                    return {"output": "", "matched": False, "steps": steps,
                            "error": f"delimiter {seg.text!r} not found in source"}
                cur = found + len(seg.text)
                steps.append(f"anchor {seg.text!r} → cursor at {cur}")
            else:
                # literal must match at the cursor exactly (mask / zero-ladder)
                if source[cur:cur + len(seg.text)] != seg.text:
                    return {"output": "", "matched": False, "steps": steps,
                            "error": f"literal {seg.text!r} does not match "
                                     f"source at position {cur + 1}"}
                cur += len(seg.text)
                steps.append(f"literal {seg.text!r} consumed → cursor at {cur}")
        elif seg.kind == "all":
            if nxt and nxt.kind == "lit":
                stop = source.find(nxt.text, cur)
                end = stop if stop >= 0 else n
            else:
                end = n
            captured = source[cur:end]
            out_parts.append(captured)
            cur = end
            steps.append(f"(X~) captured {captured!r}")
        elif seg.kind == "pos":
            captured = source[seg.a - 1:seg.b]
            out_parts.append(captured)
            cur = max(cur, seg.b)
            note = "" if seg.b <= n else " (source shorter than position — truncated)"
            steps.append(f"({seg.a}-{seg.b}) captured {captured!r}{note}")
        elif seg.kind == "class":
            count = len(seg.cls)
            chunk = source[cur:cur + count]
            if len(chunk) < count:
                return {"output": "", "matched": False, "steps": steps,
                        "error": f"({seg.cls}) needs {count} chars but only "
                                 f"{len(chunk)} remain at position {cur + 1}"}
            for c, letter in zip(chunk, seg.cls):
                if not _CLASS_TEST[letter](c):
                    return {"output": "", "matched": False, "steps": steps,
                            "error": f"({seg.cls}) expected {letter}-class char but "
                                     f"found {c!r} at position {cur + 1}"}
            out_parts.append(chunk)
            cur += count
            steps.append(f"({seg.cls}) captured {chunk!r}")

    output = "".join(out_parts)
    if not out_parts:
        steps.append("no capture group — target would be empty")
    return {"output": output, "matched": True, "steps": steps, "error": None}
