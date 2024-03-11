test1 = 38

def addDigits(num):
    while len(str(num)) > 1:
        tmp = 0
        for n in str(num):
            tmp += int(n)
        num = tmp
    
    return num

print(addDigits(test1))