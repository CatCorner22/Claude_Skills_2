#!/usr/bin/env python3
"""Measure before you read, and keep a token ledger for a multi-step task.

Usage:
  token_ledger.py estimate PATH [PATH ...] [--max 20000] [--glob '*.md'] [--json]
      Size files (or every file under a directory) in lines, characters and estimated tokens,
      largest first, and flag anything over --max estimated tokens with a cheaper way to read it.
  token_ledger.py log LEDGER --task NAME --tokens N [--phase P] [--kind subagent|inline|tool] [--ms M] [--note TEXT]
      Append one record to a JSON-lines ledger (create it if missing).
  token_ledger.py report LEDGER [--budget N] [--json]
      Totals by phase and kind, the largest entries, repeated task names (possible repeated work),
      and budget use with plain flags.
  token_ledger.py --self-test
      Offline checks; writes only to a temporary directory.

ESTIMATES, NOT MEASUREMENTS
  Tokens are estimated as characters / 3.5, rounded up. Real tokenizers vary by text type (code,
  prose, non-Latin scripts); use the estimate to compare files and to decide how to read them, not
  as a bill. Ledger entries are whatever you log: the usage figures a task notification reports
  for a subagent are the best source.

WHAT THIS DELIBERATELY DOES NOT DO
  It never reads file contents into its output, never sends anything anywhere, and never deletes a
  ledger. Binary files are sized by bytes and flagged rather than read.

Exit codes: 0 ok; 2 unreadable input; 5 bad usage.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import math
import os
import sys
import tempfile
import time

__version__ = "1.0.0"
CHARS_PER_TOKEN = 3.5
DEFAULT_MAX = 20000          # estimated tokens; above this, read a slice instead of the whole file
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", ".mypy_cache", ".pytest_cache"}
KINDS = ("subagent", "inline", "tool")


class InputError(Exception):
    pass


# ----------------------------------------------------------------------------- estimate

def est_tokens(chars: int) -> int:
    return math.ceil(chars / CHARS_PER_TOKEN) if chars > 0 else 0


def _is_binary(path: str) -> bool:
    try:
        with open(path, "rb") as fh:
            return b"\0" in fh.read(4096)
    except OSError:
        return False


def size_file(path: str) -> dict:
    if _is_binary(path):
        n = os.path.getsize(path)
        return {"path": path, "binary": True, "bytes": n, "lines": None, "chars": None, "tokens": None}
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    return {"path": path, "binary": False, "bytes": os.path.getsize(path), "lines": text.count("\n") + (0 if text.endswith("\n") or not text else 1),
            "chars": len(text), "tokens": est_tokens(len(text))}


def walk(paths: list[str], pattern: str | None = None) -> list[str]:
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
                for f in sorted(files):
                    if pattern is None or fnmatch.fnmatch(f, pattern):
                        out.append(os.path.join(root, f))
        elif os.path.isfile(p):
            if pattern is None or fnmatch.fnmatch(os.path.basename(p), pattern):
                out.append(p)
        else:
            raise InputError(f"no such file or directory: {p}")
    return out


def advice_for(rec: dict, max_tokens: int) -> str:
    if rec["binary"]:
        return "binary: do not read as text; use a purpose-built tool"
    if rec["tokens"] > max_tokens:
        lines = rec["lines"] or 0
        return (f"over budget: grep for what you need, then read a slice (e.g. lines 1-{min(lines, 200)}), "
                f"or delegate the read to a subagent that returns a summary")
    return ""


def estimate(paths: list[str], max_tokens: int = DEFAULT_MAX, pattern: str | None = None) -> dict:
    files = walk(paths, pattern)
    recs = [size_file(f) for f in files]
    for r in recs:
        r["advice"] = advice_for(r, max_tokens)
    recs.sort(key=lambda r: (r["tokens"] is None, -(r["tokens"] or 0), r["path"]))
    total = sum(r["tokens"] or 0 for r in recs)
    return {"max": max_tokens, "files": recs, "total_tokens": total,
            "over": [r["path"] for r in recs if r["advice"].startswith("over")],
            "binary": [r["path"] for r in recs if r["binary"]]}


def render_estimate(e: dict) -> str:
    lines = [f"{'est.tokens':>10}  {'lines':>7}  path"]
    for r in e["files"]:
        tok = "binary" if r["binary"] else f"{r['tokens']:,}"
        ln = "" if r["lines"] is None else f"{r['lines']:,}"
        lines.append(f"{tok:>10}  {ln:>7}  {r['path']}" + (f"   <- {r['advice']}" if r["advice"] else ""))
    lines.append(f"total ≈ {e['total_tokens']:,} tokens across {len(e['files'])} files "
                 f"({len(e['over'])} over {e['max']:,}; estimate = characters / {CHARS_PER_TOKEN})")
    return "\n".join(lines)


# ----------------------------------------------------------------------------- ledger

def log_entry(ledger: str, task: str, tokens: int, phase: str = "", kind: str = "inline",
              ms: int | None = None, note: str = "", now: float | None = None) -> dict:
    if not task.strip():
        raise InputError("--task must not be empty")
    if tokens < 0:
        raise InputError("--tokens must be zero or more")
    if kind not in KINDS:
        raise InputError(f"--kind must be one of {', '.join(KINDS)}")
    rec = {"ts": round(now if now is not None else time.time(), 3), "task": task.strip(), "phase": phase.strip() or "unphased",
           "kind": kind, "tokens": int(tokens), "ms": ms, "note": note}
    with open(ledger, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def read_ledger(ledger: str) -> list[dict]:
    try:
        with open(ledger, encoding="utf-8") as fh:
            raw = fh.read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read ledger {ledger}: {e}")
    out = []
    for i, line in enumerate(raw, 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            raise InputError(f"{ledger}:{i}: not a JSON record")
        if not isinstance(rec, dict) or "task" not in rec or not isinstance(rec.get("tokens"), int):
            raise InputError(f"{ledger}:{i}: record needs 'task' and integer 'tokens'")
        out.append(rec)
    return out


def report(records: list[dict], budget: int | None = None) -> dict:
    total = sum(r["tokens"] for r in records)
    by_phase, by_kind, by_task = {}, {}, {}
    for r in records:
        by_phase[r.get("phase", "unphased")] = by_phase.get(r.get("phase", "unphased"), 0) + r["tokens"]
        by_kind[r.get("kind", "inline")] = by_kind.get(r.get("kind", "inline"), 0) + r["tokens"]
        by_task.setdefault(r["task"].lower(), []).append(r)
    top = sorted(records, key=lambda r: -r["tokens"])[:5]
    repeated = sorted([k for k, v in by_task.items() if len(v) > 1])
    flags = []
    if budget:
        if total > budget:
            flags.append(f"over budget: {total:,} of {budget:,} ({total / budget:.0%})")
        elif total > 0.8 * budget:
            flags.append(f"near budget: {total:,} of {budget:,} ({total / budget:.0%}); re-plan before the next phase")
    if total and top and top[0]["tokens"] > 0.25 * total and len(records) > 1:
        flags.append(f"one entry is {top[0]['tokens'] / total:.0%} of the spend: '{top[0]['task']}' — was its brief or scope larger than needed?")
    if repeated:
        flags.append("repeated task names (possible repeated work): " + ", ".join(repeated))
    return {"entries": len(records), "total_tokens": total, "budget": budget,
            "by_phase": dict(sorted(by_phase.items(), key=lambda kv: -kv[1])),
            "by_kind": dict(sorted(by_kind.items(), key=lambda kv: -kv[1])),
            "top": [{"task": r["task"], "tokens": r["tokens"], "phase": r.get("phase")} for r in top],
            "repeated": repeated, "flags": flags}


def render_report(rep: dict) -> str:
    L = [f"ledger: {rep['entries']} entries, {rep['total_tokens']:,} tokens"
         + (f" of a {rep['budget']:,} budget" if rep["budget"] else "")]
    L.append("  by phase: " + "; ".join(f"{k} {v:,}" for k, v in rep["by_phase"].items()))
    L.append("  by kind:  " + "; ".join(f"{k} {v:,}" for k, v in rep["by_kind"].items()))
    L.append("  largest:  " + "; ".join(f"{t['task']} {t['tokens']:,}" for t in rep["top"]))
    for f in rep["flags"]:
        L.append(f"  FLAG: {f}")
    if not rep["flags"]:
        L.append("  no flags")
    return "\n".join(L)


# ----------------------------------------------------------------------------- self-test

def self_test() -> int:
    passed = failed = 0

    def check(cond, label):
        nonlocal passed, failed
        if cond:
            passed += 1
        else:
            failed += 1
            print(f"FAIL: {label}")

    def raises(fn, exc=InputError):
        try:
            fn()
        except exc:
            return True
        except Exception:
            return False
        return False

    check(est_tokens(0) == 0 and est_tokens(1) == 1 and est_tokens(7) == 2 and est_tokens(8) == 3, "estimate rounds characters/3.5 up")
    with tempfile.TemporaryDirectory() as td:
        small = os.path.join(td, "small.md")
        big = os.path.join(td, "big.txt")
        sub = os.path.join(td, "sub")
        os.makedirs(os.path.join(sub, "__pycache__"))
        open(small, "w").write("one\ntwo\n")
        open(os.path.join(td, "aa_first.md"), "w").write("z")      # sorts first by name, smallest by size
        open(big, "w").write(("x" * 99 + "\n") * 2000)                 # 200,000 chars
        open(os.path.join(sub, "note.md"), "w").write("abc")             # no trailing newline
        open(os.path.join(sub, "__pycache__", "skip.md"), "w").write("y" * 10)
        with open(os.path.join(sub, "img.bin"), "wb") as fh:
            fh.write(b"\x89PNG\0\0data")
        e = estimate([td])
        paths = [os.path.basename(r["path"]) for r in e["files"]]
        check("skip.md" not in paths, "cache directories are skipped")
        check(paths[0] == "big.txt", "largest file listed first")
        toks = [r["tokens"] for r in e["files"] if not r["binary"]]
        check(toks == sorted(toks, reverse=True) and paths[-2] != "big.txt", "text files are ordered by size, not by name")
        bigrec = e["files"][0]
        check(bigrec["chars"] == 200000 and bigrec["tokens"] == 57143 and bigrec["lines"] == 2000, "big file sized correctly")
        check(bigrec["advice"].startswith("over budget") and "slice" in bigrec["advice"], "a file over the limit gets slice advice")
        check(e["over"] == [bigrec["path"]], "only the big file is over the default limit")
        note = [r for r in e["files"] if r["path"].endswith("note.md")][0]
        check(note["lines"] == 1 and note["chars"] == 3, "a last line without a newline still counts")
        binrec = [r for r in e["files"] if r["binary"]]
        check(len(binrec) == 1 and binrec[0]["tokens"] is None and "binary" in binrec[0]["advice"], "binary files are flagged, not read")
        check(e["total_tokens"] == sum(r["tokens"] or 0 for r in e["files"]), "total is the sum of text files")
        e2 = estimate([td], max_tokens=10 ** 9)
        check(e2["over"] == [], "--max raises the limit")
        e3 = estimate([td], pattern="*.md")
        check(sorted(os.path.basename(r["path"]) for r in e3["files"]) == ["aa_first.md", "note.md", "small.md"], "--glob filters by file name")
        check(raises(lambda: estimate([os.path.join(td, "missing")])), "a missing path is an input error")
        text = render_estimate(e)
        check("<- over budget" in text and "total ≈" in text and "x" * 20 not in text, "rendered estimate never includes file contents")

        led = os.path.join(td, "ledger.jsonl")
        log_entry(led, "research: vendors", 120000, phase="research", kind="subagent", ms=600000, now=1.0)
        log_entry(led, "Research: Vendors", 90000, phase="research", kind="subagent", now=2.0)
        log_entry(led, "write report", 30000, phase="write", now=3.0)
        log_entry(led, "QC gate", 10000, phase="qc", kind="subagent", now=4.0)
        recs = read_ledger(led)
        check(len(recs) == 4 and recs[0]["ts"] == 1.0 and recs[2]["kind"] == "inline", "ledger appends records in order")
        rep = report(recs, budget=200000)
        check(rep["total_tokens"] == 250000 and rep["by_phase"]["research"] == 210000 and list(rep["by_phase"])[0] == "research",
              "totals by phase, largest first")
        check(rep["by_kind"] == {"subagent": 220000, "inline": 30000}, "totals by kind")
        check(rep["repeated"] == ["research: vendors"], "repeated task names are found case-insensitively")
        check(any(f.startswith("over budget") for f in rep["flags"]), "over budget is flagged")
        check(any("of the spend" in f for f in rep["flags"]), "one entry dominating the spend is flagged")
        near = report(recs, budget=300000)
        check(any(f.startswith("near budget") for f in near["flags"]) and not any(f.startswith("over") for f in near["flags"]),
              "near budget (over 80%) is flagged separately")
        calm = report([{"task": "a", "tokens": 10}, {"task": "b", "tokens": 10}, {"task": "c", "tokens": 10}, {"task": "d", "tokens": 10}])
        check(calm["flags"] == [], "a balanced ledger without a budget raises no flags")
        check(raises(lambda: log_entry(led, "  ", 5)), "an empty task name is refused")
        check(raises(lambda: log_entry(led, "x", -1)), "negative tokens are refused")
        check(raises(lambda: log_entry(led, "x", 1, kind="magic")), "an unknown kind is refused")
        check(len(read_ledger(led)) == 4, "refused entries are not written")
        bad = os.path.join(td, "bad.jsonl")
        open(bad, "w").write('{"task": "a", "tokens": 5}\nnot json\n')
        check(raises(lambda: read_ledger(bad)), "a corrupt ledger line is reported, not skipped")
        bad2 = os.path.join(td, "bad2.jsonl")
        open(bad2, "w").write('{"task": "a", "tokens": "5"}\n')
        check(raises(lambda: read_ledger(bad2)), "tokens must be an integer")
        check("FLAG: over budget" in render_report(rep), "rendered report shows flags")

        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc_ok = main(["report", led, "--budget", "200000"])
            rc_missing = main(["report", os.path.join(td, "nope.jsonl")])
            rc_usage = main(["frobnicate"])
            rc_log = main(["log", led, "--task", "cli entry", "--tokens", "5", "--kind", "tool"])
        check(rc_ok == 0 and rc_missing == 2 and rc_usage == 5 and rc_log == 0, "CLI exit codes: ok 0, unreadable 2, usage 5")
        check(read_ledger(led)[-1]["task"] == "cli entry", "CLI log appends")
    total = passed + failed
    print(f"self-test: {passed}/{total} checks passed" + ("" if failed else " — all offline logic checks passed"))
    return 0 if failed == 0 else 1


# ----------------------------------------------------------------------------- cli

def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv == ["--self-test"]:
        return self_test()
    ap = argparse.ArgumentParser(prog="token_ledger.py", description="Measure before reading; keep a token ledger.")
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("estimate"); p.add_argument("paths", nargs="+"); p.add_argument("--max", type=int, default=DEFAULT_MAX)
    p.add_argument("--glob", default=None); p.add_argument("--json", action="store_true")
    p = sub.add_parser("log"); p.add_argument("ledger"); p.add_argument("--task", required=True); p.add_argument("--tokens", type=int, required=True)
    p.add_argument("--phase", default=""); p.add_argument("--kind", default="inline"); p.add_argument("--ms", type=int, default=None)
    p.add_argument("--note", default="")
    p = sub.add_parser("report"); p.add_argument("ledger"); p.add_argument("--budget", type=int, default=None); p.add_argument("--json", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 0 if e.code == 0 else 5
    try:
        if a.mode == "estimate":
            e = estimate(a.paths, a.max, a.glob)
            print(json.dumps(e, indent=2) if a.json else render_estimate(e))
        elif a.mode == "log":
            rec = log_entry(a.ledger, a.task, a.tokens, a.phase, a.kind, a.ms, a.note)
            print(f"logged: {rec['task']} {rec['tokens']:,} tokens ({rec['phase']}, {rec['kind']})")
        else:
            rep = report(read_ledger(a.ledger), a.budget)
            print(json.dumps(rep, indent=2) if a.json else render_report(rep))
    except InputError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
