A circular route is a sequence of gains and losses. At each station the tank changes by `gas[i] - cost[i]`. Completing the circuit means that no prefix of this sequence, starting from the chosen station, ever drops the tank below zero. The right starting point is the one that keeps the running balance from going negative.

### Everyday examples

- **A road trip.** Each town has a fuel station and the next leg consumes a known amount. You look for the town where starting with an empty tank still gets you all the way around.
- **A monthly budget.** Deposits arrive and bills are due in a repeating cycle. Starting the cycle at a different month can prevent the balance from dipping below zero, even though the yearly total is unchanged.

### How it shows up here

Compute the surplus at every station. If the sum of all surpluses is negative, fuel is short overall and no start can work. Otherwise a valid start exists. Scan from index 0, maintaining a tank balance since the current candidate start. When the tank would go negative, no station from that candidate through the current index can be the start, so move the candidate to the next station and reset the balance.

The final candidate is the unique valid start.
