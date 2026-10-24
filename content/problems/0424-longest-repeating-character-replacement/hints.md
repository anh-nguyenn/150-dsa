## Hint 1

For a window to become one repeated character, which character should the window target?

## Hint 2

The cheapest target is the character that already appears most often in the window. What is the cost of making the rest match it?

## Hint 3

Expand right and keep counts plus the largest count seen. If window length minus that count exceeds k, slide the left edge once. The best window size only grows.
