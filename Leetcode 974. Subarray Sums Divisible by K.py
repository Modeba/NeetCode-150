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
    res = 0
    hashMap = {}
    total_sum = 0
    
    for i in range(len(nums)):
        total_sum += nums[i]
        remainder = total_sum % k

        if remainder not in hashMap:
            hashMap[remainder] = 1
        else:
            hashMap[remainder] += 1
    
    return hashMap

print(subarraysDivByK(test1, 5))
print(subarraysDivByK_Fast(test1, 5))