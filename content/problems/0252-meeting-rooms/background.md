Two time ranges overlap when one starts strictly before the other ends. For a whole collection, the simplest test is to put the ranges in start-time order: if any range begins before the previous one ends, two meetings collide.

### Everyday examples

- **A day of appointments.** Sorting the day's appointments by start time quickly reveals whether anything is double-booked.
- **Busy calendar.** A new invitation conflicts if its start falls inside an existing event.
- **Equipment sign-out.** Checking that no two reservations for the same projector overlap keeps the schedule feasible.

### How it shows up here

Sort by start time, then compare each meeting's start with the end of the meeting immediately before it. Because sorting puts the earliest start first, that adjacent check catches every possible conflict. Touching endpoints are fine, so the comparison is strict.
