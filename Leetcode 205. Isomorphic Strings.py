def isIsomorphic(s, t):
    Map ={}
    for i in range(len(s)):
        
        if s[i] not in Map and t[i] not in Map.values():
            Map[s[i]] = t[i]
        elif s[i] not in Map and t[i] in Map.values():
            return False
        elif Map[s[i]] != t[i]:
            return False

    return True

print(isIsomorphic("paper", "title"))