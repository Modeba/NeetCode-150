test1 = [1,2,2,3,1,4]
test2 = [1,2,3,4,5]

def maxFrequencyElements(nums):
    Map = {}

    for num in nums:
        if num not in Map:
            Map[num] = 1
        else:
            Map[num] += 1

    max_freq = 0
    for num in Map:
        max_freq = max(max_freq, Map[num])

    res = 0
    for num in Map:
        if Map[num] == max_freq:
            res += max_freq
    
    return res

print(maxFrequencyElements(test2))