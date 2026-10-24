Counting the rooms in use over time is a sweep-line problem. As meetings start and end, the number of active meetings rises and falls; the maximum concurrent count is the number of rooms required. Alternatively, process meetings by start time and keep a min-heap of the end times of rooms currently in use.

### Everyday examples

- **Restaurant tables.** Diners arrive and leave. The staff needs as many tables as the busiest moment requires.
- **Server capacity.** Requests occupy workers for a while; the peak overlap of requests sets the minimum pool size.
- **Washroom stalls.** The number of stalls needed equals the largest number of people inside at once.

### How it shows up here

Sort the meetings by start time. A min-heap stores the end time of each room currently occupied. Before placing a new meeting, if the earliest ending room is already free, reuse it; otherwise open a new room. The heap's final size is the minimum number of rooms.
