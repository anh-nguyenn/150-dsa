## Idea

Track the range of possible numbers of unmatched opening parentheses after each prefix. Update the low and high ends according to whether the character is an open, a close, or a star, clamping the low end at zero. Reject as soon as the high end becomes negative, and accept at the end only if zero is inside the range.

## Why it works

All counts between the low and high ends are achievable because a star can be switched between closing, doing nothing, and opening. A negative high means even using every star as an opening cannot offset the closes, so the prefix is already invalid. When the high is non-negative throughout, keeping the low at zero is safe: any excess closes below zero can be avoided by an interpretation that did not create them. Ending with low zero means some interpretation closes every open parenthesis.

## Edge cases

- The empty string is valid and returns true.
- A string made only of stars is always valid.
- A single opening parenthesis cannot be closed, so it is invalid.
- A single closing parenthesis is invalid immediately.
- Stars can be left unused, so they do not force extra opens or closes.
- Too many opens can exceed what the stars can close.
- A negative high is detected early, even if later stars appear.
