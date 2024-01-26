test1 = ["eat","tea","tan","ate","nat","bat"]
test2 = ["a"]

def groupAnagrams(strs):
    dictionary = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dictionary:
            dictionary[sorted_word] = [word]
        else:
            dictionary[sorted_word].append(word)

    result = []

    for elem in dictionary:
        result.append(dictionary[elem])

    return result

print(groupAnagrams(test1))
