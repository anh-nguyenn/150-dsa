def is_happy(n: int) -> bool:
    def step(value: int) -> int:
        total = 0
        while value:
            value, digit = divmod(value, 10)
            total += digit * digit
        return total

    slow = n
    fast = step(n)
    while fast != 1 and slow != fast:
        slow = step(slow)
        fast = step(step(fast))
    return fast == 1
