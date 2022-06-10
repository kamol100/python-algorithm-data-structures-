def target_indices(nums, target):
    nums.sort()
    l, r = 0, len(nums) -1
    res = []
    while l <= r:
        if nums[l] == target:
            res.append(l)
        l += 1

    return res

print(target_indices([1,2,5,2,3,2],2))
print(target_indices([1],1))
