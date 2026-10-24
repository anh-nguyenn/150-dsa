A decimal number can be taken apart from the right: the remainder after dividing by 10 is the last digit, and integer division by 10 removes it. Building a new number by repeatedly appending these digits reverses their order.

The tricky part is that computers limit how large an integer can be. A reversed value can overflow even when the original input fits, so the range must be checked before returning.

### Everyday examples

- **Reading a receipt backwards.** You copy the last digit first, then the next-to-last, and so on.
- **Turning a line around.** The person at the back of the line steps to the front repeatedly, producing the reverse order.

### How it shows up here

Work with the absolute value, repeatedly extract the last digit with `% 10`, and append it with `result = result * 10 + digit`. Apply the original sign afterward, then compare against `-2^31` and `2^31 - 1`; return 0 when the result is outside those bounds.
