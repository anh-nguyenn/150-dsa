def permute(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    used = [False] * len(nums)
    path: list[int] = []

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for index, value in enumerate(nums):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            backtrack()
            path.pop()
            used[index] = False

    backtrack()
    return result
