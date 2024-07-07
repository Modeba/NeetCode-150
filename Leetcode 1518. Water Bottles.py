def numWaterBottles(numBottles, numExchange):
    res = 0
    while numBottles >= numExchange:
        exchanged = numBottles // numExchange
        rest = numBottles % numExchange

        res += numBottles - rest
        numBottles = exchanged + rest
    
    return res + numBottles

def numWaterBottlesFast(numBottles, numExchange):
    return numBottles + (numBottles-1)//(numExchange-1)

print(numWaterBottles(15, 4))
print(numWaterBottlesFast(15, 4))