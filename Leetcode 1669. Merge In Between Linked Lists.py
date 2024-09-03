def mergeInBetween(list1, a, b, list2):
    dummy = curr = ListNode()
    curr.next = list1

    for i in range(a):
        curr = curr.next
    
    tmp = curr.next
    curr.next = list2
    
    for i in range(b - a):
        tmp = tmp.next
        
    while list2.next:
        list2 = list2.next
    list2.next = tmp.next

    return dummy.next