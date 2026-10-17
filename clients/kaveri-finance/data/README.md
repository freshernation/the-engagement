# What Kavya sent over

> "Four recent applications, statements as we received them, converted to text. The
> appraisal sheet columns are below. Please don't keep copies after the engagement. K"

| File | Bank format |
|---|---|
| `statements/KF-2291-sri-lakshmi-traders.txt` | Format A: pipe-separated, DD/MM/YYYY, withdrawal before deposit |
| `statements/KF-2297-manjunath-auto-works.txt` | Format B: CSV, DD-Mon-YY, debit before credit |
| `statements/KF-2302-ganga-steel-fabricators.txt` | Format C: one line per transaction, `Cr`/`Dr` suffix |
| `statements/KF-2305-nandi-provision-stores.txt` | Format A |

These are the text-PDF kind. About one in five real statements is a scanned image; none
of those are here.

## The appraisal sheet

What a credit officer types in today, one row per month:

| Column | Meaning |
|---|---|
| `month` | `YYYY-MM` |
| `total_credits` | Sum of all deposits in the month |
| `total_debits` | Sum of all withdrawals in the month |
| `credit_count` | Number of deposits |
| `closing_balance` | Balance after the last transaction of the month |

Every figure must be traceable to the statement lines it came from. The auditors check.

All businesses, banks and amounts are invented.
