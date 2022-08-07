def smallest_positive_int(A):
    A.sort()
    print(A)
    sm = 0
    maxs = max(A)
    if maxs < 1:
        return 1
    for i in range(1,maxs):
        if maxs - i in A:
            continue
        else:
            sm = maxs -i
    if sm == 0:
        sm = maxs + 1
    return sm

def smallest_positive_integer(A): #effecient
    max_num = max(A)
    if max_num < 1:
        return 1
    A = set(A)
    B = set(range(1, max_num + 1))
    D = B - A
    if len(D) == 0:
        return max_num + 1
    else:
        return min(D)



print(smallest_positive_integer([1,3,6,4,1,2]))
print(smallest_positive_int([1,3,6,4,1]))
