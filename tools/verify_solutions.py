#!/usr/bin/env python3
import argparse
import json
import os
import py_compile
import sys

sys.path.insert(0, os.path.dirname(__file__))
from n150_harness import run_problem

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
REQUIRED = ["meta.json", "summary.md", "background.md", "hints.md", "starter.py", "tests.json"]


def catalog_ids():
    with open(os.path.join(CONTENT, "catalog.json")) as handle:
        catalog = json.load(handle)
    ids = []
    for topic in catalog["topics"]:
        ids.extend(topic["problems"])
    return ids


def check_problem(problem_id, require_content=False):
    directory = os.path.join(CONTENT, "problems", problem_id)
    errors = []
    if not os.path.isdir(directory):
        return ["missing problem directory"] if require_content else []

    present = [name for name in REQUIRED if os.path.isfile(os.path.join(directory, name))]
    if not present:
        return ["missing all content"] if require_content else []

    for name in REQUIRED:
        if not os.path.isfile(os.path.join(directory, name)):
            errors.append(f"missing {name}")
    if errors:
        return errors

    try:
        with open(os.path.join(directory, "meta.json")) as handle:
            meta = json.load(handle)
    except Exception as error:
        return [f"meta.json: {error}"]

    approaches = meta.get("approaches") or []
    if not approaches:
        errors.append("no approaches in meta.json")
    else:
        for index, approach in enumerate(approaches, start=1):
            stem = f"{index:02d}-{approach.get('id', '')}"
            code_path = os.path.join(directory, "approaches", stem + ".py")
            note_path = os.path.join(directory, "approaches", stem + ".md")
            if not os.path.isfile(code_path):
                errors.append(f"missing approaches/{stem}.py")
            if not os.path.isfile(note_path):
                errors.append(f"missing approaches/{stem}.md")
            if os.path.isfile(code_path):
                try:
                    py_compile.compile(code_path, doraise=True)
                except py_compile.PyCompileError as error:
                    errors.append(f"{stem}.py does not parse: {error.msg}")

    if os.path.isfile(os.path.join(directory, "starter.py")):
        try:
            py_compile.compile(os.path.join(directory, "starter.py"), doraise=True)
        except py_compile.PyCompileError as error:
            errors.append(f"starter.py does not parse: {error.msg}")

    try:
        with open(os.path.join(directory, "tests.json")) as handle:
            tests = json.load(handle)
        if len(tests.get("cases", [])) < 5:
            errors.append("fewer than five test cases")
    except Exception as error:
        errors.append(f"tests.json: {error}")
        return errors

    if not errors:
        try:
            result = run_problem(directory)
        except Exception as error:
            errors.append(f"runner crashed: {error}")
            result = None
        if result is not None:
            if result.get("error"):
                errors.append(result["error"])
            for case in result["cases"]:
                if not case["passed"]:
                    detail = case.get("error") or f"expected {case.get('expected')!r}, got {case.get('actual')!r}"
                    errors.append(f"{case['name']}: {detail}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", action="append", default=[])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    ids = args.problem or catalog_ids()
    passed = 0
    failed = 0
    skipped = 0
    failures = []

    for problem_id in ids:
        if not args.all and not os.path.isfile(os.path.join(CONTENT, "problems", problem_id, "summary.md")):
            skipped += 1
            continue
        errors = check_problem(problem_id, require_content=args.all)
        if errors:
            failed += 1
            failures.append((problem_id, errors))
            print(f"FAIL {problem_id}")
            for error in errors:
                print(f"     {error}")
        else:
            passed += 1
            if not args.quiet:
                print(f"ok   {problem_id}")

    print(f"\n{passed} passed, {failed} failed, {skipped} without content")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
