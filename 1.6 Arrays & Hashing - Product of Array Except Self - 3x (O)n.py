test1 = [1,2,3,4]
test2 = [12,34,56,78]
test3 = [-1,1,0,-3,3]

def productExceptSelf(nums):
    left = [1]
    right = [1]
    result = []

    for i in range(len(nums)):
        left.append(nums[i] * left[i])
    print(left)

    for i in range(len(nums)-1):
        right.append(nums[::-1][i] * right[i])
    right.append(1)
    right = right[::-1]
    print(right)

    for i in range(1, len(right)):
        result.append(right[i] * left[i-1])

    return result
    
print(productExceptSelf(test3))
