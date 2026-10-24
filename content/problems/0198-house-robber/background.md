Dynamic programming is useful when each decision rules out a neighbour and you want the best overall combination. You summarize the past with a small state: the best total achievable up to a certain point.

### Everyday examples

- **Freelance jobs.** Each job lasts a day and pays a fee, but after taking one you need a rest day before the next. You want the largest income over the calendar.
- **Market stalls.** You sample stalls along one aisle and never visit two neighbouring stalls, because each pair sells the same thing. The best set is chosen one stall at a time.

### How it shows up here

Let `best[i]` be the maximum haul from the first `i + 1` houses. At house `i` you either skip it, keeping `best[i-1]`, or take it and add its money to `best[i-2]`. The larger of those two choices becomes `best[i]`.
