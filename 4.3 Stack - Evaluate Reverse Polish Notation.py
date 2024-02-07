test1 = ["2","1","+","3","*"]
test2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPL(tockens):
    stack = []
    for c in tockens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == '*':
            stack.append(stack.pop() * stack.pop())
        elif c == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]

print(evalRPL(test2))