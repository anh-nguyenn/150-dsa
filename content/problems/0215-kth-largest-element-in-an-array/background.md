Selection asks for one ranked item without fully sorting a collection. A heap can maintain a small candidate set, while quickselect partitions the array around a pivot. Both avoid the cost of ordering every element when only one rank is needed.

### Everyday examples

- **Exam results.** A course wants the score of the student ranked fourth, not the full ranked roster.
- **Sales dashboard.** A report highlights the third-best sales day of the month while ignoring the exact order of all other days.

### How it shows up here

We keep the k largest values in a min-heap. The root is the smallest of those candidates, which is the kth largest overall. Each new value is inserted, and whenever the heap exceeds k values, its root is discarded. This bounds both the memory and the work per element.
