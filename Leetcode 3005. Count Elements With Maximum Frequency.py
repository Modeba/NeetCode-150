test1 = [1,2,2,3,1,4]
test2 = [1,2,3,4,5]
test3 = [93]
test4 = [46,64]
test5 = [14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77,14,50,86,23,59,95,32,68,5,41,77]

def maxFrequencyElements(nums):
    Map = {}
    max_freq = 1
    for num in nums:
        if num not in Map:
            Map[num] = 1
        else:
            Map[num] += 1
            max_freq = max(max_freq, Map[num])

    print(Map)
    res = 0
    for num in Map:
        if Map[num] == max_freq:
            res += max_freq
    
    return res

print(maxFrequencyElements(test5))