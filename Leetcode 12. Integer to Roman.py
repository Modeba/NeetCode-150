def intToRoman(num):
    Map = {
        1    : 'I',
        5    : 'V',
        10   : 'X',
        50   : 'L',
        100  : 'C',
        500  : 'D',
        1000 : 'M' 
        }

    res = ''
    for m in Map:
        if m >= num:
            res += Map[m]
            num -= m
            break
    
    return res

print(intToRoman(11))