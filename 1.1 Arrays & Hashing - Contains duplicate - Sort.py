test1 = [1,1,1,3,3,4,3,2,4,2]
test2 = [1,2,3,4,5,6]
test3 = [1,2,3,4,5,6,6]

def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    else:
        return False

print(containsDuplicate(test3))
