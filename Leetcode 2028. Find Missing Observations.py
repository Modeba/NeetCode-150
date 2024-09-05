rolls = [1,5,6]
mean = 3
n = 5    

def missingRolls(rolls, mean, n):
    fill = (len(rolls) + n) * mean - sum(rolls)
    if fill > n * 6 or fill < n: return []

    average, incremented = fill // n, fill % n
    part1 = [average + 1 for _ in range(incremented)]
    part2 = [average for _ in range(n - incremented)]
    return part1 + part2
        
print(missingRolls(rolls, mean, n))