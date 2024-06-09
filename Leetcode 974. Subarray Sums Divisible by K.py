test1 = [4,5,0,-2,-3,1]

def subarraysDivByK(nums, k):
    res = 0

    for i in range(len(nums)):
        temp_sum = 0
        for e in range(i, len(nums)):
            temp_sum += nums[e]
            if temp_sum % k == 0:
                res += 1
    
    return res


def subarraysDivByK_Fast(nums, k):
    res, cumulative_sum = 0, 0
    hashmap = {0:1}

    for num in nums:
        cumulative_sum += num
        remainder = cumulative_sum % k

        res += hashmap.get(remainder, 0)
        hashmap[remainder] = 1 + hashmap.get(remainder, 0)

    return res


print(subarraysDivByK(test1, 5))
print(subarraysDivByK_Fast(test1, 5))