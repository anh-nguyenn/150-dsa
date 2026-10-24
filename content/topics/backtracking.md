# Backtracking

Backtracking explores a decision tree. At each level you choose, recurse, then undo the choice. Pruning removes branches that cannot lead to a valid answer.

Reach for it when the answer is a collection of combinations, permutations, partitions, or placements, and the input is small enough for exponential search with pruning.

It assumes you can define the choice set at each level and the condition that makes a partial answer invalid.
