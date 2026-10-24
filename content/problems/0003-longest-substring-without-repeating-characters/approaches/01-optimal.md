## Idea

Grow a window to the right and record each character's latest index. If the new character repeats inside the window, move the left edge just past its previous occurrence.

## Why it works

The window before each step contains only distinct characters. A repeat can only involve the previous occurrence of the new character. Moving left past that occurrence removes the only conflict; any earlier occurrences are already outside. The window is then the longest distinct substring ending at the current position, so taking the maximum over all right endpoints gives the global answer.

## Edge cases

An empty string returns zero. A string of one repeated character returns one. A repeat that occurred before the current left edge should not move the window, which is why the code checks `last[ch] >= left`. Spaces and punctuation are treated like any other character.
