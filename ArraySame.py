def same_array1(arr1, arr2): #unoptimize big 0n2 time complexity
    if len(arr1) != len(arr2): return False

    for n in arr1:
        item = n **2
        if item not in arr2:
            return False
    return True

def same_array2(arr1, arr2):# optimize big 0n time complexity
    if len(arr1) != len(arr2): return False
    map1, map2 = {},{}
    for i in arr1:
        map1[i] = 1 + map1.get(i, 0)
    for i in arr2:
        map2[i] = 1 + map2.get(i, 0)
    for key in map1:
        if key ** 2 not in map2:
            return False
        if map2[key ** 2] != map1[key]:
            return False

    return True





print(same_array1([1,2,3,4], [4,9,16,1]))
print(same_array2([5,4,4,3,4], [16,16,16,9,25]))
