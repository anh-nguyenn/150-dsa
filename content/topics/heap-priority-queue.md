# Heap / Priority Queue

A heap keeps the smallest or largest element available without keeping the whole collection sorted. It is the right tool when you repeatedly need the current extreme.

Reach for it for top-k problems, streaming medians, merging sorted streams, and scheduling by the next available time. A heap of size k turns an O(n log n) sort into O(n log k) when only k candidates matter.

It assumes you know whether the heap should hold candidates or rejections, and what the heap's size means.
