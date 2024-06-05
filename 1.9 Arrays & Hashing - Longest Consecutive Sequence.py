test1 = [100,4,200,1,3,2]
test2 = [0,3,7,2,5,8,4,6,0,1]

def longest_consecutive(nums):
    nums = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            length = 1

            while num + length in nums:
                length += 1
            longest = max(length, longest)

    return longest

print(longest_consecutive(test2))