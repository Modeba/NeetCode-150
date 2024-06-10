test1 = [1,1,4,2,1,3]

def heightChecker(heights):
    res = 0
    expected = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    return res

print(heightChecker(test1))