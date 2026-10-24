For a window to become one repeated character, every position that is not the target character must be changed. The cheapest target is whichever character already appears most often in the window, because it needs the fewest replacements.

### Everyday examples

- **Repainting a row of tiles.** With a limited number of repaints, you want the longest run of matching tiles. The best color to paint toward is the one already dominating that stretch.
- **Correcting a typed word.** If you can fix a few letters, the longest fixable section is the one where a single letter already appears most often.

### How it shows up here

Maintain a window and character counts. Let `max_count` be the highest frequency of any one character in the window. The window can be made uniform exactly when its length minus `max_count` is at most `k`. Expand the right edge; when the budget is exceeded, slide the left edge once. The largest window reached is the answer.
