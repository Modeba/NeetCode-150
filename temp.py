matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def bin_search(matrix, target):
    l, r = 0, len(matrix) - 1
    while l <= r:
        m = l + (r - l) // 2
        if matrix[m][0] > target:
            r = m - 1
        elif matrix[m][0] < target:
            