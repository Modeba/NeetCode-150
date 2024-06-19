bloomDay = [1,10,3,10,2]
m = 3
k = 2

def minDays(bloomDay, m, k):
    def checkDay(bloomDay, m, k, days):
        bouquet, res = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] - days <= 0:
                bouquet += 1
                if bouquet == k:
                    res += 1
                    bouquet = 0
                    if res == m:
                        return True
            else:
                bouquet = 0
        
        return False
    
    if len(bloomDay) / k < m:
        return False

    enough = []
    l, r = min(bloomDay), max(bloomDay)
    while l <= r:
        mid = l + (r - l) // 2
        if checkDay(bloomDay, m, k, mid):
            enough.append(mid)
            r = mid - 1
        else:
            l = mid + 1
    
    return min(enough)

print(minDays(bloomDay, m, k))