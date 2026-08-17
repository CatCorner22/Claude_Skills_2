"""Command-line entry point.

Usage:
  python -m fusioncash_architect.cli report <out.html> <config1.xlsx> [config2.xlsx ...]
  python -m fusioncash_architect.cli summary <config1.xlsx> [config2.xlsx ...]
  python -m fusioncash_architect.cli criteria "<expression>" field=value [field=value ...]
  python -m fusioncash_architect.cli parse "<rule>" "<source string>"

`report` and `summary` accept a directory too (all *.xlsx inside are loaded).
"""
from __future__ import annotations

import glob
import json
import os
import sys

from .ingest import load_all, IngestError
from .analyze import analyze
from .report import write_report
from .simulate import simulate_criteria, simulate_parse_rule


def _expand(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            out.extend(sorted(glob.glob(os.path.join(p, "*.xlsx"))))
        else:
            out.append(p)
    return out


def _load(paths):
    files = _expand(paths)
    if not files:
        print("no .xlsx files found", file=sys.stderr)
        raise SystemExit(2)
    return load_all(files)


def cmd_report(args):
    if len(args) < 2:
        print("usage: report <out.html> <config...>", file=sys.stderr)
        raise SystemExit(2)
    out, paths = args[0], args[1:]
    extracts = _load(paths)
    note = f"generated from {len(extracts)} extract(s): " + ", ".join(
        e.source_file for e in extracts.values())
    dest = write_report(extracts, out, note)
    h = analyze(extracts)["health"]
    print(f"wrote {dest}  (health {h['score']}/100, grade {h['grade']})")


def cmd_summary(args):
    extracts = _load(args)
    res = analyze(extracts)
    print(json.dumps({"counts": res["counts"], "health": res["health"]}, indent=2))


def cmd_criteria(args):
    if not args:
        print('usage: criteria "<expr>" field=value ...', file=sys.stderr)
        raise SystemExit(2)
    expr = args[0]
    values = {}
    for kv in args[1:]:
        if "=" in kv:
            k, v = kv.split("=", 1)
            values[k] = v
    r = simulate_criteria(expr, values)
    print(json.dumps(r, indent=2))


def cmd_parse(args):
    if len(args) < 2:
        print('usage: parse "<rule>" "<source>"', file=sys.stderr)
        raise SystemExit(2)
    print(json.dumps(simulate_parse_rule(args[0], args[1]), indent=2))


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        raise SystemExit(2)
    cmd, rest = argv[0], argv[1:]
    handlers = {"report": cmd_report, "summary": cmd_summary,
                "criteria": cmd_criteria, "parse": cmd_parse}
    if cmd not in handlers:
        print(f"unknown command {cmd!r}\n{__doc__}", file=sys.stderr)
        raise SystemExit(2)
    try:
        handlers[cmd](rest)
    except IngestError as e:
        print(f"ingest error: {e}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
