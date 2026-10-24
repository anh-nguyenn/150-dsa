## Hint 1

Compare both target values with the current node. In a BST, what does it mean if both are smaller? If both are larger?

## Hint 2

If the two values fall on opposite sides of the current node, can their paths meet any lower than this node?

## Hint 3

Start at the root. Move left while both values are smaller and right while both are larger. Stop at the first node where neither condition holds and return its value.
