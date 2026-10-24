def find_min(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        middle = (low + high) // 2
        if nums[middle] <= nums[high]:
            high = middle
        else:
            low = middle + 1
    return nums[low]
