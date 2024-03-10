test1 = [[1,2,2,1], [2,2]]
test2 = [[4,9,5], [9,4,9,8,4]]


def intersection(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    res = []

    for s in s1:
        if s in s2:
            res.append(s)

    return res

print(intersection(test2[0], test2[1]))