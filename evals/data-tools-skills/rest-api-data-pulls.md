# Evals — data-tools-skills:rest-api-data-pulls

## 1. Positive trigger (should load the skill)
> "Pull all June invoices from the Fusion REST API into a CSV — my current script only returns
> 500 rows and I know there are thousands, and sometimes it dies with a 429."

Expected: skill loads; diagnoses missing pagination (loop on `hasMore`/offset); server-side
filtering with `q=` and `fields=`; hardened session with backoff honoring Retry-After on 429;
count reconciliation via `totalResults=true`; credentials via environment variables.

## 2. Near-miss (should NOT load this skill)
> "I need to bulk-load these 10,000 journals INTO Fusion from a spreadsheet."

Expected: inbound bulk load — `oracle-fusion-finance-skills:fusion-fbdi-data-loading`. If this
skill loads, sharpen the extract/outbound framing.

## 3. Quality rubric
A good response:
- **Does the task:** complete paginated pull with retries, filtered server-side, flattened
  deliberately (children as separate keyed tables), persisted with a run log.
- **Teaches:** why partial data is the default failure mode (exhaustion + proof), the
  retry-what's-transient / fail-fast-on-4xx split, and why polite queries are reliable queries.
- **Safe:** no credentials in code or git; doesn't retry 400s blindly; reconciles fetched count
  against a server-side total instead of assuming completeness.
