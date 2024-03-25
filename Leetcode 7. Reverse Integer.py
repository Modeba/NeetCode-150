def reverse(x):
    if x < 0:
        x = -1 * int(str(abs(x))[::-1])
    else:
        x = int(str(abs(x))[::-1])
    
    if -2147483648 <= x < 2147483647:
        return x
    else:
        return 0