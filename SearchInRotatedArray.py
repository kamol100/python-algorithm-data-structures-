# leetcode 33
#https://leetcode.com/problems/search-in-rotated-sorted-array/
def search(nums, target):
    if nums is None: return -1
    left = 0
    right = len(nums) -1
    while(left < right):
        mid = left + (right - left) //2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    start = left
    left = 0
    right = len(nums) -1

    if target >= nums[start] and target <= nums[right]:
        left = start
    else:
        right = start

    while left <= right:
        mid = left + (right -left) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1



print(search([4,5,6,7,0,1,2], 1))

