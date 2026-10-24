Instead of asking where water from each cell goes, it is easier to ask which cells can send water to a given ocean. Starting at the ocean edge and walking inward, you may step to a cell only when it is at least as high as the current one; that is the reverse of water flowing downhill.

### Everyday examples

- **Tracing rivers upstream.** Start at the sea and follow tributaries backward to see which springs feed that coast.
- **Two coastlines on an island.** A ridge may drain to the north coast, the south coast, or both; working inward from each coast finds the shared watershed.

### How it shows up here

Run a reverse flood fill from all Pacific border cells, then another from all Atlantic border cells. Each fill records cells reachable while climbing to equal or higher terrain. A cell drains to both oceans exactly when it appears in both recorded sets, so return the intersection.
