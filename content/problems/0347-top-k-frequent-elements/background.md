Selection asks for the best few items without fully ordering everything. If the scores have a small, known range, you can often avoid sorting by placing items into buckets indexed by their score and then reading the buckets in priority order.

### Everyday examples

- **Word frequency.** A newsroom wants the five most common words in an article. Counting occurrences first is faster than comparing every pair of words.
- **Sales ranking.** A shop groups products by how many units they sold, then walks from the highest sales count downward until it has the requested number of products.

### How it shows up here

Every value has a frequency between 1 and the length of the list. Create one bucket per possible frequency, put each distinct value into the bucket for its count, and scan from the highest bucket downward. This avoids sorting the distinct values.
