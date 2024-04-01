def lengthOfLastWord(s):
    res = 0
    for i in range(-1, -len(s) -1, -1):
        if s[i] != ' ':
            res += 1
        elif s[i] == ' ' and res > 0:
            break
    
    return res

