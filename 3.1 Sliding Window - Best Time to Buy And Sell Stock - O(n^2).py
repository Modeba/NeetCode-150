test1 = [7,1,5,3,6,4]
test2 = [1,2]

def max_profix(prices):
    max_difference = 0
    for i in range(len(prices) - 1):
        for e in range(i + 1, len(prices)):
            max_difference = max(max_difference, prices[e] - prices[i])

    return max_difference

print(max_profix(test2))
