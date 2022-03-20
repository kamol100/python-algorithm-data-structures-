def arrayLeftRotation(d, arr):
    rotate = d%len(arr)
    for i in range(rotate):
        item = arr.pop(0)
        arr.append(item)
    print(arr)



arrayLeftRotation(4, [1,2,3,4,5])