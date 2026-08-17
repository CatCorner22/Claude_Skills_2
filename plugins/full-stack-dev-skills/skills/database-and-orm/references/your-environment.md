# Your data layer (sanitized template)

- **Engine per environment:** <dev / test / prod>
- **Conventions:** <PK type, timestamp policy, money type + minor-unit scale or Numeric(p,s),
  soft-delete stance>
- **Migration workflow:** <who reviews migrations; CI check in place?>
- **Session/transaction pattern:** <where `commit()` lives — handler, service, or `with begin()`>
- **Pooling:** <pool_size / max_overflow / workers vs the server's max_connections;
  pre_ping + recycle values; external pooler?>
- **Hot queries and their indexes:** <query → index, from evidence>
- **Postgres trigger criteria:** <what would make you switch, if on SQLite>
- **Probe results (SKILL.md step 8):** <FK enforced? money round-trip exact? teardown-commit
  reachable by error handling? — date and engine/framework versions>
