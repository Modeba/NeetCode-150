test1 = ["abc", "ahbgdc"]

def isSubsequence(s, t):
    if len(s) == 0:
        return True
    
    index = 0
    length = len(s) - 1

    for char in t:
        if char == s[index]:
            if index == length:
                return True
            index += 1
    
    return False

print(isSubsequence(test1[0], test1[1]))