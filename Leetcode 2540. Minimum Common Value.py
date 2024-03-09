test1 = [[1,2,3,6], [2,3,4,5]]

def getCommon(nums1, nums2):
    first = 0
    second = 0

    while first < len(nums1) and second < len(nums2):
        if nums1[first] < nums2[second]:
            first += 1
        elif nums1[first] > nums2[second]:
            second += 1
        else:
            return nums1[first]
        
    return -1

print(getCommon(test1[0], test1[1]))