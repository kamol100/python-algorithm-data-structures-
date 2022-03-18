from array import *

arr = array('i', [1,2,3])
arr2 = array('i')

for item in range(len(arr)):
    arr2.append(arr.pop())

print(arr2)