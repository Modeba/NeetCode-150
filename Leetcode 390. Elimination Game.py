def lastRemaining(n):
    numbers = [i for i in range(1, n + 1)]

    left_to_right = True
    while len(numbers) > 1:
        if left_to_right:
            left_to_right = False
            for i in range(0, len(numbers), 2):
                numbers[i] = False
        else:
            left_to_right = True
            for i in range(-1, -len(numbers) - 1, -2):
                numbers[i] = False

        temp = []
        for num in numbers:
            if num:
                temp.append(num)
        numbers = temp
        
    return numbers[0]

x_val = []
y_val = []

for i in range(1, 96):
    print(i, i - lastRemaining(i), lastRemaining(i))