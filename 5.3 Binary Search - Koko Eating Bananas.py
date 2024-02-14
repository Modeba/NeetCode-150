test1 = [3,6,7,11]
test2 = [30,11,23,4,20]

def minEatingSpeed(piles, h):
    '''totalTime function goes over every value in Piles and sums up time taken by them.
    Can be simplified with math.ceiling function'''
    def totalTime(piles, k):
        totalTime = 0
        for pile in piles:
            if pile % k == 0:
                hoursPerPile = pile / k
            else:
                hoursPerPile = pile // k + 1
            totalTime += hoursPerPile
        print(totalTime)
        return totalTime
 
    '''Binary search between the lowest and the highest possible speeds'''
    l = 1
    r = speed = max(piles)
    while l <= r:
        m = l + (r - l) // 2
        if totalTime(piles, m) <= h:
            speed = min(speed, m)
            r = m - 1
        else:
            l = m + 1
    return speed

print(minEatingSpeed(test2, 5))