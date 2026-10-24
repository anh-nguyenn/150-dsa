## Hint 1

Which two things must each operation know: the value for a key, and the key's position in the recency order?

## Hint 2

A hash map finds a value fast but does not track order. What linked structure lets you move an item to the front and remove the last item in constant time?

## Hint 3

Combine a map from key to node with a doubly linked list. Keep the most recent node at the front and evict from the back, updating both structures together.
