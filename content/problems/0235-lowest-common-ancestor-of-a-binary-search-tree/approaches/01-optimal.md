## Idea

Walk down the BST from the root. While both values are smaller than the current node, the answer must be to the left; while both are larger, it must be to the right. The first node that does not send both values the same way is the split point and the answer.

## Why it works

If both values are below the current node, the BST property puts both of them in the left subtree, so the current node cannot be the lowest common ancestor and neither can anything to the right. The same reasoning applies symmetrically when both are above. Otherwise the values lie on different sides or one equals the current value, so the current node is an ancestor of both and no descendant can contain both. Hence it is the lowest common ancestor.

## Edge cases

- One target equals the current node: the current node is an ancestor of the other, so it is returned immediately.
- One target is an ancestor of the other: the walk stops at that ancestor.
- A left-skewed or right-skewed BST still follows a single path.
- The constraints guarantee both values exist and differ; the final fallback is unreachable for valid input.
- Returning a value rather than a node is deliberate, matching the testable signature described above.
