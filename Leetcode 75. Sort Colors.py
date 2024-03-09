# Incomplete!

test1 = [0,0,0,2,2,2,0,2,0,2,0,0,2,2]

def asort(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        print(nums)
        while nums[r] != 0:
            r -= 1
        while nums[l] != 2:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
        r -= 1
        l += 1

        return nums
    
print(asort(test1))