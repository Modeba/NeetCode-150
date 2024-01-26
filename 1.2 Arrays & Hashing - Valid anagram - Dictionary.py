def isAnagram(s, t):
    return makeDictionary(s) == makeDictionary(t)

def makeDictionary(string):
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 0
        else:
            dictionary[letter] += 1

    return dictionary

print(isAnagram('hello', 'ellho'))
