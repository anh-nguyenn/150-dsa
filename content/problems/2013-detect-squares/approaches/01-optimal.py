class DetectSquares:
    def __init__(self):
        self.counts: dict[tuple[int, int], int] = {}

    def add(self, point: list[int]) -> None:
        key = (point[0], point[1])
        self.counts[key] = self.counts.get(key, 0) + 1

    def count(self, point: list[int]) -> int:
        px, py = point
        total = 0
        for (x, y), frequency in self.counts.items():
            if x != px and y != py and abs(x - px) == abs(y - py):
                total += (
                    frequency
                    * self.counts.get((x, py), 0)
                    * self.counts.get((px, y), 0)
                )
        return total
