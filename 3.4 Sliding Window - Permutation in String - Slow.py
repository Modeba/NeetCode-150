test1s1 = "ab"
test1s2 ="eidbaooo"

test2s1 = "adc"
test2s2 = "dcda"

test3s1 = "hello"
test3s2 = "ooolleoooleh"

def checkInclusion(s1, s2):
    
    def count(myList):
        count = {}
        for char in myList:
            count[char] = 1 + count.get(char, 0)
        return count

    short_dict = count(s1)
    for i in range(len(s2)):
        long_dict = (count(s2[i : i + len(s1)]))
        if long_dict == short_dict:
            return True
    else:
        return False

print(checkInclusion(test1s1, test1s2))