## Idea

Sort the cars by starting position from closest to farthest. Scan in that order, computing each car's arrival time as if it drove alone. Maintain the arrival time of the most recently formed fleet ahead. A car with a later arrival starts a new fleet; otherwise it merges into the fleet ahead.

## Why it works

Closer cars constrain farther cars, never the other way around. If a car behind would arrive no later than the fleet directly ahead, it must catch that fleet and join it, so it neither adds a fleet nor changes the fleet's arrival time. If it would arrive later, it never catches the fleet ahead and becomes the front of a new fleet. Scanning nearest-first therefore counts every fleet exactly once at its front car.

## Edge cases

- A single car always forms one fleet.
- Equal arrival times merge, so a tie does not create a new fleet.
- If every car has the same speed, no one catches anyone and each car is its own fleet.
- Cars may start at position 0.
- A car that catches a fleet exactly at the target still belongs to that fleet.
