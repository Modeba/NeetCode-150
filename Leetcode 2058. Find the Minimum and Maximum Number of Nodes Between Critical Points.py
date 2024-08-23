test1 = [5,3,1,2,5,1,2]

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def createNodes(arr):
    


def nodesBetweenCriticalPoints(head):
    nums = []

    while head:
        nums.append(head.val)
        head = head.next
    
    if len(nums) <= 3:
        return [-1, -1]
    
    res = []
    for i in range(1, len(nums) - 1):
        if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            res.append(i)
    
    if len(res) < 2:
        return [-1, -1]
    
    smallest = res[1] - res[0]
    for i in range(1, len(res) - 1):
        smallest = min(smallest, res[i + 1] - res[i])
    
    return [smallest, res[-1] - res[0]]
