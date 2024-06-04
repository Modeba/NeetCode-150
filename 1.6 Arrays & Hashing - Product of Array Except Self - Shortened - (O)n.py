test1 = [1,2,3,4]

def productExceptSelf(nums):
    left, right = [1], [1]
    for i in range(len(nums)):
        left.append(nums[i] * left[i])
        right.append(nums[-i - 1] * right[i])
    right = right[::-1]

    res = []
    for i in range(len(nums)):
        res.append(left[i] * right[i + 1])
    return res

print(productExceptSelf(test1))