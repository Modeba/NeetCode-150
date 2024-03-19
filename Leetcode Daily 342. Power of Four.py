def isPowerOfFour(n):
    i = 0
    sqr = 4 ** i

    while sqr <= n:
        if 4 ** i == n:
            return True
        
        i += 1
        sqr = 4 ** i

    return False