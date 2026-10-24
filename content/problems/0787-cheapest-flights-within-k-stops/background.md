When a path is limited by the number of edges it may use, it helps to think of the graph as a stack of layers, one per allowed flight. Each round relaxes edges using only the prices computed in the previous round, so one more flight is allowed. This is the bounded form of Bellman-Ford.

### Everyday examples

- **Connecting flights.** A traveller accepts at most two layovers. Each additional layover opens new routes but also consumes one unit of the budget.
- **Relay race.** A message may pass through a fixed number of relays. The cost of a relay chain is the sum of the hops, and the chain length is capped.
- **Supply chain.** Goods may change hands at most a set number of times; each handoff has a cost.

### How it shows up here

Flights are directed weighted edges and stops are the allowed number of intermediate cities. Relaxing every edge `k + 1` times, while always reading prices from the previous relaxation, computes the cheapest route with at most that many flights. Reading and writing the same array would accidentally allow more flights than permitted.
