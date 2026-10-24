## Idea

Track the total surplus over the whole circle and the tank balance since the latest candidate start. If the tank goes negative at a station, discard every start up to that station, begin again after it, and reset the tank. The total decides whether any start works.

## Why it works

Suppose a candidate start fails at station `j` because the tank becomes negative. Any start between the candidate and `j` also fails: it skips some early surplus that the original candidate had, so its balance at `j` is no better. Thus the entire block can be skipped safely. If total fuel is at least total cost, the remaining suffix must have enough surplus to finish the lap, making the last candidate valid.

## Edge cases

- One station succeeds exactly when its fuel covers its cost.
- Equal total fuel and cost can still have a unique valid start.
- A negative overall total means no start works.
- Starting near the end of the array is fine; the circuit wraps around.
- A station with zero fuel and zero cost neither helps nor hurts the balance.
