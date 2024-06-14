test1 = [3,2,1,2,1,7]
test2 = [2,2,2,1]

def minIncrementForUnique(nums):
    #counter = [0] * (10 ** 5 + 1)
    counter = [0] * (max(nums) + 1)
    moves, stored = 0, 0

    for num in nums:
        counter[num] += 1
    
    print(counter)
    for count in counter:
        print(moves, stored)
        if stored > 0:
            moves += stored
        if count > 1:
            stored += (count - 1)
        elif count == 0 and stored > 0:
            stored -= 1
    
    while stored:
        moves += stored
        stored -= 1
    return moves

print(minIncrementForUnique(test2))