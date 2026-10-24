def generate_parenthesis(n: int) -> list[str]:
    result: list[str] = []

    def backtrack(current: str, opened: int, closed: int) -> None:
        if len(current) == 2 * n:
            result.append(current)
            return
        if opened < n:
            backtrack(current + "(", opened + 1, closed)
        if closed < opened:
            backtrack(current + ")", opened, closed + 1)

    backtrack("", 0, 0)
    return result
