test1 = [1,1,2,1,3]

def majorityElement(nums):
    maj, count = None, 0

    for num in nums:
        if count == 0:
            maj = num
        count += 1 if maj == num else -1
    
    return maj

print(majorityElement(test1))