def maxSubarrayLength(nums, k):
    Map = {}
    res = l = 0
    for r in range(len(nums)):
        if nums[r] not in Map:
            Map[nums[r]] = 1
        else:
            Map[nums[r]] += 1
            while Map[nums[r]] > k:
                Map[nums[l]] -= 1
                l += 1
        res = max(res, r - l + 1)
    
    return res

print(maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
print(maxSubarrayLength([1,1,1,3], 2))