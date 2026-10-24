## Idea

Keep a list of timestamp-value pairs for each key. Since set timestamps for a key increase, appending keeps the list sorted. For a lookup, binary search for the rightmost timestamp at or below the query and return its value, or an empty string when there is no such timestamp.

## Why it works

Appending is safe because each key's timestamps arrive strictly increasing. During binary search, an entry with a timestamp at or below the query is a valid candidate, and every earlier timestamp is also valid but older, so the search moves right to improve the candidate. An entry above the query invalidates it and everything later, so the search moves left. When the range empties, the stored best is the latest valid value, or remains empty if no timestamp qualified.

## Edge cases

- A lookup for an unknown key returns an empty string.
- A lookup earlier than the key's first timestamp returns an empty string.
- A lookup exactly at a stored timestamp returns that timestamp's value.
- A lookup later than every timestamp returns the most recent value.
- Different keys may share timestamps; histories are kept separately.
- Repeated keys do not overwrite earlier versions, so past lookups remain correct.
