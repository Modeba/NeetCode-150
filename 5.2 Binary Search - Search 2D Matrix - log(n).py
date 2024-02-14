test1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

def searchMatrix(matrix, target):

    def search(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        return False
    
    if len(matrix) == 1:
        return target in matrix[0]

    for i in range(len(matrix)):
        if matrix[i][0] > target:
            return search(matrix[i - 1], target)
    else:
        return search([len(matrix) - 1], target)
        
print(searchMatrix(test1, 10))
