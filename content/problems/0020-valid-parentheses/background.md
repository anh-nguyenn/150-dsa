A stack is a pile where the last thing added is the first thing removed. That last-in, first-out rule is exactly what nested structure needs: the newest unfinished item is the one you must deal with next.

### Everyday examples

- **Plates.** You stack clean plates on top of one another and take the top plate first. Reaching the bottom plate means removing everything above it.
- **Undo history.** The most recent edit is the first one undone. Earlier edits wait until the newer ones are dealt with.
- **Nested boxes.** To open the innermost box, you first open the box that contains it. The boxes close in the reverse order they were opened.

### How it shows up here

Each opening bracket creates a promise that must be settled before any older promise. A closing bracket should match the most recently opened bracket that is still waiting. If it matches, that promise is settled and removed. If it does not match, the nesting is broken. At the end, no promises may remain.
