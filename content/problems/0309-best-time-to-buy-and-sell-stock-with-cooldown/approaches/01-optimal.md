## Idea

Track three balances after each day. `hold` is the best cash position while owning a share, `sold` is the best position immediately after selling, and `rest` is the best position while free to buy. A purchase can only come from `rest`, a sale moves from `hold` to `sold`, and `rest` either stays put or takes over yesterday's `sold` once the cooldown is over.

## Why it works

Every legal trading schedule is a path through these three states. The recurrence considers each legal transition using the previous day's snapshot, so it never buys and sells on the same day and always enforces the rest day after a sale. Since each state keeps its best possible balance, the maximum at the end is optimal.

## Edge cases

- An empty price list gives `0`.
- A single day gives `0` because nothing can be sold.
- Strictly falling prices give `0`; buying is optional.
- Strictly rising prices may still favor holding through the whole period rather than selling early.
- A sale immediately followed by another purchase is illegal and is prevented by taking purchases only from `rest`.
