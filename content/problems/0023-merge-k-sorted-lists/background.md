Merging many sorted streams is different from merging two: the next smallest value could come from any stream. Scanning all `k` current heads at every step would make the merge slow when `k` is large. A priority queue keeps the smallest available head on top instead.

### Everyday examples

- **Merging several dated piles of mail.** Each pile is already sorted by date. At any moment, the next letter to file is the earliest one among the top letters of all piles.
- **Combining multiple sorted playlists.** Each playlist is ordered by title. The next track in the combined list is the alphabetically first track among the current fronts.

### How it shows up here

The current front of each linked list is a node. Push every non-empty head into a min-heap keyed by node value. Repeatedly pop the smallest node, append it, and push that node's successor. The heap size stays at most `k`, and each of the `N` nodes enters and leaves the heap once.
