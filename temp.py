position = [10,8,0,5,3]
speed = [2,4,1,1,3]

pairs = zip(position, speed)

res = [pair for pair in pairs]
print(res)
res.sort()
print(res)