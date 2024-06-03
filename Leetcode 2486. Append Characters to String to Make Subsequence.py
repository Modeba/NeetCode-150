test1 = ["coaching", "coding"]

def appendCharacters(s, t):
    t_index = 0
    t_length = len(t)

    for i in range(len(s)):
        if t_index == t_length:
            return 0
        if t[t_index] == s[i]:
            t_index += 1
    
    return t_length - t_index

print(appendCharacters(test1[0], test1[1]))