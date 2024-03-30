def countSubarrays(nums, k):
    max_n, count = max(nums), 0
    l = 0
    res = 0

    for r in range(len(nums)):
        if nums[r] == max_n:
            count += 1
        
        while count > k or (l <= r and count == k and nums[l] != max_n):
            if nums[l] == max_n:
                count -= 1
            l += 1
        if count == k:
            res += l + 1       
            
    return res


print(countSubarrays([1,3,2,3,3],2))