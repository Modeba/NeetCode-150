test1 = [8,3,5]
test2 = [0,4,3,0,4]
test3 = [0,3,6,7,7]

def specialArray(nums):
    nums.sort()
    length = len(nums)
    
    for i in range(len(nums)):
        if nums[i] >= length - i:
            return length - i
    
    else:
        return -1

print(specialArray(test3))