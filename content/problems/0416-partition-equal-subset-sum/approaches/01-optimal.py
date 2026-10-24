def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    reachable = [False] * (target + 1)
    reachable[0] = True
    for value in nums:
        for current in range(target, value - 1, -1):
            if reachable[current - value]:
                reachable[current] = True
    return reachable[target]
