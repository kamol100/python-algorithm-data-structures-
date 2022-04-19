def palindrome_number(x):
    if x < 0: return False

    div = 1
    while x >= 10 * div:
        div *= 10
    while x:
        right = x%10
        left = x//div
        if left != right: return False
        x = (x%div)//10
        div = div //100
    return True



print(palindrome_number(121))
print("=====================")
print(palindrome_number(10))
print("=====================")
print(palindrome_number(1221))
