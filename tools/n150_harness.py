import copy
import json
import math
import os
import time
import traceback
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
