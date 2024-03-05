test1 = "cabaabac"
test2 = "aa"
test3 = "a"

def minimumLength(s):
    while len(s) > 0 and s[0] == s[-1]:
        print(s)
        left = 0
        right = len(s) - 1
        while left < right:
            print(left, right)
            while s[left] == s[0]:
                left += 1
            while s[right] == s[0]:
                right -= 1
            s = s[left + 1 : right]
    
    return len(s)
    
print(minimumLength(test1))