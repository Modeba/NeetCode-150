test1s1 = "ab"
test1s2 ="eidbaooo"

test2s1 = "adc"
test2s2 = "dcda"

test3s1 = "hello"
test3s2 = "ooolleoooleh"

def checkInclusion(s1, s2):
    def count(myList):
        count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
                 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
                 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
                 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
        for char in myList:
            count[char] += 1
        return count
    
    def display(some_dict):
        res = ''
        for char in some_dict:
            if some_dict[char] != 0:
                res += char + str(some_dict[char])
        print(res)

    s1_dict = count(s1)
    s2_dict = count(s2[:len(s1)])
    display(s1_dict)
    display(s2_dict)
    if s1_dict == s2_dict:
        return True
    
    print(len(s2), len(s1))
    for i in range(1, len(s2) - len(s1) + 1):
        print(i)
        s2_dict[s2[i + len(s1) - 1]] += 1
        display(s2_dict)
        s2_dict[s2[i - 1]] -= 1
        display(s2_dict)
        if s2_dict == s1_dict:
            return True
    return False

print(checkInclusion(test2s1, test2s2))