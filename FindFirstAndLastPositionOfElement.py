def search_range(nums, target):
    if len(nums) == 0:
        return [-1,-1]
    l, r = 0, len(nums) -1
    while l <= r:
        if nums[l] != target:
            l += 1
        if nums[r] != target:
            r -= 1
        if l < len(nums) and nums[l] == target and nums[r] == target:
            return [l,r]
    return [-1,-1]






print(search_range([5,7,7,8,8,8,10], 8))
print(search_range([1], 1))
