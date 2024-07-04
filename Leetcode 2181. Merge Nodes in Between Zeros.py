def mergeNodes(head):
    curr, zero_node = head, ListNode(None, None)

    while curr:
        if curr.val == 0:
            if not curr.next:
                zero_node.next = None
                break
            zero_node.next = curr
            zero_node = zero_node.next
        zero_node.val += curr.val
        curr = curr.next

    return head         