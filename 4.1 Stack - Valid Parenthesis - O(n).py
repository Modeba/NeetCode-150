test1 = '()'
test2 = '()[]{}'
test3 = '(['
test4 = '([)]'

def isValid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for char in s:
        if stack and stack[-1] == pairs.get(char, None):
            stack.pop()
            continue
        stack.append(char)
    return not stack

print(isValid(test3))