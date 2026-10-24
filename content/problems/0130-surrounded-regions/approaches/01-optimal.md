## Idea

Flood fill from every border `"O"` and mark the reached cells with a temporary symbol. Afterward, every `"O"` still unmarked is surrounded, so change it to `"X"`; turn the temporary marks back into `"O"`.

## Why it works

A cell is not captured exactly when some path of `"O"` cells connects it to the border, and the flood fill from the border finds precisely those cells. Everything else is enclosed. The three-valued board lets the final pass distinguish captured regions from surviving ones without a separate visited array.

## Edge cases

- A single cell on the border survives even if it is `"O"`.
- An all-`"X"` board is unchanged.
- A border-connected ring of `"O"` must survive intact.
- An `"O"` region inside the board with no border connection is captured.
- Empty boards return without changes.
