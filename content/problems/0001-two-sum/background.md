A hash map is a coat-check desk. You hand over a coat and get a ticket; later the ticket returns the coat without searching the whole rack. A missing ticket means the coat is not there; a duplicate ticket is a bug in the system.

### Everyday examples

- **Coat check.** You check a coat and keep the ticket. Later, the ticket finds the coat in one step instead of walking the rack.
- **Contacts.** You save a name under a phone number. Calling the number back is immediate because the map remembers the association.
- **Lockers.** A key opens exactly one locker. If you know the key, you do not try every door.

### How it shows up here

In this problem, the "coat" is a number you have already seen, and the "ticket" is the number you need to finish the pair. Walking the array once, you ask the desk for `target - x`. If it is there, you are done. If not, you check in `x` and keep walking.

This is why one pass is enough: the map answers "have I seen the complement?" in constant time, so you never rescan the numbers behind you.
