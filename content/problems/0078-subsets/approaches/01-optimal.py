def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])
        for index in range(start, len(nums)):
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result
