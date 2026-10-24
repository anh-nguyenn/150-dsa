A cycle in a linked list means the chain loops back on itself. Since there is no natural end, a naive traversal can run forever. Detecting a cycle is therefore about noticing repetition without storing every node you have seen.

### Everyday examples

- **A circular walking track.** Walk long enough and you pass the same landmark again. If the path is a straight trail, eventually you reach the end.
- **Two runners on a track.** One runs at a steady pace and another runs twice as fast. On a loop, the faster runner eventually laps the slower one and they meet; on a straight trail, the faster runner simply finishes.

### How it shows up here

The two runners become two node pointers. The slow pointer moves one link per step and the fast pointer moves two. If the fast pointer falls off the end, the list is finite. If the pointers meet, both are trapped in the same loop.
