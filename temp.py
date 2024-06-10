test1 = [-1,0,1,2,-1,-4]

def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        print(nums[i])
        temp_sum = nums[i]
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            temp_sum += nums[l] + nums[r]
            if temp_sum > 0:
                r -= 1
            elif temp_sum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
    
    return res

print(threeSum(test1))