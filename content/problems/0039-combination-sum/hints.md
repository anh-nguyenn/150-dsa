## Hint 1

Pick one candidate and subtract it from the target. What smaller problem is left, and which candidates may still be used?

## Hint 2

Reuse means a chosen candidate can be chosen again immediately. How should the starting position of the next recursive call differ from the Subsets problem?

## Hint 3

Sort the candidates. Recurse with the remaining target and the same index, stop when the next value is too large, and save the path when the remaining target becomes zero.
