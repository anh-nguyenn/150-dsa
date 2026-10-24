## Hint 1

When the window moves right, which old candidates can never become the maximum again?

## Hint 2

If a new value is at least as large as values behind it, those older values are dominated. What structure keeps only the useful candidates in order?

## Hint 3

Use a deque of indices with decreasing values. Remove indices that fall out of the window and smaller values at the back before adding the new index. The front is the window maximum.
