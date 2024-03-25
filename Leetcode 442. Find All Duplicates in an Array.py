def findDuplicates(nums):
    duplicates = set()
    nums.append(0)

    for i in range(len(nums)):
        while nums[i] != i:
            print(nums)
            if nums[i] == nums[nums[i]]:
                if nums[i] not in duplicates:
                    duplicates.add(nums[i])
                break
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    
    return duplicates

test1 = [4,3,2,7,8,2,3,1,8]
test2 = [79,88,22,20,11,24,37,42,18,2,99,31,31,30,81,52,34,91,90,48,41,71,54,40,58,21,14,91,35,74,17,44,54,47,68,100,83,96,94,72,67,42,67,81,94,98,46,47,82,48,57,61,44,64,17,77,74,15,58,32,52,13,57,89,45,5,63,1,46,35,56,32,28,72,71,99,93,23,93,14,30,43,2,20,78,95,45,50,1,85,65,87,55,55,85,62,75,98,39,50]
print(findDuplicates(test1))