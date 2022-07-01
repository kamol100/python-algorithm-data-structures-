#problem:137
#https://leetcode.com/problems/single-number-ii/
def single_number(nums):
    nums.sort()
    res = 0
    for index,n in enumerate(nums):
        if index+1 < len(nums) and n == nums[index+1]:
            nums.pop(index)
        res = n ^ res
    return res


print(single_number([2,2,3,2]))
print(single_number([0,1,0,1,0,1,99]))
