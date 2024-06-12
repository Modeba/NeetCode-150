test1 = [2,0,2,1,1,0]
test2 = [0,1,2,0,1,2,0,0,0,0,0]
test3 = [1,2,0]

def sortColorsOnePass(nums):
    l, r = 0, len(nums) - 1
    i = 0
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
    
    return nums

print(sortColorsOnePass(test2))