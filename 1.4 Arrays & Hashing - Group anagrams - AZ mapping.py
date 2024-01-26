test1 = ["eat","tea","tan","ate","nat","bat"]
test2 = ["a"]

def groupAnagrams(strs):
    dictionary = {}

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        count = tuple(count)

        if count not in dictionary:
            dictionary[count] = [s]
        else:
            dictionary[count].append(s)

    return dictionary.values()


print(groupAnagrams(test1))
