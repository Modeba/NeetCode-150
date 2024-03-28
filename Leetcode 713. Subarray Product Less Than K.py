def numSubarrayProductLessThanK(nums, k):
    l = res = 0
    product = 1
    
    for r in range(len(nums)):
        product *= nums[r]
        while product >= k and l <= r:
            product /= nums[l]
            l += 1
        
        res += r - l + 1
    
    return res

print(numSubarrayProductLessThanK([10,5,2,6], 100))