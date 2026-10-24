Exponentiation is repeated multiplication, but the repetition can be compressed. Squaring a value doubles its exponent, so powers whose exponents are powers of two are cheap to build. Any exponent can be written as a sum of powers of two, which means the answer can be assembled from a small number of those squared values.

### Everyday examples

- **Folding paper.** Each fold doubles the number of layers, so the layer count grows by repeated doubling rather than by counting one layer at a time.
- **Doubling a savings balance.** If the balance doubles every period, computing its value after many periods uses powers of two rather than adding the interest period by period.

### How it shows up here

The binary digits of `n` say which squared powers of `x` belong in the product. A negative exponent means the reciprocal base is raised to the positive version of the exponent. Because the exponent is halved each round, the loop runs about as many times as the exponent has bits.
