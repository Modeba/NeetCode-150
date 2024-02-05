test1 = [1, 3, -1, -3, 5, 3, 6, 7]
test2 = [1, -1]

def maxSlidingWindow(nums, k):
    if k == 1:
        return nums
    
    result = [max(nums[:k])]
    for i in range(1, len(nums) - k + 1):
        result.append(max(nums[i : i + k]))
    
    return result

print(maxSlidingWindow(test1, 2))
    