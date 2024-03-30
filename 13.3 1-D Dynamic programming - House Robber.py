def rob(nums):
    rob1, rob2 = 0, 0
    
    for num in nums:
        tmp = max(num + rob1, rob2)
        rob1 = rob2
        rob2 = tmp
        
        print(num, rob1, rob2)
    
    return rob2

print(rob([1,2,3,4]))