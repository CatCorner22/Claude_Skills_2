# Your chart of accounts (sanitized template)

Capture your **real** segment structure here — this is what makes the skill fit your books. If it contains real
entity names or account numbers, keep it in `your-environment.private.md` instead; that suffix is git-ignored, so
raw structure never gets committed. Commit only sanitized, structural examples.

## Segment structure (in order)
| # | Segment name | Width | Value set (source) | Example value |
|---|---|---|---|---|
| 1 | <Entity/company> | <2> | <legal entities> | <01> |
| 2 | <Cost center> | <4> | <departments> | <4200> |
| 3 | <Natural account> | <5> | <account master> | <61010> |
| 4 | <Optional: product/location/project> | <> | <> | <> |
| 5 | <Future / spare> | <4> | <reserved> | <0000> |

- **Full account string example:** `<01-4200-61010-...-0000>` = <plain-English meaning>
- **Delimiter:** <e.g. hyphen>

## Natural-account ranges
- Assets <1xxxx>, Liabilities <2xxxx>, Equity <3xxxx>, Revenue <4xxxx>, COGS <5xxxx>, Opex <6xxxx–8xxxx>, Other <9xxxx>
- Reserved gaps: <where new accounts should slot in>

## Reporting hierarchies / rollups
- <Management P&L tree: which detail accounts roll to which parents>
- <Statutory statement tree>
- <Any alternate/segment reporting trees>

## Intercompany & clearing accounts
- Intercompany pairs: <IC receivable / IC payable accounts and the entities they mirror>
- Clearing/suspense accounts: <which accounts, who owns them, how often reconciled>

## Governance
- **New-account request process:** <who requests, who approves, required definition + hierarchy mapping>
- **Owner of the COA:** <role/team>
- **System(s):** <ERP and any downstream consolidation/reporting tools; note any mapping/crosswalk maintained>
