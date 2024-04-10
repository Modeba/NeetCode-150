from collections import deque

def deckRevealedIncreasing(deck):
    deck.sort()
    res = [0] * len(deck)
    q = deque(range(len(deck)))

    print(deck)

    for n in deck:
        i = q.popleft()
        res[i] = n
        if q:
            q.append(q.popleft())
    
    return res

print(deckRevealedIncreasing([17,13,11,2,3,5,7]))