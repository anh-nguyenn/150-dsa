## Idea

Maintain a stack of indices whose heights increase from bottom to top. When a new height is lower than the top, pop each taller bar, measure its rectangle, and record the best. The new index is its right boundary, and the index now below it on the stack is its left boundary. A final zero clears the stack.

## Why it works

For any bar, the widest rectangle at its height ends just before the nearest strictly shorter bar on each side. The stack keeps unresolved bars in increasing height order, so when a shorter bar arrives, every taller bar on top has found its right boundary. After popping, the next stack index is the nearest shorter bar to the left. Measuring at pop time therefore covers every bar's maximal rectangle. Each index is pushed and popped once, giving linear time.

## Edge cases

- A zero-height bar cannot support a rectangle and also acts as a boundary.
- One bar returns its own area.
- Equal heights do not pop each other, so their combined width is measured when a shorter bar or the sentinel arrives.
- Strictly increasing heights are all cleared by the sentinel.
- Strictly decreasing heights are measured as they are popped by each shorter bar.
- An all-zero histogram returns 0.
