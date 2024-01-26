test1 = [2, 7, 11, 15]
test2 = [1, 2, 3, 4, 5]
test3 = [1, 1]

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return hashmap[target - nums[i]], i
        else:
            hashmap[nums[i]] = i
        
print(twoSum(test1, 26))
