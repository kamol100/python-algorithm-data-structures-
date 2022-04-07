def gameOfTwoStack(maxSum,a,b):
    total = 0
    num = 0
    i = 0
    j = 0
    while i < len(a) and total + a[i] <= maxSum:
        total += a[i]
        num += 1
        i += 1

    while j < len(b) and i >= 0:
        total += b[j]
        j += 1
        while i > 0 and total > maxSum:
            i -= 1
            total -= a[i]
        if total <= maxSum and num < i+j:
            num = i+j

    print(total, num)
    return num





maxSum = 10
a = [4,2,4,6,1]
b = [2,1,8,5]
print(gameOfTwoStack(maxSum, a, b))#4
maxSum = 10
a = [1,2,3,4,5]
b = [6,7,8,9]
print(gameOfTwoStack(maxSum, a, b))#4
maxSum = 62
a = [7,15,12,0,5,18,17,2,10,15,4,2,9,15,13,12,16]
b = [12,16,6,8,16,15,18,3,11,0,17,7,6,11,14,13,15,6,18,6,16,12,16,11,16,11]
print(gameOfTwoStack(maxSum,a,b))#6
maxSum = 5
a = [4,11,16,0,18,17,9,13,7,12,16,19,2,15,5,13,1,10,0,8,0,6,16,12,15,7,1,6,19,16,2]
b = [15,8,11,16,6,0,5,11,7,9,8,6,3,3,4,8,17,14,9,5,15,15,1,19,10,0,12,8,11,9,11,18,17,14]
#print(gameOfTwoStack(maxSum,a,b))#1
maxSum = 55
a = [11,6,1,13,14,7,8,10,3,17,7,18,6,4,5,13,17,4,16,9,17,16,12,6,7]
b = [10,15,13,17,10,7,0,16,8,13,11,8,14,13]
#print(gameOfTwoStack(maxSum,a,b))
