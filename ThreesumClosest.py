def three_sum_closest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    print(nums,res)
    for i in range(len(nums)):
        l,r = i + 1, len(nums)-1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if abs(threeSum - target) < abs(res -target):
                res = threeSum
            if threeSum > target:
                r -= 1
            else:
                l += 1
    return res


print(three_sum_closest([-1,2,1,-4],1))