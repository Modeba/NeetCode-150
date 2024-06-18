test1 = "pwwkew"

def lengthOfLongestSubstring(s):
    res, l, subs = 0, 0, set()

    for char in s:
        while char in subs:
            subs.remove(s[l])
            l += 1

        subs.add(char)
        res = max(res, len(subs)) 
    
    return res


print(lengthOfLongestSubstring(test1))