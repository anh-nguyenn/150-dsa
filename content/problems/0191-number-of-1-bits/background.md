Computers store integers as bits. A frequent task is to measure how many of those bits are switched on, which is useful for error detection, compression, and low-level performance tricks.

A neat identity is `n & (n - 1)`. Subtracting one flips the lowest set bit to 0 and turns all lower zeros into ones; ANDing with the original number removes that lowest set bit while leaving the rest unchanged.

### Everyday examples

- **Packing a suitcase.** You remove one item per trip. Counting the trips tells you how many items were packed, and each removal is guaranteed to make the load smaller.
- **Turning off lamps.** A row of lamps is on or off. A switch that turns off the rightmost lit lamp each time lets you count lit lamps by counting switch flips.

### How it shows up here

Repeatedly applying `n &= n - 1` clears one set bit per iteration. The number of iterations is exactly the number of 1s, so the loop stops as soon as the value becomes zero.
