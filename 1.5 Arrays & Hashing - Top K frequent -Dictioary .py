test1 = [1,1,1,2,2,3]
test2 = [1]
test3 = [2,6,4,2,5,6,7,5,5,4,3,3,6,8,9,7,6,6,5,5,3,3,4,5,2,3,6,6,2,3,6,9,9,9,9,9]

def topKFrequent(nums, k):
    dictionary = {}
    freq = [[] for i in range(len(nums) + 1)]
    print(freq)

    for n in nums:
        dictionary[n] = 1 + dictionary.get(n, 0)
    for n, c in dictionary.items():
        freq[c].append(n)
    print(freq)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res
    
print(topKFrequent(test3, 3))
