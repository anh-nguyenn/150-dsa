## Idea

A helper returns the height of a subtree, or -1 as a failure marker if any node inside it breaks the balance rule. Each node checks its two child reports, rejects a difference greater than one, and otherwise returns its own height.

## Why it works

If either child reports -1, the current subtree already contains an unbalanced node, so it also reports -1. Otherwise both child heights are known, and the only remaining requirement at the current node is that they differ by at most one. Returning the real height lets the parent apply the same test. The bottom-up order means each node is visited once, and a failure can short-circuit the rest of that branch.

## Edge cases

- An empty tree is balanced.
- A single node is balanced.
- A chain of three nodes is not balanced: at the top, one side is empty and the other has height 2.
- One unbalanced node deep in a subtree causes every ancestor to report failure.
- Height is measured in nodes, but comparing the two child heights makes the unit irrelevant.
