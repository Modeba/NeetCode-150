customers = [1,0,1,2,1,1,7,5]
grumpy    = [0,1,0,1,0,1,0,1]
minutes   = 3

def maxSatisfied(customers, grumpy, minutes):
    satisfied = 0
    for i in range(len(customers)):
        if not grumpy[i]:
            satisfied += customers[i]
    
    gain = 0
    for i in range(minutes):
        if grumpy[i]:
            gain += customers[i]

    best = gain
    for i in range(len(customers) - minutes):
        if grumpy[i]:
            gain -= customers[i]
        if grumpy[i + minutes]:
            gain += customers[i + minutes]
        best = max(best, gain)

    return satisfied + best
     
print(maxSatisfied(customers, grumpy, minutes))