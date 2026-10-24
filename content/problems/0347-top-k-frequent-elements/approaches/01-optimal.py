def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, count in counts.items():
        buckets[count].append(value)
    result: list[int] = []
    for count in range(len(buckets) - 1, 0, -1):
        for value in buckets[count]:
            result.append(value)
            if len(result) == k:
                return result
    return result
