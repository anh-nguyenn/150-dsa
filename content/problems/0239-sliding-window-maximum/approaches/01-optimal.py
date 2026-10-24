from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    candidates: deque[int] = deque()
    result: list[int] = []
    for i, value in enumerate(nums):
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(i)
        if candidates[0] <= i - k:
            candidates.popleft()
        if i >= k - 1:
            result.append(nums[candidates[0]])
    return result
