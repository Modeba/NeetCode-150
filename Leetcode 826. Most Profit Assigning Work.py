difficulty = [2,4,6,8,10]
profit     = [10,20,30,40,50]
worker     = [4,5,6,7]

difficulty = [35,47,52,68,86]
profit     = [67,17,1,81,3]
worker     = [92,10,85,84,82]

def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    res, i, best = 0, 0, 0
    print(jobs)

    for ability in sorted(worker):
        print(i, best, res)
        while i < len(jobs) and ability >= jobs[i][0]:
            best = max(best, jobs[i][1])
            i += 1
        res += best
    
    return res


print(maxProfitAssignment(difficulty, profit, worker))