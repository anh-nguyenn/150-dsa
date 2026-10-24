A subsequence keeps the original order but may skip elements, unlike a subarray. The key idea is that, for each possible subsequence length, only the smallest possible ending value matters.

### Everyday examples

- **Stacking boxes.** To build the tallest stack where each box is larger than the one below, you care about the smallest top that works for each height.
- **Improving scores.** Finding the longest run of strictly better results in order is a subsequence problem, not a contiguous-run problem.
- **Scheduling.** Choosing tasks with strictly increasing deadlines while preserving their given order favors earlier, smaller deadlines for each count.

### How it shows up here

Maintain an array `tails` where `tails[k]` is the smallest ending value of any increasing subsequence of length `k + 1` seen so far. For each number, replace the first tail that is at least as large as it, or append a new tail if it is larger than all of them. The length of `tails` is the best length found.
