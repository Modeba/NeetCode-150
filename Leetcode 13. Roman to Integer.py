def romanToInt(s):
    Map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }

    if len(s) == 1:
        return Map[s]

    index = 0
    res = Map[s[0]]

    for i in range(1, len(s)):
        res += Map[s[i]]
        if Map[s[i - 1]] < Map[s[i]]:
            res -= 2 * Map[s[i - 1]]
    
    return res

print(romanToInt("XXX"))