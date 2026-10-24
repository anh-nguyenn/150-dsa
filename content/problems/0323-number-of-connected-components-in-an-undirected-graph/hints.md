## Hint 1

If there were no edges at all, how many components would there be? Use that as your starting count.

## Hint 2

An edge between two nodes in different groups merges those groups. What should happen to the count of groups?

## Hint 3

Maintain disjoint sets for the nodes. Merge the endpoints of each edge only when they have different roots, decreasing the component count for each successful merge.
