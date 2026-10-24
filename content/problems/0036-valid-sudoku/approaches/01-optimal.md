## Idea

Maintain nine row sets, nine column sets, and nine box sets. Visit each cell once, skip dots, compute the box index, and reject a digit that already appears in its row, column, or box.

## Why it works

A digit is legal only if it is new to all three groups that contain its cell. The box index `(r // 3) * 3 + c // 3` numbers the nine boxes from 0 to 8 without overlap, so every cell updates exactly the box it belongs to. If the whole board is processed without a collision, no row, column, or box contains a repeated digit.

## Edge cases

- A completely empty board is valid because dots are ignored.
- A duplicate in a row, column, or box is caught by the corresponding set.
- A digit repeated in different boxes in different rows and columns is legal.
- A board can be valid without being complete or solvable.
- The board size is fixed, so the running time and the number of sets are constant.
