A dynamic program becomes much simpler when the states form a directed acyclic graph. Each state points only to states that are somehow "later", so a depth-first search that remembers finished states never has to solve the same state twice. This pattern is often called memoized search: recursion describes the choices, and a table stores the answer once per state.

### Everyday examples

- **Climbing a staircase.** From a step you can only go up. The longest route to the top is the same question at every step, so remembering the best result from each step saves repeated work.
- **Following a river downstream.** Water only flows to lower ground. Once you know how far the river runs from a particular bend, asking again later gives the same answer; you do not need to trace it twice.
- **Unlocking skill trees.** A skill may require earlier skills. The deepest chain from a node is fixed by the chains below it.

### How it shows up here

Every cell is a state. An edge goes from a cell to a strictly larger neighbor, so values always increase along an edge and cycles are impossible. A cell's answer is one plus the best answer among its larger neighbors. Caching that value turns an exponential walk into one visit per cell. The grid is small enough that a two-dimensional memo table is inexpensive.
