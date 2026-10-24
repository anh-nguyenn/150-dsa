Intervals describe a range on a number line. Two closed intervals overlap when neither ends strictly before the other begins. Merging replaces an overlapping group with the smallest single interval that covers all of them.

### Everyday examples

- **Calendar blocks.** A new meeting may swallow several adjacent existing meetings and must leave the day's schedule tidy.
- **Rental bookings.** Extending a reservation can overlap the next booking, so the front desk combines them into one occupied period.
- **Road closures.** A newly announced closure may overlap existing lane closures; the union is what drivers experience.

### How it shows up here

Because the existing intervals are sorted, the work splits into three phases: copy intervals that end before the new one starts, merge every interval that begins before the growing new interval ends, then append the rest. The new interval may also touch an existing one at a single point, so the comparison uses `<=` on the merge side.
