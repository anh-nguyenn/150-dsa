A connected component is a cluster of nodes that hang together. Within a component there is a path between every pair; between different components there is no path at all. Counting components means asking how many separate clusters the network splits into.

### Everyday examples

- **Friend groups.** People are linked when they know each other. Two people in the same group are connected through a chain of acquaintances, while separate groups share nobody.
- **Islands and bridges.** Islands joined by bridges form one landmass for travel purposes, and an island with no bridge is its own component.
- **Computer networks.** Machines in one subnet can route to each other; an isolated machine still counts as a group of one.

### How it shows up here

Start by imagining every node as its own tiny component, so the count is `n`. Each edge either joins two previously separate components, lowering the count by one, or falls inside a component that is already joined and changes nothing. A disjoint-set structure tracks which nodes are currently grouped together, making each union decision fast.
