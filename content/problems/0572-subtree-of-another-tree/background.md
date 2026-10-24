A subtree is not just any connected piece of a tree. To count as a subtree, a node must come with every descendant below it, unchanged. This is stricter than finding the same values scattered somewhere in the larger tree.

### Everyday examples

- **A branch of a family tree.** A branch matches only when the starting person and everyone below that person line up, generation by generation.
- **A subfolder in a project.** Copying a folder means copying everything inside it. A similar folder missing one nested file is not the same subfolder.

### How it shows up here

A match can start at any node of `root`, so every node is a candidate. For each candidate, compare its entire subtree with `sub_root` using the same structural-equality test as the "Same Tree" problem. If any candidate matches, the answer is true; otherwise descend and try the children.
