test1 = [2,7,11,15]
target1 = 9
test2 = [-1,0]
target2 = -1

def twoSum(my_list, target):
    first  = 0
    second = len(my_list) - 1

    while first < second:
        total = my_list[first] + my_list[second]
        if total > target:
            second -= 1
        elif total < target:
            first += 1
        else:
            return my_list[first], my_list[second]
    
print(twoSum(test2, target2))

'''Start from both ends and meet in the
middle to reduce time complexity to O(n)'''
