def subarraysWithKDistinct(nums, k):
    l = res = 0
    unique = set()

    for r in range(len(nums)):
        print(nums[l : r], unique)
        unique.add(nums[r])
        while len(unique) > k:
            unique.remove(nums[l])
            l += 1
        
        if len(unique) == k:
            res += l
        
    return res

print(subarraysWithKDistinct([1,2,1,3,4,1], 3))