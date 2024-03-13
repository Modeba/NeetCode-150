def removeZeroSumSublists(head):
    cur = dummy = ListNode(0, head)
    Map = {}
    prefix_sum = 0

    while cur:
        prefix_sum += cur.val
        if prefix_sum in Map:
            node = Map[prefix_sum]
            temp = node.next
            temp_sum = prefix_sum

            while temp != cur:
                temp_sum += temp.val
                del Map[temp_sum]
                temp = temp.next

            node.next = cur.next

        else:
            Map[prefix_sum] = cur
        
        cur = cur.next

    return dummy.next