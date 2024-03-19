def isPowerOfFour(n):
    x = 0
    sqr = x ** 4
    while sqr <= n:
        if sqr == n:
            return x
        x += 1
        sqr = x ** 4
    
    return False

print(isPowerOfFour(0))