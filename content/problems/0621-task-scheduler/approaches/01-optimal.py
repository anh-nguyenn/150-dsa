from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_frequency = max(counts.values())
    max_count = sum(1 for frequency in counts.values() if frequency == max_frequency)
    skeleton = (max_frequency - 1) * (n + 1) + max_count
    return max(len(tasks), skeleton)
