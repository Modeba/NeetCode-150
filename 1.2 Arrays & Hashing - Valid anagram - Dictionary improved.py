def isAnagram(s, t):
    return len(s) != len(t) and makeDictionary(s) == makeDictionary(t)

def makeDictionary(string):
    dictionary = {}
    for letter in string:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

print(isAnagram('hello', 'ellho'))
