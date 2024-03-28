def numSubarrayProductLessThanK(nums, k):
    res = 0
    l = r = 0
    product = 1
    while l < len(nums):
