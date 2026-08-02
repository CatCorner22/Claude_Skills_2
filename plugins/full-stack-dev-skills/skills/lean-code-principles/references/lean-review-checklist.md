# Lean review checklist (reference)

## Contents
- PR review checklist
- Signs of over-engineering
- Deletion opportunities
- Net-lines discipline

## PR review checklist
- [ ] Could a stdlib/framework feature replace any hand-rolled logic here?
- [ ] Does every new parameter/option have a caller who needs it *today*?
- [ ] Any abstraction with only one implementation? (Inline it.)
- [ ] Any helper called exactly once that doesn't clarify? (Inline it.)
- [ ] Public surface: did anything become exported/optional/configurable without need?
- [ ] Are there tests for behavior, not for implementation details that block refactors?
- [ ] Is the diff's *net* line count justified by the behavior change?
- [ ] Anything in this PR that could be deleted instead of modified?

## Signs of over-engineering
| Sign | Smell | Lean fix |
|---|---|---|
| Interface/ABC with one implementation | Speculative polymorphism | Concrete class; extract when the second impl exists |
| `utils.py` growing unrelated helpers | Abstraction landfill | Move helpers next to their single caller |
| Deep config objects / factory factories | Flexibility nobody used | Default args; hard-code until needed |
| Wrapper around a library "to swap it later" | Vendor-change insurance you'll never claim | Use the library directly; migrations are rewrites anyway |
| Generic event bus for two functions | Architecture cosplay | A function call |
| Feature flags older than a quarter | Shipped or dead | Delete flag + dead branch |
| Comments explaining clever code | Cleverness tax | Rewrite boring; delete the comment |

## Deletion opportunities (hunt monthly)
- Unused dependencies (`pip-audit` / `npm ls`, import scans)
- Dead endpoints/routes (access logs say nobody calls them)
- Commented-out code and TODOs older than 6 months (do or delete)
- Duplicate near-copies that drifted (merge or delete one)
- Tests that test mocks, not behavior

## Net-lines discipline
Track per PR: `+added / −deleted / net`. Healthy mature codebases trend near zero net while
shipping features. Celebrate the negative-net feature PR in review — it's the strongest
signal the discipline is working.
