class TimeMap:
    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        low, high = 0, len(entries) - 1
        best = ""
        while low <= high:
            middle = (low + high) // 2
            if entries[middle][0] <= timestamp:
                best = entries[middle][1]
                low = middle + 1
            else:
                high = middle - 1
        return best
