This is a reuse-allowed optimization problem. You build the answer for every amount from 0 upward, and each new amount borrows from a smaller amount that is already solved.

### Everyday examples

- **Cash register.** Making 63 cents from 25, 10, 5, and 1 cent coins is easier if you first know the best way to make every smaller amount.
- **Postage stamps.** With stamps of fixed values, the fewest stamps for a total is found by trying each stamp as the last one added.
- **Filling a container.** Repeating identical weights to hit a target weight has the same "what was the last unit?" structure.

### How it shows up here

Suppose the final coin used for amount `x` has value `c`. Before that coin, the total was `x - c`, and the rest of the solution is an optimal way to make `x - c`. Trying every denomination as the last coin and taking the smallest resulting count gives the optimum. Amounts that never become reachable stay marked as impossible.
