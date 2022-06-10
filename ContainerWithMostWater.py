def max_area(height):
    res = 0
    i = 0
    j = len(height)-1
    while i < j:
        water = (j -i) * min(height[j], height[i])
        res = max(res, water)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res


print(max_area([1,8,6,2,5,4,8,3,7]))