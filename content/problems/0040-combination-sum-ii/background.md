Backtracking becomes trickier when the input contains repeated values. The search tree can then contain identical branches that produce the same answer. A standard fix is to sort first, then skip a value if an equal value was already tried at the same level of the tree.

### Everyday examples

- **Choosing from a stack of coupons.** Several coupons may have the same discount. Two identical coupons are still two physical coupons, but a list of discounts that uses one of them looks the same regardless of which copy was picked.
- **Packing identical boxes.** If two boxes have the same weight, choosing the left one versus the right one does not create a new packing plan. Only how many identical boxes you take matters.

### How it shows up here

After sorting, equal values sit next to each other. At one level of recursion, the first copy of a value is tried, and any later copy with the same value is skipped. That prevents duplicate combinations that differ only in which identical copy was chosen. Advancing the index by one on the recursive call enforces that each input position is used at most once.

Pruning with the remaining target is the same as in Combination Sum: once a candidate is too large, all later candidates are also too large.
