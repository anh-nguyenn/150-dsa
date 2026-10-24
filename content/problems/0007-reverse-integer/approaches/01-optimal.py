def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    value = abs(x)
    result = 0
    while value:
        result = result * 10 + value % 10
        value //= 10
    result *= sign
    if result < -(1 << 31) or result > (1 << 31) - 1:
        return 0
    return result
