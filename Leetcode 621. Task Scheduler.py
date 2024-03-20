def leastInterval(tasks):
    Map = {}
    for t in tasks:
        if t not in Map:
            Map[t] = 1
        else:
            Map[t] += 1

    res = []
    while Map:
        print(Map)

        new_Map = {}
        for m in Map:
            if Map[m] > 0:
                new_Map[m] = Map[m]
        Map = new_Map

        for m in Map:
            if Map[m] > 0:
                res.append(m)
                Map[m] -= 1

    return res

print(leastInterval(["A","A","A","B","B","B"]))