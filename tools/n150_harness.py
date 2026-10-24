import ast
import copy
import json
import math
import os
import sys
import time
import traceback
import types
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, neighbors=None, next=None, random=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.next = next
        self.random = random


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_values(head):
    values = []
    seen = set()
    while head is not None:
        if id(head) in seen:
            values.append("<cycle>")
            break
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


def tree_values(root):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


def build_graph(adjacency):
    if not adjacency:
        return None
    nodes = [Node(i + 1) for i in range(len(adjacency))]
    for index, neighbors in enumerate(adjacency):
        nodes[index].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_values(node):
    if node is None:
        return []
    seen = {}
    queue = deque([node])
    seen[node] = True
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in seen:
                seen[neighbor] = True
                queue.append(neighbor)
    adjacency = []
    for current in sorted(seen, key=lambda item: item.val):
        adjacency.append(sorted(n.val for n in current.neighbors))
    return adjacency


def build_random_list(spec):
    nodes = [Node(val) for val, _ in spec]
    for index, (_, random_index) in enumerate(spec):
        if index + 1 < len(nodes):
            nodes[index].next = nodes[index + 1]
        if random_index is not None:
            nodes[index].random = nodes[random_index]
    return nodes[0] if nodes else None


def random_list_values(head):
    order = []
    current = head
    while current is not None:
        order.append(current)
        current = current.next
    index_of = {id(node): i for i, node in enumerate(order)}
    return [[node.val, index_of.get(id(node.random)) if node.random is not None else None] for node in order]


def build_arg(value):
    if isinstance(value, dict):
        if "linked_list" in value:
            head = build_list(value["linked_list"])
            cycle = value.get("cycle")
            if cycle is not None and head is not None:
                nodes = []
                current = head
                while current is not None:
                    nodes.append(current)
                    current = current.next
                if nodes:
                    nodes[-1].next = nodes[cycle]
            return head
        if "tree" in value:
            return build_tree(value["tree"])
        if "graph_adj" in value:
            return build_graph(value["graph_adj"])
        if "random_list" in value:
            return build_random_list(value["random_list"])
    if isinstance(value, list):
        return [build_arg(item) for item in value]
    return copy.deepcopy(value)


def jsonable(value):
    if isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
        return str(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, (list, tuple, set)):
        items = [jsonable(item) for item in value]
        if isinstance(value, set):
            return sorted(items, key=repr)
        return items
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, ListNode):
        return list_values(value)
    if isinstance(value, TreeNode):
        return tree_values(value)
    if isinstance(value, Node):
        if value.neighbors:
            return graph_values(value)
        if value.next is not None or value.random is not None:
            return random_list_values(value)
        return value.val
    return str(value)


def serialize(value, adapter=None):
    if adapter == "linked_list":
        return list_values(value)
    if adapter == "tree":
        return tree_values(value)
    if adapter == "graph_adj":
        return graph_values(value)
    if adapter == "random_list":
        return random_list_values(value)
    return jsonable(value)


def canonical(value):
    if isinstance(value, list):
        items = [canonical(item) for item in value]
        return sorted(items, key=repr)
    if isinstance(value, tuple):
        return canonical(list(value))
    if isinstance(value, set):
        return canonical(list(value))
    if isinstance(value, dict):
        return {key: canonical(item) for key, item in value.items()}
    return value


def compare(actual, expected, mode="exact", tolerance=1e-6):
    if mode == "unordered":
        if isinstance(actual, list) and isinstance(expected, list):
            return sorted(actual, key=repr) == sorted(expected, key=repr)
        return actual == expected
    if mode == "unordered_deep":
        return canonical(actual) == canonical(expected)
    if mode == "float":
        return compare_float(actual, expected, tolerance)
    return actual == expected


def compare_float(actual, expected, tolerance=1e-6):
    if isinstance(actual, (list, tuple)) and isinstance(expected, (list, tuple)):
        if len(actual) != len(expected):
            return False
        return all(compare_float(a, e, tolerance) for a, e in zip(actual, expected))
    if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        return math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance)
    return actual == expected


def load_namespace(code):
    namespace = {
        "ListNode": ListNode,
        "TreeNode": TreeNode,
        "Node": Node,
        "deque": deque,
    }
    exec(compile(code, "<solution>", "exec"), namespace)
    return namespace


def describe_error(error):
    return "".join(traceback.format_exception_only(type(error), error)).strip()


def run_function_case(namespace, entry, tests, case):
    args = [build_arg(arg) for arg in case.get("args", [])]
    started = time.perf_counter()
    returned = namespace[entry](*args)
    elapsed = (time.perf_counter() - started) * 1000
    result_mode = tests.get("result", "return")
    if result_mode == "arg0":
        actual = args[0] if args else None
    elif result_mode == "args":
        actual = args
    else:
        actual = returned
    adapter = tests.get("result_adapter") or case.get("result_adapter")
    actual = serialize(actual, adapter)
    expected = case.get("expected")
    return actual, expected, elapsed


def run_class_case(namespace, entry, tests, case):
    ops = case.get("ops") or []
    args = case.get("args") or []
    expected = case.get("expected") or []
    adapters = case.get("adapters") or []
    results = []
    instance = None
    elapsed = 0.0
    for index, op in enumerate(ops):
        raw_args = args[index] if index < len(args) else []
        call_args = []
        for arg in raw_args:
            if isinstance(arg, dict) and "from_op" in arg:
                call_args.append(results[arg["from_op"]])
            else:
                call_args.append(build_arg(arg))
        started = time.perf_counter()
        if index == 0:
            instance = namespace[entry](*call_args)
            value = None
        else:
            value = getattr(instance, op)(*call_args)
        elapsed += (time.perf_counter() - started) * 1000
        adapter = adapters[index] if index < len(adapters) else None
        results.append(serialize(value, adapter))
    return results, expected, elapsed


FILENAME = "<solution>"
TRACE_FRAME_CAP = 120


def scalar_value(value):
    if isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
        return str(value)
    if isinstance(value, str):
        return value if len(value) <= 60 else value[:57] + "..."
    if isinstance(value, (bool, int, float)) or value is None:
        return value
    return None


def is_scalar(value):
    return isinstance(value, (bool, int, float, str)) or value is None


def safe_text(value, limit=100):
    text = repr(value)
    return text if len(text) <= limit else text[: limit - 1] + "..."


def summarize_value(value, depth=0):
    if depth > 3:
        return {"kind": "text", "value": safe_text(value)}
    if isinstance(value, TreeNode):
        values = tree_values(value)
        return {"kind": "tree", "value": values[:63], "truncated": len(values) > 63}
    if isinstance(value, ListNode):
        values = list_values(value)
        return {"kind": "linked_list", "value": values[:40], "truncated": len(values) > 40}
    if isinstance(value, Node):
        if value.neighbors:
            return {"kind": "graph", "value": graph_values(value)}
        if value.next is not None or value.random is not None:
            return {"kind": "random_list", "value": random_list_values(value)[:40]}
        return {"kind": "scalar", "value": value.val}
    if is_scalar(value):
        if isinstance(value, str):
            return {"kind": "string", "value": value[:160], "length": len(value)}
        return {"kind": "scalar", "value": scalar_value(value)}
    if isinstance(value, (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, types.MethodType, type)):
        return None
    if isinstance(value, deque):
        items = list(value)
        return {
            "kind": "queue",
            "value": [scalar_value(item) if is_scalar(item) else summarize_value(item, depth + 1) for item in items[:30]],
            "length": len(items),
            "truncated": len(items) > 30,
        }
    if isinstance(value, dict):
        entries = []
        for key, item in list(value.items())[:20]:
            entries.append({"key": safe_text(key, 40), "value": summarize_value(item, depth + 1)})
        return {"kind": "map", "entries": entries, "length": len(value), "truncated": len(value) > 20}
    if isinstance(value, (set, frozenset)):
        items = sorted(value, key=lambda item: safe_text(item, 80))
        return {
            "kind": "set",
            "value": [scalar_value(item) if is_scalar(item) else summarize_value(item, depth + 1) for item in items[:24]],
            "length": len(items),
            "truncated": len(items) > 24,
        }
    if isinstance(value, (list, tuple)):
        items = list(value)
        if all(is_scalar(item) for item in items):
            return {
                "kind": "array",
                "value": [scalar_value(item) for item in items[:40]],
                "length": len(items),
                "truncated": len(items) > 40,
            }
        if items and all(isinstance(item, (list, tuple)) for item in items):
            rows = [list(row) for row in items]
            if all(all(is_scalar(cell) for cell in row) for row in rows):
                width = max((len(row) for row in rows), default=0)
                return {
                    "kind": "grid",
                    "value": [[scalar_value(cell) for cell in row[:14]] for row in rows[:12]],
                    "rows": len(rows),
                    "cols": width,
                    "truncated": len(rows) > 12 or width > 14,
                }
        return {
            "kind": "list",
            "value": [summarize_value(item, depth + 1) for item in items[:16]],
            "length": len(items),
            "truncated": len(items) > 16,
        }
    if hasattr(value, "__dict__"):
        attributes = []
        for name, item in list(vars(value).items())[:16]:
            if name.startswith("__"):
                continue
            summary = summarize_value(item, depth + 1)
            if summary is not None:
                attributes.append({"name": name, **summary})
        return {
            "kind": "object",
            "class": value.__class__.__name__,
            "attributes": attributes,
            "truncated": len(vars(value)) > 16,
        }
    return {"kind": "text", "value": safe_text(value)}


def summarize_locals(frame):
    variables = []
    for name, value in frame.f_locals.items():
        if name.startswith("__"):
            continue
        summary = summarize_value(value)
        if summary is None:
            continue
        variables.append({"name": name, **summary})
    return variables


def trace_depth(frame):
    depth = 0
    parent = frame.f_back
    while parent is not None and parent.f_code.co_filename == FILENAME:
        depth += 1
        parent = parent.f_back
    return depth


def statement_lines(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.stmt):
            lines.add(node.lineno)
    return lines


class TraceRecorder:
    def __init__(self, max_frames=TRACE_FRAME_CAP, lines=None):
        self.max_frames = max_frames
        self.frames = []
        self.truncated = False
        self.last_signature = None
        self.lines = lines

    def global_trace(self, frame, event, arg):
        if frame.f_code.co_filename != FILENAME:
            return None
        if self.truncated:
            return None
        return self.local_trace

    def local_trace(self, frame, event, arg):
        if self.truncated:
            return None
        if event == "line":
            if self.lines is not None and frame.f_lineno not in self.lines:
                return self.local_trace
            if len(self.frames) >= self.max_frames:
                self.truncated = True
                return None
            variables = summarize_locals(frame)
            signature = (frame.f_lineno, frame.f_code.co_name, json.dumps(variables, sort_keys=True))
            if signature != self.last_signature:
                self.last_signature = signature
                self.frames.append(
                    {
                        "line": frame.f_lineno,
                        "function": frame.f_code.co_name,
                        "depth": trace_depth(frame),
                        "vars": variables,
                    }
                )
        return self.local_trace


def execute_class_case(namespace, entry, case):
    ops = case.get("ops") or []
    args = case.get("args") or []
    results = []
    instance = None
    for index, op in enumerate(ops):
        raw_args = args[index] if index < len(args) else []
        call_args = []
        for arg in raw_args:
            if isinstance(arg, dict) and "from_op" in arg:
                call_args.append(results[arg["from_op"]])
            else:
                call_args.append(build_arg(arg))
        if index == 0:
            instance = namespace[entry](*call_args)
            results.append(None)
        else:
            results.append(getattr(instance, op)(*call_args))
    return instance, results


def trace_loaded(meta, tests, code, case_index=0):
    cases = tests.get("cases", [])
    if not cases:
        return {"ok": False, "error": "No test cases to visualize.", "frames": [], "truncated": False}
    case_index = max(0, min(case_index, len(cases) - 1))
    case = cases[case_index]
    try:
        namespace = load_namespace(code)
    except Exception as error:
        return {
            "ok": False,
            "error": describe_error(error),
            "case": {"name": case.get("name", "case"), "args": case.get("args", []), "ops": case.get("ops")},
            "frames": [],
            "truncated": False,
        }

    recorder = TraceRecorder(lines=statement_lines(code))
    error = None
    output = None
    is_class = meta.get("kind", "function") == "class"
    sys.settrace(recorder.global_trace)
    try:
        if is_class:
            execute_class_case(namespace, meta["entry"], case)
        else:
            args = [build_arg(arg) for arg in case.get("args", [])]
            output = namespace[meta["entry"]](*args)
    except Exception as caught:
        error = describe_error(caught)
    finally:
        sys.settrace(None)

    return {
        "ok": error is None,
        "error": error,
        "kind": meta.get("kind", "function"),
        "case": {
            "name": case.get("name", "case"),
            "args": case.get("args", []),
            "ops": case.get("ops"),
        },
        "output": summarize_value(output) if output is not None else None,
        "frames": recorder.frames,
        "truncated": recorder.truncated,
    }


def trace_payload(meta_json, tests_json, code, case_index=0):
    return json.dumps(trace_loaded(json.loads(meta_json), json.loads(tests_json), code, case_index))


def run_loaded(meta, tests, code):
    try:
        namespace = load_namespace(code)
    except Exception as error:
        return {
            "ok": False,
            "error": describe_error(error),
            "cases": [],
        }
    entry = meta["entry"]
    mode = tests.get("compare", "exact")
    tolerance = tests.get("tolerance", 1e-6)
    is_class = meta.get("kind", "function") == "class"
    case_results = []
    for case in tests.get("cases", []):
        try:
            if is_class:
                actual, expected, elapsed = run_class_case(namespace, entry, tests, case)
                if isinstance(expected, list) and isinstance(actual, list):
                    passed = len(actual) == len(expected) and all(
                        e == "*" or compare(a, e, mode, tolerance) for a, e in zip(actual, expected)
                    )
                else:
                    passed = expected == "*" or compare(actual, expected, mode, tolerance)
            else:
                actual, expected, elapsed = run_function_case(namespace, entry, tests, case)
                passed = compare(actual, expected, mode, tolerance)
            case_results.append(
                {
                    "name": case.get("name", "case"),
                    "passed": passed,
                    "expected": expected,
                    "actual": actual,
                    "ms": round(elapsed, 3),
                    "args": case.get("args", []),
                    "ops": case.get("ops"),
                }
            )
        except Exception as error:
            case_results.append(
                {
                    "name": case.get("name", "case"),
                    "passed": False,
                    "error": describe_error(error),
                }
            )
    return {
        "ok": all(case["passed"] for case in case_results) and bool(case_results),
        "error": None,
        "cases": case_results,
    }


def run_payload(meta_json, tests_json, code):
    meta = json.loads(meta_json)
    tests = json.loads(tests_json)
    return json.dumps(run_loaded(meta, tests, code))


def run_problem(problem_dir, code=None):
    with open(os.path.join(problem_dir, "meta.json")) as handle:
        meta = json.load(handle)
    with open(os.path.join(problem_dir, "tests.json")) as handle:
        tests = json.load(handle)
    if code is None:
        approach = meta["approaches"][0]["id"]
        code_path = os.path.join(problem_dir, "approaches", f"01-{approach}.py")
        with open(code_path) as handle:
            code = handle.read()
    return run_loaded(meta, tests, code)
