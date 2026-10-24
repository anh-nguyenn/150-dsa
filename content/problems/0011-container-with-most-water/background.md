A two-pointer sweep can search pairs without checking all of them. The trick is to prove that one side can be discarded after each step, so the search still visits every pair that could be optimal.

### Everyday examples

- **A fold-out table.** The usable area between two legs depends on how far apart they are and how tall the shorter leg is. Making the taller leg even taller does not help while the shorter one stays the same.
- **Two fence posts.** The widest gap gives plenty of width, but the lower post caps how much water the gap can hold. Moving the lower post inward is the only way to look for a better cap.

### How it shows up here

Start with the widest pair, the two ends. Its area is the full width times the shorter height. The taller side is not the bottleneck. Moving it inward only reduces the width while the shorter side still caps the area, so it cannot improve this pair. Move the shorter side inward instead and record the best area seen.
