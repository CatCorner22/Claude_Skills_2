# REST API pull patterns (reference)

## Contents
- Hardened session (retries + backoff)
- Pagination styles
- Flattening nested JSON
- Run logging

## Hardened session (retries + backoff)
```python
import requests, os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urlsplit

def make_session():
    s = requests.Session()
    retry = Retry(
        total=5, backoff_factor=1,   # sleeps: 0s, 2s, 4s, 8s, 16s — urllib3 does NOT
                                     # sleep before the first retry
        status_forcelist=[429, 500, 502, 503, 504],
        respect_retry_after_header=True,
        allowed_methods=["GET"],
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.headers["Accept"] = "application/json"
    return s


# Keep the credential OFF the Session and pass it per request.
#
# `Session.auth` is applied to every request made through that session, whatever the
# host and whatever the scheme. That is fine while you control the URL — but the
# Link-header loop below follows a URL the *server* chose, so a `next` link pointing at
# `http://` sends the Basic credential in cleartext, and one pointing at another host
# sends it to that host. This is not the redirect case: `requests` strips auth across
# hosts on redirects (`Session.rebuild_auth`), and that never runs here, because the
# loop issues a brand-new request to a URL it read out of the response.
AUTH = (os.environ["FUSION_USER"], os.environ["FUSION_PASSWORD"])  # or a token header


def same_origin(candidate: str, base: str) -> bool:
    """A server-supplied URL is untrusted input. Follow it only back to where you started."""
    c, b = urlsplit(candidate), urlsplit(base)
    return c.scheme == "https" and (c.scheme, c.netloc) == (b.scheme, b.netloc)
```
- The first retry fires immediately: `Retry.get_backoff_time()` returns 0 until two
  consecutive failures are in its history. If you need a delay on the first retry,
  urllib3's `Retry` cannot supply it — wrap the call yourself, or rely on `Retry-After`
  (`respect_retry_after_header` is already on).
- The cap comes free: urllib3 clamps each sleep to `backoff_max`, 120 s by default.
- Timeouts always (`timeout=60`); a hung request is worse than a failed one.
- 4xx (except 429): read `r.json()` / `r.text` for the API's diagnostic and fix the request.

## Pagination styles
| Style | How it looks | Loop condition |
|---|---|---|
| Offset/limit (Fusion) | `?limit=500&offset=1000`, body has `hasMore` | until `hasMore` false |
| Page number | `?page=3&per_page=100` | until short/empty page |
| Cursor | body returns `next_cursor` | until cursor null |
| Link header | `Link: <url>; rel="next"` | until no `next` link |
Cursor pagination is safest under concurrent writes (no skipped/duplicated rows when data
shifts between pages); with offset pagination, keep the pull window short and sort stable —
and note that a row-count reconciliation does not detect this failure, because one insert and
one delete during the pull duplicate one row and skip another while the total still matches.
The offset/`hasMore` loop is in the skill body; the other two styles:

Both loops below are bounded by `max_pages`, like the offset loop in the skill body — a
server that keeps handing back a cursor, or a `next` link that cycles, must not be able to
spin the pull forever.

```python
# Cursor: the body carries the next cursor; absent/null means done.
rows, cursor = [], None
for _ in range(max_pages):                          # never an unbounded while True
    r = s.get(url, params={"cursor": cursor} if cursor else {}, timeout=60, auth=AUTH)
    r.raise_for_status(); body = r.json()
    rows += body["items"]
    cursor = body.get("next_cursor")
    if not cursor:
        break
else:
    raise RuntimeError(f"cursor pagination hit max_pages={max_pages} without finishing")

# Link header: requests parses it for you — no header string parsing needed.
rows, next_url, params = [], url, {"per_page": 100}
for _ in range(max_pages):
    if not same_origin(next_url, url):              # the server chose this URL, not you
        raise RuntimeError(f"refusing to send credentials to {next_url!r}")
    r = s.get(next_url, params=params, timeout=60, auth=AUTH)
    r.raise_for_status()
    rows += r.json()
    next_url = r.links.get("next", {}).get("url")   # already absolute; carries its own query
    params = None                                   # don't re-append params to the next URL
    if not next_url:
        break
else:
    raise RuntimeError(f"link pagination hit max_pages={max_pages} without finishing")
```

**The rule behind both:** a URL or cursor that came from the response is untrusted input.
Bound the loop that consumes it, and check where it points before attaching a credential.

## Flattening nested JSON
```python
import pandas as pd
parents = pd.json_normalize(rows, sep="_")                     # scalars + nested dicts
lines = pd.json_normalize(
    [r for r in rows if r.get("invoiceLines")],                # filter first: json_normalize
    record_path="invoiceLines",                                # raises KeyError if ANY parent
    meta=["InvoiceId"], sep="_")                               # lacks the key, and APIs omit
                                                               # empty collections routinely
```
- One table per level; join on the parent key at analysis time. Parents with no children are
  absent from the child table by construction — use a left join, not an inner one, if the
  parent count has to survive.
- After flattening: IDs to `string`, dates parsed, amounts numeric — the flat-file rules apply.

## Run logging
Log one line per run: `timestamp, resource, filter_window, rows_fetched, server_total,
duration_s, output_file`. The first question about any recurring extract is "did it pull
everything?" — the log answers it without re-running.
