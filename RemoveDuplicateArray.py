def remove_duplicates(nums):
    l = 1
    for r in range(1,len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l






print(remove_duplicates([1,1,1,2]))
print('=====================')
print(remove_duplicates([0,0,1,1,1,2,2,3,3,3,4]))