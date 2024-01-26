test1 = [-1,0,1,2,-1,-4]
test2 = [0,1,1]

def three_sum(nums):
    res = []
    nums.sort()
    print(nums)
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            print(nums[i], 'duplicate')
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
        

print(three_sum(test1))
