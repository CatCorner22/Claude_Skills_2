# Practical SQL patterns (Fusion Financials)

Preserved from the source spec (Chicken Little v2026.2), with scoping and accuracy fixes.

Contents: §1 Open AP invoices · §2 AP validation status · §3 AR aging · §4 Receipt status
(Ghost Receipts) · §5 Unposted GL journals · §6 CoA lookup · §7 XLA headers (Orphan
Distributions) · §8 AP holds (Invoice Black Hole)

**Access caveat**: in pure SaaS Fusion Cloud, direct SQL against base tables is frequently
restricted. Prefer OTBI subject areas, BI Publisher, REST APIs, FBDI, or data extracts to
Autonomous Data Warehouse (ADW) via BICC. These patterns remain invaluable for understanding
the model, designing custom analytics, troubleshooting, and working with extracts or ADW.

Always filter by `ORG_ID` / business unit and `LEDGER_ID` for multi-org correctness and
security. Pair results with Polars or DuckDB for statistical work and control charts in the
DMAIC Measure/Analyze phases.

## 1. Open / partially paid AP invoices with supplier & status

```sql
SELECT
  aia.invoice_id,
  aia.invoice_num,
  aia.invoice_date,
  aia.invoice_amount,
  aia.payment_status_flag,          -- 'Y' Fully paid, 'N' Unpaid, 'P' Partial
  aia.wfapproval_status,
  aia.invoice_type_lookup_code,
  hp.party_name AS supplier_name,
  aia.org_id
FROM ap_invoices_all aia
JOIN poz_suppliers ps ON aia.vendor_id = ps.vendor_id
JOIN hz_parties hp ON ps.party_id = hp.party_id
WHERE aia.payment_status_flag IN ('N', 'P')
  AND aia.cancelled_date IS NULL
  AND aia.org_id = :org_id            -- always scope multi-org tables
ORDER BY aia.invoice_date;
```

## 2. AP validation / match status from distributions

```sql
SELECT
  aia.invoice_id,                   -- group on the PK: INVOICE_NUM is only unique per supplier+BU
  aia.invoice_num,
  aida.match_status_flag,           -- 'A' Validated, 'N'/NULL Never, 'T' Needs revalidation, 'S' Stopped
  COUNT(*) AS distribution_count,
  SUM(aida.amount) AS total_dist_amount
FROM ap_invoices_all aia
JOIN ap_invoice_distributions_all aida ON aia.invoice_id = aida.invoice_id
WHERE aia.org_id = :org_id
GROUP BY aia.invoice_id, aia.invoice_num, aida.match_status_flag
ORDER BY aia.invoice_num;
```

## 3. AR open items with basic aging buckets

```sql
SELECT
  apsa.trx_number,
  apsa.class,                       -- INV, DM, CM, etc.
  apsa.status,                      -- 'OP' Open, 'CL' Closed
  apsa.amount_due_original,
  apsa.amount_due_remaining,
  apsa.due_date,
  CASE
    WHEN TRUNC(SYSDATE) - apsa.due_date <= 0 THEN 'Current'
    WHEN TRUNC(SYSDATE) - apsa.due_date BETWEEN 1 AND 30 THEN '1-30'
    WHEN TRUNC(SYSDATE) - apsa.due_date BETWEEN 31 AND 60 THEN '31-60'
    WHEN TRUNC(SYSDATE) - apsa.due_date BETWEEN 61 AND 90 THEN '61-90'
    ELSE '90+'
  END AS aging_bucket
FROM ar_payment_schedules_all apsa
WHERE apsa.status = 'OP'
  AND apsa.class IN ('INV', 'DM', 'CB')
  AND apsa.org_id = :org_id
ORDER BY TRUNC(SYSDATE) - apsa.due_date, apsa.due_date;  -- numeric age: 'Current' first, '90+' last
```

## 4. AR cash receipt status distribution (Ghost Receipts radar)

```sql
SELECT
  status,                           -- APP, UNAPP, UNID, REV, NSF, STOP
  COUNT(*) AS receipt_count,
  SUM(amount) AS total_amount
FROM ar_cash_receipts_all
WHERE org_id = :org_id
  AND receipt_date >= :from_date    -- bound the window; whole-table scans mislead and crawl
GROUP BY status
ORDER BY status;
```

## 5. Unposted or error GL journals

```sql
SELECT
  gjh.je_header_id,
  gjh.name AS journal_name,
  gjh.period_name,
  gjh.status,                       -- 'U' Unposted, 'P' Posted, other codes = errors
  gjh.je_source,
  gjh.je_category,
  gjh.running_total_dr,
  gjh.running_total_cr
FROM gl_je_headers gjh
WHERE gjh.status != 'P'
  AND gjh.ledger_id = :ledger_id
ORDER BY gjh.period_name, gjh.creation_date;
```

## 6. Chart of accounts combinations lookup

```sql
-- CONCATENATED_SEGMENTS lives on the GL_CODE_COMBINATIONS_KFV flex view,
-- NOT on the GL_CODE_COMBINATIONS base table (a Fusion-vs-EBS difference).
-- If the KFV is unavailable in your access path, select SEGMENT1..SEGMENTn
-- from the base table and concatenate them yourself.
SELECT
  code_combination_id,
  concatenated_segments,            -- KFV-only column
  segment1, segment2, segment3,     -- adjust to your CoA structure
  enabled_flag,
  summary_flag,
  chart_of_accounts_id
FROM gl_code_combinations_kfv
WHERE enabled_flag = 'Y'
  AND chart_of_accounts_id = :coa_id;
```

## 7. XLA subledger accounting headers (AP example; Orphan Distributions radar)

```sql
SELECT
  ae_header_id,
  application_id,                   -- 200 = Payables, 222 = Receivables, 101 = GL
  accounting_date,
  accounting_entry_status_code,     -- D=Draft, F=Final, I=Invalid, N=Incomplete
  gl_transfer_status_code,          -- Y=Transferred, S=Selected, N/NT=Not transferred
  event_type_code,
  ledger_id
FROM xla_ae_headers
WHERE application_id = 200
  AND ledger_id = :ledger_id
  AND accounting_date BETWEEN :start_date AND :end_date;
-- Orphan hunt: Final-but-untransferred headers (status F, transfer <> Y) older than the
-- close window, then compare against GL_IMPORT_REFERENCES for the missing linkage.
```

## 8. LSS-friendly: AP invoices still on hold (Invoice Black Hole / cycle-time analysis)

```sql
SELECT
  aia.invoice_num,
  aia.invoice_date,
  aia.creation_date,
  TRUNC(SYSDATE) - TRUNC(aia.creation_date) AS days_open,
  ah.hold_lookup_code,
  ah.hold_date,
  aia.wfapproval_status
FROM ap_invoices_all aia
JOIN ap_holds_all ah ON aia.invoice_id = ah.invoice_id
WHERE ah.release_lookup_code IS NULL   -- still on hold
  AND aia.org_id = :org_id
ORDER BY days_open DESC;
```

These patterns support status checks, open-item analysis, aging, CoA inspection, XLA transfer
monitoring, and process metrics for DMAIC Measure/Analyze.
