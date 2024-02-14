test1 = [2,2,1,1,1,2,2]

def majority(nums):
    Map = {}
    for num in nums:
        print(Map)
        if num in Map:
            Map[num] += 1
            if Map[num] > len(nums) // 2:
                return num
        else:
            Map[num] = 1

print(majority(test1))