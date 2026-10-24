An axis-aligned square is determined by one corner and the corner diagonally opposite it. Once those two corners are fixed, the other two corners are forced: they share one coordinate with each diagonal endpoint. Counting squares therefore reduces to looking for a small set of related points.

### Everyday examples

- **Graph paper.** Choosing two opposite corners of a tilted-looking square on grid paper still pins down the two remaining corners exactly.
- **Seating blocks.** If you know the front-left and back-right seats of a rectangular block, the other two seats are at the intersection of their rows and columns.

### How it shows up here

The stored points are kept in a map from coordinate pair to how many times that point was added. For a query point, scan the stored points. A stored point can be the diagonal opposite only when its horizontal and vertical distances from the query are equal and nonzero. When that holds, look up the two side corners in the map. Multiplying the three counts gives the number of squares for that diagonal; summing over all stored points gives the answer.

Scanning all distinct points makes `count` linear in the number of distinct stored points, while `add` stays constant time.
