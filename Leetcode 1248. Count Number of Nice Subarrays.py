nums = [1,1,2,1,1]
k = 3

def numberOfSubarrays(nums, k):
    res, odds = 0, 0
    l, m = 0, 0
    for r in range(len(nums)):
        if nums[r] % 2:
            odds += 1
        
        while odds > k:
            if nums[l] % 2:
                odds -= 1 
            l += 1 
            m = l

        if odds == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l) + 1

    return res


print(numberOfSubarrays(nums, k))