def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result: list[list[int]] = []

    def backtrack(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for index in range(start, len(candidates)):
            if index > start and candidates[index] == candidates[index - 1]:
                continue
            value = candidates[index]
            if value > remaining:
                break
            path.append(value)
            backtrack(index + 1, remaining - value, path)
            path.pop()

    backtrack(0, target, [])
    return result
