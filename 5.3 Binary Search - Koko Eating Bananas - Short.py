import math

test1 = [3,6,7,11]
test2 = [30,11,23,4,20]

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = l + (r - l) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    
    return res

print(minEatingSpeed(test2, 6))