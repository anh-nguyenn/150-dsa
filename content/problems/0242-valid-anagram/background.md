Counting is the bridge between two arrangements of the same material. If order is irrelevant, the only information left is how many of each item you have. Two collections match exactly when their count tables match.

### Everyday examples

- **Scrabble racks.** Two players have anagrams of each other when their racks hold the same letters in the same quantities, even if the tiles sit in a different order.
- **Recipe ingredients.** Two shopping bags contain the same recipe if they have the same number of eggs, onions, and so on. The order inside the bag tells you nothing.

### How it shows up here

The two strings are the bags and the letters are the ingredients. Count letters in one string and subtract the counts for the other. If every count returns to zero, the strings are rearrangements of each other. Checking length first avoids counting when a match is impossible.
