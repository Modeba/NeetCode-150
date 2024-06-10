test1 = [1,1,4,2,1,3]

def heightChecker(heights):
    res = 0
    expected = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    return res

def heightCheckerFast(heights):
    counter = [0] * 101
    for h in heights:
        counter[h] += 1
    
    expected = []
    for i in range(len(counter)):
        for _ in range(counter[i]):
            expected.append(i)
    
    res = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    
    return res

print(heightChecker(test1))
print(heightCheckerFast(test1))