def minOperations(nums):
    stored = 0
    current_state = False

    for num in nums:
        value = num if not current_state else 1 - num
        
        if value == 0:
            stored += 1
            current_state = not current_state
    return stored



print(minOperations([0,1,1,0,1]))