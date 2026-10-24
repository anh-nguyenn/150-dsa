A monotonic stack stores indices whose bars are increasing in height. When a shorter bar arrives, it marks the right boundary for the taller bars still on the stack: they can no longer extend past this point. Popping them one by one lets us measure each bar's widest possible rectangle.

### Everyday examples

- **Skyline cutouts.** The largest rectangular sign that fits under a jagged skyline is limited by the lowest point above it and the gaps between taller structures.
- **Shelves under a sloped ceiling.** A rectangular cabinet can only be as tall as the lowest point of the ceiling above its width.
- **Filling a container.** Water poured over an uneven floor spreads until a lower wall or the edge stops it; each section has a natural width.

### How it shows up here

For each bar, the best rectangle using that bar's height extends left and right until it meets a strictly shorter bar. The stack finds those boundaries in one pass. Adding a zero-height sentinel at the end forces every remaining bar to be popped and measured.
