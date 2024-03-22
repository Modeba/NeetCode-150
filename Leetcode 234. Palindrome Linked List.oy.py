def isPalindrome(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst == lst[::-1]

