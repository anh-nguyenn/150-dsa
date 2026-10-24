# Sliding Window

A sliding window keeps a contiguous range and updates it as the range grows or shrinks. The goal is to avoid rescanning the whole range after every change.

Reach for it when the answer is a longest, shortest, or fixed-size subarray or substring, and when adding or removing one element is cheap. The window boundary changes for a reason: a violated constraint, a better candidate, or a fixed size.

It assumes you can define the window state and prove that shrinking never discards the answer.
