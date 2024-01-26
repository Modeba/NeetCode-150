test1 = [2,7,11,15]
target1 = 9
test2 = [-1,0]
target2 = -1

def twoSum(my_list, target):
    for i in range(len(my_list)):
        for e in range(i,len(my_list)):
            if my_list[i] + my_list[e] == target:
                print(my_list[i], my_list[e])
                return i, e

print(twoSum(test3, target3))
