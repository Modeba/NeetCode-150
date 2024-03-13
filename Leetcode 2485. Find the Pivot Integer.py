import time

def pivotInteger(n):
    '''
    total = 0
    for i in range(1, n + 1):
        total += i
    '''
    
    if n % 2 == 1:
        total = (n + 1) * (n // 2) + (n // 2 + 1)
    else:
        total = (n + 1) * (n // 2)
    
    cumulative_sum = 0
    for i in range(1, n + 1):
        if (total - i) / 2 == cumulative_sum:
            return [n, i]
        cumulative_sum += i

start = time.time()

for i in range(1000, 10001):
    result = pivotInteger(i)
    if result:
        print(result)

print(time.time() - start)