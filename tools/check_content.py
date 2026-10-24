#!/usr/bin/env python3
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
SCHEMA = 2
HARNESS_PATH = os.path.join(ROOT, "tools", "n150_harness.py")


def main():
    with open(os.path.join(CONTENT, "catalog.json")) as handle:
        catalog = json.load(handle)

    errors = []
    seen = set()
    total = 0
    for topic in catalog.get("topics", []):
        total += len(topic.get("problems", []))
        if not os.path.isfile(os.path.join(CONTENT, "topics", topic["id"] + ".md")):
            errors.append(f"missing topic intro for {topic['id']}")
        for problem_id in topic.get("problems", []):
            if problem_id in seen:
                errors.append(f"duplicate problem id {problem_id}")
            seen.add(problem_id)
            meta_path = os.path.join(CONTENT, "problems", problem_id, "meta.json")
            if not os.path.isfile(meta_path):
                errors.append(f"missing meta.json for {problem_id}")
                continue
            with open(meta_path) as handle:
                meta = json.load(handle)
            if meta.get("id") != problem_id:
                errors.append(f"meta id mismatch for {problem_id}")
            if not meta.get("title"):
                errors.append(f"missing title for {problem_id}")
            if meta.get("difficulty") not in {"Easy", "Medium", "Hard"}:
                errors.append(f"invalid difficulty for {problem_id}")

            approaches = meta.get("approaches") or []
            if not approaches:
                errors.append(f"no approaches for {problem_id}")
            else:
                code_path = os.path.join(
                    CONTENT, "problems", problem_id, "approaches", f"01-{approaches[0]['id']}.py"
                )
                tests_path = os.path.join(CONTENT, "problems", problem_id, "tests.json")
                trace_path = os.path.join(CONTENT, "traces", problem_id + ".json")
                if not os.path.isfile(trace_path):
                    errors.append(f"missing trace for {problem_id} (run npm run traces)")
                elif not os.path.isfile(code_path) or not os.path.isfile(tests_path):
                    errors.append(f"missing solution or tests for {problem_id}")
                else:
                    with open(code_path) as handle:
                        code = handle.read()
                    with open(tests_path) as handle:
                        tests = json.load(handle)
                    with open(trace_path) as handle:
                        trace = json.load(handle)
                    code_hash = hashlib.sha256(code.encode()).hexdigest()
                    with open(HARNESS_PATH, "rb") as handle:
                        harness_hash = hashlib.sha256(handle.read()).hexdigest()
                    meta_hash = hashlib.sha256(
                        json.dumps(meta, sort_keys=True, separators=(",", ":")).encode()
                    ).hexdigest()
                    if trace.get("schema") != SCHEMA:
                        errors.append(f"trace schema is old for {problem_id} (run npm run traces)")
                    if trace.get("problem") != problem_id:
                        errors.append(f"trace problem mismatch for {problem_id}")
                    if not trace.get("ok"):
                        errors.append(f"trace failed for {problem_id}: {trace.get('error')}")
                    if trace.get("code_hash") != code_hash:
                        errors.append(f"stale trace for {problem_id} (run npm run traces)")
                    if trace.get("harness_hash") != harness_hash:
                        errors.append(f"trace harness is stale for {problem_id} (run npm run traces)")
                    if trace.get("meta_hash") != meta_hash:
                        errors.append(f"trace metadata is stale for {problem_id} (run npm run traces)")
                    case_index = trace.get("case_index", 0)
                    cases = tests.get("cases", [])
                    if case_index < 0 or case_index >= len(cases):
                        errors.append(f"trace case index out of range for {problem_id}")
                    else:
                        case_hash = hashlib.sha256(
                            json.dumps(cases[case_index], sort_keys=True, separators=(",", ":")).encode()
                        ).hexdigest()
                        if trace.get("case_hash") != case_hash:
                            errors.append(f"stale trace case for {problem_id} (run npm run traces)")
                    if not trace.get("frames"):
                        errors.append(f"empty trace for {problem_id}")
                    line_count = len(code.splitlines())
                    for frame in trace.get("frames", []):
                        if not 1 <= frame.get("line", 0) <= line_count:
                            errors.append(f"trace line out of range for {problem_id}")
                            break

    if total != 150:
        errors.append(f"catalog has {total} problems, expected 150")
    if len(catalog.get("topics", [])) != 18:
        errors.append(f"catalog has {len(catalog.get('topics', []))} topics, expected 18")

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"catalog ok: {total} problems in {len(catalog['topics'])} topics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
