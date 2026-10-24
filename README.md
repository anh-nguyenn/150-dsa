# 150

A local-first study site for working through 150 algorithm problems, one lesson at a time.

Each lesson has a description with structured examples and constraints, a plain-language background, three progressive hints, an optimal solution, starter code, authored tests, and a step-through execution trace. The problem page is a practice-first split: description on the left, code and testcase runner on the right, with the background and solutions in a Learn section below. Progress and code stay in the browser.

## Run

```sh
npm install
npm run dev
```

The production build is static:

```sh
npm run build
npm run preview
```

Routing is hash-based and Vite's base is relative, so the build works on GitHub Pages under a repository path without a 404 shim.

## Content checks

```sh
npm run verify   # execute every solution against its tests
npm run check    # catalog, metadata, and required files
```

`tools/verify_solutions.py --all` is the gate: every lesson's solution must pass every authored case. The same Python harness runs in the browser worker.

## Practice layout

The problem page mirrors the useful parts of a LeetCode-style workbench:

- The left pane is the description, with numbered examples, constraints, hints, and a source link.
- The right pane is the workbench: Python editor, testcase tabs, `Run` for the selected authored case, and `Submit` for all cases. A successful submit marks the problem solved.
- Background and Solutions, including the visualization player, live below in the Learn section.
- On mobile, a sticky Statement / Code / Learn switch replaces the split.

Testcases are authored and read-only. Custom inputs and additional languages are later work.

## Visualizations

Every problem has a step-through player in the Solutions panel. The player shows the reference code with the current line highlighted, the live local state (arrays, maps, sets, grids, trees, linked lists, objects, and scalars), a caption for the line, and first/previous/play/next/last controls. The keyboard works when the player is focused: left/right steps, space plays or pauses, home/end jump.

Traces are generated at build time from each reference solution, not hand-written. `content/traces/<id>.json` contains the frames. If you change a solution or its selected test case, regenerate traces:

```sh
npm run traces
npm run check
```

`npm run check` fails when a trace is stale or missing. Traces are capped at 120 frames; the player labels a truncated trace instead of pretending it reached the end. Custom inputs and tracing your own code are not part of this layer.

## Runner

The editor is CodeMirror 6. Python runs in a dedicated Web Worker through Pyodide `0.26.4`, pinned to jsDelivr and loaded only on the first run. The worker is reused across problems, has a five-second hard timeout, and is terminated and recreated after a runaway loop. Code is autosaved under `n150:code`; progress is stored under `n150:progress`. If storage is blocked, the site runs in memory and says so.

## Authoring

`tools/CONTENT.md` is the content contract. A batch is a JSON payload written by `tools/author_topic.py`:

```sh
python3 tools/author_topic.py /tmp/batch.json
python3 tools/verify_solutions.py --problem <id>
```

Every problem directory follows the same shape:

```text
content/problems/<id>/
  meta.json                 # title, difficulty, entry, examples, constraints
  summary.md                # description only
  background.md
  hints.md
  starter.py
  tests.json
  approaches/01-optimal.py
  approaches/01-optimal.md
```

## Status

- All 150 lessons are written at the minimum viable tier and verified.
- Home, topic, problem, progress, solved state, and the browser runner work.
- All 150 problems have structured examples/constraints, a practice-first split layout, and a generated step-through trace and player.
- Hand-authored per-problem visualization captions and instrumentation are a possible future upgrade.
- Search, progress export/import, and a light theme are later.

The build plan and product truth live in [PLAN.md](PLAN.md) and [PRODUCT.md](PRODUCT.md).

## Disclaimer

Unaffiliated study project. Problems belong to LeetCode. Problem text here is written in original words and links out to LeetCode.
