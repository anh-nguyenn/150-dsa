## Hint 1

Which `O` regions can never be captured, no matter how large they are?

## Hint 2

A region survives exactly when it touches the border. How can you find every region that touches the border without testing regions one by one?

## Hint 3

Flood fill from every border `O` and mark what you reach. Then turn every unmarked `O` into `X` and restore the marked cells to `O`.
