import math

def search_insert_position(arr,target):
    left = 0
    right = len(arr)-1
    mid = math.floor((right+left)/2)
    if target > arr[right]:
        return right + 1
    if target < arr[left]:
        return 0
    while target != arr[mid]:
        if target < arr[mid]:
            right = mid -1
        else:
            left = mid + 1

        mid = math.floor((right+left)/2)
        if arr[mid] < target and arr[mid + 1] > target:
            return mid + 1
    return mid



arr = [1,3,4,5,20]
print(search_insert_position(arr, 6))