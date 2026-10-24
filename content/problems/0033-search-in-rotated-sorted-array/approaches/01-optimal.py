def search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] == target:
            return middle
        if nums[low] <= nums[middle]:
            if nums[low] <= target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        else:
            if nums[middle] < target <= nums[high]:
                low = middle + 1
            else:
                high = middle - 1
    return -1
