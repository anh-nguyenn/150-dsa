## Hint 1

Which balloon should you think about last rather than first?

## Hint 2

If a chosen balloon is burst last inside a range, what are its neighbors at that moment, and what independent subproblems remain?

## Hint 3

Pad the array with 1s and let `dp[left][right]` be the best coins from bursting everything strictly between two boundaries. Try each possible final balloon inside that range.
