#!/usr/bin/env python3
import argparse
import ast
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from n150_harness import TRACE_FRAME_CAP, trace_loaded

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
TRACES = os.path.join(CONTENT, "traces")


SCHEMA = 2
HARNESS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "n150_harness.py")


def base_name(node):
    while isinstance(node, ast.Subscript):
        node = node.value
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def index_names(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {}
    mapping = {}

    def add(container, names):
        if container:
            mapping.setdefault(container, set()).update(names)

    def collect_slices(node):
        names = set()
        if isinstance(node, ast.Subscript):
            for child in ast.walk(node.slice):
                if isinstance(child, ast.Name):
                    names.add(child.id)
            names.update(collect_slices(node.value))
        return names

    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            add(base_name(node), collect_slices(node))
        elif isinstance(node, ast.For):
            target = node.target
            target_names = []
            if isinstance(target, ast.Name):
                target_names = [target.id]
            elif isinstance(target, ast.Tuple):
                target_names = [item.id for item in target.elts if isinstance(item, ast.Name)]
            if not target_names:
                continue
            iterator = node.iter
            if isinstance(iterator, ast.Call) and isinstance(iterator.func, ast.Name):
                if iterator.func.id == "enumerate" and iterator.args:
                    add(base_name(iterator.args[0]), {target_names[0]})
                elif iterator.func.id == "range" and iterator.args:
                    first = iterator.args[0]
                    if (
                        isinstance(first, ast.Call)
                        and isinstance(first.func, ast.Name)
                        and first.func.id == "len"
                        and first.args
                    ):
                        add(base_name(first.args[0]), {target_names[0]})
    return {name: sorted(names) for name, names in mapping.items()}


def catalog_ids():
    with open(os.path.join(CONTENT, "catalog.json")) as handle:
        catalog = json.load(handle)
    ids = []
    for topic in catalog["topics"]:
        ids.extend(topic["problems"])
    return ids


TRIVIAL_WORDS = (
    "empty",
    "no ",
    "none",
    "impossible",
    "single",
    "missing",
    "all water",
    "all walls",
    "all land",
    "all o",
    "misses",
)


def is_meaningful(name):
    lowered = str(name).lower()
    return not any(word in lowered for word in TRIVIAL_WORDS)


def choose_case(meta, tests, code):
    candidates = []
    for index, case in enumerate(tests.get("cases", [])):
        result = trace_loaded(meta, tests, code, index)
        frames = len(result.get("frames", []))
        if result.get("ok") and frames >= 2:
            candidates.append(
                {
                    "index": index,
                    "result": result,
                    "frames": frames,
                    "truncated": bool(result.get("truncated")),
                    "meaningful": is_meaningful(case.get("name", "")),
                }
            )
    if not candidates:
        return 0, trace_loaded(meta, tests, code, 0)

    meaningful = [c for c in candidates if c["meaningful"]]
    first = candidates[0]
    if first["meaningful"] and not first["truncated"] and 6 <= first["frames"] <= 100:
        return first["index"], first["result"]

    good = [c for c in meaningful if not c["truncated"] and 6 <= c["frames"] <= 100]
    if good:
        selected = min(good, key=lambda candidate: abs(candidate["frames"] - 50))
        return selected["index"], selected["result"]

    complete = [c for c in meaningful if not c["truncated"]]
    if complete:
        selected = min(complete, key=lambda candidate: abs(candidate["frames"] - 70))
        return selected["index"], selected["result"]

    if meaningful:
        selected = max(meaningful, key=lambda candidate: candidate["frames"])
        return selected["index"], selected["result"]

    selected = min(candidates, key=lambda candidate: candidate["frames"])
    return selected["index"], selected["result"]

def finish_trace(result, problem_id, case_index, tests, code, meta):
    result["version"] = 1
    result["schema"] = SCHEMA
    result["problem"] = problem_id
    result["case_index"] = case_index
    result["code_hash"] = hashlib.sha256(code.encode()).hexdigest()
    with open(HARNESS_PATH, "rb") as handle:
        result["harness_hash"] = hashlib.sha256(handle.read()).hexdigest()
    result["meta_hash"] = hashlib.sha256(
        json.dumps(meta, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    cases = tests.get("cases", [])
    if case_index < len(cases):
        result["case_hash"] = hashlib.sha256(
            json.dumps(cases[case_index], sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
    else:
        result["case_hash"] = None
    result["index_names"] = index_names(code)
    return result


def build(problem_id, force=False):
    directory = os.path.join(CONTENT, "problems", problem_id)
    meta_path = os.path.join(directory, "meta.json")
    tests_path = os.path.join(directory, "tests.json")
    with open(meta_path) as handle:
        meta = json.load(handle)
    with open(tests_path) as handle:
        tests = json.load(handle)
    approach = meta["approaches"][0]["id"]
    with open(os.path.join(directory, "approaches", f"01-{approach}.py")) as handle:
        code = handle.read()

    case_index, result = choose_case(meta, tests, code)
    if result.get("ok") and len(result.get("frames", [])) >= 2:
        result = finish_trace(result, problem_id, case_index, tests, code, meta)
        os.makedirs(TRACES, exist_ok=True)
        path = os.path.join(TRACES, problem_id + ".json")
        with open(path, "w") as handle:
            json.dump(result, handle, separators=(",", ":"))
            handle.write("\n")
        return result, os.path.getsize(path)

    result = trace_loaded(meta, tests, code, 0)
    result = finish_trace(result, problem_id, 0, tests, code, meta)
    os.makedirs(TRACES, exist_ok=True)
    path = os.path.join(TRACES, problem_id + ".json")
    with open(path, "w") as handle:
        json.dump(result, handle, separators=(",", ":"))
        handle.write("\n")
    return result, os.path.getsize(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", action="append", default=[])
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    ids = args.problem or catalog_ids()
    failures = []
    total_bytes = 0
    truncated = 0
    for problem_id in ids:
        result, size = build(problem_id)
        total_bytes += size
        frames = len(result.get("frames", []))
        if result.get("truncated"):
            truncated += 1
        status = "ok" if result.get("ok") and frames >= 2 else "FAIL"
        if status == "FAIL":
            failures.append((problem_id, result.get("error"), frames))
        if not args.quiet:
            print(f"{status:4} {problem_id:52} frames={frames:3} {size / 1024:6.1f} KiB")
    print(f"{len(ids) - len(failures)} traces written, {len(failures)} failed, {truncated} truncated, {total_bytes / 1024 / 1024:.1f} MiB total")
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
