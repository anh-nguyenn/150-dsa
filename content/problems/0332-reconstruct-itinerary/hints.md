## Hint 1

Using every ticket once sounds like walking every edge of a graph exactly once. What property must the start and end airports have?

## Hint 2

If you greedily take the alphabetically first flight, you may reach a dead end while tickets remain elsewhere. How can you splice those leftover trips in?

## Hint 3

Follow unused flights from the current airport. Record an airport only after it has no unused flights left, then reverse the recorded list.
