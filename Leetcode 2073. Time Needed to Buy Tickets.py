def timeRequiredToBuy(tickets, k):
    res = 0
    while tickets[k] > 0:
        for i in range(len(tickets)):
            if tickets[i] > 0:
                tickets[i] -= 1
                res += 1
                if tickets[k] == 0:
                    break
    return res

def timeRequiredToBuy2(tickets, k):
    res = 0
    for i in range(len(tickets)):
        print(tickets[i], res)
        if i <= k:
            res += min(tickets[i], tickets[k])
        else:
            res += min(tickets[i], tickets[k] - 1)
    
    return res

#print(timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))
print(timeRequiredToBuy2([84,49,5,24,70,77,87,8], 3))