class Solution:
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(0)
current = head
for i in range(1, 999999):
    current.next = ListNode(i)
    current = current.next

solution = Solution()
middle = solution.middleNode(head)
print("Middle node:", middle.val)