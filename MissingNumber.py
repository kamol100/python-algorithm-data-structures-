#problem: 268
#https://leetcode.com/problems/missing-number/submissions/
def missing_number(nums):
    res = len(nums)

    for i in range(len(nums)):
        res += (i - nums[i])
        print(res)
    return res



print(missing_number([1,0]))
print(missing_number([3,1,0]))
