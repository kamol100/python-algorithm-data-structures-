def remove_elements(nums, val):
    k = 0
    for i in range(len(nums)-1):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(nums)
    return k






print(remove_elements([3,2,2,3],3))