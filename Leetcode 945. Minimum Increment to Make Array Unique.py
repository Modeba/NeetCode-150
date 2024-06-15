test1 = [3,2,1,2,1,7]
test2 = [2,2,2,1]
test3 = [1,2,2,2,2,3,3]

def minIncrementForUnique(nums):
    counter = [0] * (max(nums) + 1)
    res, stored = 0, 0

    for num in nums:
        counter[num] += 1

    for count in counter:
        res += stored
        if count > 1:
            stored += (count - 1)
        elif count == 0 and stored > 0:
            stored -= 1

    return res + stored * (stored + 1) // 2

print(minIncrementForUnique(test3))