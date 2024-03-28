def mergeAlternately(word1, word2):
    res = ''
    for i in range(min(len(word1), len(word2))):
        res += word1[i]
        res += word2[i]
    
    # If length of the string is 3, string[3] will cause
    # an error but string [3:] somehow does not.
    res += word1[i + 1:]
    res += word2[i + 1:]

    return res

print(mergeAlternately('abc', 'defghi'))

sss = 'abc'
print(sss[3:])