from collections import deque

test1 = [1, 3, -1, -3, 5, 3, 6, 7]
test2 = [1, -1]
test3 = [9,9,9,9,9,9,9,9,9,9]

def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i + k]))
    
    return res

def maxSlidingWindowFast(nums, k):
    res = []
    l = 0
    q = deque() # Indices

    for r in range(len(nums)):
        while q and nums[r] > nums[q[-1]]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        
        if r + 1 >= k:
            res.append(nums[q[0]])
            l += 1
    
    return res

print(maxSlidingWindow(test1, 3))
print(maxSlidingWindowFast(test1, 3))