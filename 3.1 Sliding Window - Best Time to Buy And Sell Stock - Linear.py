test1 = [7,1,5,3,6,4]
test2 = [1,2]

def max_profix(prices):
    res = 0
        
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res
    

print(max_profix(test1))
