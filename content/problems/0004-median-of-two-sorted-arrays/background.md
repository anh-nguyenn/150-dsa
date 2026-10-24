The median splits a sorted collection into two halves of nearly equal size. With two sorted arrays, instead of merging them, you can cut each array so that the left sides together hold exactly half the elements and every left value is no larger than every right value. That cut determines the median.

### Everyday examples

- **Two queues merging at a gate.** Each queue is ordered. The middle arrival across both queues can be identified by comparing the last person taken from each queue.
- **Two sorted stacks of cards.** You want the middle card without interleaving every card. A clean split puts the same number of cards on each side while keeping every left card no larger than every right card.
- **Two salary bands.** Combining two sorted salary lists, the midpoint salary can be found by balancing how many entries come from each list below the split.

### How it shows up here

Binary search the cut position in the shorter array. The cut in the longer array follows from the required half size. If the largest left value is at most the smallest right value, the cut is valid. Otherwise shift the cut left or right until the crossing condition holds. The median then comes from the boundary values around the cut.
