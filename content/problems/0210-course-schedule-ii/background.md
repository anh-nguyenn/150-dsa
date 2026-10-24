A topological order lines up the nodes of a directed graph so that every arrow points forward. It turns a set of one-way requirements into a workable sequence. If the arrows contain a loop, no line-up can satisfy all of them, because the loop forces a step to come before itself.

### Everyday examples

- **Getting dressed.** Socks come before shoes, and a shirt comes before a jacket. A valid order lists each item after everything it depends on.
- **Assembling furniture.** The frame goes together before the cushions are attached. A numbered instruction booklet is a topological order of those steps.
- **Build pipelines.** Compiling a dependency before the module that imports it produces a safe build sequence.

### How it shows up here

Courses are nodes and prerequisite pairs are directed edges from the earlier course to the later one. A topological order of this graph is exactly a course schedule. The same peeling process used to detect a cycle also produces the schedule: repeatedly take a course whose prerequisites are all satisfied, append it to the answer, and release the courses that were waiting on it.
