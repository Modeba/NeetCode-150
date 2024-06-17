from math import sqrt, ceil, floor

def judgeSquareSum(c):
    if c <= 2:
        return True
    
    for i in range(c):
        for e in range(i, c):
            print(i, e)
            curr = i ** 2 + e ** 2
            if curr == c:
                return True
    return False

def judgeSquareSumFast(c):
    if c <= 2:
        return True
    
    root = ceil(sqrt(c))
    for i in range(root + 1):
        second = c - i ** 2
        if second < 0:
            break
        second = sqrt(second)
        if second == int(second):
            return i, i ** 2, second, second ** 2
    return False

def judgeSquareSumSet(c):
    squares = set(i ** 2 for i in range(ceil(sqrt(c)) + 1))
    for square in squares:
        if c - square in squares:
            return True
    return False

def judgeSquareSumTwoPointers(c):
    squares = [i ** 2 for i in range(int(sqrt(c)) + 1)]
    print(squares)
    l, r = 0, len(squares) - 1

    while l <= r:
        s = squares[l] + squares[r]
        if s < c:
            l += 1
        elif s > c:
            r -= 1
        else:
            return True

    return False 


def judgeSquareSumTwoPointersNoArray(c):
    l, r = 0, int(sqrt(c)) + 1
    while l <= r:
        s = l ** 2 + r ** 2
        if s < c:
            l += 1
        elif s > c:
            r -= 1
        else:
            return True
    return False

print(judgeSquareSumTwoPointersNoArray(4))