test1 = "abccccdd"

def longestPalindrome(s):
    hashMap = {}
    for char in s:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    
    print(hashMap)
    res = 0
    odd_value_used = False
    for value in hashMap.values():
        print(res, value, odd_value_used)
        if value % 2 == 1:
            if not odd_value_used:
                res += value
                odd_value_used = True
            else:
                res += (value - 1)
        else:
            res += value
    return res

def longestPalindrome_sol2(s):
    non_duplicates = set()
    for char in s:
        non_duplicates.add(char) if char not in non_duplicates else non_duplicates.remove(char)
    
    if len(non_duplicates) != 0:
        return len(s) - len(non_duplicates) + 1
    else:
        return len(s)

print(longestPalindrome(test1))
print(longestPalindrome_sol2(test1))