test1 = [[4,9,5], [9,4,9,8,4]]

def intersection(nums1, nums2):
    my_set = set(nums1)
    res = []
    for num in nums2:
        if num in my_set:
            res.append(num)
            my_set.remove(num)
    return res

print(intersection(test1[0], test1[1]))