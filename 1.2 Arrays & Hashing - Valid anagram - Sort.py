def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    s = sorted(s)
    t = sorted(t)
    
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    else:
        return True

print(isAnagram('hello', 'ellho'))
