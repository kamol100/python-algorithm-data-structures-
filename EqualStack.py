
def equalStack(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while True:
        min_sum = min(sum1, sum2, sum3)
        if sum1 == sum2 == sum3:
            print(min_sum)
            return
        if sum1 > min_sum:
            stack1 = h1.pop(0)
            sum1 = sum1 - stack1
        if sum2 > min_sum:
            stack2 = h2.pop(0)
            sum2 = sum2 - stack2
        if sum3 > min_sum:
            stack3 = h3.pop(0)
            sum3 = sum3 - stack3






h1 = [3,2,1,1,1]
h2 = [4,3,2]
h3 = [1,1,4,1]
equalStack(h1, h2, h3)

k1 = [1,2,1,1]
k2 = [1,1,2]
k3 = [1,1]
equalStack(k1, k2, k3)
