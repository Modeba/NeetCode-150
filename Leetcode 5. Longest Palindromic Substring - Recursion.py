def longestPalindrome(s):
    def is_palindrome(substr):
        return substr == substr[::-1]

    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if is_palindrome(substr) and len(substr) > len(max_palindrome):
                max_palindrome = substr
    return max_palindrome

print(longestPalindrome("babad"))
