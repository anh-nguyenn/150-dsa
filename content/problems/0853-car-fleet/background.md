When objects move at constant speeds along the same line, arrival time is distance divided by speed. Sorting by starting position turns the problem into a sweep from the cars nearest the target backward. A car joins the fleet ahead exactly when it would arrive no later than that fleet.

### Everyday examples

- **Runners merging on a track.** A faster runner who reaches a slower runner cannot pass on a narrow path, so they finish together.
- **Cars in a tunnel.** A slow car in front holds up faster cars behind it; they bunch up rather than overtake.
- **Conveyor items.** Items moving toward the same exit merge when one catches another, and the group moves at the slower pace.

### How it shows up here

Process cars from closest to the target to farthest. Compute each car's solo arrival time. If that time is later than the fleet immediately ahead, the car cannot catch it and starts a new fleet. If it is earlier or equal, the car merges into the existing fleet, which is governed by the slower arrival time.
