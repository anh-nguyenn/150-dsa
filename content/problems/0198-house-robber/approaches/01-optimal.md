## Idea

Scan left to right keeping the best total for the row up to the previous house and the one before that. For each house, choose between skipping it (keep the previous best) and taking it (add its value to the best from two houses back).

## Why it works

Any valid selection either contains house `i` or does not. If it does not, it is a selection from the first `i` houses, bounded by `best[i-1]`. If it does, house `i - 1` is forbidden, so the rest is a selection from the first `i - 1` houses, giving `best[i-2] + nums[i]`. The two cases cover every valid selection, so the maximum is correct.

## Edge cases

- One house: the loop returns its value.
- All zeros: the answer is 0.
- Two houses: the larger single amount wins.
- Zero-valued houses can be taken freely; they never reduce the total.
- Negative amounts are not allowed, so skipping is never worse than a negative gain.
