test1 = [3,6,7,11]
test2 = [30,11,23,4,20]
test3 = [30,11,23,4,20]

def minEatingSpeed(piles, h):
    def totalTime(piles, h, k):
        totalTime = 0
        for pile in piles:
            if pile % k == 0:
                hoursPerPile = pile / k
            else:
                hoursPerPile = pile // k + 1
            totalTime += hoursPerPile
        if totalTime < h:
            return k
    
    for k in range(1, max(piles)):
        time = totalTime(piles, h, k)
        if time:
            return time

print(minEatingSpeed(test1, 5))