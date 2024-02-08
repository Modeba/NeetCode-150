temps = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temps):
    res = []
    for i in range(len(temps)):
        for e in range(i + 1, len(temps)):
            if temps[e] > temps[i]:
                res.append(e - i)
                break
        else:
            res.append(0)
    return res


print(dailyTemperatures(temps))
