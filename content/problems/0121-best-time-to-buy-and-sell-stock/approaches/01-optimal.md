## Idea

Scan once while remembering the cheapest price seen so far. The best sale ending today is today's price minus that minimum.

## Why it works

Any optimal trade buys at some earlier price and sells at a later one. When the scan reaches the selling day, the cheapest earlier price has already been recorded, so the profit computed for that day is at least as good as that trade. Taking the maximum over all days therefore finds the best legal trade.

## Edge cases

A single day has no later selling day and yields zero. Strictly falling prices keep resetting the minimum and never produce a positive profit. Equal prices produce zero. Prices can drop to zero without changing the logic.
