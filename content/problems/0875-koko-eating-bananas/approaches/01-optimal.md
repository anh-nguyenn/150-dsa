## Idea

Binary search the eating speed. For each candidate, compute the total hours using ceiling division per pile. If the total fits the deadline, record the candidate by moving the upper bound down; otherwise move the lower bound up. The bounds meet at the smallest feasible speed.

## Why it works

Ceiling division gives the exact number of hours for a pile: the pile needs `floor((pile - 1) / speed) + 1` hours, which the expression `(pile + speed - 1) // speed` computes. Total hours never increase as speed rises, so feasibility is monotonic. Binary search can therefore discard every speed below a feasible one and every speed above an infeasible one, leaving the minimum feasible speed.

## Edge cases

- A speed equal to the largest pile finishes every pile in one hour, which is always enough because `h` is at least the number of piles.
- A single pile with a deadline equal to its size allows a speed of 1.
- A single huge pile may require the pile's full size as the speed when only one hour is available.
- Equal piles need separate hours; they are not combined.
- The upper bound only needs to reach the maximum pile, since larger speeds cannot improve on one hour per pile.
