# Your API extracts (sanitized template)

Fill in per extract. Hostnames, credentials references, and real samples go in
`your-environment.private.md` (git-ignored).

Per extract:
- **API / resource:** <e.g. Fusion invoices; Bank X balance API>
- **Auth:** <method; which env vars hold credentials; integration user's roles>
- **Filter window and fields:** <what you pull and why>
- **Pagination style:** <offset+hasMore / cursor / etc.>
- **Rate limits observed:** <requests per window; backoff behavior>
- **Count reconciliation source:** <totalResults, count endpoint, or report figure>
- **Schedule and output:** <when it runs; file naming; where it lands>
