The median splits a collection into a lower half and an upper half. When values arrive continuously, rebuilding a sorted list after every insertion is expensive. Two heaps let us keep the halves separate and expose only their boundary values.

### Everyday examples

- **Price tracking.** A store watches the median sale price throughout the day so a single expensive item does not distort the typical price.
- **Response times.** A service dashboard reports the median request latency, and the median must update as each new request completes.

### How it shows up here

A max-heap holds the smaller half and a min-heap holds the larger half. Both halves stay nearly the same size, with the max-heap allowed to hold one extra value. The median then comes from one heap root or the average of both roots.
