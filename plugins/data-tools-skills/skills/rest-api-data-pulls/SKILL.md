---
name: rest-api-data-pulls
description: >-
  Pulls data from REST APIs into files and DataFrames reliably — authentication patterns, query
  and field selection, pagination until exhaustion, retries with backoff for rate limits and
  transient failures, and flattening nested JSON. Use when extracting data from a REST API, when
  a pull returns partial data, or when hardening a recurring API extract. Triggers: rest api pull,
  call api python, paginate an api, saas api export, pagination, api rate limit, 429 retry,
  requests python, extract data from api, api to csv, json to dataframe, oauth token api.
metadata:
  version: "1.2.0"
---

# REST API data pulls

## When to use
- Extracting records from a REST API — a CRM, ERP, ticketing system, or any SaaS endpoint — into
  CSV/Parquet/DataFrames for analysis.
- Fixing pulls that silently return partial data, hit rate limits, or break on nested JSON.
- Not for: bulk-*loading* data into a SaaS platform — that is the platform's own import pipeline
  (file templates, staging tables, error reports) and differs per vendor. This skill pulls data out.
  For analyzing the extracted data → see `data-tools-skills:duckdb-local-analytics` or
  `data-analytics-bi-skills` skills.

## Do it
1. **Read the API's contract before writing code:** base URL, auth method, pagination style,
   rate limits, and the resource's field list. Most SaaS platforms publish a versioned resource
   path and a per-resource field list; find both before writing a line of code, because they
   determine your pagination style and how much you can ask for per call.
2. **Authenticate the simplest way the API allows, and keep secrets out of code.** Enterprise
   platforms commonly take Basic auth (a dedicated integration user) or OAuth2/JWT; most other
   SaaS APIs use bearer tokens or API keys. Load credentials from environment variables or a secrets manager — never
   literals in the script, never in git (see `data-tools-skills:data-file-hygiene`).
3. **Ask for less: filter and select server-side.** Every API has a query idiom — Fusion uses
   `q=` for filters, `fields=` to trim columns, `orderBy`, and `expand=` for children. Pulling
   only June's rows with five fields is faster, kinder to rate limits, and less likely to
   time out than pulling everything and filtering locally:
   `.../invoices?q=InvoiceDate>=2026-06-01;InvoiceDate<2026-07-01&fields=InvoiceId,InvoiceNumber,InvoiceAmount&limit=500`.
4. **Paginate to exhaustion — partial data is the default failure.** Fusion returns
   `limit`/`offset` pages with a `hasMore` flag; other APIs use page numbers, cursors, or `next`
   links. Loop until the API says done, and count as you go:

```python
def fetch_all(session, url, params, page=500, max_pages=1000):
    rows, offset = [], 0
    for _ in range(max_pages):                       # never an unbounded while True
        r = session.get(url, params={**params, "limit": page, "offset": offset}, timeout=60)
        r.raise_for_status()
        body = r.json()
        items = body["items"]
        rows += items
        print(f"offset={offset} rows={len(items)} cumulative={len(rows)}")   # count as you go
        if not body.get("hasMore") or not items:     # done — or hasMore is lying
            total = body.get("totalResults")         # step 7's reconciliation, at the source
            if total is not None and len(rows) != total:
                raise AssertionError(f"fetched {len(rows)} != server total {total}")
            return rows
        offset += len(items)                         # advance by what arrived, not by `limit`
    raise RuntimeError(f"pagination did not terminate after {max_pages} pages")
```

   The four guards matter as much as the loop: advancing the offset by `len(items)` rather
   than by `page` survives a server that returns a short page while `hasMore` is still true
   (advancing by `page` would silently skip the rows it withheld), an empty page ends the loop
   even when `hasMore` stays true, `max_pages` turns a server-side bug into an error instead
   of a hung script, and the `totalResults` assertion makes a short pull fail loudly rather
   than look plausible. Know what that last guard cannot see: offset pagination over a table
   still being written to duplicates a row onto the next page for every insert ahead of your
   offset and skips one for every delete, so a pull that does both matches the total while
   holding wrong rows. Compare distinct key counts to `len(rows)` as well, and prefer cursor
   pagination when the API offers it.

5. **Retry transient failures with backoff; respect 429.** Wrap requests so 429 (honor
   `Retry-After`) and 5xx/timeouts retry with exponential backoff and a cap; 4xx other than 429
   are *your* bug (bad filter, bad auth) — fail fast and read the error body.
   `references/api-patterns.md` has a hardened session recipe and per-style pagination loops.
6. **Flatten deliberately.** `pd.json_normalize(rows)` handles nesting; child collections
   (invoice lines under invoices) become separate tables keyed by the parent ID — mirroring how
   you'd analyze them. Type the result like any flat file: IDs as strings, dates parsed,
   amounts numeric.
7. **Verify and persist.** Compare the fetched count to a server-side count when available
   (Fusion: `totalResults=true`; otherwise a count endpoint or a UI/report figure), spot-check a
   few records against the source UI, then write Parquet/CSV with the pull date in the filename.
   For a recurring extract, log run time, row count, and filter window every run.

## Why / learn
API extraction fails differently from file loading: a file is all-or-nothing, but an API hands
you data *one polite page at a time*, and every convenience in the protocol is a place to lose
rows silently — stop before `hasMore` is false, drop a page to an unretried timeout, or hit a
rate limit mid-pull, and you get a plausible-looking partial dataset with no error. That's why
the discipline centers on *exhaustion and proof*: loop until the server says done, retry what's
transient, and reconcile your row count against a server-side total, exactly like footing a
report. Server-side filtering matters for the same systemic reason — you're sharing the API
with the business's own transactions, so the polite query is also the reliable one. And the
auth rule (secrets in the environment, never the code) isn't just hygiene: an extraction script
gets shared, and a credential in a script is a credential published.

## Common mistakes
- Fetching one page and moving on → check `hasMore`/`next` until exhaustion; count rows against a server total.
- Filtering client-side after pulling everything → slow, rate-limited, timeout-prone; push filters and field lists to the API.
- No retry, or retrying 400s → backoff on 429/5xx/timeouts only; a 400 means fix the request.
- Credentials pasted in the script → environment variables or a secrets manager; scripts travel.
- Flattening children into the parent row → one row per line item in a child table keyed by parent ID.
- Ignoring the error body on failure → Fusion and most APIs return a diagnostic message; read it before guessing.
- Recurring extract with no run log → silent drift; log window, count, and duration each run.

## Tailor to your environment
Record your extracts in `references/your-environment.md` (endpoints with real hostnames and any
credentials references in `your-environment.private.md`, git-ignored): which resources you pull,
filter windows, field lists, the integration user's roles, rate limits observed, and where
outputs land. **Never commit tokens, passwords, or real pulled data.**

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/rest-api-data-pulls.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/api-patterns.md — hardened session with retries, pagination styles, query idioms, json flattening
- references/your-environment.md — your endpoints, resources, and extract schedules (fill in)
