test1 = [-1,0,3,5,9,12]

def search(nums, target):
    l = 0
    r = len(nums) - 1
    
    '''In some languages l + r can result in a number greater than 
    2^32 which can cause overflow so l + (l - r) // 2 is recomended'''

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

print(search(test1, 111))