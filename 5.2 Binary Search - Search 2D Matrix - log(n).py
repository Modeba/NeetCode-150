test1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

def searchMatrix(matrix, target):
    row = None
    l, r = 0, len(matrix) - 1
    while l <= r:
        m = l + (r - l) // 2
        if target > matrix[m][-1]:
            l = m + 1
        elif target < matrix[m][0]:
            r = m - 1
        else:
            row = matrix[m]
            break
    if not row: return False

    l, r = 0, len(row) - 1
    while l <= r:
        m = l + (r - l) // 2
        if target > row[m]:
            l = m + 1
        elif target < row[m]:
            r = m - 1
        else:
            return True
    return False

print(searchMatrix(test1, 3))
