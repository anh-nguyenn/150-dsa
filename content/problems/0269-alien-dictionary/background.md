A topological order arranges the vertices of a directed graph so that every edge points forward. It exists only when the graph has no directed cycle. Kahn's algorithm repeatedly removes a vertex with no incoming edges, appends it to the order, and deletes its outgoing edges.

### Everyday examples

- **Course prerequisites.** If course A must come before course B, any valid study plan is a topological order of the prerequisite graph.
- **Getting dressed.** Socks before shoes and shirt before jacket create precedence rules; a cycle such as tying shoes before putting them on would make the list impossible.
- **Build systems.** Source files depend on generated headers, and a valid compilation order respects those dependencies.

### How it shows up here

Each pair of adjacent sorted words reveals at most one letter ordering: at their first differing character, the letter from the earlier word must come before the letter from the later word. These facts form directed edges. The letters are the vertices, and any topological order satisfies every observed fact. A cycle means the words contradict each other, and an impossible prefix pair also makes the input invalid.
