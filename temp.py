def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    # Sorting allows for two pointer approach
    nums.sort()

    for i in range(len(nums) - 2):
        # To avoid duplicates we check if the element at i index is not
        # the same as previus one. First element doesn't need this check
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Standard two pointer approach
        l, r = i + 1, len(nums) - 1
        while l < r:
            Sum = nums[i] + nums[l] + nums[r]
            if Sum > 0:
                r -= 1
            elif Sum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # Update left pointer if the result is found to avoid ininite loop
                l += 1
                # To further avoid duplicates keep incrementing left pointer until
                # a non duplicate value is found or it reaches right pointer
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    
    return res