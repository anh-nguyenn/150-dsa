## Hint 1

Start with a table that counts ways to make every amount using no coin types at all. What should the entry for amount 0 be?

## Hint 2

When you allow a new coin, every total either uses none of that coin or adds one copy to a smaller total. Which direction should you scan so the new coin can be reused?

## Hint 3

Loop over coin types first and totals upward. This fixes a canonical order for the coins, so the same set of coins is counted only once.
