test1 = [2, 7, 11, 15]
test2 = [1, 2, 3, 4, 5]
test3 = [1, 1]

def twoSum(nums, target):
    for i in range(len(nums)-1):
        if target - nums[i] in nums[i+1 : len(nums)]:
            return i, nums[i + 1 : len(nums)].index(target - nums[i]) + i + 1
        
print(twoSum(test3, 2))
