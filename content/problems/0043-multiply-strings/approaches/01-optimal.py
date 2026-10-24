def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    digits = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            product = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
            low = i + j + 1
            total = product + digits[low]
            digits[low] = total % 10
            digits[i + j] += total // 10

    start = 0
    while start < len(digits) and digits[start] == 0:
        start += 1
    return "".join(str(d) for d in digits[start:])
