Level-order traversal visits a tree breadth first: the root, then all nodes one level down, then all nodes two levels down, always left to right. It is the same order used by the level-order lists that describe trees in this exercise.

### Everyday examples

- **A building tour by floor.** You visit every room on the ground floor before moving to the first floor, and within a floor you go left to right.
- **Ripples in water.** The disturbance spreads outward one ring at a time, so the nearest ring is fully reached before the next one.

### How it shows up here

A queue naturally produces breadth-first order: remove a node, add its children to the back, and repeat. The only extra detail is grouping. Recording the queue's size before processing a round tells you exactly how many nodes belong to the current level, so the traversal can emit one inner list per level.
