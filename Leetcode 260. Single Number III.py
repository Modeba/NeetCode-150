test1 = [7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8,1,2,1,3,2,5]

def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    
    diff_bit = 1
    while not(xor & diff_bit):
        diff_bit <<= 1
    
    a, b = 0, 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num
    
    return [a, b]

print(singleNumber(test1))