test1 = [1,1,1,3,3,4,3,2,4,2]
test2 = [1,2,3,4,5,6]

def containsDuplicate(nums):
    uniques = []
    for num in nums:
        if num not in uniques:
            uniques.append(num)
        else:
            return True

    return False

print(containsDuplicate(test1))
