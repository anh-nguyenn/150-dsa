There are `n` cities numbered from `0` to `n-1`. Each flight `[from, to, price]` is a one-way route with a cost. Starting at `src`, find the cheapest way to reach `dst` using at most `k` intermediate stops. Return `-1` if no such route exists.

**Example**

```text
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1  ->  200
```

The one-stop route through city 1 costs 200 and beats the direct 500 flight.

**Constraints, in plain words**

- At most 100 cities and about 5,000 flights.
- Prices are positive.
- `k` counts intermediate stops, so a route may use at most `k + 1` flights.
- The source and destination may be the same city.

[Cheapest Flights Within K Stops on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
