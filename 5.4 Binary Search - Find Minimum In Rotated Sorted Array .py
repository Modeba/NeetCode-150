test1 = [3,4,5,1,2]
test2 = [4,5,6,7,8,1,2,3]

def findMin(nums):
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = l + (r - l) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    
    return res

print(findMin(test2))