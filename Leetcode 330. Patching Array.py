test1 = [1,3]

def minPatches(nums, n):
    missing, res, i = 1, 0, 0

    while missing <= n:
        print(missing, res, i, nums[i])
        if i < len(nums) and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            missing *= 2
            res += 1
    
    return res

print(minPatches(test1, 6))