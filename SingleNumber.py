#problem:136
#https://leetcode.com/problems/single-number/
def single_number(nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res


print(single_number([2,2,5]))