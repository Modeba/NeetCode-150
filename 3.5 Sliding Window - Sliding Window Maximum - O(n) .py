import collections

test1 = [1, 3, -1, -3, 5, 3, 6, 7]
test2 = [1, -1]

def maxSlidingWindow(nums, k):
    if k == 1:
        return nums
    q = collections.deque()
    output = []
    l = r = 0
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        if l > q[0]:
            q.popleft()
        if (r + 1) >= k:
            l += 1
            output.append(nums[q[0]])
        r += 1
    
    return output

print(maxSlidingWindow(test1, 2))
    