# REST API pull patterns (reference)

## Contents
- Hardened session (retries + backoff)
- Pagination styles
- Oracle Fusion query idioms
- Flattening nested JSON
- Run logging

## Hardened session (retries + backoff)
```python
import requests, os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def make_session():
    s = requests.Session()
    retry = Retry(
        total=5, backoff_factor=2,                 # 2s, 4s, 8s, 16s, 32s
        status_forcelist=[429, 500, 502, 503, 504],
        respect_retry_after_header=True,
        allowed_methods=["GET"],
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.auth = (os.environ["FUSION_USER"], os.environ["FUSION_PASSWORD"])  # or token header
    s.headers["Accept"] = "application/json"
    return s
```
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
shifts between pages); with offset pagination, keep the pull window short and sort stable.

## Oracle Fusion query idioms
```
GET /fscmRestApi/resources/11.13.18.05/invoices
    ?q=InvoiceDate>=2026-06-01;InvoiceDate<2026-07-01;InvoiceAmount>1000
    &fields=InvoiceId,InvoiceNumber,Supplier,InvoiceAmount,InvoiceDate
    &orderBy=InvoiceDate:asc
    &limit=500&offset=0
    &totalResults=true          # adds totalResults for count reconciliation
```
- `;` = AND in `q`; comparison operators and `LIKE` supported per resource docs.
- Children: `expand=invoiceLines` inlines them, or hit the child URL
  `.../invoices/{id}/child/invoiceLines` — for volume, prefer separate pulls per level.
- The integration user needs the same functional data security as a human — missing rows often
  means missing data access, not a bug.
- Other useful finance resources: `receivablesInvoices`, `standardReceipts`,
  `cashTransactions`, `cashBankAccounts`, `ledgerBalances`, `journalBatches` (availability
  varies by release — check the REST API guide for yours).

## Flattening nested JSON
```python
import pandas as pd
parents = pd.json_normalize(rows, sep="_")                     # scalars + nested dicts
lines = pd.json_normalize(rows, record_path="invoiceLines",    # child collection
                          meta=["InvoiceId"], sep="_")
```
- One table per level; join on the parent key at analysis time.
- After flattening: IDs to `string`, dates parsed, amounts numeric — the flat-file rules apply.

## Run logging
Log one line per run: `timestamp, resource, filter_window, rows_fetched, server_total,
duration_s, output_file`. The first question about any recurring extract is "did it pull
everything?" — the log answers it without re-running.
