def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if abs(target) > total or (total + target) % 2 != 0:
        return 0

    goal = (total + target) // 2
    ways = [0] * (goal + 1)
    ways[0] = 1
    for value in nums:
        for current in range(goal, value - 1, -1):
            ways[current] += ways[current - value]
    return ways[goal]
