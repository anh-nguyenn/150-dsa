A level-order traversal, also called breadth-first search, visits a tree one horizontal layer at a time. It holds the nodes still to visit in a queue: remove a node from the front, add its children to the back, and repeat. Because children enter behind every node already waiting, the queue naturally finishes one layer before starting the next.

### Everyday examples

- **A crowd on stadium rows.** If you stand at one end, the last person in each row is the one you see. You still have to count each row to know where it ends.
- **Floors of an office building viewed from outside.** On every floor, the office nearest your side hides the ones behind it. The visible set is one office per floor.

### How it shows up here

The right-side view is the last node processed on each level of a level-order traversal. The queue makes level boundaries explicit: record the queue size before processing a layer, and the final node in that batch is the visible one. The answer always has one value per level, so its length equals the tree's height.

This avoids the tempting shortcut of always following right children. When a right child is missing, a node from the left of that level may be the one exposed to the viewer.
