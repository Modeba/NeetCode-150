def removeZeroSumSublists(head):
    cur = dummy = ListNode(0, head)
    Map = {}
    prefix_sum = 0

    while cur:
        prefix_sum += cur.val
        if prefix_sum in Map:
            
        else:
            Map[prefix_sum] = cur