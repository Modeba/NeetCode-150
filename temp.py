test1 = "A man, a plan, a canal: Panama"
test2 = ""
test3 = "a."

def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            print(s[l:r + 1])
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome(test3))