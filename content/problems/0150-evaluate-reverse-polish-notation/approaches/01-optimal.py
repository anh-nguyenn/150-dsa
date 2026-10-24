def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for token in tokens:
        if token == "+":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif token == "-":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == "*":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif token == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[-1]
