Choosing the largest set of mutually compatible activities is a classic greedy problem. Sorting by finishing time and always taking the activity that ends earliest leaves the most room for later activities. Any optimal solution can be exchanged for one that starts with the earliest finisher.

### Everyday examples

- **Booking a conference room.** You want the most meetings possible in one room; favouring the meeting that frees the room soonest leaves the largest gaps.
- **Watching talks.** At a festival, attending the talk that ends earliest lets you consider more of the remaining schedule.
- **Machine jobs.** Scheduling the job that finishes first maximizes the number of jobs completed.

### How it shows up here

Keep as many intervals as possible; the number removed is the rest. Sort by end time, keep the end of the last accepted interval, and reject any interval that starts before that end. Rejected intervals are the ones to remove.
