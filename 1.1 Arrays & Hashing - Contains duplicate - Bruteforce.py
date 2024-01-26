test1 = [1,1,1,3,3,4,3,2,4,2]
test2 = [1,2,3,4,5,6]
test3 = [1,3,4,3,2,4,2]

def containsDuplicate(nums):
    for i in range(len(nums)):
        for e in range(i+1, len(nums)):
            if nums[i] == nums[e]:
                return True

    return False

print(containsDuplicate(test3))
