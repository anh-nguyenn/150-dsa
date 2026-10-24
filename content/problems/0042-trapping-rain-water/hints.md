## Hint 1

How much water sits on a single position?

## Hint 2

That amount depends on the tallest bar to its left and the tallest to its right. Can you know the smaller of those two without storing both arrays?

## Hint 3

Keep a left pointer with its running maximum and a right pointer with its own. Process the side whose current bar is shorter, because the other side already guarantees a wall at least that high.
