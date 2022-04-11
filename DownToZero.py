from collections import deque
from math import sqrt
def down_to_zero(n):
    memo = set()
    count = 0
    q = deque([[n,count]])

    while q:
        n,count = q.popleft()
        if n <= 1:
            if n == 1:
                count +=1
            break
        if n-1 not in memo:
            memo.add(n-1)
            q.append([n-1, count+1])
        for i in range(int(sqrt(n)), 1, -1):
            if n%i == 0:
                factor = max(n//i, i)
                if factor not in memo:
                    memo.add(factor)
                    q.append([factor, count+1])

    return count



print(down_to_zero(3))
print("==============")
print(down_to_zero(966514))#8
print("=============")
print(down_to_zero(812849))#10
