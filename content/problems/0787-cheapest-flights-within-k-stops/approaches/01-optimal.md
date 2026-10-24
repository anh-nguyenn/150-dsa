## Idea

Keep an array of the cheapest known prices when at most a certain number of flights may be used. Start with only the source reachable at price zero. Each round builds a fresh copy of the array and relaxes every flight using the prices from the round before, which permits exactly one additional flight. After `k + 1` rounds the array holds the best prices with at most `k + 1` flights.

## Why it works

By induction, after `i` rounds `prices[v]` is the cheapest cost from the source to `v` using at most `i` flights. Round `i + 1` considers every final flight `u -> v` and combines it with a route of at most `i` flights, so it cannot miss a cheaper bounded route. The snapshot prevents several new flights from being chained inside one round, which would violate the stop limit. If the destination remains unreachable, no valid route exists.

## Edge cases

- If the source equals the destination, the zero-flight route costs `0`.
- A direct flight is allowed when `k` is at least zero.
- Too few stops may leave only expensive routes or no route at all.
- Cycles are harmless; the bounded number of rounds limits how often they can be used.
