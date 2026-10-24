When many queries ask the same kind of question about a static collection, it often pays to answer them offline: sort the queries and sweep through the data once, maintaining a data structure that represents exactly the candidates relevant to the current query.

### Everyday examples

- **Store coverage.** For each customer location, find the nearest branch whose delivery radius covers it. Sorting locations lets one pass add and expire candidate branches.
- **Umbrella sizes.** For each person at a position on a rainy street, find the smallest umbrella that covers them. As you walk down the street, umbrellas enter and leave consideration.
- **Signal towers.** For each device, find the smallest tower whose range includes it; sorting devices by position lets towers enter and leave the active set.

### How it shows up here

Sort intervals by start and queries by value. Sweep queries from smallest to largest, adding every interval whose start has been reached into a min-heap keyed by length. Remove intervals that end before the current query. The heap top is then the shortest interval covering the query. Answers are written back in the original query order.
