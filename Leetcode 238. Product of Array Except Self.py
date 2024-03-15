test1 = [1,2,3,4]
test2 = [-1,1,0,-3,3]

def productExceptSelf(nums):
    left = []
    right = []

    left.append(1)
    product = 1
    for num in nums:
        product *= num
        left.append(product)
    
    product = 1
    for num in nums[::-1]:
        product *= num
        right.append(product)
    right = right[::-1]
    right.append(1)

    res = []
    for i in range(len(left) - 1):
        res.append(left[i] * right[i + 1])
    
    return res

print(productExceptSelf(test2))