test1 = [1,2,0]
test2 = [3,4,-1,1]
test3 = [7,8,9,11,12]
test4 = [1,2]
test5 = [0,0,0,7,8,9,11,12]
test6 = [0]
test7 = [1]
test8 = [2]
test9 = [1, 1]
test10 = [1, 1, 1]
test11 = [1, 1, 2]
test12 = [1, 100]

def firstMissingPositive(nums):
    nums.append(0)

    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] < 0 or nums[i] > len(nums) - 1 or nums[i] == nums[nums[i]]:
                break
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    for i in range(1, len(nums)):
        if nums[i] != i and i > 0:
            return i
    else:
        return len(nums)
    
def firstMissingPositive2(nums):
        nums = set(nums)
        i = 1
        while(i):
            if i not in nums:
                return i
            i += 1

print(firstMissingPositive(test1), 3, 'test1')
print(firstMissingPositive(test2), 2, 'test2')
print(firstMissingPositive(test3), 1, 'test3')
print(firstMissingPositive(test4), 3, 'test4')
print(firstMissingPositive(test5), 1, 'test5')
print(firstMissingPositive(test6), 1, 'test6')
print(firstMissingPositive(test7), 2, 'test7')
print(firstMissingPositive(test8), 1, 'test8')
print(firstMissingPositive(test9), 2, 'test9')
print(firstMissingPositive(test10), 2, 'test10')
print(firstMissingPositive(test11), 3, 'test11')
print(firstMissingPositive(test12), 2, 'test12')