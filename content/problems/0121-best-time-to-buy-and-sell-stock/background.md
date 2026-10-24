A running minimum is a one-pointer pattern: while scanning forward, remember the best earlier opportunity and combine it with the current value. It turns a search over pairs into a single pass.

### Everyday examples

- **Market shopping.** You see prices day by day and remember the cheapest price so far. Today's gain is today's price minus that remembered low.
- **Timing a run.** You track your fastest split so far and compare each new split against it. You never need to remember every earlier split, only the best one.

### How it shows up here

At each day, the best possible buy is the cheapest price seen strictly before it. Track that minimum and the best profit. For each price, first measure the profit using the prior minimum, then update the minimum with today's price. Failing to update in that order could create a trade that sells before it buys.
