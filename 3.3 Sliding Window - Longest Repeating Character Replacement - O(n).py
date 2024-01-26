# 3.3 Sliding Window - Longest Repeating Character Replacement O(n)

test1 = "AABABBA"
k = 1

def characterReplacement(s, k):
    count = {}
    l = 0
    res = 0
    maxf = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])        

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            res = max(res, r - l + 1)
    return res

print(characterReplacement(test1, k))
