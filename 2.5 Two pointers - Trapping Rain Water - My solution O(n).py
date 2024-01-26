test1 = [0,1,0,2,1,0,1,3,2,1,2,1]
test2 = [4,2,0,3,2,5]
test3 = [4, 4, 3, 4, 10, 2, 10, 11, 8, 0, 0, 2]
test4 = [0,0]

def trap(height):
    total_water = 0
    puddle = 0
    start = height[0]
    last_edge = 0
    
    for i in range(1, len(height)):
        if height[i] < start:
            puddle += start - height[i]
        else:
            total_water += puddle
            puddle = 0
            start = height[i]
            last_edge = i

    puddle = 0
    start = height[len(height) - 1]
    
    for i in range(len(height) - 1, last_edge - 1, -1):
        if height[i] < start:
            puddle += start - height[i]
        else:
            total_water += puddle
            puddle = 0
            start = height[i]

    return total_water

print(trap(test1))
