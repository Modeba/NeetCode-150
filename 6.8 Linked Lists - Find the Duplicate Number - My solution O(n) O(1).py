test1 = [7,4,1,5,9,2,3,6,8,10,5]

def findDuplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            print(nums)
            if  nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            

print(findDuplicate(test1))