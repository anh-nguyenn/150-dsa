Dynamic programming often handles a line of choices easily, then needs one extra idea for a cycle. The usual trick is to remove one edge of the cycle and solve the resulting line, considering each way of breaking it.

### Everyday examples

- **A round table.** Guests sit in a circle, and you cannot choose two neighbours. Cutting the circle at one seat turns it into a row.
- **A circular train route.** Stations repeat around a loop, and some adjacent stops cannot both be served. Choosing where to break the loop lets you reuse a line-based plan.

### How it shows up here

In a circle, either house `0` is robbed or it is not. If it is, house `n - 1` cannot be; if it is not, house `n - 1` may be. Solving the straight-line problem on `nums[0:n-1]` and on `nums[1:n]` covers both cases, and the larger answer wins.
