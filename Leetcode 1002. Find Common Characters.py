from collections import Counter

test1 = ["bella","label","roller"]

def commonChars(words):
    count = Counter(words[0])

    for word in words:
        current = Counter(word)
        for char in count:
            count[char] = min(count[char], current[char])
    
    res = []
    for char in count:
        for i in range(count[char]):
            res.append(char)
    
    return res

print(commonChars(test1))