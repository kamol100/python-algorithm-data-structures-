def two_sum(nums, target):
    map = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in map:
            return [map[diff],i]
        else:
            map[nums[i]] = i



nums = [2,7,11,15]
print(two_sum(nums, 26))
print("===============")
nums = [3,2,3]
print(two_sum(nums, 6))
print("===============")
nums = [3,2,4]
print(two_sum(nums, 6))
print("===============")
nums = [3,2,3,5,8,12,20,3]
print(two_sum(nums, 22))
print("===============")
nums = [3,2,3,5,8,12,20,3]
print(two_sum(nums, 28))
