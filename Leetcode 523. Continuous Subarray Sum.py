test1 = [23,2,4,6,7]
test2 = [23,2,6,4,7]

def checkSubarraySum(nums, k):
    for i in range(len(nums)):
        temp_sum = nums[i]
        for e in range(i + 1, len(nums)):
            temp_sum += nums[e]
            if temp_sum % k == 0:
                return True    

    return False

def checkSubarraySumFast(nums, k):
    hashMap = {}
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        remainder = total % k
        if remainder not in hashMap:
            hashMap[remainder] = i
        elif remainder in hashMap and i - hashMap[remainder] > 1:
            return True
    
    return False

print(checkSubarraySum(test2, 13))
print(checkSubarraySumFast(test2, 13))