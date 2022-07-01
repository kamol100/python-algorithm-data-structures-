#problem:260
#https://leetcode.com/problems/single-number-iii/
def single_number(nums):
    nums.sort()
    res = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 2
        else:
            res.append(nums[i])
            i += 1

    return res


print(single_number([1,2,1,3,2,5]))
print(single_number([-1,0]))
print(single_number([1,2,5,3,3,5]))
print(single_number([0,0,1,2]))
