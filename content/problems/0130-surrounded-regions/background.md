Trying to prove that a region is enclosed can be awkward. It is easier to identify the opposite: a region escapes if it touches the border. Flood fill inward from every border `"O"` and mark everything connected to the outside. Whatever remains unmarked is truly surrounded.

### Everyday examples

- **Rooms with windows.** A room is safe from being sealed only if it connects to a room that has an outside window; start at the windows and walk inward.
- **Water leaking from the edge of a map.** Everything reachable from the map boundary stays dry; pockets with no path to the edge do not.

### How it shows up here

Mark every `"O"` reachable from a border with a temporary symbol, using a stack or queue. Then scan the board: unmarked `"O"` cells are enclosed and become `"X"`, while temporary marks return to `"O"`. The temporary symbol prevents border regions from being captured during the final scan.
