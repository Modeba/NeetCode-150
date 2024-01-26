test1 = [100,4,200,1,3,2]
test2 = [0,3,7,2,5,8,4,6,0,1]

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in num_set:
        if (n - 1) not in num_set:
            length = 1

            while (n + length) in num_set:
                length += 1

            longest = max(length, longest)

    return longest

print(longest_consecutive(test2))
