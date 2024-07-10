test1 = ["d1/","d2/","../","d21/","./"]

def minOperations(logs):
    res = 0

    for log in logs:
        if log == './':
            continue
        elif log == '../':
            res = max(0, res - 1)
        else:
            res += 1
    
    return res

print(minOperations(test1))