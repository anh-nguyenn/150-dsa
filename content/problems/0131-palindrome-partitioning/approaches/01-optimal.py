def partition(s: str) -> list[list[str]]:
    result: list[list[str]] = []

    def backtrack(start: int, pieces: list[str]) -> None:
        if start == len(s):
            result.append(pieces[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                pieces.append(piece)
                backtrack(end, pieces)
                pieces.pop()

    backtrack(0, [])
    return result
