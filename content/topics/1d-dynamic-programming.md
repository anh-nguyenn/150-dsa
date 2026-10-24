# 1-D Dynamic Programming

1-D dynamic programming defines a state over a prefix or a position, then reuses smaller states. The recurrence is the whole idea; the array is bookkeeping.

Reach for it when a greedy choice fails because a local decision affects later options, and when the answer can be expressed as a best/count/boolean over a one-dimensional state.

It assumes you can write the base cases, the transition, and the order in which states are filled.
