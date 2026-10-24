# 150

A local-first study site for working through 150 algorithm problems, one lesson at a time.

Each lesson has an own-words summary, a plain-language background, three progressive hints, an optimal solution with time and space, starter code, and authored tests. Progress and code stay in the browser.

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
  meta.json
  summary.md
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
- Frame-by-frame visualizations are not authored yet. The approach panel says so rather than showing a fake player.
- Search, progress export/import, and a light theme are later.

The build plan and product truth live in [PLAN.md](PLAN.md) and [PRODUCT.md](PRODUCT.md).

## Disclaimer

Unaffiliated study project. Problems belong to LeetCode. Problem text here is written in original words and links out to LeetCode.
