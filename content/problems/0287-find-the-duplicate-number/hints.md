## Hint 1

Treat each index as a node and its value as a pointer to another index. Why must this graph contain a loop?

## Hint 2

If one pointer moves one index at a time and another moves two, where do they meet, and how could you locate the loop's entrance?

## Hint 3

Run slow and fast from index 0 until they meet. Then put one pointer back at 0 and move both one step at a time; the index where they meet again is the duplicate value.
