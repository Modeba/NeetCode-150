test1 = [1,2,3,6,2,3,4,7,8]

def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize:
        return False
    
    hashMap = {}
    for card in hand:
        if card not in hashMap:
            hashMap[card] = 1
        else:
            hashMap[card] += 1

    uniques = list(hashMap.keys())
    uniques.sort()
    
    res = []
    for card in uniques:
        group = []
        increment = 0
        while card + increment in hashMap and hashMap[card] > 0:
            group.append(card + increment)
            hashMap[card + increment] -= 1
            increment += 1
            print(group)
        res.append(group)
    
    return res

print(isNStraightHand(test1, 3))