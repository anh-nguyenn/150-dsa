## Hint 1

Sort the candidates. Where do equal values end up, and why is that helpful for avoiding duplicate answers?

## Hint 2

Each input position can be used once, so the next recursive call must start after the chosen position. What should happen when two adjacent candidates are equal?

## Hint 3

At a given recursion level, skip a candidate if it equals the previous candidate at that same level. Recurse with the next index, and prune when the remaining target is smaller than the candidate.
