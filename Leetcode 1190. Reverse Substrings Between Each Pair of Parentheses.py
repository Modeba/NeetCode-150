test1 = "(ed(et(oc))el)"

def reverseParentheses(s):
    stack = []

    for c in s:
        if c == ')':
            portion = []
            while stack[-1] != '(':
                portion.append(stack.pop())
            stack.pop()
            stack.extend(portion)
        else:
            stack.append(c)
    return ''.join(stack)


print(reverseParentheses(test1))