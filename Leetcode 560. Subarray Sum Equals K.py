test1 = [1,1,1]
test2 = [1,1,1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1]

def subarraySum(nums, k):
    res = 0
    for i in range(len(nums)):
        tmp_sum = 0
        for e in range(i, len(nums)):
            tmp_sum += nums[e]
            if tmp_sum == k:
                res += 1
    
    return res

def subarraySumFast(nums, k):
        res, cumulative_sum = 0, 0
        # Cumulative_sum of 0 has already been seen once, even before loop begins
        hashmap = {0:1}

        for num in nums:
            # Increase cumulative_sum
            cumulative_sum += num
            diff = cumulative_sum - k

            # Increase result by the value of "diff" key in hashmap
            # Get function returns 0 if key is not in the dictioanry
            res += hashmap.get(diff, 0)
            # Increment the instance of how many times "cumulative_sum" was seen by 1
            hashmap[cumulative_sum] = 1 + hashmap.get(cumulative_sum, 0)

        return res

print(subarraySum(test2, 2))
print(subarraySumFast(test2, 2))