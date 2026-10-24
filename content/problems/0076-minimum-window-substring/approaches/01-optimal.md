## Idea

Expand the right edge until the window contains all of `t`, then shrink the left edge while it still does. Every valid window's shortest version is recorded.

## Why it works

The window is valid exactly when `missing` is zero. For each right edge, the inner loop removes every unnecessary left character, so the last window recorded before validity is lost is the shortest valid window ending at that right edge. Every possible valid window is considered this way, so the smallest recorded length is globally minimal.

## Edge cases

If `s` is shorter than `t` or lacks a required letter, the answer is empty. Repeated letters in `t` raise the required count and are tracked in `need`. Characters outside `t` get negative counts and can be safely shrunk away. A one-character match returns that character.
