test1 = [-2,1,-3,4,-1,2,1,-5,4]
test2 = [1,2,-1,-2,2,1,-2,1,4,-5,4]

def maxSubArray(nums):
    res = sum(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        print(nums[l], nums[r], res, nums[l:r + 1])
        if nums[l] > nums[r]:
            r -= 1
        elif nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
        res = max(res, sum(nums[l:r + 1]))
    
    return res

print(maxSubArray(test2))