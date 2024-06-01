def subarraysWithKDistinct(nums, k):
    l = res = 0
<<<<<<< HEAD
    unique = set()

    for r in range(len(nums)):
        

print(subarraysWithKDistinct([1,2,1,3,4,1], 3))
=======
    uniques = {}

    for r in range(len(nums)):
        print(uniques)
        if nums[r] in uniques:
            uniques[nums[r]] += 1
        else:
            uniques[nums[r]] = 0

        while len(uniques) > k and l <= r:
            uniques[nums[l]] -= 1
            if uniques[nums[l]] == 0:
                del uniques[nums[l]]
            l += 1
        
        if len(uniques) == k:
            res += r - l
        
    return res

print(subarraysWithKDistinct([1,2,1,3,4], 2))
>>>>>>> 20624f20e5851adf8fef324f87586be57d76f7da
