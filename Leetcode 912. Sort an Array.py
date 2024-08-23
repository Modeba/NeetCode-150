nums = [-2,-3,-9,5,1,1,2,0,0]

def sortArray(nums):
    counterPos = [0] * (5 * 10 ** 4 + 1)
    counterNeg = [0] * (5 * 10 ** 4 + 1)

    for num in nums:
        if num >= 0:
            counterPos[num] += 1
        else:
            counterNeg[abs(num)] += 1

    res = []
    for i in range(len(counterNeg)):
        for _ in range(counterNeg[i]):
            res.append(-i)
    res = res[::-1]

    for i in range(len(counterPos)):
        for _ in range(counterPos[i]):
            res.append(i) 

    return res

print(sortArray(nums))