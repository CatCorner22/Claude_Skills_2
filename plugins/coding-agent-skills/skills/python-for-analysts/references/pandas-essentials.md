# pandas essentials (task-oriented)

The small vocabulary that covers most analyst work: load → inspect → select → filter → derive →
group → combine → write. Examples assume `import pandas as pd`. Behavior can differ slightly across
pandas versions — confirm your version with `pd.__version__` if something here behaves differently.

## Contents
- Load
- Inspect
- Select columns and rows
- Filter
- Derive new columns (safely)
- Group and aggregate
- Combine tables (merge/concat)
- Sort and rank
- Write out
- Gotchas that change your numbers

## Load
```python
df = pd.read_csv("data.csv", parse_dates=["date"], dtype={"account_id": "string"})
df = pd.read_excel("book.xlsx", sheet_name="Q3")          # needs openpyxl
df = pd.read_parquet("data.parquet")                       # fast, typed, preferred for reuse
```
Always pass `parse_dates=` for date columns and set `dtype=` for IDs so they don't become floats
(a leading zero or a big integer will otherwise be mangled).

## Inspect
```python
df.head(); df.tail()          # eyeball the data
df.shape                       # (rows, cols)
df.info()                      # dtypes + non-null counts — read this first
df.describe(include="all")     # quick stats
df.isna().sum()                # missing values per column
df["account"].value_counts()   # category frequencies
```

## Select columns and rows
```python
df["amount"]                   # one column (Series)
df[["date", "amount"]]         # several columns (DataFrame)
df.loc[10, "amount"]           # by label
df.iloc[0:5, 0:3]              # by position
```

## Filter
```python
df[df["amount"] > 0]                                   # boolean mask
df[(df["amount"] > 0) & (df["account"] == "OPS")]      # combine with & | ~, parenthesize each
df[df["account"].isin(["OPS", "PAYROLL"])]
df.query("amount > 0 and account == 'OPS'")            # readable alternative
```

## Derive new columns (safely)
```python
df = df.assign(net=df["amount"] - df["fee"])           # returns a new frame; chainable
df.loc[df["amount"] < 0, "flag"] = "debit"             # conditional assign — use .loc, not chaining
```

## Group and aggregate
```python
df.groupby("account", as_index=False)["amount"].sum()
df.groupby("account").agg(total=("amount", "sum"),
                          n=("amount", "size"),
                          avg=("amount", "mean")).reset_index()
df.groupby([df["date"].dt.to_period("M"), "account"])["amount"].sum()   # by month + account
```
`as_index=False` (or `.reset_index()`) keeps the group keys as normal columns.

## Combine tables (merge/concat)
```python
out = left.merge(right, on="account_id", how="left", validate="many_to_one")
out = pd.concat([jan, feb], ignore_index=True)         # stack rows with the same columns
```
Set `how` deliberately (`inner`/`left`/`right`/`outer`) and pass `validate=` so an unexpected
fan-out (duplicate keys silently multiplying rows) raises instead of corrupting your totals.

## Sort and rank
```python
df.sort_values("amount", ascending=False)
df.sort_values(["account", "date"])
df["rank"] = df.groupby("account")["amount"].rank(method="dense", ascending=False)
```

## Write out
```python
df.to_csv("out.csv", index=False)          # index=False unless the index is meaningful
df.to_parquet("out.parquet")               # keeps dtypes; best for a pipeline hand-off
with pd.ExcelWriter("out.xlsx") as xl:     # multiple sheets
    summary.to_excel(xl, sheet_name="summary", index=False)
```

## Gotchas that change your numbers
- **Chained indexing** (`df[m]["col"] = ...`) may write to a copy → no effect. Use `df.loc[m, "col"]`.
- **Merge fan-out**: duplicate keys on the "one" side multiply rows and inflate sums. Use `validate=`.
- **Wrong dtypes**: IDs read as float lose leading zeros; dates read as strings won't compare. Set them at load.
- **NaN in comparisons**: `NaN != NaN`; filters silently drop them. Handle with `.isna()` / `.fillna()` on purpose.
- **`inplace=True`**: encourages hidden state and is being deprecated in places — prefer reassigning the result.
- **Float equality**: `0.1 + 0.2 != 0.3`. Compare money with rounding or integer cents, not `==`.
- **Silent index alignment**: arithmetic between two Series aligns on index, not position — reset indexes first if unsure.
