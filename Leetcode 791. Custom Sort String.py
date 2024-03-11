def customSortString(order, s):
    Map = {}
    for char in s:
        if char in Map:
            Map[char] += 1
        else:
            Map[char] = 1
    
    res = ''
    for o in order:
        if o in Map:
            while Map[o] > 0:
                res += o
                Map[o] -= 1
    
    for char in Map:
        for i in range(Map[char]):
            res += char
    
    return res 

print(customSortString("cba", "abcd"))