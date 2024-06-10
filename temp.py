test1 = [0,1,0,2,1,0,1,3,2,1,2,1]
test2 = [4,2,3]


def trap(height):
    def findPuddles(height, start, puddle, total, tallest, end):
        for i in range(end):
            if height[i] >= height[tallest]:
                tallest = i
            if height[i] < height[start]:
                puddle += height[start] - height[i]
            else:
                total += puddle
                puddle,start = 0, i
        
        return [total, tallest]
    
    myList = findPuddles(height, 0, 0, 0, 0, len(height))
    return findPuddles(height[::-1], 0, 0, myList[0], myList[1], myList[1] + 2)[0]

print(trap(test2))