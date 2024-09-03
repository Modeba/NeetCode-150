temps = [73,74,75,71,69,72,76,73]

def dailyTemperaturesSlow(temps):
    res = []
    for i in range(len(temps)):
        for e in range(i + 1, len(temps)):
            if temps[e] > temps[i]:
                res.append(e - i)
                break
        else:
            res.append(0)
    return res

def dailyTemperatures(temperatures):
    res, stack = [0 for _ in range(len(temperatures))], []
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    return res

print(dailyTemperaturesSlow(temps))                        
print(dailyTemperatures(temps))