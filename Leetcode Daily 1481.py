test1 = [5,5,4]
test2 = [4,3,1,1,3,3,2,1,1,1,1,1]

def findLeastNumOfUniqueInts(arr, k):
        Map = {}

        for ar in arr:
            if ar not in Map:
                Map[ar] = 1
            else:
                Map[ar] += 1
        
        unique = []
        for char in Map:
            unique.append(Map[char])

        unique.sort(reverse = True)
        return(unique)

print(findLeastNumOfUniqueInts(test2, 1))