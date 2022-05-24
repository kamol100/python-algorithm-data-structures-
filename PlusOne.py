def plus_one(digits):
    sm = ""
    res = []
    for d in digits:
        sm += str(d)
    sm = int(sm) + 1
    for i in str(sm):
        res.append(int(i))
    return res
    #print(list(sm))


print(plus_one([1,2,3]))
print(plus_one([9]))
