
def extraLongFactorials(num):
    ans = 1
    while num != 1:
        ans *= num
        num -= 1


    print(ans)

extraLongFactorials(100)