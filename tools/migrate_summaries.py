#!/usr/bin/env python3
import argparse
import ast
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
LINK_RE = re.compile(r"\n*\[[^\]]+\]\(https://leetcode\.com/problems/[^)]+\)\s*$")
CONSTRAINTS_RE = re.compile(r"^\*\*Constraints[^*]*\*\*\s*$", re.M)
EXAMPLE_RE = re.compile(r"^\*\*Examples?\*\*\s*$", re.M)
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
TRIVIAL = ("empty", "single", "zero", "no ", "none", "impossible", "all water", "all walls", "all land")


def strip_link(text):
    return LINK_RE.sub("", text).strip()


def split_summary(text):
    text = strip_link(text)
    constraints_match = CONSTRAINTS_RE.search(text)
    if constraints_match:
        before = text[: constraints_match.start()].strip()
        tail = text[constraints_match.end() :]
        constraints = [line.strip()[2:].strip() for line in tail.splitlines() if line.strip().startswith("- ")]
    else:
        before = text.strip()
        constraints = []

    example_match = EXAMPLE_RE.search(before)
    if example_match:
        description = before[: example_match.start()].strip()
        example_text = before[example_match.end() :].strip()
    else:
        fence = re.search(r"```[^\n]*\n.*?```", before, re.S)
        if fence:
            description = before[: fence.start()].strip()
            example_text = before[fence.start() :].strip()
        else:
            description = before.strip()
            example_text = ""
    return strip_link(description), example_text, constraints


def balanced(text):
    return all(text.count(left) == text.count(right) for left, right in (("[", "]"), ("(", ")"), ("{", "}")))


def plausible_input(text):
    text = text.strip()
    if not text:
        return False
    return text[0] in '[-"\'({' or "=" in text or "(" in text


def parse_block(block):
    block = block.strip()
    normalized = re.sub(r"\n\s*(?:->|=>)\s*", " -> ", block)
    lines = [line for line in normalized.splitlines() if line.strip()]
    arrow_lines = [index for index, line in enumerate(lines) if re.search(r"\s(?:->|=>)\s", line)]
    if not arrow_lines:
        return [{"body": f"```text\n{block}\n```"}]

    if len(arrow_lines) == 1:
        arrow_index = arrow_lines[0]
        left, right = re.split(r"\s(?:->|=>)\s", lines[arrow_index], maxsplit=1)
        left = "\n".join(lines[:arrow_index] + [left])
        right = "\n".join([right] + lines[arrow_index + 1 :])
        if balanced(left) and balanced(right) and plausible_input(left):
            return [{"input": left.strip(), "output": right.strip()}]
        return [{"body": f"```text\n{block}\n```"}]

    if len(arrow_lines) != len(lines):
        return [{"body": f"```text\n{block}\n```"}]

    examples = []
    for line in lines:
        left, right = re.split(r"\s(?:->|=>)\s", line, maxsplit=1)
        if not balanced(left) or not balanced(right) or not plausible_input(left):
            return [{"body": f"```text\n{block}\n```"}]
        examples.append({"input": left.strip(), "output": right.strip()})
    return examples


def parse_examples(example_text):
    if not example_text:
        return []
    parts = re.split(r"(```[^\n]*\n.*?```)", example_text, flags=re.S)
    examples = []
    trailing = []
    for part in parts:
        if part.startswith("```"):
            block = re.sub(r"^```[^\n]*\n|```$", "", part.strip())
            examples.extend(parse_block(block))
        elif part.strip():
            trailing.append(part.strip())
    if trailing:
        note = " ".join(item.replace("\n", " ").strip() for item in trailing)
        if examples and ("input" in examples[-1] or "output" in examples[-1]):
            existing = examples[-1].get("explanation", "")
            examples[-1]["explanation"] = (existing + "\n\n" + note).strip()
        elif examples:
            examples[-1]["body"] = (examples[-1].get("body", "") + "\n\n" + note).strip()
        else:
            examples.append({"body": note})
    return examples


def format_arg(arg):
    if isinstance(arg, dict):
        if "tree" in arg:
            return "tree = " + json.dumps(arg["tree"])
        if "linked_list" in arg:
            return "list = " + json.dumps(arg["linked_list"])
        if "graph_adj" in arg:
            return "adjacency = " + json.dumps(arg["graph_adj"])
        if "random_list" in arg:
            return "nodes = " + json.dumps(arg["random_list"])
    return json.dumps(arg)


def function_params(problem_id, meta):
    if meta.get("kind") == "class":
        return []
    directory = os.path.join(CONTENT, "problems", problem_id)
    for filename in ("starter.py", "approaches/01-optimal.py"):
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
        try:
            with open(path) as handle:
                tree = ast.parse(handle.read())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == meta.get("entry"):
                return [arg.arg for arg in node.args.args]
    return []


def format_named_arg(arg, name):
    if isinstance(arg, dict):
        if "tree" in arg:
            return f"{name} = {json.dumps(arg['tree'])}"
        if "linked_list" in arg:
            return f"{name} = {json.dumps(arg['linked_list'])}"
        if "graph_adj" in arg:
            return f"{name} = {json.dumps(arg['graph_adj'])}"
        if "random_list" in arg:
            return f"{name} = {json.dumps(arg['random_list'])}"
    return f"{name} = {json.dumps(arg)}"


def test_examples(problem_id, meta, tests):
    cases = tests.get("cases", [])
    if not cases:
        return []
    chosen = cases[0]
    for case in cases:
        lowered = str(case.get("name", "")).lower()
        if not any(word in lowered for word in TRIVIAL):
            chosen = case
            break
    if meta.get("kind") == "class":
        ops = chosen.get("ops", [])
        args = chosen.get("args", [])
        lines = []
        for index, op in enumerate(ops):
            call_args = args[index] if index < len(args) else []
            rendered = ", ".join(format_arg(arg) for arg in call_args)
            lines.append(f"{op}({rendered})")
        return [{"input": "\n".join(lines), "output": json.dumps(chosen.get("expected"))}]
    params = function_params(problem_id, meta)
    args = chosen.get("args", [])
    rendered = []
    for index, arg in enumerate(args):
        if index < len(params):
            rendered.append(format_named_arg(arg, params[index]))
        else:
            rendered.append(format_arg(arg))
    return [{"input": ", ".join(rendered), "output": json.dumps(chosen.get("expected"))}]


def migrate(problem_id, apply=False, force=False):
    directory = os.path.join(CONTENT, "problems", problem_id)
    summary_path = os.path.join(directory, "summary.md")
    meta_path = os.path.join(directory, "meta.json")
    with open(summary_path) as handle:
        original = handle.read()
    with open(meta_path) as handle:
        meta = json.load(handle)
    if apply and not force and meta.get("examples") and "**Constraints" not in original:
        return None, None, None, None
    with open(os.path.join(directory, "tests.json")) as handle:
        tests = json.load(handle)

    description, example_text, constraints = split_summary(original)
    examples = parse_examples(example_text)
    if not examples:
        examples = test_examples(problem_id, meta, tests)
    if not description:
        description = "Solve the problem and return the required result."
    if not constraints:
        constraints = ["See the problem statement for the input bounds."]

    meta["examples"] = examples
    meta["constraints"] = constraints
    if apply:
        with open(meta_path, "w") as handle:
            json.dump(meta, handle, indent=2)
            handle.write("\n")
        with open(summary_path, "w") as handle:
            handle.write(description.rstrip() + "\n")
    return description, examples, constraints, example_text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--problem", action="append", default=[])
    args = parser.parse_args()
    with open(os.path.join(CONTENT, "catalog.json")) as handle:
        catalog = json.load(handle)
    ids = args.problem or [problem_id for topic in catalog["topics"] for problem_id in topic["problems"]]
    stats = {"examples": 0, "input_output": 0, "body": 0, "constraints": 0, "test_fallback": 0, "short": 0}
    report = []
    for problem_id in ids:
        description, examples, constraints, example_text = migrate(problem_id, apply=args.apply, force=args.force)
        if description is None:
            print(f"skip {problem_id}: already migrated (use --force)")
            continue
        stats["examples"] += len(examples)
        stats["constraints"] += len(constraints)
        if len(description.split()) < 20:
            stats["short"] += 1
        if any(example.get("input") for example in examples):
            stats["input_output"] += 1
        if any(example.get("body") for example in examples):
            stats["body"] += 1
        if not parse_examples(example_text):
            stats["test_fallback"] += 1
        report.append(
            {
                "id": problem_id,
                "words": len(description.split()),
                "examples": examples,
                "constraints": constraints,
            }
        )
    print(json.dumps(stats, indent=2))
    if not args.apply:
        with open("/tmp/summary_migration_preview.json", "w") as handle:
            json.dump(report, handle, indent=2)
        print("preview written to /tmp/summary_migration_preview.json")
    else:
        print(f"migrated {len(ids)} problems")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
