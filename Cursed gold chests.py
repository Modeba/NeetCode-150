gold1 = [2, 1, 0, 3, 5]  # 10
gold2 = [1, 0, 2, 0, 3]  # 3
gold3 = [0, 2, 0, 3, 0, 4]  # 0
gold4 = [2, 0, 3, 0, 4, 0]  # 0
gold5 = [0, 0, 2, 4, 0]  # 2
gold6 = [0, 0, 4, 2, 0]  # 4
gold7 = [0, 0, 2, 0, 4, 0]  # 0
gold8 = [0, 0, 2, 4, 0, 0]  # 6
gold9 = [0, 2, 4, 0, 0]  # 4
gold10 = [100, 0, 4]  # 100
gold11 = [100, 0, 10, 0, 10000] # 10000

def get_gold(chests):
    while 0 in chests:
        index = chests.index(0)
        if index == 0:
            chests.pop(index)
            chests.pop(index)
        elif index == len(chests) - 1:
            chests.pop(index)
            chests.pop(index -1)
        else:
            if chests[index - 1] < chests[index + 1]:
                chests.pop(index)
                chests.pop(index - 1)
            else:
                chests.pop(index)
                chests.pop(index)
    
    return sum(chests)

print(get_gold(gold9))