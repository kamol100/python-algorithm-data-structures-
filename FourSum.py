def four_sum(nums, target):
    result = []
    nums.sort()
    print(nums)
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        for j  in range(i+1,len(nums)):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l,r = j + 1, len(nums)-1
            while l < r:
                sums = a + nums[j] + nums[l] + nums[r]
                if sums > target:
                    r -= 1
                elif sums < target:
                    l += 1
                else:
                    result.append([a, nums[j], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
    return result






print(four_sum([1,0,-1,0,-2,2],0))
print(four_sum([2,2,2,2,2],8))
