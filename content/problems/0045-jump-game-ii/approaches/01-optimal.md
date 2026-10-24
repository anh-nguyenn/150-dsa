## Idea

Treat the array as an implicit graph and explore it in layers. The current layer is the range of indices reachable with the jumps used so far. Scan that range to find the farthest index reachable with one more jump, then advance the layer boundary and count the jump.

## Why it works

If a set of indices is reachable in `k` jumps, every index between the nearest and farthest of them is also reachable, because jumps can stop short. Therefore the boundary of the layer is enough to describe it. Expanding from every index in the layer finds the true farthest point of layer `k + 1`. Counting layers gives the minimum number of jumps, since each layer corresponds to one additional jump.

## Edge cases

- A one-element array returns zero because no movement is needed.
- A zero jump at the start is only possible when the array already has one element, given the reachability guarantee.
- Jumps that overshoot the end are fine; the boundary may extend past the last index.
- The loop intentionally stops before the last index so reaching it does not add an unnecessary layer.
- Zeros inside a layer do not shrink the layer, since other indices in the same layer may reach farther.
