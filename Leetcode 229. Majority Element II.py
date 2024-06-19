test1 = [3,2,3]
test2 = [1,2]
test3 = [2,1,1,3,1,4,5,6]

def majorityElement(nums):
    if not nums:
        return []
    
    num1, num2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1, count1 = num, 1
        elif count2 == 0:
            num2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    res = []
    count1, count2 = 0, 0
    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1

    if count1 > len(nums) // 3:
        res.append(num1)
    if count2 > len(nums) // 3:
        res.append(num2)

    return res

print(majorityElement(test3))