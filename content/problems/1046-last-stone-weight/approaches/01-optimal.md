## Idea

Store each weight as a negative number in a min-heap. The smallest negative value corresponds to the heaviest stone. Each round pops the two heaviest stones and pushes the difference back if it is nonzero.

The loop stops when zero or one stone is left. An empty heap means everything cancelled, so the answer is 0.

## Why it works

Because the heap always exposes the maximum available weight, each pop removes one of the two heaviest stones exactly as the rules require. Every round reduces the number of stones by at least one, so the simulation terminates. The surviving value is precisely the result of applying the smashing rule until no pair remains.

## Edge cases

- A single stone is returned unchanged.
- Two equal stones cancel, leaving 0.
- An odd number of stones can leave one survivor.
- Large weights are handled the same as small ones; only differences matter.
