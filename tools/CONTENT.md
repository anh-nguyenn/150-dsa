# Lesson content contract

Each problem already has `content/problems/<id>/meta.json` from the catalog. Do not edit `content/catalog.json`, the app, or another problem's files.

Write one payload JSON for a batch of problems, then run:

```sh
python3 tools/author_topic.py /tmp/<name>.json
python3 tools/verify_solutions.py --problem <id> --problem <id2>
```

`author_topic.py` writes `summary.md`, `background.md`, `hints.md`, `starter.py`, `tests.json`, `approaches/01-optimal.py`, `approaches/01-optimal.md`, and updates `meta.json`.

## Payload

```json
{
  "problems": [
    {
      "id": "0001-two-sum",
      "entry": "two_sum",
      "kind": "function",
      "approach_name": "One-pass hash map",
      "time": "O(n)",
      "space": "O(n)",
      "summary": "Markdown. Own words, one or two examples, constraints in plain language, LeetCode link.",
      "background": "Markdown. Concept first, two everyday examples, how it appears here.",
      "hints": ["No code.", "A narrower question.", "The key insight, still no code."],
      "starter": "def two_sum(nums: list[int], target: int) -> list[int]:\n    # Return the indices of the two numbers that add up to target.\n    pass",
      "solution": "def two_sum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    ...",
      "tests": {"compare": "exact", "cases": []}
    }
  ]
}
```

All fields are required. `kind` is `"function"` or `"class"`. Use plain functions, not `class Solution`, unless the problem is a design problem. For a design problem, set `"kind": "class"` and `entry` to the class name.

The approach note is generated from `Idea`, `Why it works`, and `Edge cases`. Keep each to a short paragraph or a few bullets.

## Writing

- Explain in your own words. Never copy LeetCode statements or editorial text.
- Summary: task, one or two tiny examples, constraints in plain language, link to `https://leetcode.com/problems/<slug>/`.
- Background: the general concept first, then two everyday examples, then the role it plays here.
- Hints: exactly three, progressive, no code in the last two.
- Solution: optimal, clean, typed where it helps, no instrumentation, no `viz`.
- Starter: the entry signature plus a single comment and `pass` (or the class shell for design problems).
- Tests: at least five, including edge cases from the constraints. Expected values are authored by you, never produced by running the solution.
- Test names are short and descriptive.

## Function tests

```json
{
  "compare": "exact",
  "cases": [
    {"name": "typical", "args": [[2, 7, 11, 15], 9], "expected": [0, 1]}
  ]
}
```

Comparison modes:

- `exact` (default): direct equality.
- `unordered`: sort the top-level list only. Use for answers where order between items is free but each item must stay intact (permutations, combinations, interval lists).
- `unordered_deep`: recursively sort nested lists. Use when nested order is also free (group anagrams, subsets).
- `float`: numeric comparison with `"tolerance"` (default `1e-6`).

Optional fields:

- `"result": "return"` (default), `"arg0"` for an in-place mutation of the first argument, or `"args"` for every argument.
- `"result_adapter": "linked_list" | "tree" | "graph_adj" | "random_list"`.
- `case.result_adapter` overrides for one case.

Arguments may be wrappers:

```json
{"linked_list": [1, 2, 3, 4]}
{"linked_list": [3, 2, 0, -4], "cycle": 1}
{"tree": [3, 9, 20, null, null, 15, 7]}
{"graph_adj": [[2, 4], [1, 3], [2, 4], [1, 3]]}
{"random_list": [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]}
```

Wrappers may appear inside argument lists (for example, an array of linked lists).

Tree results and arguments use level-order lists with `null` holes. Linked list results use plain arrays. Graph results use neighbor arrays sorted by node value. Random-list results use `[value, random_index_or_null]`.

In-place example:

```json
{"compare": "exact", "result": "arg0", "cases": [{"name": "3x3", "args": [[[1,2,3],[4,5,6],[7,8,9]]], "expected": [[7,4,1],[8,5,2],[9,6,3]]}]}
```

Linked-list result example:

```json
{"compare": "exact", "result_adapter": "linked_list", "cases": [{"name": "four nodes", "args": [{"linked_list": [1,2,3,4]}], "expected": [4,3,2,1]}]}
```

Tree result example:

```json
{"compare": "exact", "result_adapter": "tree", "cases": [{"name": "small", "args": [{"tree": [4,2,7,1,3,6,9]}], "expected": [4,7,2,9,6,3,1]}]}
```

## Class tests

```json
{
  "kind": "class",
  "compare": "exact",
  "cases": [
    {
      "name": "push and min",
      "ops": ["MinStack", "push", "push", "getMin"],
      "args": [[], [-2], [0], []],
      "expected": [null, null, null, -2]
    }
  ]
}
```

The first op is the constructor; `args[0]` is its argument list. Later ops call methods on the instance. Use `"*"` as an expected value to ignore a return value. Use `"adapters"` aligned with `ops` when a return needs a wrapper adapter, for example `[null, null, "tree"]`.

To pass one op's return into a later op, use `{"from_op": 1}` as an argument. This is required for encode/decode pairs:

```json
{
  "name": "round trip",
  "ops": ["Codec", "encode", "decode"],
  "args": [[], [["lint", "code", "love", "you"]], [{"from_op": 1}]],
  "expected": [null, "*", ["lint", "code", "love", "you"]]
}
```

Use `"compare": "float"` for median-style classes.

## Special signatures

Keep LeetCode names but adapt node-reference problems for a testable signature:

- LCA BST: `lowest_common_ancestor(root, p, q)` takes the tree and the two **values**, and returns the value. State this in the starter.
- Design problems: class name and public methods exactly as LeetCode, but no `obj = ...` wrapper.
- Encode/decode and serialize/deserialize: class `Codec` with methods; use `from_op` tests.

## Before finishing

- Run the verifier for every problem in your batch.
- Fix code/tests until every case passes.
- Regenerate the execution traces after changing a solution or its selected case: `python3 tools/build_traces.py --problem <id>`.
- Run `python3 tools/check_content.py` to confirm the trace is current.
- Do not add instrumentation or visualization calls; traces are generated from the clean solution.
- Do not touch files outside your assigned problem directories.
- Delete temporary payload files.
- Report the problem ids you completed and any case you could not verify.
