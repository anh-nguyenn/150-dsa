def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])
        for index in range(start, len(nums)):
            if index > start and nums[index] == nums[index - 1]:
                continue
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result
