test1 = [1,2,3,4]
test2 = [12,34,56,78]
test3 = [-1,1,0,-3,3]

def productExceptSelf(nums):
    res = [1] * (len(nums))
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
    
print(productExceptSelf(test1))
