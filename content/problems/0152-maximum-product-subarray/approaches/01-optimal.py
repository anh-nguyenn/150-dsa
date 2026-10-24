def max_product(nums: list[int]) -> int:
    best = current_max = current_min = nums[0]
    for value in nums[1:]:
        if value < 0:
            current_max, current_min = current_min, current_max
        current_max = max(value, current_max * value)
        current_min = min(value, current_min * value)
        best = max(best, current_max)
    return best
