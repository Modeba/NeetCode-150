test1 = "abcabcbb"
test2 = "bbbbb"
test3 = "pwwkew"
test4 = "bbtablud"

def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[i])
        res = max(res, i - l + 1)
    return res

print(lengthOfLongestSubstring(test4))
