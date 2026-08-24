# Evals — data-tools-skills:rest-api-data-pulls

## 1. Positive trigger (should load the skill)
> "Pull all June invoices from our ERP's REST API into a CSV — my current script only returns
> 500 rows and I know there are thousands, and sometimes it dies with a 429."

Expected: skill loads; diagnoses missing pagination (loop on `hasMore`/offset); server-side
filtering with `q=` and `fields=`; hardened session with backoff honoring Retry-After on 429;
count reconciliation via `totalResults=true`; credentials via environment variables.

## 2. Near-miss (should NOT load this skill)
> "I need to bulk-load these 10,000 journal entries INTO the ERP from a spreadsheet."

Expected: an inbound bulk load into the ERP — the opposite direction from this skill's outbound
extracts, and a task no active skill in this library owns; nothing should load. If this
skill loads, sharpen the extract/outbound framing.

## 3. Quality rubric
A good response:
- **Does the task:** complete paginated pull with retries, filtered server-side, flattened
  deliberately (children as separate keyed tables), persisted with a run log.
- **Teaches:** why partial data is the default failure mode (exhaustion + proof), the
  retry-what's-transient / fail-fast-on-4xx split, and why polite queries are reliable queries.
- **Safe:** no credentials in code or git; doesn't retry 400s blindly; reconciles fetched count
  against a server-side total *and* recognises that the count alone is not sufficient — a total that
  moves during pagination, or a short page returned while the cursor still advances, defeats it.
