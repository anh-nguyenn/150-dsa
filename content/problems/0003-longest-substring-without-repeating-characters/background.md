A sliding window is a stretch of the sequence with a movable left edge and right edge. The right edge explores new material, and the left edge repairs the window when a rule is broken.

### Everyday examples

- **A playlist with no repeated song.** You keep extending the queue until the next song is already in it, then drop songs from the front until that song is allowed again.
- **A guest list with unique names.** You read invitations left to right. If a name repeats, everyone before the earlier copy must leave before the new guest can join.

### How it shows up here

The window always holds distinct characters. Remember the most recent position of each character. When the new character was last seen inside the window, move the left edge just past that old position. The window length after each step is a candidate answer.
