test1 = '010'
test2 = '0101'

def maximumOddBinaryNumber(s):
    lst = []
    for digit in s:
        lst.append(int(digit))

    lst.sort(reverse = True)
    return lst


print(maximumOddBinaryNumber(test2))