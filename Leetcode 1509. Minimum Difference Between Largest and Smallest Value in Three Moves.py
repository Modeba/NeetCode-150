import heapq

test1 = [1,5,0,10,14]

def minDifference(nums):
    if len(nums) <= 4:
        return 0
    
    nums.sort()
    res = nums[-1] - nums[0]

    for l in range(4):
        r = len(nums) - 4 + l
        res = min(res, nums[r] - nums[l])
    
    return res

def minDifferenceFast(nums):
    if len(nums) <= 4:
        return 0
    
    min_four = sorted(heapq.nsmallest(4, nums))
    max_four = sorted(heapq.nlargest(4, nums))

    res = max_four[0] - min_four[0]
    for i in range(1, 4):
        res = min(res, max_four[i] - min_four[i])
    
    return res


print(minDifference(test1))
print(minDifferenceFast(test1))