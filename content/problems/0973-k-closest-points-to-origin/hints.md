## Hint 1

How can you compare distances without computing a square root? What quantity still gives the same ordering?

## Hint 2

You only need k answers, so keeping all n distances may be wasteful. Which candidate is safe to discard when a better one appears?

## Hint 3

Maintain a max-heap of size k keyed by squared distance. If a new point is closer than the heap maximum, remove that maximum and insert the new point.
