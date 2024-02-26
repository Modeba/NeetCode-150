# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''

        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        res = str(int(str1) + int(str2))

        dummy = curr = ListNode()
        for i in range(len(res)):
            curr.val = int(res[i])
            if i != len(res) - 1:
                curr.next = ListNode()
            curr = curr.next
        
        return dummy