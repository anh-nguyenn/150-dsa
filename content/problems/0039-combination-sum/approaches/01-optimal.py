def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result: list[list[int]] = []

    def backtrack(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for index in range(start, len(candidates)):
            value = candidates[index]
            if value > remaining:
                break
            path.append(value)
            backtrack(index, remaining - value, path)
            path.pop()

    backtrack(0, target, [])
    return result
