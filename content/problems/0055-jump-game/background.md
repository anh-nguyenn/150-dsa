Reachability problems often reduce to a moving frontier. Instead of recording every possible route, track the farthest position that can be reached so far. If the scan ever moves past that frontier, there is a gap that no earlier jump can cross.

### Everyday examples

- **Stepping stones.** Each stone shows the maximum stride you can take from it. You only need to know the farthest stone you can currently land on; the exact path does not matter.
- **A bus with limited range.** At each stop you learn how far the bus can go from there. You are fine as long as the next stop is not beyond the best range you have seen.

### How it shows up here

Start with a frontier of zero, since you already stand at index 0. Scan left to right. Before using a position, check that it lies within the frontier. Then push the frontier forward to the larger of its current value and `i + nums[i]`. If the frontier reaches or passes the last index, the answer is yes.

A position beyond the frontier means every earlier position could only jump to somewhere before it, so the remaining array is unreachable.
