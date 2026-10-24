Many problems are really about moving through a network where the network is not drawn for you. Here each word is a node, and two words are neighbors when they differ in exactly one position. The task is then a shortest-path question: how few neighbor steps separate the start word from the target?

### Everyday examples

- **Word games.** Players change one letter at a time, and a good player looks for the shortest route to the target rather than wandering through dead ends.
- **Subway travel.** If every stop is a node and a ride between adjacent stops is an edge, the fewest stops to a destination is a shortest-path problem.
- **Version migration.** Each configuration differs from the next by one setting; finding the fewest configuration changes is the same shape of search.

### How it shows up here

Search outward from `begin_word` one layer at a time. Layer one contains words one change away, layer two contains words two changes away, and so on. Because breadth-first search visits nodes in increasing distance, the first time the target is reached gives the shortest chain. Grouping words by wildcard patterns makes it cheap to find every one-letter neighbor of a word.
