# Your SQL environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (connection strings, real table or
column names, sample rows), keep it in `your-environment.private.md` instead — that suffix is
git-ignored. Commit only sanitized, structural examples.

- **Dialect / engine:** <Postgres | Snowflake | BigQuery | Oracle | SQL Server | Databricks | …>
- **How you connect:** <BI tool, notebook, CLI; read-only role?>
- **Core tables (name → grain):**
  - `<schema.table>` → one row per <grain>
  - `<schema.table>` → one row per <grain>
- **Standard join keys:** <e.g. orders.customer_id = customers.id>
- **Date columns & time zone convention:** <e.g. event_ts stored UTC; report in ET>
- **Partitioning / clustering:** <e.g. partitioned by event_date; clustered by account_id>
- **Naming conventions:** <snake_case, fact_/dim_ prefixes, surrogate vs. natural keys>
- **Row-limit / dialect quirks to remember:** <QUALIFY available? LIMIT vs FETCH? etc.>
- **Known slow spots / big tables:** <tables to filter early, avoid full scans>
