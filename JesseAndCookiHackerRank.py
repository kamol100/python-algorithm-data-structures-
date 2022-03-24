from heapq import heapify,heappop,heappush

def jesseAndCookies(K,A):
    heapify(A)
    itr = 0
    while True:
        if not A:
            return -1
        min1 = heappop(A)
        if min1 >= K:
            return itr

        if not A:
            return -1
        min2 = heappop(A)
        if min1 < K > min2:
            sweet = min1 + (2 * min2)
            heappush(A , sweet)
        itr += 1





A = [2,7,3,6,4,6]
print(jesseAndCookies(9,A))

B = [1,2,3,9,10,12]
print(jesseAndCookies(7, B))
C = [1,1,1]
print(jesseAndCookies(10, C))