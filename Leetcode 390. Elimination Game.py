def lastRemaining(n):
    numbers = [i for i in range(n + 1)]

    left_to_right = True
    while len(numbers) > 1:
        if left_to_right == True:
            left_to_right = False
            i = 0
            while len(numbers) > 1 and i < len(numbers):
                print(numbers)
                numbers.remove[i]
                i += 2
            

print(lastRemaining(10))