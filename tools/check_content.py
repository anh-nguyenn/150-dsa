#!/usr/bin/env python3
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")


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
