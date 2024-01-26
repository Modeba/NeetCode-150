test1 = "A man, a plan, a canal: Panama"
test2 = "race a car"
test3 = "race car"
test4 = " "

def is_palindrome(string):
    clean = ''
    for letter in string:
        if letter.isalnum():
            clean += letter.lower()

    return clean == clean[::-1]

print(is_palindrome(test3))
