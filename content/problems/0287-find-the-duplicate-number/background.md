A functional graph has one outgoing edge from every node. Here each index `i` is a node, and the value `nums[i]` tells you which node comes next. Because there are more indices than possible values, two indices must point to the same value, and following those pointers creates a cycle.

### Everyday examples

- **A treasure hunt with repeated clue numbers.** Each clue sends you to another clue number. If one number is used twice, two different places lead to the same clue, and walking the clues eventually loops.
- **A filing system with a shared cabinet.** Two folders can point to the same cabinet even though each folder has only one pointer. The shared cabinet is the repeated destination.

### How it shows up here

The duplicate value is exactly the entrance to the cycle in the index graph. Floyd's slow-and-fast pointers detect that a cycle exists, and a second phase finds where the cycle begins. That entrance index is the repeated number, found without a hash set and without touching the array.
