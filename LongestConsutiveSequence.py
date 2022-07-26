def longest_consecutive_sequence(nums):
    numSet = set(nums)

    print(numSet)
    longest = 0
    for i in nums:
        if (i - 1) not in numSet:
            length = 0
            while (i + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest



print(longest_consecutive_sequence([100,101,102,4,200,103,1,3,2,5,104,105]))
print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))
print(longest_consecutive_sequence([1,2,0,1]))
