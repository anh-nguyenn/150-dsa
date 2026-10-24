## Hint 1

A square with the query point as one corner also has a diagonally opposite corner among the stored points. What must be true of the two coordinate differences?

## Hint 2

Once a stored point is chosen as the opposite corner, which two points would complete the square, and how can a hash map check whether they exist?

## Hint 3

For each stored point at equal nonzero horizontal and vertical distance, multiply the count of that diagonal point by the counts of the two side corners. Sum the products.
