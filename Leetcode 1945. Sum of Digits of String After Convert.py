s = "zbax"
k = 2

def getLucky(s, k):
    nums = []
    for letter in s:
        nums.append(ord(letter) - ord('a') + 1)
    
    temp = []
    for _ in range(k):
        for number in nums:
            for digit in str(number):
                temp.append(int(digit))
            
        temp = str(sum(temp))
        nums = []
        for digit in temp:
            nums.append(int(digit))
        temp = []

    temp = ''
    for digit in nums:
        temp += str(digit)

    return temp

print(getLucky(s, k))