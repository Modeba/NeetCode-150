# 3.3 Sliding Window - Longest Repeating Character Replacement
test1 = "ABAB"
k = 2

def characterReplacement(s, k):
    count = {}
    res, l = 0, 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, res - l + 1)
    return res

print(characterReplacement(test1, k))