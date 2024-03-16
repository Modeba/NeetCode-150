def findMaxLength(nums):
    ones, zeros = 0, 0
    res = 0
    Map = {0 : -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        elif nums[i] == 1:
            ones += 1

        diff = zeros - ones
        
        if diff in Map:
            res = max(res, i - Map[diff])

        else:
            Map[diff] = i

    return res

print(findMaxLength([0,1,0,1]))