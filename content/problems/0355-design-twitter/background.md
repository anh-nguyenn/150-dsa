A news feed combines several ordered streams into one ordered stream. A global timestamp makes it possible to compare tweets from different users, and a heap can merge the most recent tweet from each followed user without sorting everything. Follow relationships form a small directed graph.

### Everyday examples

- **Email inbox.** Messages from several accounts are merged into one list, with the newest message at the top.
- **News aggregator.** Articles from many publishers are combined by publication time while the reader only sees the latest page.

### How it shows up here

Each posted tweet gets an increasing timestamp and is appended to its author's list. A feed grabs the latest tweet from the user and every followee, puts those candidates in a max-heap by timestamp, and repeatedly pops the newest, replacing it with that author's previous tweet until ten entries are collected.
