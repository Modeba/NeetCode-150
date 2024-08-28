from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"

def minWindow(s,t):
    count = Counter(t)
    l, overall, res = 0, len(count), ''

    for r in range(len(s)):
        if s[r] in count:
            count[s[r]] -= 1
            if count[s[r]] == 0:
                overall -= 1
            
        while overall == 0:
            if not res or len(res) > r - l + 1:
                res = s[l:r + 1]
            if s[l] in count:
                count[s[l]] += 1
                if count[s[l]] > 0:
                    overall += 1
            l += 1
        
    return res

print(minWindow(s, t))