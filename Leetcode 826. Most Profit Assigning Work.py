difficulty = [2,4,6,8,10]

l, r = 0, len(difficulty)

while l <= r:
    print(l, r)
    m = l + (r - l) // 2
    if difficulty[m] > 4:
        l = m
    elif difficulty[m] < 4:
        r = m
    else:
        print('=', difficulty[m])
    l += 1
    r -= 1
    
print(difficulty[m - 1])
