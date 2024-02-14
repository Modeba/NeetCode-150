import collections

test1 = [3,1,-2,-5,2,-4]
test2 = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]

def rearrangeArray(nums):
    i = 0
    j = 1
    res = [[]] * len(nums)
    print(res)

    for num in nums:
        print(i, j, num)
        if num > 0:
            res[i] = num
            i += 2
        else:
            res[j] = num
            j += 2

    return res

print(rearrangeArray(test1))