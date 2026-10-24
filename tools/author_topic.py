#!/usr/bin/env python3
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as handle:
        handle.write(text.rstrip() + "\n")


def main():
    if len(sys.argv) != 2:
        print("usage: author_topic.py <payload.json>")
        return 2
    with open(sys.argv[1]) as handle:
        payload = json.load(handle)

    problems = payload.get("problems", [])
    if not problems:
        print("payload has no problems")
        return 2

    for item in problems:
        problem_id = item["id"]
        required = ["entry", "kind", "time", "space", "summary", "background", "hints", "starter", "solution", "idea", "why", "edge_cases", "tests"]
        missing = [key for key in required if key not in item]
        if missing:
            print(f"{problem_id}: missing fields {', '.join(missing)}")
            return 1
        if len(item["hints"]) < 3:
            print(f"{problem_id}: needs at least three hints")
            return 1
        cases = item["tests"].get("cases", [])
        if len(cases) < 5:
            print(f"{problem_id}: needs at least five tests")
            return 1

        directory = os.path.join(CONTENT, "problems", problem_id)
        meta_path = os.path.join(directory, "meta.json")
        if not os.path.isfile(meta_path):
            print(f"{problem_id}: no meta.json; run from the site catalog")
            return 1
        with open(meta_path) as handle:
            meta = json.load(handle)

        approach_id = item.get("approach_id", "optimal")
        approach_name = item.get("approach_name", "Optimal")
        meta["entry"] = item["entry"]
        meta["kind"] = item["kind"]
        meta["approaches"] = [
            {
                "id": approach_id,
                "name": approach_name,
                "time": item["time"],
                "space": item["space"],
            }
        ]
        write(meta_path, json.dumps(meta, indent=2))
        write(os.path.join(directory, "summary.md"), item["summary"])
        write(os.path.join(directory, "background.md"), item["background"])
        hints = "\n\n".join(f"## Hint {index}\n\n{text}" for index, text in enumerate(item["hints"], start=1))
        write(os.path.join(directory, "hints.md"), hints)
        write(os.path.join(directory, "starter.py"), item["starter"])
        write(
            os.path.join(directory, "tests.json"),
            json.dumps(item["tests"], indent=2),
        )
        stem = "01-" + approach_id
        write(os.path.join(directory, "approaches", stem + ".py"), item["solution"])
        note = f"## Idea\n\n{item['idea']}\n\n## Why it works\n\n{item['why']}\n\n## Edge cases\n\n{item['edge_cases']}"
        write(os.path.join(directory, "approaches", stem + ".md"), note)
        print(f"wrote {problem_id}")

    print(f"{len(problems)} problems written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
