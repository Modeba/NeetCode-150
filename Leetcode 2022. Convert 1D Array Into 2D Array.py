original = [1,2,3,4]
m = 2
n = 2

def construct2DArraySimple(original, n, m):
    if len(original) != n * m: return []
    
    res, row = [], []
    for element in original:
        row.append(element)
        if len(row) == n:
            res.append(row)
            row = []

    return res

def construct2DArrayFast(original, n, m):
    if len(original) != n * m: return []

    res = []
    for i in range(0, len(original), n):
        res.append(original[i:i + n])
    
    return res

print(construct2DArraySimple(original, n, m))
print(construct2DArrayFast(original, n, m))