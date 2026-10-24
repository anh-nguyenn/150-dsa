# Graphs

Graph problems start with a representation: a grid, an adjacency list, or a list of edges. Then they ask what is reachable, connected, or shortest.

Reach for DFS when you need to flood a component, BFS when every edge has the same cost and you need distance, and union-find when the question is about connectivity under additions.

It assumes you mark visited nodes at the right moment and can state what a node's distance or component id means.
