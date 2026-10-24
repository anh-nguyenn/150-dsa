Dependencies often point in only one direction. Flour has to exist before bread, and a foundation has to be poured before walls go up. A collection of one-way requirements is a directed graph, and the important question is whether the arrows ever lead back to a place you have already been. A loop in those requirements makes the plan impossible, because each step in the loop waits on another step in the same loop.

### Everyday examples

- **Cooking.** You cannot ice a cake before baking it, and you cannot bake it before mixing the batter. The steps form a chain, not a loop.
- **Building software.** A library must compile before the program that imports it. If two modules each needed the other to compile first, neither could ever be built.
- **Course planning.** Calculus II needs Calculus I, which needs algebra. A catalog with a circular prerequisite chain would contain courses that no student could ever take.

### How it shows up here

Treat every course as a node. A prerequisite pair draws an arrow from the prerequisite to the course that needs it. All courses can be completed exactly when this directed graph has no cycle. One practical way to check that is to repeatedly remove courses that have no remaining prerequisites; if the removals stall before every course is gone, the leftover courses are trapped in a cycle.
