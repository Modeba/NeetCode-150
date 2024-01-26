test1 = [1,1,1,3,3,4,3,2,4,2]
test2 = [1,2,3,4,5,6]
test3 = [1,2,3,4,5,6,6]

def containsDuplicate(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

print(containsDuplicate(test3))
