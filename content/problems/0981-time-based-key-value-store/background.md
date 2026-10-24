A versioned record keeps every value together with the time it became active. A lookup at time `t` wants the newest version whose timestamp is at most `t`. Because versions of one key arrive in increasing time order, their timestamps are already sorted, and the wanted version can be found by binary search.

### Everyday examples

- **Price history.** A product has a list of price changes with dates. Asking for the price on a past date means finding the latest change on or before that date.
- **Document versions.** Each save creates a version with a timestamp. Restoring the document as of a particular moment means choosing the newest version at or before that moment.
- **Thermostat settings.** Every adjustment is recorded with a time. To know the setting at 8 a.m., find the last adjustment no later than 8 a.m.

### How it shows up here

Each key maps to a list of `(timestamp, value)` pairs. `set` appends, which is correct because timestamps for a key only grow. `get` binary searches that list for the last timestamp not exceeding the query. If every timestamp is too large, it returns an empty string.
