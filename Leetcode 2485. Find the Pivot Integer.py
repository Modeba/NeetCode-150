def pivotInteger(n):

    total = 0
    for i in range(1, n + 1):
        total += i
    
    cumulative_sum = 0
    for i in range(1, n + 1):
        if (total - i) / 2 == cumulative_sum:
            return i
        cumulative_sum += i
        
    return -1

for i in range(1, 11):
    print(pivotInteger(i))