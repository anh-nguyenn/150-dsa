# NeetCode 150 Study Site — Build Plan

A static site for one learner working through NeetCode 150. Each problem is a lesson: an own-words summary, plain-language background, progressive hints, brute-force-to-optimal solutions with complexity, a Python editor with tests, and a hand-authored visualization of the algorithm.

This plan is optimized for a solo build. It prioritizes a working pilot topic over a complete but unmaintainable site. "Done" means the page is usable in a real study session, not that all 150 folders exist.

## Status

The build has moved past the pilot-first scope. All 150 lessons exist at the minimum viable tier and pass the verifier; home, topic, problem, progress, and the in-browser Pyodide runner are live. What remains is the visualization layer: instrumentation, frame building, the player, and renderers. The M4 gate now applies to that layer, not to content coverage.

## 1. Decisions

| Topic | Choice |
|---|---|
| Audience | You, studying solo. Sharing and accounts are not v1 concerns. |
| Hosting | GitHub Pages, static, hash routing. Local dev first; deploy at the pilot. |
| Stack | React + Vite + TypeScript. |
| Python | Pyodide in a Web Worker, lazy-loaded, hard timeout. |
| Editor | CodeMirror 6 with Python mode. |
| Visuals | Hand-authored instrumentation compiled to frames JSON, played by a generic player. |
| Solutions | One optimal approach per problem at the minimum tier; brute-force contrasts are upgrades. |
| Progress | localStorage; export/import later. |
| Content | 150 problems, 18 topics, NeetCode order. |
| v1 | All 150 minimum-tier lessons, runner, progress; the visual layer comes next. |
| Not v1 | Accounts, notes, custom test inputs, auto-tracing your code, search, spaced repetition, native app. |

Success for v1: you can open the site, work a problem from summary to passing tests, mark it solved, and return the next day with progress intact. The visualization player is the next layer.

## 2. The study loop

Every page decision serves this loop. If a feature does not make one of these steps faster or clearer, it waits.

1. **Pick.** Home shows the next unsolved problem and the current topic; the topic page lists what is left.
2. **Prime.** Read the summary and constraints. No solution is visible yet.
3. **Recall the background.** Plain concept first, then everyday examples, then how it appears in this problem.
4. **Attempt.** Write in the starter code. Run tests. See which case failed and why.
5. **Take a hint.** Hints expand one at a time. The last hint names the key insight, never the code.
6. **Compare.** Open a solution only when ready. Read the idea, then the code, then the complexity.
7. **Watch.** Step the visualization. Each caption says what changed and why it matters.
8. **Confirm.** Mark solved. The next problem is one click away.

Design consequences:

- The solution is collapsed by default, but never locked. This is a study tool, not an exam.
- The editor keeps its code per problem; navigating away and back must not lose work.
- Hints and solutions are progressive disclosure, not separate pages.
- The visualization and code sit together: watching a solution should not require losing your place.

## 3. Pages

### 3.1 Home

- "Next up": the first unsolved problem in topic order, with topic and difficulty.
- Overall progress: solved / 150, plus a thin per-topic progress list.
- 18 topic cards: name, problem count, solved count, one-line pattern description.
- Continue link: last visited problem.
- No marketing hero. The first screen is the next action.

### 3.2 Topic page

- Topic intro: what the pattern is, when to reach for it, and what earlier patterns it assumes.
- Problem list: order, title, difficulty, solved state. Each row links to the problem.
- Topic progress bar and "next unsolved in this topic."

### 3.3 Problem page (the core)

Top bar: back to topic, title, difficulty, solved toggle, previous/next problem.

Sections in order:

1. **Summary**: own-words statement, one or two examples, constraints rewritten in your own words, LeetCode link.
2. **Background**: the concept, everyday examples with scenarios and outcomes, how it shows up here, prerequisite links.
3. **Hints**: two or three progressive hints, collapsed.
4. **Solutions**: tabs, one per approach. Each tab: idea, code, time/space, edge cases, visualization player.
5. **Try it**: editor, starter code, Run tests, results, autosave, reset.
6. **Mark solved**.

Desktop layout: a reading column for prose (max roughly 72ch), a sticky "on this page" rail, and a full-width code/visualization workbench. The workbench is the widest element on the page; prose never squeezes it.

Mobile: single column. A sticky segmented control switches Read / Code / Watch so the editor and player get the full width. No side-by-side code and visualization below roughly 900px.

### 3.4 States

| State | What the learner sees |
|---|---|
| First visit | Next-up problem, empty progress, "start here." |
| No progress | Zeroed bars, no fake activity. |
| Pyodide loading | One-time download notice, progress, Run disabled. |
| Running | Cancel button; inputs disabled; elapsed time. |
| Pass | Per-case rows green; runtime; "all cases passed." |
| Fail | Per-case expected vs actual; failing input; captured output. |
| Time limit | "Time limit exceeded on case N"; worker restarted; complexity hint. |
| Error | Traceback in a readable panel; worker state preserved. |
| Storage unavailable | Quiet banner: progress will not persist; site remains usable. |
| All solved | Topic and home show completion; next action is review, not a confetti screen. |
| Missing content | 404 route; no half-rendered lesson. |

### 3.5 URLs and navigation

- `#/` home
- `#/topic/<topic-id>`
- `#/problem/<problem-id>?approach=<approach-id>`
- Hash routing so GitHub Pages deep links work without a 404 shim.
- Browser back restores the last section and approach where practical.
- Set `base` in `vite.config.ts` to the repository name.

### 3.6 Keyboard and accessibility

- `Cmd/Ctrl+Enter`: run tests.
- `Left/Right`: step the visualization; `Space`: play/pause; `Home/End`: first/last frame.
- Visible focus on every control; no keyboard traps in the editor.
- Player controls have labels; the current frame's state is available as text, not only color.
- `prefers-reduced-motion`: no autoplay, no transitions; stepping is instant.
- Contrast checked for code, captions, and pass/fail states.

## 4. UI direction

Mode: **Operate**. The learner is completing a task, not being sold to.

Stance: **a workshop, not a course platform.** The problem, the code, and the visualization are the only things allowed to be loud. Chrome is quiet and dense. No hero, no streaks, no confetti, no card shadows, no decorative gradients, no icon tiles.

- **Hierarchy**: problem title, then the current task, then supporting material. One primary action per section.
- **Typography**: three roles only: reading text, code, UI labels. Prose is comfortable at roughly 65-72ch. Code is monospace with clear line numbers. Labels are small, tracked, and sparse.
- **Color**: mostly neutral. Color is state: current line, active pointer, visited node, pass, fail. The visualization is the one place a saturated palette is allowed.
- **Density**: high but breathable. The page should feel like a well-set textbook and a good editor, not a dashboard.
- **Motion**: only for stepping, running, and revealing. No entrance animations, no parallax.
- **Theme**: dark-first, low-chroma ground, because sessions are long and the visualizations use luminous state color. Confirm at M0; one theme until the pilot ships. A light theme is a later adaptation, not a parallel build.
- **Anti-goals**: gamification, streak pressure, marketing copy, fake social proof, generic dashboard cards, decorative icon sets.

This is a direction brief, not a token spec. [PRODUCT.md](PRODUCT.md) holds product truth. DESIGN.md is written after the pilot UI exists, from the built system; do not invent a palette or typeface before then.

## 5. Content model

### 5.1 Repository layout

```
content/
  catalog.json                 # topics, order, problem ids
  topics/<topic-id>.md         # topic intro
  problems/<problem-id>/
    meta.json
    summary.md
    background.md
    hints.md
    starter.py
    tests.json
    approaches/
      01-brute.py              # source of truth; contains viz.* instrumentation
      01-brute.md              # idea, why it works, complexity, edge cases
      02-hashmap.py
      02-hashmap.md
src/
  app/                         # router, layout, theme
  pages/                       # Home, Topic, Problem
  components/
    editor/                    # CodeMirror wrapper
    runner/                    # results, case rows, traceback
    viz/                       # player + renderers
    progress/
  lib/
    content/                   # loaders + schema checks
    pyodide/                   # worker, harness, adapters
    frames/                    # frame types + line map
    storage/
generated/
  code/<problem-id>/<approach-id>.py    # clean, instrumentation stripped
  frames/<problem-id>/<approach-id>/<example>.json
tools/
  scaffold_problem.py
  verify_solutions.py
  build_frames.py
  check_content.py
```

Convention over configuration: fixed filenames inside each problem folder; `meta.json` only carries what varies. `generated/` is build output, never hand-edited; a prebuild step creates it before Vite imports the content manifest.

### 5.2 `catalog.json`

```json
{
  "version": 1,
  "topics": [
    {
      "id": "arrays-hashing",
      "name": "Arrays & Hashing",
      "problems": ["0217-contains-duplicate", "0242-valid-anagram"]
    }
  ]
}
```

Topic order is array order. Problem order within a topic is array order. One file is the source of truth for navigation and progress totals.

### 5.3 `meta.json`

```json
{
  "id": "0001-two-sum",
  "title": "Two Sum",
  "slug": "two-sum",
  "difficulty": "Easy",
  "entry": "two_sum",
  "approaches": [
    {
      "id": "brute",
      "name": "Brute force",
      "time": "O(n^2)",
      "space": "O(1)",
      "viz_examples": [
        { "name": "typical", "args": [[2, 7, 11, 15], 9] },
        { "name": "edge", "args": [[3, 3], 6] }
      ]
    }
  ]
}
```

The approach id maps to `approaches/<order>-<id>.py` and `.md`; the order comes from the array. `viz_examples` are small, fixed inputs used to build frames; custom inputs are not supported in v1.

### 5.4 `tests.json`

```json
{
  "compare": "exact",
  "cases": [
    { "name": "typical", "args": [[2, 7, 11, 15], 9], "expected": [0, 1] },
    { "name": "duplicate", "args": [[3, 3], 6], "expected": [0, 1] },
    { "name": "negative", "args": [[-1, -2, -3, -4], -6], "expected": [1, 3] }
  ]
}
```

Comparison modes:

- `exact`: deep equality.
- `unordered`: recursively sorts nested lists before comparison (anagrams, subsets, groups).
- `float`: elementwise numeric comparison with a `tolerance` field, default `1e-6`.
- `custom`: `checker` field containing a Python function `check(actual, expected, args) -> bool`, for multiple valid answers.

Adapters keep JSON plain:

- An arg is either a raw JSON value or `{"adapter": "tree", "value": [...]}`. Supported adapters: `tree`, `linked_list`, `graph_adj`, `graph_edges`.
- `"result_adapter": "tree"` serializes the return value before comparison.
- The same adapters exist in the CI verifier and the browser harness; one Python module, two callers.

Rules: at least five cases per problem, including the empty or single-element case where the constraints allow it, duplicates, negatives, and a near-limit case. Expected values are authored, not generated from the solution.

Every problem page links `https://leetcode.com/problems/<slug>/` and includes the footer: "Unaffiliated study project. Problems belong to LeetCode."

### 5.5 Solution files and instrumentation

Each approach has one Python file. It is the source of truth for both the readable code and the visualization.

- The entry function is named in `meta.json`.
- Instrumentation is full-line `viz.*` calls, one call per line, indented normally.
- The build strips those lines to produce `generated/code/...`: the code the learner reads and the CI runner executes.
- The frame builder records the caller's line automatically (`inspect.currentframe().f_back.f_lineno`), then maps it through the strip map to the clean line. Authors never pass line numbers.
- A `viz.*` call may not be the only statement in a block; the generated clean code must still parse. `verify_solutions.py` fails if it does not.
- Multi-line `viz.*` calls are not allowed; keep them to one line.
- `viz` is a reserved name; do not use it for a variable.

This removes the classic twin/clean drift: there is no second copy of the algorithm to forget to update.

### 5.6 Visualization API

Small on purpose. Authors should write 15-30 lines of instrumentation per approach.

```python
def two_sum(nums, target):
    seen = {}
    viz.init(note="Start with an empty map.",
             nums=viz.array(nums),
             seen=viz.map(seen))
    for i, x in enumerate(nums):
        need = target - x
        viz.frame(note=f"Need {need} to pair with {x}. Is it in the map?",
                  pointers={"nums": {"i": i}})
        if need in seen:
            viz.frame(note=f"Found it: indices {seen[need]} and {i}.",
                      highlight={"nums": [i, seen[need]]}, done=True)
            return [seen[need], i]
        seen[x] = i
        viz.frame(note=f"Not found. Remember {x} at index {i}.")
```

- Panels: `array`, `map`, `set`, `stack`, `queue`, `grid`, `tree`, `graph`, `linked_list`, `dp`, `heap`, `intervals`, `callstack`.
- `viz.init(**panels)` records frame 0 with the note. The keyword is the panel name.
- `viz.frame(note=..., highlight=..., pointers=..., done=False)` snapshots every panel.
- `highlight` is `{panel_name: [indices]}`; `pointers` is `{panel_name: {label: index}}`.
- State is deep-copied and converted to JSON-safe values (sets to sorted lists, dict keys to strings, tree nodes to nested objects). A frame is a snapshot, so stepping backward is free.
- The frame builder deep-copies each example's args, so in-place solutions do not leak state between examples.

### 5.7 Frames JSON

```json
{
  "problem": "0001-two-sum",
  "approach": "hashmap",
  "example": "typical",
  "code": "def two_sum(nums, target):\n    ...",
  "panels": [{ "name": "nums", "kind": "array" }],
  "frames": [
    {
      "line": 3,
      "state": { "nums": [2, 7, 11, 15], "seen": {} },
      "pointers": { "nums": { "i": 0 } },
      "highlight": {},
      "note": "Need 7 to pair with 2. Is it in the map?",
      "done": false
    }
  ]
}
```

Limits: at most 80 frames per example, at most 128KB per frame file, notes at most 200 characters. The build fails if a limit is exceeded.

### 5.8 Storage

```json
{
  "version": 1,
  "lastProblem": "0001-two-sum",
  "problems": {
    "0001-two-sum": { "solved": true, "at": 1730000000000 }
  },
  "code": {
    "0001-two-sum": "def two_sum(nums, target):\n    ..."
  }
}
```

Two namespaced keys: `n150:progress` and `n150:code`. Every access is wrapped; if storage throws, the app runs in memory and shows a quiet banner. Export/import is a later milestone.

## 6. Visualization system

### 6.1 Pipeline

1. Author `approaches/NN-id.py` with `viz.*` calls.
2. `build_frames.py` strips instrumentation to produce clean code and a line map.
3. It executes the clean code against `tests.json` (must pass).
4. It executes the instrumented source with the `viz` recorder injected into the module globals and each `viz_example`, producing frames.
5. It maps each frame's twin line to its clean line, validates limits, and writes `generated/frames/...`.
6. The browser fetches one frames file per approach/example when the learner opens the visualization.

CI repeats steps 2-5. A visual can never ship teaching an algorithm that fails the tests.

### 6.2 Renderers

Build each once; reuse across topics. Every renderer takes one panel's state plus optional highlights and pointers.

| Renderer | Used by |
|---|---|
| ArrayRow | Two Pointers, Sliding Window, Binary Search, Kadane, arrays |
| HashMap / Set | Hashing, frequency counts, seen-sets |
| Stack / Queue / Deque | Stack, monotonic stack, BFS |
| Linked List | Linked List topic |
| Tree | Trees, BST, Trie |
| Graph | Graphs, Advanced Graphs |
| Grid | Islands, Rotting Oranges, 2-D DP |
| DP table | 1-D and 2-D DP |
| Heap | Heap / priority queue problems |
| Intervals | Intervals |
| Recursion tree / call stack | Backtracking, DFS, memoization |

Pilot needs only ArrayRow, HashMap/Set, and Grid. Top K Frequent Elements uses the map + array renderers (frequency map, bucket array), not the Heap renderer. Do not build the rest before the pilot proves the player.

### 6.3 Player

- Left: clean solution code with the current line highlighted. Right: the panels.
- Below: the caption for the current frame.
- Controls: play/pause, step back/forward, first/last, speed, scrub bar.
- Example selector: the fixed `viz_examples`; one is the edge case.
- Keyboard as in section 3.6.
- Captions carry the teaching. A frame with no caption is a bug.
- `prefers-reduced-motion`: no autoplay, no tweening; state changes are instant.

### 6.4 What makes a good visual

- It shows the invariant, not just the loop. The caption says what is true now.
- One thing changes per frame; the eye can follow it.
- The input is small enough to read at a glance (arrays of 6-10, grids of 5-9).
- Color marks the active comparison or the visited set, not decoration.
- The last frame shows the answer and why it is the answer.
- The edge example is chosen to expose the failure mode of the naive approach.

### 6.5 Authoring cost controls

- Caption sequence first, code second: write the 5-10 captions, then place the calls.
- Optimal approach first for all 150; brute-force visuals only where the contrast teaches something.
- Two examples per approach by default; three only when an edge case earns it.
- 80-frame cap; prefer 20-40.
- No custom inputs in v1; that is a different feature (auto-tracing), not a small addition.

## 7. Python runner

### 7.1 Lifecycle

- One dedicated Web Worker, created on the first Run on a problem page.
- The worker imports Pyodide from a pinned CDN URL, loads the harness, and reports ready.
- Pyodide is never loaded on Home, Topic, or read-only problem sections.
- The worker is reused across runs and problems until it times out or crashes.
- On timeout: terminate the worker, create a fresh one, reload Pyodide, report which case was running.

### 7.2 Execution

- Input: `{ code, entry, tests, compare, adapters }`.
- The harness executes the code in a fresh namespace per run; defines `ListNode`, `TreeNode`, builders, and adapters.
- Captures stdout and stderr per case.
- Measures each case with `time.perf_counter`.
- Compares with the selected mode; returns per-case results as JSON.
- A hard 5-second timeout covers the whole run. The worker reports the case index before each call, so a timeout can name the case.
- `setInterruptBuffer` is a later optimization; termination is the v1 guarantee.

### 7.3 Failure behavior

- Syntax error: show the traceback, do not run cases.
- Missing entry function: name the expected signature.
- Exception in a case: stop on the first exception, show that case's traceback; the learner fixes the crash before seeing later results.
- Infinite loop: terminate, report the case, suggest the complexity.
- Worker crash: offer "restart runner"; never leave a dead spinner.

### 7.4 Editor behavior

- Starter code defines the entry signature and a short comment, nothing else.
- Autosave per problem, debounced; restore on return.
- "Reset to starter" asks once.
- `Cmd/Ctrl+Enter` runs.
- No autocomplete in v1; line numbers, bracket matching, and Python indentation are enough.

## 8. Content pipeline

### 8.1 Per-problem order

1. `scaffold_problem.py <id>` creates the folder and placeholder files.
2. Write `summary.md`, `background.md`, `hints.md`.
3. Write `starter.py` and `tests.json` (at least five cases).
4. Write the clean solution, then instrument it with `viz.*`; run `verify_solutions.py` until clean and instrumented versions pass.
5. Write `approaches/NN-id.md` (idea, why it works, complexity, edge cases).
6. Run `build_frames.py`; inspect the player.
7. Review in the browser at desktop and 390px; check keyboard and reduced motion.
8. Mark the problem done in the tracker.

### 8.2 Quality bar for `background.md`

- One or two short paragraphs: the concept in plain words, no jargon first.
- Two or three everyday examples, each with two or three scenarios and outcomes.
- "How it shows up here": the specific role the concept plays in this problem.
- Prerequisites linked to the problem where they first appeared.
- Prefer a small diagram or the visualization over a wall of text.

Worked example, Two Sum:

> A hash map is a coat-check desk. You hand over a coat and get a ticket; later the ticket returns the coat without searching the whole rack. A missing ticket means the coat is not there; a duplicate ticket is a bug in the system.
>
> In this problem, the "coat" is a number you have already seen, and the "ticket" is the number you need to finish the pair. Walking the array once, you ask the desk for `target - x`. If it is there, you are done. If not, you check in `x` and keep walking.
>
> This is why one pass is enough: the map answers "have I seen the complement?" in constant time, so you never rescan.

Hints:

1. What would you do with a pencil and paper, without code?
2. For each number, what single other number would complete the pair?
3. What could you remember as you walk the array once so you never look back?

### 8.3 Cadence and scope tiers

The honest bottleneck is authoring, not code. Two tiers:

| Tier | Per problem | Use |
|---|---|---|
| Minimum viable lesson | summary, one background section, 3 hints, optimal solution, 2 viz examples, 5 tests | Ship all 150 first |
| Full lesson | adds brute force, a second visual, richer background | Upgrade after the site is complete |

Pilot: Arrays & Hashing (Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Top K Frequent Elements, Encode and Decode Strings, Product of Array Except Self, Valid Sudoku, Longest Consecutive Sequence), full lessons, 3-5 weeks at 6-8 hours per week. The remaining 141 at the minimum tier: roughly 1-2 hours each, 5-10 months part-time. The plan assumes the minimum tier is the default and brute-force visuals are the exception.

Work in topic batches and finish a topic completely before starting the next. Deploy after the pilot so phone review is real.

## 9. Build order

| # | Milestone | Deliverable | Done when |
|---|---|---|---|
| M0 | Walking skeleton | Vite app, router, layout, content loader, Two Sum rendered from Markdown with a temporary static code block | Two Sum page renders from content files; no Python yet; the strip pipeline arrives in M2 |
| M1 | Runner | Worker + Pyodide + harness + comparison modes; Two Sum's tests run | All Two Sum cases pass and fail correctly; timeout works |
| M2 | Visualizer MVP | Strip + line map, frame builder for Two Sum, player, ArrayRow + HashMap | Two Sum's optimal visual plays, steps, and highlights the clean line |
| M3 | Pipeline | `scaffold`, `verify`, `build_frames`, `check_content` | One command verifies all content; broken cases fail loudly |
| M4 | Pilot topic | Arrays & Hashing complete: 9 problems, progress, home and topic pages | A full study session works end-to-end; deployed and checked on a phone |
| M5 | Renderers | Stack, LinkedList, Tree, Graph, Grid, DP, Heap, Intervals, Recursion | Each renderer proven on at least one real problem |
| M6 | Remaining topics | Topics 2-18, minimum tier first | All 150 lessons reach the minimum tier |
| M7 | Finish | Search/filter, progress export/import, accessibility pass, README, optional upgrades | The site is maintainable and pleasant to use daily |

M4 is the gate. Do not start M5 until the pilot has been used for real study sessions. The pilot answers the questions this plan cannot: is the lesson the right length, does the visualization teach, does the runner get in the way.

Next build path after approval: M0 -> M1 -> M2 -> M3 -> M4.

## 10. Quality gates

Local, before every commit after M3:

- `python tools/verify_solutions.py`: every clean solution passes every test; every instrumented source strips to parseable code; every approach has tests.
- `python tools/build_frames.py --check`: frames build, limits hold, clean line map is valid.
- `python tools/check_content.py`: catalog/meta consistency, required files, at least five cases, viz examples exist.
- `npm run typecheck` and `npm run build`.

CI (add at M4, not before):

- The same Python checks.
- TypeScript check, lint, unit tests for comparison modes and the strip/line-map functions.
- `vite build`.

Definition of done for one problem:

- [ ] Own-words summary, examples, constraints, LeetCode link.
- [ ] Background to the quality bar, with prerequisite links.
- [ ] Two or three progressive hints; no code in hints.
- [ ] Two or three approaches, brute force to optimal; each passes at least five tests.
- [ ] Complexity and edge cases written for each approach.
- [ ] Visualization for the optimal approach; captions teach, two examples, 80 frames or fewer.
- [ ] Starter code and correct comparison mode.
- [ ] Reviewed at desktop and 390px; keyboard and reduced motion checked.

Performance budgets:

- Pyodide is never part of the initial route bundle.
- One frames file is fetched per approach/example, not all 150 at once.
- The problem page's own JS stays small; Markdown and frames are lazy.
- No blocking font or analytics request.

## 11. Risks

| Risk | Mitigation |
|---|---|
| 150 lessons is too much authoring | Minimum viable tier; topic batches; pilot before mass production; brute-force visuals only where they teach |
| The visual looks impressive but does not teach | Captions first; two examples; pilot review against the study loop; cut frames that do not change understanding |
| Twin and clean solution drift | Single source of truth; clean code is generated; CI runs both |
| Pyodide is large and slow | Lazy load, pinned CDN, progress state, browser cache |
| Infinite loop freezes the page | Worker + hard timeout + terminate + fresh worker |
| Copyright of problem text | Own words, links out, disclaimer; never copy statements or editorial text |
| localStorage is unavailable or cleared | try/catch, in-memory fallback, export/import later |
| Frame files grow | Small examples, 80-frame cap, per-approach lazy fetch |
| The plan becomes procrastination | M0 is a walking skeleton; the pilot is the real checkpoint; timebox planning |
| Content order is wrong | One `catalog.json`; verify against the official list when scaffolding |
| Dependency rot | Pin Pyodide and CodeMirror; review versions at milestones, not continuously |
| Mobile editor is cramped | Full-width segmented Code/Watch view; test at 390px before the pilot ships |

## 12. Open decisions

1. **Theme.** Dark-first is the working assumption. Confirm at M0; do not build two themes before the pilot.
2. **Clean generation.** Validate the strip-and-line-map approach in M2. Fallback: keep two files and an explicit line map, at the cost of drift risk.
3. **Deploy timing.** M4, after the pilot works locally. Earlier deploy is fine if it helps phone review.
4. **Approach count.** Two per problem is the default; a third only when it teaches a distinct idea.
5. **Pyodide version.** Pin at M1 and record it; upgrade only with a passing full test run.
6. **Custom inputs.** Out of v1. Revisit only after all 150 have a lesson.

## 13. Later

- Per-problem notes.
- Search and filter by difficulty, topic, solved state.
- Progress export/import.
- Spaced-repetition review queue.
- Auto-tracing the learner's own code with `sys.settrace` in Pyodide.
- Light theme.
- A second visualization for brute force where the contrast is worth it.
