def climbing_stairs(n):
    one = 1
    two = 1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one


print(climbing_stairs(10))
print(climbing_stairs(5))
