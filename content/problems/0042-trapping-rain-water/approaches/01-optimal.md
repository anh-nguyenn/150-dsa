## Idea

Walk inward from both ends, tracking the tallest bar seen on each side. Process the shorter side, because the taller opposite side guarantees that the lower surrounding wall is already known.

## Why it works

For the side being processed, the opposite current bar is at least as tall as the current bar. Thus the true limiting wall for that position is the larger of its own side maximum and the opposite bar, which equals its own side maximum. Any water it can hold is determined there, so adding the difference and advancing is safe. Every position is processed once.

## Edge cases

A single bar, a strictly increasing row, or a strictly decreasing row traps nothing. Zero-height bars can still receive water if both surrounding walls are taller. Arrays with equal maximum heights on both sides are handled by the `else` branch without double counting.
