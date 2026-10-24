## Hint 1

How many flights may a valid route use when `k` stops are allowed?

## Hint 2

Suppose you know the cheapest price to each city using at most `i` flights. How can you extend those prices to `i + 1` flights?

## Hint 3

Repeat a full edge relaxation `k + 1` times, but compute the next prices from a copy of the previous round so a single round cannot chain several new flights.
