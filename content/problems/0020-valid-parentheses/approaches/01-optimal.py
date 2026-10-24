def is_valid(s: str) -> bool:
    partners = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in s:
        if char in partners:
            if not stack or stack[-1] != partners[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
