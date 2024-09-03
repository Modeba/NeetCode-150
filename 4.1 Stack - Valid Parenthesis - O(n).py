test1 = '()'
test2 = '()[]{}'
test3 = '(['
test4 = '([)]'

def isValid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for char in s:
        stack.pop() if stack and stack[-1] == pairs.get(char, None) else stack.append(char)

    return not stack

def isValidShort(s):
    pairs, stack = {")": "(", "]": "[", "}": "{"}, []
    [stack.pop() if stack and stack[-1] == pairs[char] else stack.append(char) for char in s if char in pairs.values() or char in pairs]
    return not stack

print(isValid(test2))
print(isValidShort(test2))