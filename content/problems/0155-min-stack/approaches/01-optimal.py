class MinStack:
    def __init__(self):
        self.values: list[int] = []
        self.minimums: list[int] = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.minimums or val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        value = self.values.pop()
        if value == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
