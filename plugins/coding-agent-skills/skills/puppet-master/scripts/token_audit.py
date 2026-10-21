#!/usr/bin/env python3
"""token_audit.py — where did the tokens go in an agent run?

Reads a Claude Code transcript (JSON lines: the session file under ~/.claude/projects/, or a
subagent's output file) and reports what the run cost and which moves cost the most:

  turns           unique model calls (assistant messages, de-duplicated by message id)
  final context   tokens in the context at the last call
  processed       every call re-sends the context: sum of input + cache write + cache read + output
  weighted        the same sum at typical price ratios (cache read 0.1, cache write 1.25,
                  output 5, plain input 1), in input-token equivalents — the number to minimise
  tool results    the largest results that entered the context, with the call that made them
  waste signals   repeated reads, unbounded commands, single-call turns, subagent spawns

It reads only the transcript it is given and never prints tool-result contents, only sizes.

Usage:
  token_audit.py <transcript.jsonl> [--top N] [--json]
  token_audit.py --self-test
Exit codes: 0 ok, 2 unreadable or empty transcript, 5 bad usage.
"""
import argparse, contextlib, io, json, math, os, re, sys, tempfile

CHARS_PER_TOKEN = 3.5
WEIGHTS = {"input": 1.0, "cache_creation": 1.25, "cache_read": 0.1, "output": 5.0}
READ_TOOLS = {"Read"}
SPAWN_TOOLS = {"Agent", "Task"}
UNBOUNDED = [
    (re.compile(r"(?:^|[;&|]\s*)cat\s+(?![^|]*\|\s*(?:head|tail|wc|grep|sed|cut|jq|python))[^|<>]+$"), "cat of a whole file with no bound"),
    (re.compile(r"\bls\s+(?:-\w*R\w*|--recursive)"), "recursive listing"),
    (re.compile(r"\bfind\s+(?![^|]*\|\s*(?:head|wc))(?![^|]*-maxdepth)[^|]*$"), "find with no depth limit or head"),
]


class InputError(Exception):
    pass


def est_tokens(chars):
    return math.ceil(chars / CHARS_PER_TOKEN) if chars > 0 else 0


def _text_len(content):
    if isinstance(content, str):
        return len(content)
    if isinstance(content, list):
        n = 0
        for c in content:
            if isinstance(c, dict):
                if c.get("type") == "text":
                    n += len(c.get("text", ""))
                elif c.get("type") == "image":
                    n += 1600 * 4  # an image costs on the order of 1.6k tokens; count it, never decode it
            elif isinstance(c, str):
                n += len(c)
        return n
    return 0


def _summary(name, inp):
    if not isinstance(inp, dict):
        return name
    for k in ("command", "file_path", "pattern", "url", "description", "query", "skill"):
        if inp.get(k):
            return f"{name}: {str(inp[k]).splitlines()[0][:90]}"
    return name


def load(path):
    if not os.path.isfile(path):
        raise InputError(f"no such file: {path}")
    events = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue  # transcripts can end mid-write; a torn line is not a reason to stop
    if not events:
        raise InputError(f"{path}: no JSON records")
    return events


def audit(events, top=8):
    calls, order = {}, []
    uses, results = {}, {}
    for i, ev in enumerate(events):
        msg = ev.get("message") if isinstance(ev, dict) else None
        if not isinstance(msg, dict):
            continue
        role = msg.get("role")
        if role == "assistant":
            mid = msg.get("id") or f"line{i}"
            if mid not in calls:
                calls[mid] = {"usage": msg.get("usage") or {}, "tools": []}
                order.append(mid)
            elif msg.get("usage"):
                calls[mid]["usage"] = msg["usage"]
            for c in msg.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("id") not in uses:
                    uses[c.get("id")] = {"name": c.get("name", "?"), "input": c.get("input") or {}, "call": mid}
                    calls[mid]["tools"].append(c.get("id"))
        elif role == "user":
            for c in msg.get("content") or [] if isinstance(msg.get("content"), list) else []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    results[c.get("tool_use_id")] = _text_len(c.get("content"))
    if not order:
        raise InputError("no assistant turns found — is this a Claude Code transcript?")

    totals = {k: 0 for k in WEIGHTS}
    for mid in order:
        u = calls[mid]["usage"]
        totals["input"] += int(u.get("input_tokens") or 0)
        totals["cache_creation"] += int(u.get("cache_creation_input_tokens") or 0)
        totals["cache_read"] += int(u.get("cache_read_input_tokens") or 0)
        totals["output"] += int(u.get("output_tokens") or 0)
    last = calls[order[-1]]["usage"]
    final_context = sum(int(last.get(k) or 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
    processed = sum(totals.values())
    weighted = round(sum(totals[k] * w for k, w in WEIGHTS.items()))
    first = calls[order[0]]["usage"]
    start_context = sum(int(first.get(k) or 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    start_share = round(100 * start_context * len(order) / processed) if processed else 0

    by_tool, rows = {}, []
    for uid, u in uses.items():
        by_tool[u["name"]] = by_tool.get(u["name"], 0) + 1
        chars = results.get(uid, 0)
        rows.append({"tool": u["name"], "call": _summary(u["name"], u["input"]), "chars": chars, "tokens": est_tokens(chars)})
    rows.sort(key=lambda r: (-r["chars"], r["call"]))

    findings = []
    reads = {}
    for u in uses.values():
        if u["name"] in READ_TOOLS and u["input"].get("file_path"):
            key = (u["input"]["file_path"], u["input"].get("offset"), u["input"].get("limit"))
            reads[key] = reads.get(key, 0) + 1
        elif u["name"] == "Bash" and u["input"].get("command"):
            key = ("$", u["input"]["command"].strip())
            reads[key] = reads.get(key, 0) + 1
    for key, n in sorted(reads.items(), key=lambda kv: (-kv[1], str(kv[0]))):
        if n > 1:
            what = f"command `{key[1][:70]}`" if key[0] == "$" else f"file {key[0]}"
            findings.append({"kind": "repeated", "detail": f"{what} run or read {n} times", "count": n})
    for u in uses.values():
        if u["name"] != "Bash":
            continue
        cmd = str(u["input"].get("command", ""))
        for part in re.split(r"\n|&&|;", cmd):
            for rx, why in UNBOUNDED:
                if rx.search(part.strip()):
                    findings.append({"kind": "unbounded", "detail": f"{why}: `{part.strip()[:70]}`", "count": 1})
                    break
    single = sum(1 for mid in order if len(calls[mid]["tools"]) == 1)
    multi = sum(1 for mid in order if len(calls[mid]["tools"]) > 1)
    if single >= 3 and single > 2 * multi:
        findings.append({"kind": "batching", "detail": f"{single} turns made a single tool call and {multi} made several; independent calls can share a turn", "count": single})
    spawns = [u for u in uses.values() if u["name"] in SPAWN_TOOLS]
    if spawns:
        findings.append({"kind": "subagents", "detail": f"{len(spawns)} subagent(s) spawned; each starts with its own full system context", "count": len(spawns)})
    if len(order) >= 3 and start_share >= 50:
        findings.append({"kind": "startup", "detail": f"the {start_context:,}-token start-up context, re-sent every turn, is ~{start_share}% of processed; "
                         "look for tool definitions, skill listings and connector instructions the run never used", "count": len(order)})
    big = [r for r in rows if r["tokens"] > 5000]
    for r in big:
        findings.append({"kind": "large-result", "detail": f"{r['tokens']} tokens from {r['call']}", "count": 1})

    return {"turns": len(order), "final_context": final_context, "start_context": start_context, "start_share": start_share,
            "processed": processed, "weighted": weighted,
            "usage": totals, "tool_calls": sum(by_tool.values()), "by_tool": dict(sorted(by_tool.items())),
            "largest_results": rows[:top], "result_tokens": sum(r["tokens"] for r in rows), "findings": findings}


def render(rep):
    u = rep["usage"]
    out = [f"turns {rep['turns']}   tool calls {rep['tool_calls']}   final context {rep['final_context']:,}",
           f"processed {rep['processed']:,}   weighted {rep['weighted']:,} (input-token equivalents)",
           f"start-up context {rep['start_context']:,} (re-sent each turn: ~{rep['start_share']}% of processed)",
           f"  input {u['input']:,} · cache write {u['cache_creation']:,} · cache read {u['cache_read']:,} · output {u['output']:,}",
           f"tool results entered context: ~{rep['result_tokens']:,} tokens", "", "largest tool results:"]
    for r in rep["largest_results"]:
        out.append(f"  {r['tokens']:>7,}  {r['call']}")
    out.append("")
    out.append("waste signals:" if rep["findings"] else "waste signals: none")
    for f in rep["findings"]:
        out.append(f"  [{f['kind']}] {f['detail']}")
    return "\n".join(out)


def self_test():
    checks, fails = 0, []
    def check(name, cond):
        nonlocal checks
        checks += 1
        if not cond:
            fails.append(name); print(f"FAIL {name}")
    def a(mid, usage, tools=()):
        return {"type": "assistant", "message": {"id": mid, "role": "assistant", "usage": usage,
                "content": [{"type": "tool_use", "id": t[0], "name": t[1], "input": t[2]} for t in tools]}}
    def r(tid, text):
        return {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tid, "content": text}]}}
    U = lambda i, cw, cr, o: {"input_tokens": i, "cache_creation_input_tokens": cw, "cache_read_input_tokens": cr, "output_tokens": o}
    ev = [
        a("m1", U(2, 1000, 0, 10), [("t1", "Read", {"file_path": "/x/big.py"})]),
        a("m1", U(2, 1000, 0, 10)),                       # same message split across lines: counted once
        r("t1", "x" * 35000),
        a("m2", U(2, 100, 1000, 20), [("t2", "Read", {"file_path": "/x/big.py"})]),
        r("t2", [{"type": "text", "text": "y" * 700}]),
        a("m3", U(2, 50, 1100, 30), [("t3", "Bash", {"command": "cat /x/data.csv"})]),
        r("t3", "z" * 70),
        a("m4", U(2, 10, 1150, 40), [("t4", "Bash", {"command": "ls -laR /x"}), ("t5", "Agent", {"description": "survey"})]),
        r("t4", "w" * 7), r("t5", "v" * 3500),
        a("m5", U(2, 5, 1160, 400)),
    ]
    rep = audit(ev, top=3)
    check("turns de-duplicated by message id", rep["turns"] == 5)
    check("processed sums every call", rep["processed"] == (2 + 1000 + 0 + 10) + (2 + 100 + 1000 + 20) + (2 + 50 + 1100 + 30) + (2 + 10 + 1150 + 40) + (2 + 5 + 1160 + 400))
    w = 10 * 1 + 1165 * 1.25 + 4410 * 0.1 + 500 * 5
    check("weighted applies price ratios", rep["weighted"] == round(w))
    check("final context is the last call", rep["final_context"] == 2 + 5 + 1160 + 400)
    check("start-up context is the first call's input side", rep["start_context"] == 2 + 1000 + 0)
    check("start-up share of processed", rep["start_share"] == round(100 * 1002 * 5 / rep["processed"]))
    check("start-up re-sending flagged", any(f["kind"] == "startup" and "1,002" in f["detail"] for f in rep["findings"]))
    check("tool calls counted", rep["tool_calls"] == 5 and rep["by_tool"] == {"Agent": 1, "Bash": 2, "Read": 2})
    check("largest result first", rep["largest_results"][0]["tokens"] == 10000 and rep["largest_results"][0]["tool"] == "Read")
    check("top limit honoured", len(rep["largest_results"]) == 3)
    check("list-form result measured", any(x["tokens"] == 200 for x in rep["largest_results"]))
    kinds = [f["kind"] for f in rep["findings"]]
    check("repeated read found", any(f["kind"] == "repeated" and "big.py" in f["detail"] and f["count"] == 2 for f in rep["findings"]))
    check("cat without bound flagged", any(f["kind"] == "unbounded" and "cat" in f["detail"] for f in rep["findings"]))
    check("recursive listing flagged", any(f["kind"] == "unbounded" and "recursive" in f["detail"] for f in rep["findings"]))
    check("bounded cat not flagged", not audit([a("q", U(1, 1, 1, 1), [("b", "Bash", {"command": "cat f.csv | head -5"})]), r("b", "1")])["findings"])
    check("subagent spawn reported", "subagents" in kinds)
    check("large result flagged", any(f["kind"] == "large-result" and "10000" in f["detail"] for f in rep["findings"]))
    check("batching flagged on single-call turns", "batching" in kinds)
    ev2 = [a("b1", U(1, 1, 1, 1), [("p", "Bash", {"command": "wc -l a"}), ("q", "Bash", {"command": "wc -l b"})]), r("p", "1"), r("q", "1")]
    check("no batching flag when calls share turns", "batching" not in [f["kind"] for f in audit(ev2)["findings"]])
    check("no start-up flag on a one-turn run", "startup" not in [f["kind"] for f in audit(ev2)["findings"]])
    ev4 = [a("g1", U(1, 9, 0, 1)), a("g2", U(1, 900, 9, 1)), a("g3", U(1, 50, 909, 1))]
    check("no start-up flag when the run's own content dominates", "startup" not in [f["kind"] for f in audit(ev4)["findings"]])
    ev3 = [a("s1", U(1, 1, 1, 1), [("s", "Read", {"file_path": "/x/a.py", "offset": 1, "limit": 50}), ("t", "Read", {"file_path": "/x/a.py", "offset": 51, "limit": 50})]), r("s", "1"), r("t", "2")]
    check("different slices of one file are not a repeat", not any(f["kind"] == "repeated" for f in audit(ev3)["findings"]))
    check("est tokens rounds up", est_tokens(1) == 1 and est_tokens(7) == 2 and est_tokens(0) == 0)
    text = render(rep)
    check("contents never printed", "xxxx" not in text and "yyyy" not in text and "zzz" not in text)
    check("start-up line rendered", "start-up context 1,002" in text)
    try:
        audit([{"type": "user", "message": {"role": "user", "content": "hi"}}]); check("no assistant turns is an error", False)
    except InputError:
        check("no assistant turns is an error", True)
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "t.jsonl")
        with open(p, "w") as f:
            f.write("\n".join(json.dumps(e) for e in ev) + "\n{torn")
        check("torn last line tolerated", audit(load(p))["turns"] == 5)
        try:
            load(os.path.join(td, "missing.jsonl")); check("missing file is an error", False)
        except InputError:
            check("missing file is an error", True)
        empty = os.path.join(td, "e.jsonl"); open(empty, "w").close()
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            rc_empty, rc_usage, rc_ok = main([empty]), main(["a", "b"]), main([p, "--json"])
        check("empty file exits 2", rc_empty == 2)
        check("bad usage exits 5", rc_usage == 5)
        check("good file exits 0", rc_ok == 0)
    if fails:
        print(f"self-test: {checks - len(fails)}/{checks} checks passed")
        return 1
    print(f"self-test: {checks}/{checks} checks passed — all offline logic checks passed")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="token_audit.py", description="Where did the tokens go in an agent run?")
    p.add_argument("transcript", nargs="?")
    p.add_argument("--top", type=int, default=8)
    p.add_argument("--json", action="store_true")
    p.add_argument("--self-test", action="store_true")
    try:
        a = p.parse_args(argv)
    except SystemExit:
        return 5
    if a.self_test:
        return self_test()
    if not a.transcript or a.top < 1:
        print("error: give one transcript path (and --top of at least 1)", file=sys.stderr)
        return 5
    try:
        rep = audit(load(a.transcript), top=a.top)
    except InputError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(json.dumps(rep, indent=1) if a.json else render(rep))
    return 0


if __name__ == "__main__":
    sys.exit(main())
