test1 = "babad"
test2 = "a"
test3 = ""

def longestPalindrome(s):
    res = ''
    for i in range(len(s)):
        for e in range(i, len(s)):
            substring = s[i:e + 1]
            print(substring)
            if substring == substring[::-1]:
                if len(substring) > len(res):
                    res = substring
                    print('found', res)
    return res

print(longestPalindrome(test1))