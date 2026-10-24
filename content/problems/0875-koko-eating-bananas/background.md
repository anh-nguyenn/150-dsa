Sometimes the answer itself can be searched rather than the input. If a candidate speed works, every larger speed also works, so the feasible speeds form a suffix of the number line. That monotonic property allows binary search over the range of possible answers.

### Everyday examples

- **Setting a minimum delivery rate.** If a courier can finish a route in time at a certain speed, any faster speed also finishes in time, so you can search for the slowest acceptable speed.
- **Choosing oven power.** If a dish cooks through at a given power, higher power also cooks it through; the useful question is the lowest setting that works.
- **Budgeting workers.** If a team size meets a deadline, a larger team also meets it, so the smallest sufficient team can be found without testing every size.

### How it shows up here

The speed ranges from 1 to the largest pile. For a candidate speed, add up the hours each pile needs. If the total is within the deadline, try a smaller speed; otherwise try a larger one. The first feasible speed is the answer.
