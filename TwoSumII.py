def two_sum_2(num, target):
    i = 0
    k = len(num)-1
    while i < k:
        print(num[i],num[k])
        if num[i] + num[k] == target:
            return [i+1, k+1]
        if num[i] + num[k] > target:
            k -= 1
        else:
            i += 1



print(two_sum_2([2,7,11,15], 9))
print(two_sum_2([2,3,4], 6))
print(two_sum_2([-1,0], -1))
