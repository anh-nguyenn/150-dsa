Copying a graph is harder than copying a list because graphs contain cycles. If you follow neighbors naively, you can keep arriving at nodes you already copied, creating duplicates or looping forever. The standard remedy is a lookup table from each original node to its copy.

### Everyday examples

- **Photocopying a road map.** Each junction is copied once; roads between junctions are then drawn between the existing copies instead of creating new junctions.
- **Duplicating a friendship network.** You create a new profile for every person exactly once, then connect the new profiles the same way the originals are connected.

### How it shows up here

Start from the given node, create its copy, and record it in a map. Walk the graph with a stack or queue. For each neighbor, create a copy only if it is missing from the map, then add the mapped copy to the current copy's neighbor list. Reusing map entries keeps cycles from exploding.
