## Idea

For every node of `root`, compare the subtree rooted there with `sub_root`. The comparison checks value equality and recurses into corresponding children, so it requires the shapes to match too. If the comparison fails, search the left and right children of `root`.

## Why it works

A subtree of `root` is exactly the full subtree rooted at one of its nodes. The search tries every possible root, and `same` accepts only an exact structural and value match. Therefore a true result means some node's entire subtree equals `sub_root`, and a false result means no such node exists. The `root is None` base case is reached only after all candidates have failed.

## Edge cases

- A single-node `sub_root` matches any node with the same value, including a leaf or an internal node.
- A candidate can share the top value with `sub_root` and still fail deeper down because of one extra or missing child.
- A deep chain can make the repeated comparisons take O(m * n) time in the worst case.
- The stated constraints have at least one node in each tree, but the code treats an empty `sub_root` as a match and an empty `root` as a failure.
- Comparing values before structure can reject quickly, but the structural check is still required.
