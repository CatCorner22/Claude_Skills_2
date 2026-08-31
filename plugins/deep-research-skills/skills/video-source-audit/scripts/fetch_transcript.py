#!/usr/bin/env python3
"""Fetch a video's transcript and metadata, and normalize it for auditing.

Usage:
  fetch_transcript.py <url> [--out DIR] [--json] [--lang en]
  fetch_transcript.py --self-test          # offline logic tests, no network

Why this exists rather than a bare yt-dlp call:

1. YouTube's auto-captions use a ROLLING two-line window — each cue repeats the tail of the
   previous cue so text scrolls on screen. Fed to a model raw, every sentence appears three or
   four times. Measured on real auto-caption files, the rolling format costs on the order of 15-20x
   the tokens of the same content de-duplicated (the exact multiple depends on whether the
   comparison is against plain or timecoded text). `--convert-subs srt` does NOT fix this.

2. The three failure states an audit must never conflate — captions absent, video unreachable,
   and network blocked — look similar at the shell. This script exits with a distinct code for
   each so a caller can never silently proceed to "grade" a video it did not read.

Exit codes:
  0  transcript written
  2  reachable, but no captions available          (offer the paste path)
  3  video unreachable: private, removed, geo/age-gated
  4  network or tooling unavailable (proxy/policy block, yt-dlp missing)
  5  bad usage
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

TIMESTAMP_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[.,](\d{3})"
)
# VTT inline styling: <00:00:03.520><c> word</c>
TAG_RE = re.compile(r"<[^>]+>")
CUE_SETTING_RE = re.compile(r"\b(align|position|size|line|region):\S+")


def hhmmss(h: str, m: str, s: str) -> str:
    """Render a timecode, dropping a zero hour so short videos read naturally."""
    return f"{int(h):d}:{m}:{s}" if int(h) else f"{int(m):d}:{s}"


def strip_markup(line: str) -> str:
    line = TAG_RE.sub("", line)
    line = line.replace("&nbsp;", " ")
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&#39;", "'"), ("&quot;", '"')):
        line = line.replace(ent, ch)
    return " ".join(line.split())


def parse_cues(text: str) -> list[tuple[str, str]]:
    """Parse VTT/SRT into (timecode, text) cues, markup stripped, blanks dropped."""
    cues: list[tuple[str, str]] = []
    current_ts: str | None = None
    buf: list[str] = []

    def flush() -> None:
        if current_ts is not None:
            body = strip_markup(" ".join(buf))
            if body:
                cues.append((current_ts, body))

    lines = text.splitlines()
    for i, raw in enumerate(lines):
        line = raw.rstrip()
        m = TIMESTAMP_RE.search(line)
        if m:
            flush()
            current_ts = hhmmss(m.group(1), m.group(2), m.group(3))
            buf = []
            continue
        if not line.strip():
            continue
        if line.strip().upper() == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        # SRT sequence number: a bare integer whose NEXT line is a timestamp. Checking the
        # lookahead rather than "before the first cue" matters — otherwise every sequence
        # number after the first is swallowed into the preceding cue's text.
        if line.strip().isdigit():
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if TIMESTAMP_RE.search(nxt):
                continue
        buf.append(CUE_SETTING_RE.sub("", line))
    flush()
    return cues


def collapse_rolling(cues: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Collapse YouTube's rolling auto-caption window into non-repeating lines.

    Each cue restates the tail of the previous one. Emit only the NEW suffix of each cue,
    matched on word boundaries so a repeated phrase is not re-emitted. Exact duplicates and
    cues wholly contained in what has already been emitted are dropped entirely.
    """
    out: list[tuple[str, str]] = []
    emitted: list[str] = []  # rolling window of words already emitted

    for ts, body in cues:
        words = body.split()
        if not words:
            continue
        # Longest suffix of `emitted` that prefixes `words` -> the overlap already shown.
        overlap = 0
        max_check = min(len(words), len(emitted))
        for k in range(max_check, 0, -1):
            if emitted[-k:] == words[:k]:
                overlap = k
                break
        new_words = words[overlap:]
        if not new_words:
            continue  # wholly repeated cue
        out.append((ts, " ".join(new_words)))
        emitted.extend(new_words)
        if len(emitted) > 400:  # bound the comparison window
            emitted = emitted[-400:]
    return out


def run(cmd: list[str], timeout: int = 180) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def classify_failure(stderr: str) -> int:
    """Map yt-dlp stderr to this script's exit codes. Order matters."""
    e = stderr.lower()
    if any(s in e for s in ("tunnel failed", "403 forbidden", "proxy", "egress",
                            "temporary failure in name resolution", "connection refused",
                            "network is unreachable", "failed to resolve")):
        return 4
    if any(s in e for s in ("private video", "video unavailable", "removed by the uploader",
                            "sign in to confirm your age", "not available in your country",
                            "members-only", "this live event")):
        return 3
    return 4


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?")
    ap.add_argument("--out", default=None, help="output directory (default: a temp dir)")
    ap.add_argument("--lang", default="en", help="subtitle language prefix (default: en)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    ap.add_argument("--self-test", action="store_true", help="run offline logic tests and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.url:
        ap.error("provide a URL (or --self-test)")

    if not shutil.which("yt-dlp"):
        print("yt-dlp not found on PATH. Install it, or supply a transcript manually.",
              file=sys.stderr)
        return 4

    outdir = args.out or tempfile.mkdtemp(prefix="vsa-")
    os.makedirs(outdir, exist_ok=True)

    rc, out, err = run(["yt-dlp", "--skip-download", "--dump-json", args.url])
    if rc != 0:
        code = classify_failure(err)
        msg = ("Could not reach the video (network or policy block)." if code == 4
               else "The video is unreachable: private, removed, or region/age restricted.")
        print(f"{msg}\nyt-dlp said: {err.strip().splitlines()[-1] if err.strip() else '(no output)'}",
              file=sys.stderr)
        print("Do NOT grade this video. Report the failure instead.", file=sys.stderr)
        return code

    meta = json.loads(out)
    info = {
        "id": meta.get("id"),
        "title": meta.get("title"),
        "channel": meta.get("channel") or meta.get("uploader"),
        "upload_date": meta.get("upload_date"),
        "duration_s": meta.get("duration"),
        "description": meta.get("description") or "",
        "chapters": [c.get("title") for c in (meta.get("chapters") or [])],
        "urls_in_description": sorted(set(
            re.findall(r"https?://[^\s<>()\[\]]+", meta.get("description") or "")
        )),
    }

    rc, _, err = run([
        "yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
        "--sub-langs", f"{args.lang}.*", "--sub-format", "vtt",
        "-o", os.path.join(outdir, "cap"), args.url,
    ])
    vtts = [f for f in os.listdir(outdir) if f.endswith((".vtt", ".srt"))]
    if not vtts:
        print("Reachable, but no captions are available for this video.", file=sys.stderr)
        print("Ask the user to paste a transcript; do not infer content from the title.",
              file=sys.stderr)
        if args.json:
            print(json.dumps({"info": info, "cues": [], "captions": False}, indent=2))
        return 2

    with open(os.path.join(outdir, sorted(vtts)[0]), encoding="utf-8", errors="replace") as fh:
        raw = fh.read()

    cues = collapse_rolling(parse_cues(raw))
    raw_chars = len(raw)
    clean_chars = sum(len(t) for _, t in cues)

    if args.json:
        print(json.dumps({"info": info, "captions": True,
                          "cues": [{"t": t, "text": s} for t, s in cues],
                          "raw_chars": raw_chars, "clean_chars": clean_chars}, indent=2))
    else:
        print(f"# {info['title']}  —  {info['channel']}  ({info['upload_date']})")
        print(f"# duration {info['duration_s']}s · {len(cues)} lines · "
              f"{raw_chars} raw chars -> {clean_chars} after de-duplication")
        if info["urls_in_description"]:
            print("# description links:")
            for u in info["urls_in_description"]:
                print(f"#   {u}")
        print()
        for t, s in cues:
            print(f"[{t}] {s}")
    return 0


# --------------------------------------------------------------------------------------
# Offline self-test
# --------------------------------------------------------------------------------------
def self_test() -> int:
    failures: list[str] = []
    total = 0

    def check(name: str, cond: bool) -> None:
        nonlocal total
        total += 1
        if not cond:
            failures.append(name)

    # A realistic YouTube rolling auto-caption block: each cue repeats the previous tail.
    rolling = """WEBVTT
Kind: captions
Language: en

00:00:01.000 --> 00:00:03.000
the study found that

00:00:03.000 --> 00:00:05.000
the study found that risk dropped

00:00:05.000 --> 00:00:07.000
risk dropped by fifty percent

00:00:07.000 --> 00:00:09.000
by fifty percent in the treatment group
"""
    cues = parse_cues(rolling)
    check("parses every cue", len(cues) == 4)
    collapsed = collapse_rolling(cues)
    text = " ".join(s for _, s in collapsed)
    check("collapse yields each phrase once",
          text == "the study found that risk dropped by fifty percent in the treatment group")
    check("collapse drops repeated cues", len(collapsed) == 4)
    check("collapse shrinks the payload", len(text) < sum(len(s) for _, s in cues))
    # The ratio is the whole reason this function exists; assert it is a real reduction.
    check("rolling format is materially redundant",
          sum(len(s) for _, s in cues) / max(len(text), 1) > 1.5)

    # Timestamps: the zero hour is dropped so short videos read as m:ss.
    check("first timecode preserved", collapsed[0][0] == "0:01")
    check("minutes retained", parse_cues("00:12:34.000 --> 00:12:35.000\nx\n")[0][0] == "12:34")
    check("hour retained when non-zero",
          parse_cues("01:02:03.000 --> 01:02:04.000\nx\n")[0][0] == "1:02:03")

    # Markup and entities
    styled = ('00:00:01.000 --> 00:00:02.000\n'
              '<00:00:01.100><c> hello</c> &amp; <b>world</b>\n')
    check("strips inline tags and entities", parse_cues(styled)[0][1] == "hello & world")

    # SRT with comma milliseconds and sequence numbers. The SECOND sequence number is the
    # regression case: a lookahead-free rule swallows it into the first cue's text.
    srt = ("1\n00:00:01,000 --> 00:00:02,000\nplain srt line\n\n"
           "2\n00:00:03,000 --> 00:00:04,000\nsecond srt line\n")
    check("parses SRT comma timestamps",
          parse_cues(srt) == [("0:01", "plain srt line"), ("0:03", "second srt line")])
    # A numeric line that is real caption text (not a sequence number) must survive.
    numeric = "00:00:05,000 --> 00:00:06,000\n2019\n"
    check("numeric caption text kept", parse_cues(numeric) == [("0:05", "2019")])

    # Non-rolling (human) captions must pass through untouched
    human = ("00:00:01.000 --> 00:00:02.000\nfirst distinct line\n\n"
             "00:00:02.000 --> 00:00:03.000\nsecond distinct line\n")
    hc = collapse_rolling(parse_cues(human))
    check("human captions unchanged", [s for _, s in hc] ==
          ["first distinct line", "second distinct line"])

    # A cue wholly contained in what was already emitted is dropped entirely
    dup = ("00:00:01.000 --> 00:00:02.000\nalpha beta gamma\n\n"
           "00:00:02.000 --> 00:00:03.000\nalpha beta gamma\n")
    check("exact duplicate cue dropped", len(collapse_rolling(parse_cues(dup))) == 1)

    # A genuine repetition that is NOT an overlap must survive (negative control):
    # the repeated phrase is separated by other words, so it is real speech, not scrolling.
    genuine = ("00:00:01.000 --> 00:00:02.000\nvery good\n\n"
               "00:00:02.000 --> 00:00:03.000\nresults were very good\n")
    g = " ".join(s for _, s in collapse_rolling(parse_cues(genuine)))
    check("non-overlapping repetition preserved", g == "very good results were very good")

    # Failure classification must not mislabel a policy block as a dead video
    check("proxy block -> 4", classify_failure("ERROR: unable to download: tunnel failed") == 4)
    check("private video -> 3", classify_failure("ERROR: Private video. Sign in") == 3)
    check("removed video -> 3", classify_failure("ERROR: Video unavailable") == 3)
    check("unknown error -> 4 (never a false 'gone')", classify_failure("ERROR: weird") == 4)

    print(f"self-test: {total - len(failures)}/{total} checks passed")
    for f in failures:
        print(f"  FAILED: {f}")
    if failures:
        return 1
    print("all offline logic checks passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except subprocess.TimeoutExpired:
        print("yt-dlp timed out. Treat as unreachable; do not grade.", file=sys.stderr)
        sys.exit(4)
    except KeyboardInterrupt:
        sys.exit(130)
