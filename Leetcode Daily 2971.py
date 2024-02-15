test1 = [1,12,1,2,5,50,3]

def largestPerimeter(nums):
    while len(nums) >= 3:
        total = sum(nums)
        for i, num in enumerate(nums):
            print(total, num)
            if num >= (total - num):
                nums.pop(i)
                break
        else:
            return total
    return -1

print(largestPerimeter(test1))