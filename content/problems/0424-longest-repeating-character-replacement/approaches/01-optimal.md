## Idea

Slide a window and track how often each character appears. A window of length `L` with most frequent count `M` costs `L - M` replacements; keep that cost within `k`.

## Why it works

For any window, making every character match the most common one costs exactly the number of other characters, which is the minimum possible cost. If that cost is within `k`, the window is achievable. The window only shrinks when no achievable window of that size exists at the current right edge, so the largest size ever recorded is optimal. Reusing the largest count seen is safe because a stale larger count can only keep the recorded width from shrinking, not invent a wider achievable window.

## Edge cases

When `k` is zero, the answer is the longest run already equal. A one-character string returns one. A string with all distinct letters and a small budget returns at most `k + 1`. When `k` is at least the window length, the whole string qualifies.
