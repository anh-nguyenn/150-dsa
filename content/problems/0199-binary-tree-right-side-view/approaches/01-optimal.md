## Idea

Process the tree level by level with a queue. At the start of each level, note how many nodes are waiting. Remove exactly that many nodes, appending their children as you go, and keep the value of the final node removed from the level. Those final values form the right-side view.

Recording the level size is what separates one layer from the next; without it, the queue would blend levels together.

## Why it works

Every node sits on exactly one level, and the right-side view contains exactly the last node visited on each level. A breadth-first queue visits nodes in level order, with all of a level's nodes ahead of the next level's. Therefore the last node in each batch is the rightmost one for that level. Each node enters and leaves the queue once, so the traversal is linear in the number of nodes.

## Edge cases

- A tree whose right side is empty partway down: the leftmost node on that level becomes visible instead.
- A single-node tree returns just that value.
- A left-heavy tree still produces one value per level.
- The queue holds at most the widest level, so auxiliary memory follows the tree's width rather than its node count.
