class Solution:
    def deleteMiddle(self, head):
        if head.next == None:
            return None

        slow = ListNode(0, head)
        dummy = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(0)
current = head
for i in range(1, 9):
    current.next = ListNode(i)
    current = current.next

solution = Solution()
new_list = solution.deleteMiddle(head)

# Check result
result = []
curr = head
while curr:
    result.append(curr.val)
    curr = curr.next

print(result)