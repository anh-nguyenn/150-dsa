You are given a list of triplets and a target triplet. You may pick any two triplets and replace them with a new triplet formed by taking the larger value in each of the three positions. Repeat as needed. Decide whether the target triplet can be produced.

**Example**

```text
triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target   = [2, 7, 5]  ->  true
```

Merging `[2, 5, 3]` with `[1, 7, 5]` gives `[2, 7, 5]`.

**Constraints, in plain words**

- Between 1 and 1,000 triplets.
- Each value is between 1 and 1,000.
- The target also has three positive values.
- Merging takes the maximum in each coordinate.
- Triplets that are not used simply remain in the list.

[Merge Triplets to Form Target Triplet on LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)
