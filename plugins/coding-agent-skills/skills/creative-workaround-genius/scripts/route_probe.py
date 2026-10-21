#!/usr/bin/env python3
"""Inventory what is on board before inventing a workaround: local tools, Python modules, proxy and
certificate configuration, and (opt-in) which public channels this machine can actually reach.

Usage:
  route_probe.py                         # local tools and modules only; makes no network call
  route_probe.py --net                   # also probe each public channel once
  route_probe.py --net --url https://example.org/   # add channels of your own (repeatable)
  route_probe.py --json                  # machine-readable output
  route_probe.py --self-test             # offline checks; no network, no real tools needed

WHAT THIS DOES
  - Lists installed programs by category (fetch, documents, data, runtimes, build, cloud, browser,
    science) and importable Python modules, so the route ledger starts from what exists.
  - Reports whether a proxy and a certificate bundle are configured: names only, never values.
  - With --net, sends ONE request per channel (in parallel, short timeout) and classifies the result:
      reachable        the origin answered (any HTTP status, shown) -- the channel works
      refused-by-origin  the origin answered 401/403/407/429 -- a control on that path: do not retry
      refused-at-proxy the proxy refused the tunnel -- a policy control (or an unknown host): do not retry
      dns-fail         the name did not resolve
      timeout          no answer within the time limit
      tls-fail         certificate verification failed -- point the tool at the right CA bundle;
                       never disable verification
      error            anything else (message shown)

WHAT THIS DELIBERATELY DOES NOT DO
  No retries, ever: a refusal is a control, and repeating a refused request is not a workaround.
  No authentication, no cookies, no credentials, no proxy or certificate changes, no downloads beyond
  the first bytes of each probe. It reports; the skill decides.

Exit codes: 0 ok; 5 bad usage.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import importlib.util
import json
import os
import shutil
import socket
import ssl
import sys
import urllib.error
import urllib.request

__version__ = "1.0.0"

TOOLS = {
    "fetch": ["curl", "wget", "git", "gh", "aria2c", "rsync", "ssh", "scp"],
    "documents": ["pdftotext", "pdftoppm", "pdfinfo", "qpdf", "pandoc", "soffice", "libreoffice",
                  "tesseract", "convert", "magick", "rsvg-convert", "inkscape", "ffmpeg"],
    "data": ["sqlite3", "duckdb", "jq", "yq", "csvlook", "xsv", "qsv", "xmllint"],
    "runtimes": ["python3", "pip", "pip3", "node", "npm", "npx", "deno", "bun", "java", "Rscript",
                 "go", "cargo", "ruby", "perl"],
    "build": ["make", "cmake", "gcc", "cc", "clang", "docker", "podman", "tar", "unzip", "zip", "7z"],
    "cloud": ["gcloud", "gsutil", "bq", "aws", "az", "kubectl"],
    "browser": ["chromium", "chromium-browser", "google-chrome", "firefox"],
    "science": ["samtools", "bcftools", "bedtools", "plink", "plink2"],
}
MODULES = ["requests", "httpx", "bs4", "lxml", "pandas", "numpy", "scipy", "openpyxl", "docx", "pptx",
           "pypdf", "pdfplumber", "fitz", "PIL", "cairosvg", "matplotlib", "playwright", "yaml"]
# Configuration names whose presence matters to routing. Values are never printed.
CONFIG_VARS = ["HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "NO_PROXY", "SSL_CERT_FILE",
               "REQUESTS_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "PIP_CERT", "GIT_SSL_CAINFO"]
# Public channels, one cheap request each. (name, url, method)
CHANNELS = [
    ("PyPI index", "https://pypi.org/simple/", "HEAD"),
    ("PyPI files", "https://files.pythonhosted.org/", "HEAD"),
    ("npm registry", "https://registry.npmjs.org/-/ping", "GET"),
    ("GitHub raw files", "https://raw.githubusercontent.com/octocat/Hello-World/master/README", "GET"),
    ("GitHub web/git", "https://github.com/", "HEAD"),
    ("GitHub API", "https://api.github.com/", "GET"),
    ("GitHub release assets", "https://objects.githubusercontent.com/", "HEAD"),
    ("jsDelivr CDN", "https://cdn.jsdelivr.net/", "HEAD"),
    ("unpkg CDN", "https://unpkg.com/", "HEAD"),
    ("Hugging Face", "https://huggingface.co/", "HEAD"),
    ("Internet Archive", "https://web.archive.org/", "HEAD"),
    ("Wikipedia", "https://en.wikipedia.org/", "HEAD"),
    ("Crossref API", "https://api.crossref.org/works?rows=0", "GET"),
    ("NCBI E-utilities", "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi", "GET"),
]
REFUSAL_CODES = {401, 403, 407, 429}
TIMEOUT = 8.0

ADVICE = {
    "refused-at-proxy": "a control: do not retry; use a permitted channel or ask the owner",
    "refused-by-origin": "a control on this path: do not retry; find a permitted path or ask",
    "tls-fail": "point the tool at the configured CA bundle; never disable verification",
    "dns-fail": "the name does not resolve here; try another channel",
    "timeout": "no answer in time; try another channel before retrying this one",
}


# ----------------------------------------------------------------------------- local inventory

def inventory_tools(which=shutil.which) -> dict[str, list[str]]:
    return {cat: [t for t in names if which(t)] for cat, names in TOOLS.items()}


def inventory_modules(find_spec=importlib.util.find_spec) -> list[str]:
    found = []
    for m in MODULES:
        try:
            if find_spec(m) is not None:
                found.append(m)
        except (ImportError, ValueError):
            pass
    return found


def inventory_config(environ=None) -> dict[str, bool]:
    env = os.environ if environ is None else environ
    return {k: bool(env.get(k)) for k in CONFIG_VARS}


# ----------------------------------------------------------------------------- network probes

def _ssl_context(environ=None) -> ssl.SSLContext:
    env = os.environ if environ is None else environ
    cafile = env.get("SSL_CERT_FILE") or env.get("REQUESTS_CA_BUNDLE")
    if cafile and os.path.exists(cafile):
        return ssl.create_default_context(cafile=cafile)
    return ssl.create_default_context()


def classify(exc: BaseException | None, status: int | None = None) -> tuple[str, str]:
    """Map one probe's outcome to (verdict, detail). Pure function: the self-test drives it directly."""
    if exc is None:
        return "reachable", f"HTTP {status}"
    if isinstance(exc, urllib.error.HTTPError):
        if exc.code in REFUSAL_CODES:
            return "refused-by-origin", f"HTTP {exc.code}"
        return "reachable", f"HTTP {exc.code}"
    reason = exc.reason if isinstance(exc, urllib.error.URLError) else exc
    text = str(reason)
    if isinstance(reason, ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in text:
        return "tls-fail", text[:120]
    if "Tunnel connection failed" in text and any(c in text for c in ("403", "407")):
        return "refused-at-proxy", text[:120]
    if isinstance(reason, socket.gaierror) or "Name or service not known" in text or "nodename nor servname" in text:
        return "dns-fail", text[:120]
    if isinstance(reason, (socket.timeout, TimeoutError)) or "timed out" in text:
        return "timeout", text[:120]
    return "error", f"{type(reason).__name__}: {text[:110]}"


def probe(url: str, method: str = "HEAD", opener=None, context=None, timeout: float = TIMEOUT) -> tuple[str, str]:
    """Exactly one request; never retried, whatever the outcome."""
    opener = opener or urllib.request.urlopen
    req = urllib.request.Request(url, method=method, headers={"User-Agent": f"route_probe/{__version__}"})
    try:
        resp = opener(req, timeout=timeout, context=context)
        status = getattr(resp, "status", None) or getattr(resp, "code", None)
        try:
            resp.read(256)
            resp.close()
        except Exception:
            pass
        return classify(None, status)
    except BaseException as exc:  # noqa: BLE001 -- every failure is data here
        if isinstance(exc, KeyboardInterrupt):
            raise
        return classify(exc)


def probe_all(channels, opener=None, context=None, workers: int = 8) -> list[dict]:
    out = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(probe, url, method, opener, context): (name, url) for name, url, method in channels}
        for fut in concurrent.futures.as_completed(futs):
            name, url = futs[fut]
            verdict, detail = fut.result()
            out.append({"channel": name, "url": url, "verdict": verdict, "detail": detail,
                        "advice": ADVICE.get(verdict, "")})
    order = {name: i for i, (name, _, _) in enumerate(channels)}
    return sorted(out, key=lambda r: order.get(r["channel"], 999))


# ----------------------------------------------------------------------------- report

def build_report(net: bool, extra_urls=(), which=shutil.which, find_spec=importlib.util.find_spec,
                 environ=None, opener=None) -> dict:
    report = {"version": __version__, "tools": inventory_tools(which), "python_modules": inventory_modules(find_spec),
              "config": inventory_config(environ), "channels": None}
    if net:
        channels = list(CHANNELS) + [(u, u, "HEAD") for u in extra_urls]
        report["channels"] = probe_all(channels, opener=opener, context=_ssl_context(environ))
    return report


def render_text(r: dict) -> str:
    lines = [f"route_probe {r['version']} — what is on board"]
    for cat, found in r["tools"].items():
        lines.append(f"  {cat:10s} {', '.join(found) if found else '(none)'}")
    lines.append(f"  {'python':10s} {', '.join(r['python_modules']) if r['python_modules'] else '(none of the listed modules)'}")
    cfg = r["config"]
    proxy = any(cfg.get(k) for k in ("HTTPS_PROXY", "https_proxy"))
    ca = [k for k in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "NODE_EXTRA_CA_CERTS", "PIP_CERT", "GIT_SSL_CAINFO") if cfg.get(k)]
    lines.append(f"  {'config':10s} proxy {'set' if proxy else 'not set'}; CA bundle variables set: {', '.join(ca) if ca else 'none'}")
    if r["channels"] is None:
        lines.append("  channels   not probed (add --net to probe each public channel once)")
    else:
        lines.append("  channels (one request each, never retried):")
        for c in r["channels"]:
            lines.append(f"    {c['verdict']:17s} {c['channel']:22s} {c['detail']}")
        controls = [c["channel"] for c in r["channels"] if c["verdict"].startswith("refused")]
        if controls:
            lines.append(f"  refused (controls, do not retry): {', '.join(controls)}")
        if any(c["verdict"] == "tls-fail" for c in r["channels"]):
            lines.append("  certificate failures: point the tool at the CA bundle; never disable verification")
    return "\n".join(lines)


# ----------------------------------------------------------------------------- self-test

class _FakeResp:
    def __init__(self, status):
        self.status = status

    def read(self, n=-1):
        return b""

    def close(self):
        pass


def self_test() -> int:
    passed = failed = 0

    def check(cond, label):
        nonlocal passed, failed
        if cond:
            passed += 1
        else:
            failed += 1
            print(f"FAIL: {label}")

    def http_err(code):
        return urllib.error.HTTPError("https://x/", code, "msg", {}, None)

    # classification, one case per verdict
    check(classify(None, 200) == ("reachable", "HTTP 200"), "a 200 is reachable")
    check(classify(http_err(404))[0] == "reachable", "an origin 404 still means the channel is reachable")
    check(classify(http_err(400))[0] == "reachable", "an origin 400 still means the channel is reachable")
    for code in (401, 403, 407, 429):
        check(classify(http_err(code))[0] == "refused-by-origin", f"origin {code} is a control")
    tunnel = urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden"))
    check(classify(tunnel)[0] == "refused-at-proxy", "a refused tunnel is a proxy control")
    check(classify(urllib.error.URLError(OSError("Tunnel connection failed: 407 Proxy Authentication Required")))[0]
          == "refused-at-proxy", "a 407 tunnel refusal is a proxy control")
    check(classify(urllib.error.URLError(OSError("Tunnel connection failed: 502 Bad Gateway")))[0] == "error",
          "a 502 tunnel failure is not called a control")
    check(classify(urllib.error.URLError(socket.gaierror(-2, "Name or service not known")))[0] == "dns-fail",
          "a resolver failure is dns-fail")
    check(classify(urllib.error.URLError(socket.timeout("timed out")))[0] == "timeout", "a socket timeout is timeout")
    check(classify(TimeoutError("timed out"))[0] == "timeout", "a bare TimeoutError is timeout")
    cert = ssl.SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed")
    check(classify(urllib.error.URLError(cert))[0] == "tls-fail", "certificate failure is tls-fail")
    check(classify(urllib.error.URLError(ConnectionResetError("reset")))[0] == "error", "anything else is error")
    check("never disable verification" in ADVICE["tls-fail"] and "do not retry" in ADVICE["refused-at-proxy"]
          and "do not retry" in ADVICE["refused-by-origin"], "advice keeps verification on and refuses retries")

    # probe: exactly one call per channel, whatever happens
    calls = []

    def opener_factory(outcome):
        def opener(req, timeout=None, context=None):
            calls.append((req.full_url, req.get_method()))
            if isinstance(outcome, BaseException):
                raise outcome
            return _FakeResp(outcome)
        return opener

    calls.clear()
    check(probe("https://a/", "HEAD", opener_factory(tunnel)) [0] == "refused-at-proxy" and len(calls) == 1,
          "a refused probe is made once and not retried")
    calls.clear()
    check(probe("https://a/", "GET", opener_factory(http_err(403)))[0] == "refused-by-origin" and len(calls) == 1
          and calls[0][1] == "GET", "an origin refusal is made once, with the requested method")
    calls.clear()
    check(probe("https://a/", "HEAD", opener_factory(200)) == ("reachable", "HTTP 200") and len(calls) == 1,
          "a successful probe is one request")

    # probe_all: one request per channel, results in channel order
    calls.clear()
    chans = [("one", "https://one/", "HEAD"), ("two", "https://two/", "GET"), ("three", "https://three/", "HEAD")]
    outcomes = {"https://one/": 200, "https://two/": tunnel, "https://three/": http_err(404)}

    def mixed(req, timeout=None, context=None):
        calls.append(req.full_url)
        o = outcomes[req.full_url]
        if isinstance(o, BaseException):
            raise o
        return _FakeResp(o)

    res = probe_all(chans, opener=mixed)
    check([r["channel"] for r in res] == ["one", "two", "three"], "results come back in channel order")
    check(sorted(calls) == sorted(outcomes) and len(calls) == 3, "probe_all makes exactly one request per channel")
    check([r["verdict"] for r in res] == ["reachable", "refused-at-proxy", "reachable"], "probe_all verdicts")
    check(res[1]["advice"].startswith("a control"), "a refused channel carries the control advice")

    # local inventory with injected lookups
    fake_which = lambda name: f"/usr/bin/{name}" if name in ("git", "pdftotext", "python3") else None  # noqa: E731
    tools = inventory_tools(fake_which)
    check(tools["fetch"] == ["git"] and tools["documents"] == ["pdftotext"] and tools["runtimes"] == ["python3"]
          and tools["cloud"] == [], "tool inventory lists only what exists, by category")

    def fake_spec(name):
        if name == "pandas":
            return object()
        if name == "fitz":
            raise ValueError("broken spec")
        return None
    check(inventory_modules(fake_spec) == ["pandas"], "module inventory survives a broken spec and lists only found")

    env = {"HTTPS_PROXY": "http://user:secret@proxy:8080", "SSL_CERT_FILE": "/etc/ca.pem"}
    cfg = inventory_config(env)
    check(cfg["HTTPS_PROXY"] is True and cfg["SSL_CERT_FILE"] is True and cfg["PIP_CERT"] is False,
          "config reports presence")

    # report: no network unless asked; values never printed
    def forbidden(*a, **k):
        raise AssertionError("network used without --net")
    r = build_report(False, which=fake_which, find_spec=fake_spec, environ=env, opener=forbidden)
    check(r["channels"] is None, "the default report makes no network call")
    text = render_text(r)
    blob = text + json.dumps(r)
    check("secret" not in blob and "/etc/ca.pem" not in blob and "proxy:8080" not in blob,
          "configuration values never appear in the output")
    check("proxy set" in text and "SSL_CERT_FILE" in text and "not probed" in text, "text report names config and the no-net state")
    calls.clear()
    r2 = build_report(True, extra_urls=["https://extra/"], which=fake_which, find_spec=fake_spec, environ={},
                      opener=opener_factory(tunnel))
    check(len(r2["channels"]) == len(CHANNELS) + 1 and len(calls) == len(CHANNELS) + 1,
          "--net probes every listed channel plus extras, once each")
    t2 = render_text(r2)
    check("refused (controls, do not retry)" in t2, "refusals are summarised as controls")

    # CLI
    import contextlib, io
    with contextlib.redirect_stderr(io.StringIO()):
        rc_bad = main(["--bogus"])
        rc_url = main(["--url", "https://x/"])
    check(rc_bad == 5, "bad usage exits 5")
    check(rc_url == 5, "--url without --net exits 5 instead of probing")

    total = passed + failed
    print(f"self-test: {passed}/{total} checks passed" + ("" if failed else " — all offline logic checks passed"))
    return 0 if failed == 0 else 1


# ----------------------------------------------------------------------------- cli

def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv == ["--self-test"]:
        return self_test()
    ap = argparse.ArgumentParser(prog="route_probe.py", description="Inventory local tools and reachable channels.")
    ap.add_argument("--net", action="store_true", help="probe each public channel once (never retried)")
    ap.add_argument("--url", action="append", default=[], help="extra channel URL to probe with --net")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--version", action="version", version=__version__)
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 0 if e.code == 0 else 5
    if a.url and not a.net:
        print("--url needs --net", file=sys.stderr)
        return 5
    r = build_report(a.net, a.url)
    print(json.dumps(r, indent=2) if a.json else render_text(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
