def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b & mask:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a & 0x80000000 == 0 else ~(a ^ mask)
