def findDuplicate1(nums):
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

def findDuplicate2(nums):
    slow, fast = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    fast = nums[0]
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    
    return slow

print(findDuplicate2([1,3,4,2,2]))