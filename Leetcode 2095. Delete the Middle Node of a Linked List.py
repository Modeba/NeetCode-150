# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0, head)
        length = -1

        while curr:
            length += 1
            curr = curr.next
        
        curr = dummy

        for i in range(1, (length // 2) + 1):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next