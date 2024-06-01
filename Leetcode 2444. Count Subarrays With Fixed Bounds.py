def countSubarrays(nums, minK, maxK):
    filtered = []
    res = 0
    l = 0

    for num in nums:
        if not minK <= num <= maxK:
            filtered.append(False)
        else:
            filtered.append(num)
    
    print(filtered)

    while l < len(filtered):
        if filtered[l]:
            r = l
            while r < len(filtered) and filtered[r]:
                r += 1
            res += 1
            l = r
        l += 1

    return res

print(countSubarrays([1,3,5,2,7,5], 1, 5))