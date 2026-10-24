# Binary Search

Binary search is not only for finding a value in a sorted array. It is for any monotone predicate: a boolean that stays false and then becomes true, or the reverse.

Reach for it when you can test a candidate answer cheaply and the test is monotone. The search space may be indices, values, times, or capacities.

It assumes a precise loop invariant and careful handling of the boundary where the predicate flips.
