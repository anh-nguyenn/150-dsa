When some symbols are flexible, tracking a single count of open parentheses is not enough: the same prefix can lead to several possible counts. The useful observation is that those counts form a contiguous range. Each prefix therefore has a lowest and highest possible number of unmatched opening parentheses, and any count between them is achievable.

### Everyday examples

- **A flexible budget.** Some entries may be income, an expense, or skipped. To know whether the month can end balanced without ever going negative, you track the best and worst possible balances rather than one fixed balance.
- **A walk with optional steps.** Some steps may go up, down, or nowhere. The set of possible heights after a stretch is an interval, so keeping its floor and ceiling describes every reachable height.

### How it shows up here

Maintain `low` and `high`, the smallest and largest possible number of unmatched opens after the prefix. An opening parenthesis raises both. A closing parenthesis lowers both, with `low` clamped at zero because extra closes can be thought of as ignored only if some interpretation avoided them; `high` going negative means even the most optimistic interpretation has too many closes. A star can close, so it lowers `low` (clamped) and raises `high`.

At the end, the string is valid exactly when zero is among the possible open counts, which is `low == 0`.
