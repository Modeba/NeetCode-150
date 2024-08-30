from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"

def minWindow(s, t):
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

def minWindowFast(s, t):
    if len(t) > len(s):
        return ""

    count = {}
    for char in t:
        count[char] = count.get(char, 0) + 1

    l, start, end, overall = 0, 0, 0, len(count)
    min_len = float("inf")

    for r in range(len(s)):
        if s[r] in count:
            count[s[r]] -= 1
            if count[s[r]] == 0:
                overall -= 1

        while overall == 0:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                start, end = l, r

            if s[l] in count:
                count[s[l]] += 1
                if count[s[l]] > 0:
                    overall += 1
            l += 1

    return s[start:end + 1] if min_len != float("inf") else ""

print(minWindow(s, t))
print(minWindowFast(s, t))