def max_sub_array(arr):
    maxSum = arr[0]
    currSum = 0
    for n in arr:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(maxSum, currSum)
    return maxSum


print(max_sub_array([2,-5,3]))
print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
